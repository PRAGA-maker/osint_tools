---
id: mapjam
name: MapJam
description: Use when you want to make a simple stylized custom map with points of interest — a basic map maker that appears defunct; verify before relying on it.
url: http://mapjam.com
category: geolocation
path:
- geolocation
bestFor: Creating a simple stylized custom map with labeled points of interest (legacy/likely defunct map maker).
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: down
pricing: free
costNote: Was a freemium map-making site; the service appears inactive — confirm it loads before use.
opsec: passive
opsecNote: You would plot points you supply; no lookups against any target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legacy custom-map maker; the domain appears inactive, so treat as unavailable until confirmed live.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- geospatial-research-and-mapping-tools
- custom-maps
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MapJam

> Legacy maker of simple stylized custom maps with labeled points — appears defunct; treat as unavailable unless you confirm it loads.

## When to use
In principle, when you want a clean branded/stylized map with a handful of labeled `geolocation`/`address` points for a briefing or sharing. In practice the service appears inactive, so this is a low-value entry: use a current no-code mapper (`[[maphub]]`, Google My Maps) instead. It was a presentation tool and never an investigative data source, so its relevance to locating a person is low even if it were live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Attempt to open http://mapjam.com. If it does not load, stop and use a live alternative such as `[[maphub]]`.
2. (If live) create an account, add labeled markers for your points of interest, pick a style.
3. Export/share the resulting map.

## Inputs → Outputs
- **In:** `geolocation`/`address` (points you add)
- **Out:** `geolocation` (a styled custom map)
- **Empty/negative result looks like:** the site fails to load — the most likely outcome; verify availability first.

## Gotchas & OpSec
- Strong likelihood the service is defunct; do not present it as working without confirming the page loads.
- A styling/presentation tool only — no data, no lookups.
- OpSec: passive.

## Overlaps ("do both")
- Fully superseded by `[[maphub]]` and Google My Maps for no-code custom maps.

## Trust & verifiability
`trust: unverified` — a legacy map maker whose domain appears inactive. Marked `status: down` pending a live check; prefer a maintained alternative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mapjam |
| category | geolocation |
| selectorsIn → selectorsOut | geolocation, address → geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
