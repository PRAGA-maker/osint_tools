---
id: minipaint
name: miniPaint
description: Use when you need a free in-browser photo editor to crop, sharpen, adjust, or annotate a missing-person image before running face/reverse-image search — returns an edited image.
url: https://viliusle.github.io/miniPaint/
category: image-video-face
path:
- image-video-face
bestFor: Browser-based, no-install image editing (crop/rotate/sharpen/annotate) of a photo before search.
selectorsIn:
- image
selectorsOut:
- image
status: live
pricing: free
costNote: Fully free and open-source (MIT); runs client-side, no account.
opsec: passive
opsecNote: Runs entirely in your browser; the image is processed locally and not uploaded to a server, so it does not leak the subject photo.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by Vilius Lešauskas (viliusle on GitHub) with public source; widely used. Not an investigative service, just an editor.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases: []
tags:
- image-editor
- photo-prep
source: osint4all
lastVerified: ''
enrichment: full
---

# miniPaint

> A free, open-source, browser-based image editor (a lightweight Photoshop-in-the-tab) for prepping photos before search.

## When to use
You have an `image` of a missing person (or a screenshot, a still from a video, a low-quality lead photo) and you need to crop to the face, rotate/deskew, sharpen, adjust brightness/contrast, remove a watermark or background clutter, or annotate features before feeding it into face-match or reverse-image-search tools. It is a pre-processing step, not a search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://viliusle.github.io/miniPaint/ — it loads instantly, no login.
2. **File → Open** the photo (or paste/drag it in).
3. Edit: use Crop to isolate one face, Rotate/Resize to deskew, and the Effects/Filters menu (Sharpen, Brightness/Contrast, Sharpen) to improve a soft image. Use layers to annotate.
4. **File → Save / Export** as PNG or JPG.
5. Pivot: feed the cleaned `image` into a face engine like [[mxface-ai]] or a reverse-image search; for upscaling instead, use [[neural-network-image-super-resolution-and-enhancement]].

## Inputs → Outputs
- **In:** `image`
- **Out:** `image` (edited/cropped/sharpened)
- **Empty/negative result looks like:** N/A — it is an editor, not a lookup; "failure" is simply a file that does not open (unsupported format) or an edit that does not improve usability.

## Gotchas & OpSec
- Human-in-the-loop: all editing is manual; there is no automated enhancement and no scientifically-defensible "enhancement" — do not over-sharpen and create artifacts that could mislead a face match.
- OpSec: passive. Processing is client-side in JavaScript, so the subject image is not sent to a remote server — safe for sensitive case photos.

## Overlaps ("do both")
- Pairs with [[neural-network-image-super-resolution-and-enhancement]] (Let's Enhance) when you also need AI upscaling rather than manual editing.

## Trust & verifiability
`trust: community` — established open-source editor (MIT, public GitHub by viliusle) used broadly; reliable as a tool, but it produces no investigative claims to verify.

---
## Metadata
| field | value |
|---|---|
| id | minipaint |
| category | image-video-face |
| selectorsIn → selectorsOut | image → image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
