# 3D Flip BookVizon

Independent copy of the hardcover flipbook. The seed is `flipbook18.html`, taken from [Harlows-Accidental-Journey](https://github.com/MyDigitalStudioz/Harlows-Accidental-Journey) on 2026-10-29. That file is the official best hardcover viewer. Future tweaks start here.

`flipbook18.html` sits beside the `flipbook1/` folder. The page images, favicon, and manifest are loaded by relative path, so keep that layout.

Open it with a local server:

```powershell
python -m http.server 8091
```

Then go to http://127.0.0.1:8091/flipbook18.html

The pages are the v2 review mocks and are marked not for print. `flipbook1/page-flip.browser.js` is the vendored StPageFlip library (MIT, Nodlik). This viewer draws the page turn itself.
