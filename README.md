# An Abundance of Understanding

A bilingual essay by **Luke Bailey\*** and **Kaiyue Wen\***. \* Co-first authors; the website randomizes their order on every page load.

**Website:** https://abundance-of-understanding.wen.chatgpt.site/

## Edit the website

- Edit [`essay.md`](essay.md) for English or [`essay-zh.md`](essay-zh.md) for Chinese. Update both when changing the argument.
- Edit [`build.py`](build.py) for layout, styling, author information, or UI translations.
- Commit or merge changes into `main`. The **Publish website** GitHub Actions workflow builds and checks both pages, then writes the generated files to `published`.
- The existing website serves those public files from GitHub. No manual Sites publish or private deployment token is needed for article/layout changes. Allow a few minutes for the workflow and GitHub CDN caches to refresh.
- Pull requests run build checks but do not publish. A failed build leaves the last published version online. To roll back, revert the source commit on `main`.

The Markdown format is intentionally simple: one title, four `##` section headings, and paragraphs separated by blank lines. Inline Markdown syntax is displayed as text by the current builder.

## Preview locally

Python 3.9+ is sufficient; there are no third-party dependencies.

```sh
python3 build.py
python3 scripts/check-site.py
python3 -m http.server 8765 --directory dist
```

Open http://127.0.0.1:8765/. Generated HTML and `dist/` are ignored on `main`; do not edit the generated `published` branch manually.

## Hosting bridge

[`hosting/worker.js`](hosting/worker.js) is the small Sites worker that serves the generated files from this repository's `published` branch at the existing website URL. It forwards no visitor cookies or authorization headers to GitHub and only serves the two pages and two Markdown downloads. If GitHub is unavailable it returns a retryable error. Changes to this bridge itself or adding new URL routes require a separate Sites deployment; normal content and layout edits do not.

## 中文说明

修改 `essay.md`（英文）或 `essay-zh.md`（中文）后提交到 `main`，GitHub Actions 会自动生成网页并更新 `published` 分支。现有网址读取这个分支，不需要再次手动部署 Sites。通常等待几分钟即可看到更新。排版和署名设置在 `build.py` 中。
