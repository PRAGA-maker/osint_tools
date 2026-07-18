---
id: full-page-screen-capture-chrome-extension
name: Full Page Screen Capture Chrome Extension
description: Use when you have a live web page (`social-profile`, `domain` or any URL) and want a scroll-stitched full-page screenshot for evidence — returns a PNG/PDF `metadata-exif`-bearing capture.
url: https://github.com/mrcoles/full-page-screen-capture-chrome-extension
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: One-click full-length screenshots of long/scrolling pages for documentation and evidence preservation.
selectorsIn:
- social-profile
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open source (MIT); install from the Chrome Web Store or load unpacked from GitHub. No account.
opsec: passive
opsecNote: The extension captures what your browser already rendered — it makes no extra requests to the target, so it adds no footprint beyond your normal page visit. OpSec risk lives in how you loaded the page (log in with a sock puppet / route through a clean profile) and in the fact that captures can embed your session UI (usernames, tabs) — crop those before sharing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular open-source extension (mrcoles, ~1.5k GitHub stars, MIT-licensed); the code is auditable, though the Web Store build tracks a separate private branch, so pin a known version for high-stakes evidence work.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Full Page Screen Capture
- mrcoles full page screenshot
tags:
- evidence-capture
- screenshot
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Full Page Screen Capture Chrome Extension

> A one-click Chrome extension that scrolls a page and stitches the whole thing into a single image — the quick way to preserve a long profile or article as evidence.

## When to use
You've found a page worth preserving — a `social-profile`, a `domain`/website, a forum thread, a classified ad — and need a full-length capture before it changes or is deleted. The viewport-only screenshot misses everything below the fold; this extension auto-scrolls and stitches the entire page into one PNG (or PDF). Use it for contemporaneous documentation of what you saw, when.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Chrome Web Store ("Full Page Screen Capture") or clone the GitHub repo and load it unpacked via `chrome://extensions` → Developer mode → Load unpacked.
2. Navigate to the target page in the browser profile you want on record (ideally a clean/sock-puppet profile, logged in as needed).
3. Click the extension's camera icon; it scrolls the page top-to-bottom and assembles the capture.
4. Save the result as **PNG** (or print to PDF). Record the URL and the capture time alongside it — the image itself does not reliably carry a trustworthy timestamp.
5. Pivot: file the capture in your evidence log; for stronger provenance also archive the URL to a public web archive.

## Inputs → Outputs
- **In:** a rendered page — from a `social-profile`, `domain`, or any URL
- **Out:** a full-page PNG/PDF capture (a `metadata-exif`-bearing image file) plus whatever the page showed
- **Empty/negative result looks like:** lazy-loaded/infinite-scroll pages, canvas/WebGL content, or iframes may capture blank or partial — stitching fails silently, so eyeball the output for gaps.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must have the page loaded/authenticated yourself first.
- OpSec: **passive** — no extra requests hit the target beyond your visit. Beware capturing your own logged-in UI (your username, other tabs) into the image; crop before sharing.
- Not forensically sound on its own: it proves *what you rendered*, not an independently timestamped record. Pair with an archive service for stronger provenance.
- Infinite-scroll and dynamic pages are the main failure mode — verify the stitch is complete.

## Overlaps ("do both")
- Do both with a public web-archive capture: the extension gives you a self-held full-page image, the archive gives a third-party timestamped copy. Together they make defensible evidence.

## Trust & verifiability
`trust: community` — a widely-used MIT-licensed open-source extension; the source is auditable, but the Web Store build follows a private branch, so pin/verify the version when the capture must stand as evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | full-page-screen-capture-chrome-extension |
| category | evidence-capture |
| selectorsIn → selectorsOut | social-profile, domain → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
