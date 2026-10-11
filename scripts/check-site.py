from html.parser import HTMLParser
from pathlib import Path

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.authors = set(), [], []
        self.language = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate ID: {attrs['id']}"
            self.ids.add(attrs['id'])
        if tag == 'html': self.language = attrs.get('lang')
        if tag == 'a': self.links.append(attrs.get('href', ''))
        if attrs.get('class') == 'author': self.authors.append(attrs['data-name'])

for filename, language in [('index.html', 'en'), ('zh.html', 'zh-CN')]:
    text = (Path('dist') / filename).read_text()
    page = Page()
    page.feed(text)
    assert page.language == language
    assert set(page.authors) == {'Luke Bailey', 'Kaiyue Wen'}
    assert text.count('<sup>*</sup>') == 2
    assert all(name in page.ids for name in ['motivation','deep-learning','agents','open-science'])
    for link in page.links:
        if link.startswith('#'): assert link[1:] in page.ids, link
        elif not link.startswith(('https:', 'http:')): assert (Path('dist') / link).is_file(), link
    assert '__BODY__' not in text and '__TITLE__' not in text
    print(f'{filename}: language, authors, sections, and links checked')
