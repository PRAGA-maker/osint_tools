---
id: nanpa-area-code-query
name: NANPA Area Code Query
description: Use when you have a North American `phone` number (or just its area code) and want the authoritative region it belongs to — returns the `geolocation`/`address`-level area (state/province and locality) the NPA serves.
url: https://www.nationalnanpa.com/enas/npa_query.do
category: phone
path:
- phone
bestFor: Authoritatively mapping a US/Canada/Caribbean area code (NPA) to the geographic region it serves.
selectorsIn:
- phone
selectorsOut:
- geolocation
- address
status: live
pricing: free
costNote: Free official government-contractor service. No account, no payment.
opsec: passive
opsecNote: You query a static numbering-plan database about an area code, not the subscriber. Nothing touches the target's line and the person is never contacted or notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the North American Numbering Plan Administrator (the official NANP administrator). This is authoritative allocation data, not a crowd-sourced guess.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fcc-io
- the-directory-area-code-listings-worldwide
- nanpa-area-code-map
aliases:
- NANPA NPA query
- nationalnanpa area code lookup
tags:
- phone
- area-code
- numbering-plan
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# NANPA Area Code Query

> The official North American Numbering Plan lookup: enter an area code (NPA) and get the authoritative geographic region, dialing plan, and status it's assigned to.

## When to use
You have a `phone` number in the North American Numbering Plan (US, Canada, and participating Caribbean territories) and need to place its `area code` geographically with authority — which state/province and region the NPA serves, whether it's a geographic or non-geographic (toll-free/service) code, and its dialing rules. This narrows a `geolocation` for a number and flags when an area code is *not* tied to a place (e.g. toll-free 800/888, which tells you the number gives no location signal).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the NPA Query report at https://www.nationalnanpa.com/enas/npa_query.do (part of nationalnanpa.com).
2. Enter the three-digit `area code` (NPA) from the target `phone` number.
3. Read the result: the geographic area served (state/province, region), the NPA's type and status, in-service date, and associated dialing plan.
4. Cross-check against the broader area-code database or maps if you need locality detail below state level.
5. Pivot: the region narrows where the subscriber likely registered the line; combine with carrier/HLR lookups and `[[fcc-io]]` for further phone context.

## Inputs → Outputs
- **In:** `phone` (specifically its three-digit NPA / area code)
- **Out:** `geolocation`/`address`-level region (state/province + area) the code serves, plus NPA type/status
- **Empty/negative result looks like:** the code returns as unassigned/reserved, or as a non-geographic/toll-free code — meaning the area code carries no residential-location signal, not that the query failed.

## Gotchas & OpSec
- Human-in-the-loop: none; a simple database query.
- OpSec: **passive** — you look up an area code, never the subscriber. Nothing reaches the target.
- Area codes only localise to region/state, and number portability plus mobile numbers mean the holder may live nowhere near the NPA's geography. Treat it as a weak prior, not a location.

## Overlaps ("do both")
- Pairs with `[[fcc-io]]` and `[[the-directory-area-code-listings-worldwide]]` — NANPA is the authoritative source for the *allocation* of North American codes, while those add carrier/context and international coverage. Use NANPA to confirm the official assignment, the others to enrich.

## Trust & verifiability
`trust: trusted` — this is the North American Numbering Plan Administrator's own query tool, so the code-to-region mapping is authoritative. The caveat is analytical, not data-quality: an area code is a weak locator once portability and mobile are in play.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nanpa-area-code-query |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
