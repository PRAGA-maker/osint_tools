---
id: bmobile-in-india
name: bmobile.in (India)
description: Use when you have a 10-digit Indian mobile number and need its telecom operator and circle (region) to localise the subscriber.
url: https://bmobile.in
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
- phone
- india
- carrier
source: metaosint
lastVerified: '2026-06-13'
enrichment: full
---

# bmobile.in (India)

> Free Indian mobile-number lookup — turns a 10-digit Indian number into its telecom operator and circle (region), shown on a map. (Same service as `[[bmobile-in]]`, https URL.)

## When to use
You have an Indian `phone` number (starts 7/8/9) and want a rough `geolocation` (telecom circle/state) and the original operator to narrow where a subscriber is based or which carrier to focus on. Carrier/region enrichment, not subscriber-name identification.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://bmobile.in.
2. Enter the 10-digit Indian mobile number.
3. Read the result: telecom operator, circle (state/region), and an approximate map location (`geolocation` + number `metadata-exif`).
4. Pivot: the circle narrows the region for Indian people-search/social tools; the operator guides carrier-specific avenues.

## Inputs → Outputs
- **In:** `phone` (Indian, 10-digit)
- **Out:** `geolocation` (circle/region), `metadata-exif` (operator)
- **Empty/negative result looks like:** no match / invalid number for non-Indian or malformed inputs.

## Gotchas & OpSec
- MNP caveat (site's own disclaimer): after porting the *circle* stays correct but the *operator* may be wrong.
- Result is region-level only, not a precise address.
- India only.
- OpSec: passive; range/circle lookup, no contact to the subscriber.

## Overlaps ("do both")
- Duplicate of `[[bmobile-in]]` (same service, http URL) — use either. Pair with carrier-line tools for non-Indian numbers (`[[carrier-lookup]]`, `[[aql-com]]`).

## Trust & verifiability
`trust: community` — community-maintained Indian telecom site; reliable for region, subject to the MNP caveat for the operator field.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bmobile-in-india |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, metadata-exif (operator/circle) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
