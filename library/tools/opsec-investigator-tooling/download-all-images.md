---
id: download-all-images
name: Download All Images (Firefox add-on)
description: Use when you have a web page and want to bulk-collect every `image` on it (including iframes) for reverse-search / EXIF triage — returns the downloaded `image` files.
url: https://addons.mozilla.org/en-US/firefox/addon/save-all-images-webextension/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Bulk-saving all images from a web page, with size/type/dimension filters, for downstream image OSINT.
selectorsIn: []
selectorsOut:
- image
status: live
pricing: free
costNote: Free Firefox add-on (~100k users); optional donations, no paywall.
opsec: passive
opsecNote: It gathers images already loaded on the page and downloads them; this is normal browsing traffic to the page's hosts. Do it from your usual sock-puppet/VPN session, especially on a target's own site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular, actively-updated AMO extension (100k+ users, June 2026); a convenience utility with no data-quality stake — what it saves is exactly what the page served.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- exif-viewer-addons-mozilla-org
aliases:
- Save All Images
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- image
- bulk-download
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Download All Images (Firefox add-on)

> One click to grab every image on a page — including ones tucked inside iframes — into a gallery you can filter and bulk-download.

## When to use
You've found a page dense with photos — a profile, a marketplace listing, a gallery, a forum thread — and want all the images at once rather than saving them one by one. Collecting the full set lets you run each through reverse-image search and EXIF triage. A time-saver at the top of an image-OSINT workflow.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Save All Images" from https://addons.mozilla.org/en-US/firefox/addon/save-all-images-webextension/ in Firefox.
2. Open the target page and click the toolbar icon; the add-on scans the page (and iframes) and shows every image in a gallery.
3. Filter by file size, dimensions, or type to drop thumbnails/spacers and keep the substantive images.
4. Download the selected set to a local folder.
5. Pivot: run the saved images through reverse-image search and inspect each with [[exif-viewer-addons-mozilla-org]] for GPS/camera metadata.

## Inputs → Outputs
- **In:** a loaded web page
- **Out:** the page's `image` files, saved locally (filtered by size/type/dimensions)
- **Empty/negative result looks like:** no images found — the page loads images lazily/behind interaction or via a canvas/CSS background the scanner can't capture; scroll to load them first, or save manually.

## Gotchas & OpSec
- Lazy-loaded or login-gated images may not appear until you scroll/authenticate; the tool only sees what the page has actually loaded.
- Saving from a target's own site is normal browsing but still hits their host — use a clean session.
- Downloading images does not preserve anything the server stripped; EXIF is only present if the site served it.

## Overlaps ("do both")
- Feeds directly into [[exif-viewer-addons-mozilla-org]] (metadata/GPS on each saved image) and any reverse-image-search workflow — this collects, those analyze.

## Trust & verifiability
`trust: community` — a widely-used AMO utility; it just saves what the page delivered, so there's no data-quality risk beyond the source page itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | download-all-images |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
