---
id: fireshot
name: FireShot
description: Use when you have a web page you need to preserve as evidence and want a full-length screenshot saved as PDF/PNG — returns a captured, timestampable image of the page.
url: https://chromewebstore.google.com/detail/take-webpage-screenshots-fireshot/mcbpblocgmgfnpjjppndjkmgjaogfceg
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Capturing an entire web page (including below-the-fold content) as a PDF/PNG for evidence preservation.
selectorsIn: []
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free tier captures full pages and saves as PDF/PNG/image; a paid Pro upgrade adds OCR, bulk capture, and richer export/annotation.
opsec: passive
opsecNote: Capturing runs locally in your browser and does not re-contact the page beyond your own visit — the site sees a normal page load. Capture from a sock-puppet browser profile if the visit itself must be non-attributable; the saved file records what you saw, so timestamp and hash it for chain-of-custody.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A long-established, widely used screenshot extension; the capture is only as trustworthy as your handling — note the URL, date, and a hash alongside the file.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Take Webpage Screenshots (FireShot)
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- evidence-capture
- screenshot
source: toddington-resources
lastVerified: '2026-08-05'
enrichment: full
---

# FireShot

> A browser extension for capturing an entire web page — not just the visible viewport — as a single PDF or image, the workhorse move for preserving online evidence before it changes or disappears.

## When to use
You have found a page that matters to the investigation — a profile, a post, a listing, a cached result — and it could be edited or deleted at any moment. FireShot captures the whole scrollable page in one file so you have a fixed, shareable record. This is investigator tooling for evidence preservation; it produces a file, not data about a subject.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Take Webpage Screenshots — FireShot" from the Chrome Web Store (also available for Firefox/Edge) in your working browser profile.
2. Navigate to the page you need to preserve (use a sock-puppet profile if the visit must be non-attributable).
3. Click the FireShot icon → "Capture entire page," then save as PDF or PNG.
4. Immediately record provenance: the full URL, capture date/time, and ideally a hash of the file.
5. Pivot: file the capture with your case notes; the preserved page backs any claim you later make from it.

## Inputs → Outputs
- **In:** the web page currently open in your browser (no subject data typed)
- **Out:** a full-page PDF/PNG capture (its own `metadata-exif`/timestamp is part of the evidentiary record)
- **Empty/negative result looks like:** capture fails or truncates on lazy-loading/infinite-scroll or canvas-heavy pages — scroll to force-load content first, or fall back to a page-archiving service.

## Gotchas & OpSec
- Human-in-the-loop: none beyond clicking capture.
- OpSec: passive — capturing is local; the site only sees your normal visit. The evidentiary weakness is handling, not the tool: without a recorded URL, timestamp, and hash, a screenshot is easy to dispute.
- Dynamic pages (infinite scroll, JS canvas) can defeat full-page capture — verify the saved file actually contains what you needed.

## Overlaps ("do both")
- Pairs with an independent archive such as the Wayback Machine / archive.today — FireShot is your own instant capture, a public archive is third-party corroboration; do both so a preserved page has two sources.

## Trust & verifiability
`trust: community` — a mature, popular extension, but a screenshot is only as credible as its provenance. Always pair the file with URL, timestamp, and hash, and corroborate important pages with an independent archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fireshot |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
