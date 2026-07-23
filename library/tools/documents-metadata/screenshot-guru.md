---
id: screenshot-guru
name: Screenshot.guru
description: Use when you have a public webpage URL (`domain`) and want a high-resolution full-page screenshot for evidence — returns a downloadable `image` of the rendered page.
url: https://screenshot.guru
category: documents-metadata
path:
- documents-metadata
bestFor: Capturing a clean, full-length, high-resolution screenshot of a public web page from just its URL.
selectorsIn:
- domain
selectorsOut:
- image
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: active
opsecNote: Screenshot.guru renders the target page from ITS OWN servers, so your IP doesn't hit the target — but the page is actually fetched and can log a visit from the service. It cannot capture login-walled or heavily-dynamic (AJAX/Flash) pages. Preserve the source URL and capture time yourself for provenance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple, long-available hosted screenshot service (by the Digital Inspiration/Labnol author); reliable for public static pages within its stated limits.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- screenshot.guru
tags:
- screenshot
- evidence-capture
- full-page
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Screenshot.guru

> A hosted tool that renders a public web page and returns a high-resolution, full-length screenshot from just its URL.

## When to use
You need to preserve a public web page as visual evidence — a tweet, article, profile, or listing — and want a clean full-page image (including content below the fold) captured server-side, rather than stitching your own scroll captures. Good for documenting a page before it changes, when the page doesn't require login.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://screenshot.guru and paste the public page URL.
2. Let it render — it captures the full page, including below-the-fold content.
3. Download the resulting high-resolution `image`.
4. Log the source URL and capture timestamp alongside the file for provenance.
5. Pivot: the saved image feeds annotation, OCR, or (for embedded photos) reverse-image search.

## Inputs → Outputs
- **In:** a public webpage URL (`domain`/path)
- **Out:** a full-page, high-resolution `image` of the rendered page
- **Empty/negative result looks like:** blank/partial capture or an error — the page likely requires login or uses AJAX/Flash/maps that the renderer can't handle; capture it manually instead.

## Gotchas & OpSec
- Cannot capture authenticated, Flash, or AJAX-heavy pages (e.g. Google Maps).
- The service fetches the target (logged as a visit from screenshot.guru); don't submit URLs you shouldn't access.
- No built-in chain-of-custody — record URL + time yourself.

## Overlaps ("do both")
- Pairs with the Wayback Machine and area-capture tools (e.g. `[[lightshot-screen-capture-add-on]]`) — Screenshot.guru grabs the whole page image while an archive preserves the live DOM/metadata and a crop tool isolates a detail.

## Trust & verifiability
`trust: community` — a straightforward hosted renderer; reliable within its limits, but keep your own copy and provenance notes since it's a third-party service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | screenshot-guru |
