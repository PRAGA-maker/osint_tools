---
id: nanpa-area-code-map
name: 'NANPA : Area Code Map'
description: Use when you have a US/Canada `phone` number and want the geographic region its area code maps to — returns geolocation (the region/state served by that code).
url: https://www.nationalnanpa.com/area_code_maps/ac_map_static.html
category: phone
path:
- phone
bestFor: Mapping a North American area code to the geographic region/state it serves.
selectorsIn:
- phone
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official reference maintained by the North American Numbering Plan Administrator.
opsec: passive
opsecNote: A static reference lookup — nothing is sent about the subject; you are reading a public map. Fully anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by NANPA, the official administrator of the North American Numbering Plan; area-code-to-region assignments are authoritative.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nanpa-area-code-lookup
- twilio-lookup
aliases:
- NANPA area code map
- North American area code map
tags:
- phone
- area-code
- geolocation
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# NANPA : Area Code Map

> The official North American area-code map: convert the first three digits of a US/Canada number into the geographic region it was assigned to.

## When to use
You have a US or Canadian `phone` number and want a quick, authoritative read on where its area code is based — a coarse `geolocation` anchor that helps corroborate a subject's stated location, narrow a search region, or flag a number that doesn't match the claimed area. It's a reference map, not a subscriber lookup: it tells you the region a code serves, not who holds the number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nationalnanpa.com/area_code_maps/ac_map_static.html.
2. Take the 3-digit area code from the number (the digits after the +1 country code).
3. Locate that code on the map (or the per-state/province index) to read the geographic region it serves.
4. Note that many codes overlay a metro area rather than a whole state — treat it as regional, not pinpoint.
5. Pivot: combine with a carrier/line-type lookup (mobile numbers are portable and less tied to geography) and with people-search filtered to that region.

## Inputs → Outputs
- **In:** `phone` (specifically its area code)
- **Out:** `geolocation` (region/state/province served), a rough `address` region
- **Empty/negative result looks like:** the code is a non-geographic/toll-free code (800, 888, 877, 866, etc.) or an unassigned code — those carry no location signal.

## Gotchas & OpSec
- **Number portability breaks the geography link**: mobile users keep their number when they move, so the area code reflects where the number was *issued*, not where the person is now.
- Toll-free and special-service codes have no geography.
- Overlay codes mean an area can have several codes; don't over-narrow.
- OpSec: passive; a static map, no queries leave your machine.

## Overlaps ("do both")
- Pairs with a live carrier/line-type lookup like [[twilio-lookup]] — the map gives issued-region; a HLR/carrier lookup gives current carrier and whether the line is mobile (and thus portable), which together are far stronger than either alone.

## Trust & verifiability
`trust: trusted` — it is the numbering-plan administrator's own map, so area-code-to-region assignments are authoritative; the limitation is portability, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nanpa-area-code-map |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
