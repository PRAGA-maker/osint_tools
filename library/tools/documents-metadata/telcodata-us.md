---
id: telcodata-us
name: TelcoData.US
description: Use when you have a US/Canada `phone` (or an NPA-NXX prefix) and want the carrier, rate center, and switch behind it — returns employer-org (carrier) and geolocation (rate center) leads.
url: https://www.telcodata.us/
category: documents-metadata
path:
- documents-metadata
bestFor: Resolving a North American phone number or NPA-NXX prefix to its carrier, rate center, and switching data.
selectorsIn:
- phone
selectorsOut:
- employer-org
- geolocation
status: live
pricing: freemium
costNote: Free lookups for area codes, exchanges (NPA-NXX), and rate centers via the web interface. Bulk downloads, CSV upload, API access, and the "Number Sleuth" reports require a paid subscription.
opsec: passive
opsecNote: Queries hit TelcoData's own numbering database, not the subscriber's line — the phone's owner is never contacted or alerted. This reveals the carrier/rate-center of a number, not the person; do not confuse the original carrier with the current one after porting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-running independent telecom database rebuilt from public FCC/NANPA numbering data; carrier data can lag number portability.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telcodata-us-area-code-search
aliases:
- Telco Data US
- US Telecommunications Database
tags:
- phone
- carrier-lookup
- rate-center
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# TelcoData.US

> A public North American numbering database: turn a phone number or NPA-NXX prefix into its carrier, rate center, and switch details.

## When to use
You have a US/Canada `phone` number (or just its area code + exchange) and want to know which carrier the block was assigned to, what geographic rate center it belongs to, and the switching infrastructure behind it. Good for placing a landline/original-assignment region, distinguishing mobile vs landline blocks, and building context around a number before a deeper people-search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.telcodata.us/.
2. Use the area-code / exchange lookup: enter the NPA (area code) and NXX (prefix) of the target `phone`, or drill down by carrier/location.
3. Read the result: assigned carrier/OCN, rate center (city/state), LATA, and switch (CLLI) with coordinates (`selectorsOut`).
4. Pivot: the rate center gives an approximate geographic origin; the carrier feeds phone-validation and reverse-lookup tools. Bulk/API work needs the paid tier.

## Inputs → Outputs
- **In:** `phone` (or NPA-NXX prefix)
- **Out:** `employer-org` (assigning carrier/OCN), `geolocation` (rate center + switch coordinates), LATA/CLLI metadata
- **Empty/negative result looks like:** an unassigned or reserved block returns no carrier — meaning the prefix isn't in service, not that the specific number is invalid.

## Gotchas & OpSec
- Human-in-the-loop: none for basic lookups; a subscription gate blocks bulk export, CSV, and API.
- OpSec: passive — you query a reference database, so the number's owner is never touched.
- Number portability: the listed carrier is the block's *original* assignee and may not be the number's *current* carrier. Use a live HLR/portability check when the current carrier matters.

## Overlaps ("do both")
- Pairs with [[telcodata-us-area-code-search]] — same provider, focused on the area-code/prefix drill-down. Cross-check with a live phone-validation/HLR service to catch ported numbers TelcoData won't show.

## Trust & verifiability
`trust: unverified` — an independent site built from public FCC/NANPA numbering allocations; the raw assignment data is reliable, but it does not reflect real-time porting, so treat carrier as "originally assigned."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telcodata-us |
| category | documents-metadata |
| selectorsIn → selectorsOut | phone → employer-org, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
