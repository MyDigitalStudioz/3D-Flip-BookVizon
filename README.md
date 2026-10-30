# 3D Flip BookVizon

> The BookVizion 3D flipbook viewer — hardcover edition, seeded from flipbook18.

**Branch policy:** work happens on the latest *-vN / project branch. List branches before editing. Never assume the GitHub default is the working line. Working line: 3D-Flip-BookVizon-v2 (GitHub default is main).

[![Preview](https://img.shields.io/badge/Preview-Live-brightgreen)](https://mydigitalstudioz.github.io/3D-Flip-BookVizon/)
![GitHub Pages](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/actions/workflows/pages/pages-build-deployment/badge.svg)
![Last commit](https://img.shields.io/github/last-commit/MyDigitalStudioz/3D-Flip-BookVizon)
![Repo size](https://img.shields.io/github/repo-size/MyDigitalStudioz/3D-Flip-BookVizon)
![Static site](https://img.shields.io/badge/site-static-blue)
![Version](https://img.shields.io/badge/version-1.0.0-orange)

## Live preview

**https://mydigitalstudioz.github.io/3D-Flip-BookVizon/**

Double-click `flipbook18.html` to open the same viewer with no server. The page images ride along as data URIs, so the 3D turn still works. GitHub Pages does not download that file; it keeps using the JPGs. Open PDF, or drop a PDF on the page, reads that file on this computer. It does not fetch a PDF by path.

![Harlow cover on the dark hardcover stage](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/3D-Flip-BookVizon-v2/media/hero.jpg?v=20261029-4)

## Screenshots

Captured from the working viewer on `3D-Flip-BookVizon-v2`. Refresh these files, and the `?v=` stamp, whenever the viewer changes. Pages still serves `main`.

**Cover** — the book closed on the dark stage.

![Harlow cover](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/3D-Flip-BookVizon-v2/media/hero.jpg?v=20261029-4)

**Mid-book** — pages 4–5, the first story spread.

![Story spread, pages 4 and 5](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/3D-Flip-BookVizon-v2/media/spread.jpg?v=20261029-4)

**Phone** — the same cover at a 390px-wide window.

![Phone view of the cover](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/3D-Flip-BookVizon-v2/media/mobile.jpg?v=20261029-4)

## What's inside

- `flipbook18.html` — the hardcover viewer. Future tweaks start here. The folder button opens a folder of images, or you can drop the folder on the page. Open PDF, beside it, opens one interior PDF the same way. Drop a PDF on the page too.
- `index.html` — opens that viewer.
- `flipbook1/` — the book: `manifest.js` plus the page images and favicon. The HTML file loads them by relative path, so the folder stays beside it.
- `flipbook1/pages-data.js` — those same JPGs as data URIs, loaded only when the page is opened from disk. The JPGs stay the source. Rebuild with `python scripts/build-pages-data.py` after a page image changes.
- `vendor/pdfjs/` — pdf.js 3.11.174 (Apache-2.0) as classic scripts. The worker script is loaded in the page so a double-click uses the main-thread worker. Newer pdf.js builds are ES modules and will not run from disk.
- `media/` — the README shots. `hero.jpg` is also the social preview.

The pages are the Harlow review mocks and are marked not for print.

## Design language

Charcoal stage (`#191919`), cream page paper, and the painted art full-bleed on the leaf. The bar has a page-turn choice, Hardcover or Magazine, plus a folder button, an Open PDF button, a pages grid, a fullscreen mark, and white side arrows. The book sits centered with a soft shadow. Hardcover is the 3D sheet. Magazine is the corner peel. The choice is remembered on this browser.

The folder button takes a folder of JPG, PNG, or WebP pages. Files sort by the first number in the name. A wide image is treated as an open spread and split at the fold. The first image is the cover unless that box is unchecked. A missing number is a warning under the book; the pages still turn.

Open PDF takes one interior PDF. Square and portrait pages stay one page. A wide page, about twice as wide as it is tall, splits at the fold. The panel can force single pages or wide spreads, and the first page can be the cover. The title becomes the file name. NOT FOR PRINT stays on unless that box is unchecked. An odd page count adds a blank facing page and the counter says so. A cover wrap PDF is not a book here.

## Tech stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Viewer | Single-file HTML | `flipbook18.html` is the whole hardcover viewer |
| Page turn | WebGL leaf or corner peel | Hardcover turns the 3D sheet. Magazine peels the corner. |
| Script | Vanilla JS | Fit, arrows, paging, fullscreen |
| Book | `flipbook1/manifest.js` + JPGs | Page list and images |
| PDF | pdf.js 3.11.174, vendored | Renders a local PDF into the same page list |
| Host | GitHub Pages | Serves `main` at the preview URL |

`flipbook1/page-flip.browser.js` is the vendored StPageFlip library (MIT, Nodlik). This viewer draws the turn itself.

## Project structure

```
├── index.html
├── flipbook18.html
├── .nojekyll
├── flipbook1/
│   ├── manifest.js
│   ├── pages-data.js
│   ├── page-flip.browser.js
│   ├── favicon.png
│   └── 01-front.jpg … 52-back.jpg
├── scripts/
│   └── build-pages-data.py
├── vendor/
│   └── pdfjs/
└── media/
    ├── hero.jpg
    ├── spread.jpg
    └── mobile.jpg
```

## Branches

Changes land on new branches. `main` is the published mirror, and GitHub Pages serves `main`. List branches before editing. The working line above is updated whenever it moves.

## Status

| Metric | Value |
| :--- | :--- |
| **Stack** | Static HTML · WebGL leaf · GitHub Pages |
| **Preview** | 🌐 [mydigitalstudioz.github.io/3D-Flip-BookVizon](https://mydigitalstudioz.github.io/3D-Flip-BookVizon/) |
| **Status** | 🟢 Live preview |
