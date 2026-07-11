---
id: area-code-decoder-united-states
name: Area Code Decoder (United States)
description: Use when you have a US `phone` (or just its area code) and want the geographic region it maps to — returns the city/state/timezone the NANP area code covers.
url: http://decoder.americom.com
category: phone
path:
- phone
bestFor: Translating a US/NANP area code into its geographic region, timezone, and coverage.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free reference lookup; no account or payment.
opsec: passive
opsecNote: This is a static reference database of area-code-to-region mappings — you look up a code, nothing is sent to the number or its owner. Fully passive; no notification to anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing NANP area-code reference; the geographic mapping is accurate for the code's assigned region, but says nothing about where the current holder actually is (mobiles keep their number when they move).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Area Code Decoder
- decoder.americom.com
tags:
- toddington
- curated-directory
- telephone-numbers
- area-code
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Area Code Decoder (United States)

> A quick NANP reference — enter an area code and learn the city/state/timezone it was assigned to.

## When to use
You have a US `phone` and want a fast geographic read on it: which region the area code (and prefix) was originally assigned to, and the timezone. Useful for a rough origin/timezone signal and for sanity-checking a claimed location — with the big caveat that number portability and mobiles mean the area code reflects where the number was *issued*, not necessarily where the person is now.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `http://decoder.americom.com`.
2. Enter the 3-digit area code (or full number) and search.
3. Read the result: the city/state/region and timezone the code covers.
4. Treat it as origin/timezone context, not a current location.
5. Pivot: the region → narrows people-search and reverse-phone (`[[www-spydialer-com]]`) geographically; combine with `[[free-carrier-lookup]]` for line type.

## Inputs → Outputs
- **In:** `phone` / area code
- **Out:** `geolocation` (assigned city/state/region + timezone)
- **Empty/negative result looks like:** an unrecognized or unassigned code — likely a mistyped number or a non-geographic/toll-free code (800/888 etc.), which have no single region.

## Gotchas & OpSec
- Mobiles and ported numbers keep their original area code after the owner moves — the region is where the number *started*, not where they live now. Don't over-read it.
- Toll-free and VoIP numbers aren't geographic.
- OpSec: fully **passive** — a static reference lookup.

## Overlaps ("do both")
- Pairs with `[[free-carrier-lookup]]` (line type) and `[[www-spydialer-com]]` (owner) — area code gives origin/timezone, carrier-lookup gives line type, SpyDialer attempts the actual owner.

## Trust & verifiability
`trust: community` — an accurate reference for the code's *assigned* region; its limitation is interpretive (portability/mobiles), not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | area-code-decoder-united-states |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
