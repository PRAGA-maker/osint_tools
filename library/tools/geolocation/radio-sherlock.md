---
id: radio-sherlock
name: Radio-Sherlock
description: Use when you have a radio callsign/term and want related amateur-radio data — returns search results across DX/ham-radio sources, useful for locating operators.
url: http://dxmaps.com/search.html
category: geolocation
path:
- geolocation
bestFor: Searching amateur/professional radio content — callsigns, DX spots, and propagation references.
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free search interface on DXMaps; the wider DXMaps site offers free real-time propagation maps.
opsec: passive
opsecNote: Passive search over public radio/DX data — no target interaction. Amateur-radio callsigns are inherently public (licences are on public registers), but they can tie to a real name and location, so treat the linkage carefully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of DXMaps (by EA6VQ), a long-running, respected amateur-radio propagation site; the search aggregates public radio-hobby sources rather than an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- DXMaps search
- Radio Sherlock
tags:
- amateur-radio
- callsign
- geolocation
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Radio-Sherlock

> A search engine for the amateur/professional radio world, hosted on DXMaps — look up callsigns and radio topics across ham-radio sources.

## When to use
An investigation touches amateur radio — you have a callsign, an operator handle, or a radio-related term and want to find associated activity, DX spots, or references. Because ham licences are public and often list a real name and location, a callsign can be a genuine identity/`geolocation` pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://dxmaps.com/search.html.
2. Enter the callsign, operator name, or radio subject and search.
3. Review the aggregated results linking to radio-hobby sources, spots, and references.
4. Pivot: a callsign feeds public callsign registries (e.g. QRZ.com, national licence databases) which frequently list the operator's name and address (`geolocation`); DX spots feed time/location of activity.

## Inputs → Outputs
- **In:** a callsign, operator `name`, or radio term
- **Out:** radio-hobby search results; via callsign registries, an operator's `geolocation`/name
- **Empty/negative result looks like:** no results — the term/callsign isn't referenced in the indexed radio sources; try a dedicated callsign registry directly.

## Gotchas & OpSec
- It's a search over hobby sources, not the authoritative licence registry — use QRZ/national databases to confirm operator identity.
- Callsign→person links are strong (licences are public) but can be outdated (address changes, club calls, vanity calls).
- Niche: only relevant when radio is actually part of the case.

## Overlaps ("do both")
- Pairs with callsign registries (QRZ.com, national licence lookups) — Radio-Sherlock surfaces activity/references, while registries resolve the callsign to a licensed name and address.

## Trust & verifiability
`trust: community` — hosted on a reputable long-running amateur-radio site, but it aggregates hobby sources; confirm any identity via the official callsign registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radio-sherlock |
| category | geolocation |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
