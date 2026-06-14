---
id: fireshot-addons-mozilla-org
name: fireshot (addons.mozilla.org)
description: Use when you need to capture a full-page screenshot of a web profile or post to preserve evidence before it is edited or deleted.
url: https://addons.mozilla.org/en-US/firefox/addon/fireshot/?src=search
category: image-video-face
path:
- image-video-face
bestFor: Full-page web screenshot capture for evidence preservation (not face/image search).
selectorsIn:
- social-profile
- domain
selectorsOut:
- image
- metadata
status: live
pricing: freemium
costNote: Core capture (PNG/JPG) is free; PDF export, multi-page capture, and editing features are in the paid Pro version.
opsec: passive
opsecNote: Captures the page as your browser renders it; the act of capturing is local. OpSec depends on how you reached the page (logged-in vs sock puppet), not on FireShot.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: browser-extension
trust: community
trustNote: FireShot is a long-established, widely used Firefox/Chrome screenshot extension; it is a capture utility, not an OSINT search tool, and was mistagged "Reverse Image Searching" in the source list.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- FireShot
tags:
- screenshot
- evidence-capture
source: uk-osint
lastVerified: ''
enrichment: full
---

# fireshot (addons.mozilla.org)

> A browser extension that captures full-page screenshots — a evidence-preservation utility, not a face/image search engine.

## When to use
You are viewing a `social-profile`, post, or page on a `domain` and need to snapshot it as `image`/PDF before it changes or is deleted. Essential for preserving volatile evidence (a missing person's last post, a suspect's profile) with on-screen `metadata` (URL, timestamp) visible in the capture.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install FireShot from addons.mozilla.org (Firefox) or the Chrome Web Store.
2. Navigate to the page you want to preserve.
3. Click the FireShot icon and choose "Capture entire page".
4. Save as PNG/JPG (free) or export to PDF (Pro); make sure the URL and date are visible/added.
5. Pivot: store the capture in your case file; if it contains a `face`, feed the cropped photo into `[[facecheck-facial-recognition-search]]`.

## Inputs → Outputs
- **In:** a rendered web page (`social-profile` / `domain`).
- **Out:** `image` (full-page screenshot) with embedded on-page `metadata`.
- **Empty/negative result looks like:** n/a — it captures whatever is rendered; lazy-loaded content may need scrolling first.

## Gotchas & OpSec
- Human-in-the-loop: you frame and verify each capture; annotate with source URL + timestamp for chain-of-custody.
- OpSec: **passive** as a tool, but the capture reflects your session — if you are logged in, that may be visible. Reach the page via a sock puppet when needed.

## Overlaps ("do both")
- Pairs with archiving services (e.g. Wayback Machine) for an independent, timestamped record alongside your local capture.

## Trust & verifiability
`trust: community` — a mature, popular screenshot extension; reliable for what it does. Not a search/identification tool despite the source-list tag.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fireshot-addons-mozilla-org |
| category | image-video-face |
| selectorsIn → selectorsOut | social-profile, domain → image, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes |
