// Public build output is produced by the repository's Publish website workflow.
const origin = 'https://raw.githubusercontent.com/WhenWen/abundance-of-understanding/published/';
const routes = new Map([
  ['/', 'index.html'], ['/index', 'index.html'], ['/index.html', 'index.html'],
  ['/zh', 'zh.html'], ['/zh.html', 'zh.html'],
  ['/essay.md', 'essay.md'], ['/essay-zh.md', 'essay-zh.md'],
]);

export default {
  async fetch(request) {
    if (!['GET', 'HEAD'].includes(request.method)) {
      return new Response('Method not allowed', {status: 405, headers: {Allow: 'GET, HEAD'}});
    }
    const url = new URL(request.url);
    // Canonicalize trailing slashes so existing relative language/download links work.
    if (['/zh/', '/index/'].includes(url.pathname)) {
      url.pathname = url.pathname.slice(0, -1);
      return Response.redirect(url.toString(), 308);
    }
    const file = routes.get(url.pathname);
    if (!file) return new Response('Not found', {status: 404});
    try {
      // Only a fixed public GitHub URL is fetched; visitor headers are not forwarded.
      const upstream = await fetch(origin + file, {
        redirect: 'error',
        signal: AbortSignal.timeout(10000),
        cf: {cacheTtl: 60, cacheEverything: true},
      });
      if (!upstream.ok) throw new Error('Upstream unavailable');
      const headers = new Headers({
        'Content-Type': file.endsWith('.html') ? 'text/html; charset=utf-8' : 'text/markdown; charset=utf-8',
        'Content-Language': file.startsWith('zh') || file.includes('-zh') ? 'zh-CN' : 'en',
        'Cache-Control': 'public, max-age=0, must-revalidate',
        'X-Content-Type-Options': 'nosniff',
        'Referrer-Policy': 'strict-origin-when-cross-origin',
      });
      return new Response(request.method === 'HEAD' ? null : upstream.body, {headers});
    } catch {
      return new Response(request.method === 'HEAD' ? null : 'The essay is temporarily unavailable. Please try again shortly.', {
        status: 503,
        headers: {'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store', 'Retry-After': '30'},
      });
    }
  },
};
