---
id: quickmaps
name: QuickMaps
description: Use when you want a one-click Chrome extension to map highlighted text (an address or coordinates) without leaving the page.
url: https://chrome.google.com/webstore/detail/quick-maps/bgbojmobaekecckmomemopckmeipecij
category: geolocation
path:
- geolocation
bestFor: A lightweight Chrome browser extension to quickly map a selected address or coordinates.
selectorsIn: [address, geolocation]
selectorsOut: [geolocation]
status: unknown
pricing: free
opsec: passive
opsecNote: A browser extension that sends selected text to a map provider; vet its permissions before installing, as extensions can read page content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Third-party Chrome Web Store extension by an unknown publisher; cannot confirm current availability or exact behavior without installing — vet permissions.
missingPersonsRelevance: medium
coverage: [global]
auth: none
api: false
localInstall: true
registration: false
aliases: [Quick Maps]
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# QuickMaps

> A lightweight Chrome extension to quickly plot a highlighted address or coordinate on a map from any web page.

## When to use
You are reading a page (a report, a social post, a listing) containing an `address` or `geolocation` (coordinates) and want to map it in one action without copy-pasting into a separate map site. Convenience tool, not an analysis tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store link, reviewing the requested permissions first.
2. On any page, select an `address` or coordinate string.
3. Trigger the extension (toolbar button or context menu) to open the location on a map (`geolocation`).
4. Pivot: open the same point in a richer tool — `[[satellites-pro]]` for imagery or `[[scribblemaps]]` to annotate.

## Inputs → Outputs
- **In:** `address`, `geolocation` (selected text)
- **Out:** a map view of that `geolocation`
- **Empty/negative result looks like:** the extension fails to geocode ambiguous or partial text — refine the selection.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installation.
- OpSec: a browser extension can read page content and sends the selected text to a map provider. Vet its permissions; do not install on a machine handling sensitive case data without review.
- Availability is uncertain — Chrome Web Store listings by small publishers can be removed.

## Overlaps ("do both")
- Redundant with simply pasting into `[[satellites-pro]]` or Google Maps; value is only the one-click workflow.

## Trust & verifiability
`trust: unverified` — a third-party extension by an unknown publisher. I cannot confirm its current behavior or availability from the URL/name alone; treat with caution and review permissions before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quickmaps |
| category | geolocation |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
