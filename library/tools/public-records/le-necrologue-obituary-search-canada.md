---
id: le-necrologue-obituary-search-canada
name: Le Nécrologue (Canada Obituary Search)
description: Use when you have a `name` and want Canadian death notices/obituaries — returns `dob`/death date, `address` (city/province), funeral home and `associate` (surviving family).
url: https://www.lenecrologue.com
category: public-records
path:
- public-records
bestFor: Searching Canadian (Quebec-heavy) death notices to confirm a death and surface family, dates and location.
selectorsIn:
- name
selectorsOut:
- dob
- address
- associate
status: live
pricing: freemium
costNote: Historically free; since Sept 2025 many notices depend on funeral-home paid subscriptions, though basic browsing/search remains. No cost to search names.
opsec: passive
opsecNote: Public obituary database; searching is passive and the subject/family isn't notified. No login for basic search. Be mindful this concerns the recently deceased and grieving families — handle findings sensitively.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large Canadian obituary aggregator (1.2M+ notices); notices originate from funeral homes/families, so details are generally reliable but not an official vital record.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Le Necrologue
- lenecrologue.com
tags:
- toddington
- curated-directory
- specialty-search
- obituary
- death-records
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Le Nécrologue (Canada Obituary Search)

> A large Canadian death-notice database (1.2M+ obituaries, Quebec-heavy): search a name to confirm a death, get the date and place, and read out the surviving family named in the notice.

## When to use
You have a subject `name` with a Canadian connection and need to know whether they (or a relative) have died — a common resolution in missing-person and locate work — or you want to mine an obituary for `associate` links. Obituaries name surviving spouse, children, siblings and sometimes the town and funeral home, which both confirms an outcome and opens family pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lenecrologue.com and search by name (also filter by funeral home, city, or province).
2. Open a matching notice: death date, age, city/province, funeral home, and the list of surviving/predeceased family.
3. Note the death/birth dates (`dob`), the location (`address` = city/province), and family names (`associate`).
4. Since Sept 2025 some notices sit behind funeral-home subscriptions — cross-check the same obituary on the funeral home's own site or other aggregators if gated.
5. Pivot: run named family members through people-search; the funeral home + city anchors location; the death date closes or reframes the timeline.

## Inputs → Outputs
- **In:** `name` (+ optional city/province/funeral home)
- **Out:** death/birth `dob`, `address` (city/province), funeral home, `associate` (surviving family)
- **Empty/negative result looks like:** no notice — the person isn't deceased (or not recorded here), died outside Canada, or the notice is subscription-gated; absence is not proof they're alive, only that no notice was found.

## Gotchas & OpSec
- Canada-focused (strongest in Quebec); not a France/global database despite the French name.
- Not an official vital record — notices are family/funeral-home authored; corroborate a death via a second source before asserting it.
- Post-2025 subscription changes may hide some notices; use the funeral home's site as a fallback.
- Sensitive subject matter — handle family details with care.

## Overlaps ("do both")
- Pairs with other obituary aggregators and official vital-records/genealogy sources — cross-check to confirm the death and fill in family/date detail the notice omits.

## Trust & verifiability
`trust: community` — a reputable, large aggregator, but notices are family/funeral-home supplied, not government vital records; treat a match as a strong lead to confirm officially.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | le-necrologue-obituary-search-canada |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, address, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
