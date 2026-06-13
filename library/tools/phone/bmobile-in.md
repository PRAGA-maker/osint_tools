---
id: bmobile-in
name: bmobile.in
description: Use when you have a 10-digit Indian mobile number and need its telecom operator and circle (region) to localise the subscriber.
url: http://bmobile.in/
category: phone
path:
- phone
bestFor: Indian mobile number to operator + telecom circle (approximate region).
selectorsIn:
- phone
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free web lookup; ad-supported.
opsec: passive
opsecNote: Looks up the number's allocation range/circle; does not contact the handset.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run Indian telecom info site; circle/operator are derived from numbering ranges and may be wrong if the number was ported (MNP).
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
aliases:
- bmobile.in
tags:
- mobilephone
- Mobile & Phone Related
- india
- carrier
source: uk-osint
lastVerified: '2026-06-13'
enrichment: full
---

# bmobile.in

> Free Indian mobile-number lookup — turns a 10-digit Indian number into its telecom operator and circle (region), shown on a map.

## When to use
You have an Indian `phone` number (starts 7/8/9) and want a rough `geolocation` (telecom circle/state) and the original operator to narrow where a subscriber is based or which carrier to focus on. This is region/carrier enrichment, not subscriber-name identification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://bmobile.in/ (also reachable at https://bmobile.in).
2. Enter the 10-digit Indian mobile number.
3. Read the result: telecom operator, circle (state/region), and an approximate location on a map (`geolocation` + number `metadata-exif`).
4. Pivot: the circle narrows the search region for Indian people-search/social tools; the operator helps choose carrier-specific avenues.

## Inputs → Outputs
- **In:** `phone` (Indian, 10-digit)
- **Out:** `geolocation` (circle/region), `metadata-exif` (operator)
- **Empty/negative result looks like:** no match / invalid number for non-Indian or malformed inputs.

## Gotchas & OpSec
- MNP caveat (site's own disclaimer): the *circle* is still correct after porting, but the *operator* may be wrong if the subscriber kept their number across networks.
- Result is region-level, not a precise address — do not over-interpret the map pin.
- India only.
- OpSec: passive; range/circle lookup with no contact to the subscriber.

## Overlaps ("do both")
- Duplicate of `[[bmobile-in-india]]` (same service, https URL). Pair with carrier-line tools for non-Indian numbers (`[[carrier-lookup]]`, `[[aql-com]]`).

## Trust & verifiability
`trust: community` — community-maintained Indian telecom site; circle/operator come from numbering ranges and are reliable for region but subject to the MNP caveat for operator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bmobile-in |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, metadata-exif (operator/circle) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
