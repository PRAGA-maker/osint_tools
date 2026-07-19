---
id: copernix
name: COPERNIX
description: Use when you have a place name or `geolocation` and want to see every Wikipedia article geotagged to that area on a map — returns local `geolocation` context (landmarks, streets, sites).
url: https://copernix.io/
category: geolocation
path:
- geolocation
bestFor: Exploring a map to discover what Wikipedia knows about a specific area — buildings, streets, landmarks, and attractions near a point.
selectorsIn:
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Completely free with discreet advertising; no account required. English-language Wikipedia content only.
opsec: passive
opsecNote: You browse a public map/Wikipedia mashup and never touch the target's infrastructure, so this leaks nothing about your subject. Ordinary web hygiene (own IP is fine) suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party geographic search engine layering English Wikipedia over a map. Underlying facts trace to Wikipedia; the site itself is a small independent project.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Copernix
tags:
- Maps, Geolocation and Transport
- wikipedia
- geolocation
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# COPERNIX

> A geographic search engine that overlays English Wikipedia articles onto a world map so you can explore what's documented about any place.

## When to use
You have a `geolocation` or a place name and want fast context on the landmarks, streets, buildings, and notable sites around it — for example while geolocating a photo and trying to identify a monument, church, or attraction in frame. It combines free-text search with a map, so you can query "art deco buildings" or a specific landmark and see it pinned in context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://copernix.io/ in a browser.
2. Pan/zoom the map to your area of interest, or type a place name / feature into the search box.
3. Read the side panel: geotagged Wikipedia articles for the visible area appear as a list and as map pins.
4. Click a pin/article to read its Wikipedia summary and confirm the identity of a feature you're trying to match.
5. Pivot: use a confirmed landmark to anchor a photo geolocation, then cross-check street-level detail in a mapping tool.

## Inputs → Outputs
- **In:** `geolocation` / place name / free-text feature query
- **Out:** map-pinned, geotagged Wikipedia articles describing nearby `geolocation` features
- **Empty/negative result looks like:** few or no pins in view — the area simply has little geotagged Wikipedia coverage (common for rural/non-English regions), not that the place doesn't exist.

## Gotchas & OpSec
- English Wikipedia only — coverage is thin outside major English-documented places; a quiet residential street will have nothing.
- It surfaces notable/encyclopedic features, not addresses or people — it is context, not a locator.
- OpSec: fully passive; nothing reaches the target.

## Overlaps ("do both")
- Pairs with `[[bellingcat-openstreetmap-search]]` — Copernix gives encyclopedic context on landmarks; the OSM tool lets you geolocate by combining nearby feature types.

## Trust & verifiability
`trust: unverified` — a small independent site, but its content is sourced from English Wikipedia, so any specific claim should be confirmed against the underlying article.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | copernix |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
