import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
const source = await readFile(new URL('./worker.js', import.meta.url), 'utf8');
const worker = (await import('data:text/javascript;base64,' + Buffer.from(source).toString('base64'))).default;
const originalFetch = globalThis.fetch;
const originalWarn = console.warn;
console.warn = () => {};
const request = (path, method = 'GET') => new Request('https://example.test' + path, {method});
try {
  globalThis.fetch = async (url, options) => {
    assert.match(url, /^https:\/\/raw.githubusercontent.com\/WhenWen\/abundance-of-understanding\/published\//);
    assert.equal(options.headers, undefined);
    assert.equal(options.redirect, 'manual');
    return new Response('<!doctype html><title>Fresh GitHub publication</title>');
  };
  let result = await worker.fetch(request('/'));
  assert.equal(result.headers.get('X-Essay-Source'), 'github');
  assert.match(await result.text(), /Fresh GitHub publication/);
  const failures = [
    async () => {throw new TypeError('network unavailable');},
    async () => new Response('blocked', {status: 403}),
    async () => new Response('', {status: 302, headers: {Location: 'https://untrusted.example/'}}),
    async () => new Response(''),
    async () => new Response(new ReadableStream({start(c) {c.error(new Error('broken stream'));}})),
  ];
  for (const fail of failures) {
    globalThis.fetch = fail;
    for (const path of ['/', '/zh.html', '/essay.md', '/essay-zh.md']) {
      result = await worker.fetch(request(path));
      assert.equal(result.status, 200);
      assert.equal(result.headers.get('X-Essay-Source'), 'bundled');
      assert.ok((await result.text()).length > 1000);
    }
  }
  globalThis.fetch = (_url, options) => new Promise((_resolve, reject) => {
    options.signal.addEventListener('abort', () => reject(new DOMException('Timed out', 'AbortError')), {once:true});
  });
  const started = Date.now();
  result = await worker.fetch(request('/'));
  assert.equal(result.status, 200);
  assert.ok(Date.now() - started < 6500);
  globalThis.fetch = async () => {throw new Error('offline');};
  result = await worker.fetch(request('/zh.html', 'HEAD'));
  assert.equal(await result.text(), '');
  assert.equal(result.headers.get('Content-Language'), 'zh-CN');
  assert.equal((await worker.fetch(request('/unknown'))).status, 404);
  assert.equal((await worker.fetch(request('/', 'POST'))).status, 405);
  assert.equal((await worker.fetch(request('/zh/'))).headers.get('location'), 'https://example.test/zh');
  console.log('PASS: live content, network/HTTP/empty/stream failures, timeout, bilingual downloads, HEAD and routing');
} finally {
  globalThis.fetch = originalFetch;
  console.warn = originalWarn;
}
