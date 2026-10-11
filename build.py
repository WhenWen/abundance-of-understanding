from pathlib import Path
from html import escape
import math
import re
import shutil

root = Path(__file__).parent
authors = ('Luke Bailey', 'Kaiyue Wen')
section_anchors = ['motivation', 'deep-learning', 'agents', 'open-science']
template = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="On AI, abstraction, and building a public foundation for understanding deep learning.">
<meta name="color-scheme" content="light dark">
<meta name="author" content="__AUTHOR_METADATA__">
<title>__TITLE__</title>
<style>
:root{--paper:#f8f6f0;--ink:#252a25;--muted:#686e65;--line:#dcded3;--green:#41674e;--wash:#ebeee5;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;--serif:Georgia,"Times New Roman",serif}
:root[data-theme="dark"]{--paper:#1b211d;--ink:#e8e8df;--muted:#a9b3a6;--line:#3b443c;--green:#a7c5a2;--wash:#283329}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:44px}body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased}::selection{background:var(--green);color:var(--paper)}a{color:inherit}button,a{-webkit-tap-highlight-color:transparent}a:focus-visible,button:focus-visible{outline:2px solid var(--green);outline-offset:6px}.skip{position:fixed;top:-100px;left:20px;background:var(--paper);padding:12px;z-index:10}.skip:focus{top:10px}.progress{position:fixed;top:0;left:0;height:3px;background:var(--green);width:0;z-index:5;pointer-events:none}
.shell{max-width:1240px;margin:auto;padding:0 56px}.masthead{display:flex;align-items:center;justify-content:space-between;padding:29px 0;border-bottom:1px solid var(--line)}.brand{text-decoration:none;display:flex;align-items:center;gap:11px;font-size:13px;font-weight:600;letter-spacing:.02em}.mark{width:20px;height:20px;display:inline-block;border:1px solid var(--green);border-radius:50%;position:relative}.mark:after{content:"";position:absolute;inset:4px;border:1px solid var(--green);border-radius:50%}.tools{display:flex;align-items:center;gap:22px}.tools a,.tools button{font-family:var(--sans);font-size:12px;color:var(--muted);text-decoration:none;background:none;border:0;padding:5px 0;cursor:pointer}.tools a:hover,.tools button:hover{color:var(--green)}
.hero{padding:72px 0 48px;margin-left:228px;max-width:850px}.eyebrow{font-size:10px;letter-spacing:.17em;text-transform:uppercase;color:var(--green);display:flex;gap:13px;align-items:center}.eyebrow:before{content:"";display:block;width:26px;height:1px;background:var(--green)}h1{font-family:var(--serif);font-size:clamp(42px,5.2vw,66px);font-weight:400;line-height:1.1;letter-spacing:-.042em;margin:23px 0 27px;max-width:790px}h1 em{font-weight:400;color:var(--green)}.meta{color:var(--muted);font-size:11px;letter-spacing:.04em;display:flex;align-items:center;gap:11px}.meta .dot{width:3px;height:3px;background:var(--muted);border-radius:50%}
.byline{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:16px;line-height:1.5;margin:0 0 7px}.author{white-space:nowrap}.author sup{font-size:.75em;color:var(--green);margin-left:2px}.author-note{font-size:12px;line-height:1.6;color:var(--muted);margin:0 0 18px}
.layout{display:grid;grid-template-columns:180px minmax(0,700px);gap:48px;align-items:start}.outline{position:sticky;top:40px;border-top:1px solid var(--line);padding-top:19px}.outline h2{font-size:10px;letter-spacing:.13em;text-transform:uppercase;font-weight:500;color:var(--muted);margin:0 0 21px}.outline a{display:flex;gap:10px;text-decoration:none;font-size:11px;line-height:1.5;color:var(--muted);margin:0 0 18px}.outline a span{font-size:9px;font-variant-numeric:tabular-nums;opacity:.6;padding-top:2px}.outline a.active,.outline a:hover{color:var(--green)}.outline a.active{font-weight:600}.outline .side-note{border-top:1px solid var(--line);margin-top:28px;padding-top:18px;font-size:11px;line-height:1.8;color:var(--muted);max-width:154px}
article{font-family:var(--serif);font-size:19px;line-height:1.82;padding-bottom:65px}article p{margin:0 0 24px;scroll-margin-top:44px}article .lead{font-size:23px;line-height:1.65;letter-spacing:-.01em;margin-top:-7px}article .thesis{border-left:2px solid var(--green);padding:4px 0 4px 25px;margin:37px 0 38px;font-size:25px;line-height:1.5;color:var(--green);font-style:italic}article h2{font-size:1.5em;font-weight:400;line-height:1.35;letter-spacing:-.02em;margin:48px 0 24px;scroll-margin-top:44px}article p:last-child{margin-top:38px}.end-mark{color:var(--green);font-size:18px;margin-top:20px}
footer{border-top:1px solid var(--line);padding:25px 0 32px;display:flex;justify-content:space-between;gap:20px;color:var(--muted);font-size:11px}footer a{text-decoration:none;color:var(--green)}
html[lang="zh-CN"]{--serif:"Songti SC","Noto Serif CJK SC","Source Han Serif SC",serif}html[lang="zh-CN"] h1{font-size:clamp(36px,4.7vw,58px);line-height:1.4;letter-spacing:0}html[lang="zh-CN"] h1 em{font-style:normal}html[lang="zh-CN"] article{line-height:1.95}html[lang="zh-CN"] article .lead{line-height:1.85}html[lang="zh-CN"] article .thesis{font-style:normal;line-height:1.7}.tools .language{display:inline-block;white-space:nowrap;color:var(--green)}
@media(min-width:1440px){.hero{padding-top:88px}}@media(max-width:1000px){.shell{padding:0 34px;max-width:850px}.hero{margin-left:0;padding-top:55px}.layout{grid-template-columns:minmax(0,1fr);gap:0}.outline{display:none}article{max-width:700px}.hero h1{max-width:720px}}@media(max-width:560px){.shell{padding:0 23px}.masthead{padding:23px 0}.brand{font-size:11px}.tools{gap:15px}.tools a{display:none}.hero{padding:43px 0 35px}h1{font-size:43px;line-height:1.09;margin:21px 0 24px}.eyebrow{font-size:9px;letter-spacing:.12em}.meta{font-size:10px}article{font-size:18px;line-height:1.8}article .lead{font-size:21px}article .thesis{font-size:23px;padding-left:20px}footer{font-size:10px}article{padding-bottom:35px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}@media print{.outline,.tools,.progress,.skip{display:none}.shell{max-width:none;padding:0}.hero{margin:0;padding:30px 0}.layout{display:block}h1{font-size:36px}article{font-size:12pt}article .lead{font-size:14pt}:root,:root[data-theme="dark"]{--paper:#fff;--ink:#000;--green:#243d2a;--muted:#555;--line:#ccc}footer{display:none}}
</style>
</head>
<body>
<a class="skip" href="#essay">Skip to essay</a>
<div class="progress" aria-hidden="true"></div>
<div class="shell">
<header class="masthead" id="top"><a class="brand" href="#top"><span class="mark" aria-hidden="true"></span>Notes on understanding</a><div class="tools">__LANGUAGE_LINK__<a href="essay.md" download>Download essay ↗</a><button id="theme" type="button" aria-label="Switch to dark mode" aria-pressed="false">Dark mode</button></div></header>
<main>
<div class="hero"><div class="eyebrow">Artificial intelligence · Open science</div><h1>From an Abundance of Proof to an Abundance of <em>Understanding</em></h1><div class="byline" id="authors" aria-label="Authors" aria-describedby="author-note">__AUTHORS__</div><p class="author-note" id="author-note">* Co-first authors · Order randomized on each page load</p><div class="meta"><span>An essay</span><span class="dot" aria-hidden="true"></span><span>__MINUTES__ min read</span></div></div>
<div class="layout"><aside class="outline"><nav aria-label="In this essay"><h2>In this essay</h2>__NAV__</nav><p class="side-note">On turning extraordinary capabilities into shared understanding.</p></aside><article id="essay" aria-label="__TITLE__">__BODY__<div class="end-mark" aria-hidden="true">∎</div></article></div>
</main>
<footer><span>AI · Understanding · Open science</span><a href="#top">Back to top ↑</a></footer>
</div>
<script>
const byline = document.querySelector('#authors');
const authorElements = [...byline.querySelectorAll('.author')];
if (Math.random() < 0.5) authorElements.reverse();
byline.replaceChildren(...authorElements);
document.querySelector('meta[name="author"]').content = authorElements.map(author => author.dataset.name).join(', ');
const root = document.documentElement;
const themeButton = document.querySelector('#theme');
function applyTheme(dark) { root.dataset.theme = dark ? 'dark' : 'light'; themeButton.textContent = dark ? 'Light mode' : 'Dark mode'; themeButton.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode'); themeButton.setAttribute('aria-pressed', String(dark)); }
try { applyTheme(localStorage.getItem('essay-theme') === 'dark'); } catch (_) { applyTheme(false); }
themeButton.addEventListener('click', () => { const dark = root.dataset.theme !== 'dark'; applyTheme(dark); try { localStorage.setItem('essay-theme', dark ? 'dark' : 'light'); } catch (_) {} });
const anchors = [...document.querySelectorAll('article h2[id]')];
const links = [...document.querySelectorAll('.outline nav a')];
const progress = document.querySelector('.progress');
let queued = false;
function updateReading() { const limit = document.documentElement.scrollHeight - innerHeight; progress.style.width = (limit > 0 ? Math.min(100, 100 * scrollY / limit) : 100) + '%'; let active = anchors[0]; for (const anchor of anchors) { if (anchor.getBoundingClientRect().top <= innerHeight * .35) active = anchor; } for (const link of links) { const current = link.hash === '#' + active.id; link.classList.toggle('active', current); if (current) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); } queued = false; }
addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(updateReading); } }, {passive:true});
addEventListener('resize', updateReading); updateReading();
</script>
</body>
</html>'''
translations = {
    'Co-first authors · Order randomized on each page load': '共同第一作者 · 每次加载页面时随机排列署名顺序',
    'aria-label="Authors"': 'aria-label="作者"',
    'On AI, abstraction, and building a public foundation for understanding deep learning.': '关于 AI、抽象，以及如何为理解深度学习建立公共知识基础。',
    'Skip to essay': '跳至正文',
    'Notes on understanding': '关于理解的笔记',
    'Download essay ↗': '下载文章 ↗',
    'Switch to dark mode': '切换至深色模式',
    'Switch to light mode': '切换至浅色模式',
    'Dark mode': '深色模式',
    'Light mode': '浅色模式',
    'Artificial intelligence · Open science': '人工智能 · 开放科学',
    'From an Abundance of Proof to an Abundance of <em>Understanding</em>': '从证明的充裕，<br>到<em>理解的充裕</em>',
    'An essay': '随笔',
    ' min read': ' 分钟阅读',
    'In this essay': '文章目录',
    'On turning extraordinary capabilities into shared understanding.': '让非凡的能力，成为可以共享的理解。',
    'AI · Understanding · Open science': 'AI · 理解 · 开放科学',
    'Back to top ↑': '返回顶部 ↑',
}

for language, source, output in [('en', 'essay.md', 'index.html'), ('zh-CN', 'essay-zh.md', 'zh.html')]:
    essay = (root / source).read_text()
    title, *paragraphs = essay.strip().split('\n\n')
    title = title.removeprefix('# ')
    body, nav = [], []
    for i, paragraph in enumerate(paragraphs):
        if paragraph.startswith('## '):
            heading = paragraph.removeprefix('## ')
            label = re.sub(r'^\d+\.\s*', '', heading)
            anchor = section_anchors[len(nav)]
            nav.append(f'<a href="#{anchor}"><span>{len(nav)+1:02}</span>{escape(label)}</a>')
            body.append(f'<h2 id="{anchor}">{escape(heading)}</h2>')
            continue
        classes = ' class="lead"' if i == 0 else ''
        body.append(f'<p{classes}>{escape(paragraph)}</p>')
    if len(nav) != len(section_anchors):
        raise ValueError(f'{source} must have four section headings')
    page = template.replace('__AUTHORS__', ''.join(f'<span class="author" data-name="{escape(author)}">{escape(author)}<sup>*</sup></span>' for author in authors)).replace('__AUTHOR_METADATA__', escape(', '.join(authors)))
    if language == 'zh-CN':
        for original, translated in translations.items():
            page = page.replace(original, translated)
        page = page.replace('<html lang="en">', '<html lang="zh-CN">').replace('href="essay.md"', 'href="essay-zh.md"')
        language_link = '<a class="language" href="index.html" lang="en" hreflang="en" aria-label="Read in English">English</a>'
        reading_minutes = math.ceil((len(re.findall(r'[\u4e00-\u9fff]', essay)) + len(re.findall(r'[A-Za-z]+', essay))) / 400)
    else:
        language_link = '<a class="language" href="zh.html" lang="zh-CN" hreflang="zh-CN" aria-label="阅读中文版">中文</a>'
        reading_minutes = math.ceil(len(essay.split()) / 220)
    page = page.replace('__LANGUAGE_LINK__', language_link).replace('__TITLE__', escape(title)).replace('__MINUTES__', str(reading_minutes)).replace('__NAV__', '\n'.join(nav)).replace('__BODY__', '\n'.join(body))
    (root / output).write_text(page)
    print(f'Built {output}: {len(paragraphs)} paragraphs.')

distribution = root / 'dist'
distribution.mkdir(exist_ok=True)
for filename in ('index.html', 'zh.html', 'essay.md', 'essay-zh.md'):
    if filename.endswith('.md'):
        title, body = (root / filename).read_text().split('\n\n', 1)
        names = ' · '.join(author + r'\*' for author in authors)
        note = (r'\* 共同第一作者。网页中的署名顺序在每次加载时随机排列。' if filename == 'essay-zh.md' else r'\* Co-first authors. Author order on the website is randomized on each page load.')
        (distribution / filename).write_text(title + '\n\n' + names + '\n\n' + note + '\n\n' + body)
    else:
        shutil.copy2(root / filename, distribution / filename)
