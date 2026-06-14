---
id: flash-earth-2
name: Flash Earth
description: Use when referencing the legacy flashearth.com satellite viewer — it relied on Adobe Flash and is effectively defunct; use zoom.earth instead.
url: http://www.flashearth.com
category: geolocation
path:
- geolocation
bestFor: Legacy multi-provider satellite viewer; superseded by zoom.earth.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
- image
status: down
pricing: free
costNote: Was free; original Flash-based site no longer functional.
opsec: passive
opsecNote: Would only render public map tiles; no target contact. Now non-functional, so not usable in practice.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The original Flash Earth at flashearth.com depended on Adobe Flash, which reached end-of-life in 2020/2021; the modern replacement is zoom.earth (see flash-earth).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
deprecated: true
aliases:
- flashearth.com
tags:
- geospatial-research-and-mapping-tools
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Flash Earth

> The original flashearth.com — an Adobe Flash-based viewer that let you flip one location across multiple satellite providers. Flash is dead, so this legacy site is effectively non-functional; the living replacement is zoom.earth.

## When to use
Historically you used it to compare a `geolocation` across NASA, Bing, and other imagery sources in one viewer. In practice today, skip it: use `[[flash-earth]]` (zoom.earth) for recent imagery or `[[google-earth]]`/`[[earthexplorer]]` for historical/high-res.

## How to use it (`bestInteractionPattern`: web-manual)
1. The flashearth.com URL no longer renders a working Flash viewer in modern browsers (Flash EOL).
2. Go to `[[flash-earth]]` (zoom.earth) for the maintained equivalent.
3. For multi-provider tile comparison, `[[dualmaps]]` provides synchronized Google/Bing views.

## Inputs → Outputs
- **In (historically):** `geolocation`/`address`.
- **Out (historically):** multi-source satellite `image`.
- **Empty/negative result looks like:** blank page or missing-plugin notice — expected, since Flash is no longer supported anywhere.

## Gotchas & OpSec
- Human-in-the-loop: none, but the tool itself is dead.
- Do not rely on this entry as a live capability; it is retained for lineage only.
- OpSec: moot — non-functional.

## Overlaps ("do both")
- Direct successor: `[[flash-earth]]` (zoom.earth). For provider comparison use `[[dualmaps]]`.

## Trust & verifiability
`trust: community` — was a well-known viewer, but the Flash dependency makes it defunct (`status: down`); verify any need via zoom.earth instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flash-earth-2 |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
