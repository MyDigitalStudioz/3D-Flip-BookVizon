# 3D Flip BookVizon

> The BookVizion 3D flipbook viewer — hardcover edition, seeded from flipbook18.

**Branch policy:** work happens on the latest *-vN / project branch. List branches before editing. Never assume the GitHub default is the working line. Working line: main (GitHub default is main).

[![Preview](https://img.shields.io/badge/preview-live-brightgreen?style=flat)](https://mydigitalstudioz.github.io/3D-Flip-BookVizon/)
[![Pages](https://img.shields.io/github/deployments/MyDigitalStudioz/3D-Flip-BookVizon/github-pages?label=pages)](https://mydigitalstudioz.github.io/3D-Flip-BookVizon/)
[![Last commit](https://img.shields.io/github/last-commit/MyDigitalStudioz/3D-Flip-BookVizon?style=flat)](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/commits/main)
[![Repo size](https://img.shields.io/github/repo-size/MyDigitalStudioz/3D-Flip-BookVizon?style=flat)](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon)
[![Static site](https://img.shields.io/badge/site-static-blue)](https://mydigitalstudioz.github.io/3D-Flip-BookVizon/)

## Live preview

**https://mydigitalstudioz.github.io/3D-Flip-BookVizon/**

![Harlow cover on the dark hardcover stage](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/main/media/hero.jpg?v=20261029-1)

## Screenshots

Captured from the live Pages site. Refresh these files, and the `?v=` stamp, whenever the viewer changes.

**Cover** — the book closed on the dark stage.

![Harlow cover](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/main/media/hero.jpg?v=20261029-1)

**Mid-book** — pages 4–5, the first story spread.

![Story spread, pages 4 and 5](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/main/media/spread.jpg?v=20261029-1)

**Phone** — the same cover at a 390px-wide window.

![Phone view of the cover](https://github.com/MyDigitalStudioz/3D-Flip-BookVizon/raw/main/media/mobile.jpg?v=20261029-1)

## What's inside

- `flipbook18.html` — the hardcover viewer. Future tweaks start here.
- `index.html` — opens that viewer.
- `flipbook1/` — the book: `manifest.js` plus the page images and favicon. The HTML file loads them by relative path, so the folder stays beside it.
- `media/` — the README shots. `hero.jpg` is also the social preview.

The pages are the Harlow review mocks and are marked not for print.

## Design language

Charcoal stage (`#191919`), cream page paper, and the painted art full-bleed on the leaf. Controls are small round buttons on the dark bar: a pages grid, a fullscreen mark, and white side arrows. The book sits centered with a soft shadow.

## Tech stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| Viewer | Single-file HTML | `flipbook18.html` is the whole hardcover viewer |
| Page turn | WebGL leaf | The sheet turns on the spine |
| Script | Vanilla JS | Fit, arrows, paging, fullscreen |
| Book | `flipbook1/manifest.js` + JPGs | Page list and images |
| Host | GitHub Pages | Serves `main` at the preview URL |

`flipbook1/page-flip.browser.js` is the vendored StPageFlip library (MIT, Nodlik). This viewer draws the turn itself.

## Project structure

```
├── index.html
├── flipbook18.html
├── .nojekyll
├── flipbook1/
│   ├── manifest.js
│   ├── page-flip.browser.js
│   ├── favicon.png
│   └── 01-front.jpg … 52-back.jpg
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
