---
id: lightshot-screen-capture-add-on
name: Lightshot Screen Capture Add-on
description: Use when you need to quickly screenshot a selected area of a browser tab to preserve `metadata-exif`-free visual evidence during an investigation — returns an annotated image capture.
url: https://addons.mozilla.org/en-US/firefox/addon/lightshot/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Fast selective-area screenshots with light annotation for evidence capture inside the browser.
selectorsIn: []
selectorsOut:
- image
status: live
pricing: free
costNote: Free Firefox (and Chrome) browser add-on.
opsec: active
opsecNote: The convenient "upload & share" feature sends your screenshot to Lightshot's prnt.sc servers, producing a PUBLIC, sequentially-numbered link — a known privacy leak (prnt.sc URLs are routinely scraped). For investigation evidence, ALWAYS save locally and NEVER use the upload/share button, or sensitive captures become world-readable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular, long-lived extension distributed via the official Mozilla add-ons store; functional but the upload feature has a documented public-exposure risk.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Lightshot
- prnt.sc
tags:
- screenshot
- evidence-capture
- browser-extension
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Lightshot Screen Capture Add-on

> A browser add-on for grabbing and lightly annotating a selected screen area — handy for evidence capture, with one major upload-privacy caveat.

## When to use
During an investigation you find something ephemeral in a browser tab (a post, profile, listing, or map) and need to preserve it as an `image` before it changes or is deleted. Lightshot lets you drag-select just the relevant region, add arrows/text, and save it — faster than a full-page capture. Treat it as a documentation utility, not an investigative lookup.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the official store: https://addons.mozilla.org/en-US/firefox/addon/lightshot/ (Chrome version also available).
2. Click the Lightshot icon (or its hotkey) and drag to select the area to capture.
3. Annotate if needed — arrows, boxes, text to mark the relevant detail.
4. **Save to disk** (the download/save button). Record the URL and timestamp separately for provenance.
5. Do **not** use the upload/share button — see OpSec below.

## Inputs → Outputs
- **In:** none (captures whatever is on screen)
- **Out:** a local `image` file of the selected region, optionally annotated
- **Empty/negative result looks like:** nothing to note — capture either succeeds locally or you cancel the selection.

## Gotchas & OpSec
- **Do not upload/share:** Lightshot's cloud share posts to prnt.sc with predictable, sequential public URLs that are widely scraped — treat any uploaded capture as instantly public. Save locally only.
- Screenshots may carry no EXIF, but you must log source URL + time yourself for evidence integrity.
- Prefer the OS native capture or a local-only tool if you handle sensitive material and want zero cloud path.

## Overlaps ("do both")
- Pairs with full-page archiving tools (e.g. web archive/capture services) — Lightshot grabs a precise cropped detail while a full-page archiver preserves the whole page and its metadata; do both for defensible evidence.

## Trust & verifiability
`trust: community` — a widely-used extension from the official Mozilla store; reliable for capture, but its upload path is a documented exposure risk, so keep captures local.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lightshot-screen-capture-add-on |
