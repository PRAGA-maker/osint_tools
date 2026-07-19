---
id: land-valuation-bermuda
name: Land Valuation - Bermuda
description: Use when you have a Bermuda property `address` (parish/road) or assessment number and want its official valuation record — returns the property `address`, assessment number, and rateable value.
url: http://www.landvaluation.bm
category: public-records
path:
- public-records
bestFor: Looking up the Bermuda Government's official land-valuation record for a property by parish/road/assessment number.
selectorsIn:
- address
selectorsOut:
- address
status: live
pricing: free
costNote: Free public government portal; personal use only (commercial use needs written permission). No account.
opsec: passive
opsecNote: Passive — you query a public government valuation list, not any individual. The department may log queries, but nothing is sent to a subject. Personal-use terms apply; do not scrape or reuse commercially.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Bermuda Government Land Valuation Department portal maintaining the statutory Valuation List for land-tax purposes; authoritative for valuation data.
missingPersonsRelevance: medium
coverage:
- bm
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Bermuda Land Valuation
- landvaluation.bm
tags:
- property
- public-records
- bermuda
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# Land Valuation - Bermuda

> Bermuda's official property valuation list — search a parish/road or assessment number to confirm a property exists and its rateable value.

## When to use
Your case touches a Bermuda property and you want to confirm it in the government record: verify an `address` exists, get its assessment number and annual rental/rateable value, and use the interactive map to pinpoint the parcel. Note the public interface searches by property, **not by owner name** — it will not return who owns a parcel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.landvaluation.bm.
2. Search by assessment number, or select a parish and optionally enter road name / building number / building name. Or use the interactive map.
3. Read the output: the matching property's `address`, assessment number, and valuation figure.
4. Pivot: use the confirmed address/parcel to cross-reference other Bermuda registries; owner identity must come from a different source (deeds/registry), not here.

## Inputs → Outputs
- **In:** a Bermuda `address` (parish + road/building) or assessment number
- **Out:** property `address`, assessment number, rateable/valuation figure
- **Empty/negative result looks like:** no match means the parish/road combination or assessment number is wrong — refine the road name or browse the map; it does not confirm the property doesn't exist.

## Gotchas & OpSec
- **No owner-name search** — this is valuation/property data only, not an ownership lookup; don't expect a person's name out of it.
- Personal-use licence: do not scrape or reuse commercially without permission.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Complements other Bermuda public registries — this confirms the property/valuation; pair with a deeds/companies registry for ownership.

## Trust & verifiability
`trust: trusted` — first-party government portal; valuation data is authoritative for land-tax purposes and citable directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | land-valuation-bermuda |
| category | public-records |
| selectorsIn → selectorsOut | address → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
