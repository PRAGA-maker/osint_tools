---
id: legacy-com
name: legacy.com
description: Use when you have a `name` and want to find a death notice or obituary — returns date of death, age, location, funeral home and surviving/predeceased family members.
url: https://www.legacy.com/search
category: public-records
path:
- public-records
bestFor: Searching the largest US obituary database to confirm a death and harvest family/associate links.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- address
- name
status: live
pricing: free
costNote: Free to search and read obituaries (40M+ records); optional paid extras (flowers, memorial products) are unrelated to the search.
opsec: passive
opsecNote: You search a public obituary aggregator, not the subject — no notification reaches anyone. Obituaries are published by families/funeral homes and are inherently public. Use a sock-puppet browser as routine hygiene; the content is sensitive (bereavement) so handle findings with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Legacy.com aggregates obituaries published by newspapers and funeral homes across the US and beyond; the death notices come from vetted publishers, though family-submitted detail can contain errors.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Legacy.com obituaries
- legacy.com/search
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- obituaries
- death-records
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- legacy
- obituaries-from-newspapers-north-america
---

# legacy.com

> The largest US obituary database — search a name to confirm a death and map the surviving family.

## When to use
You have a `name` and need to know whether the person has died, or you want to mine an obituary for the family network around a subject. A found obituary can resolve a missing-person case (confirming a death, with date and place) or, when the subject is alive, expose relatives named as survivors/predeceased — a rich source of `associate` links to living people you can pivot to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.legacy.com/search (or the /obituaries/search form).
2. Enter the `name`; narrow with location, death date, keyword, or newspaper if you have them.
3. Scan results — each entry shows name, age, date of death, and location; open the full obituary.
4. Read the obituary for: `dob`/age and date of death, city/`address` context, funeral home, and named family (`associate`s — spouse, children, siblings, parents), often with their current cities.
5. Pivot: named survivors feed people-search (`[[radaris-people-and-business-search-north-america]]`); a confirmed death date closes a whereabouts question; the funeral home can be contacted for service details.

## Inputs → Outputs
- **In:** `name` (+ optional location/date/newspaper)
- **Out:** date of death, age/`dob`, location/`address`, funeral home, family `associate`s
- **Empty/negative result looks like:** no matching obituary — the person may be alive, the family may not have published, or the notice ran only in a paper not indexed here. Absence is weak evidence, not proof of life.

## Gotchas & OpSec
- Coverage is broad but not total — many deaths get no published obituary, and some notices sit only in local papers or funeral-home sites Legacy doesn't index. Cross-check with `[[findagrave]]`-style and SSDI sources.
- Family-submitted detail can be imprecise (ages, relationships); corroborate before asserting.
- OpSec: **passive** and public, but the subject matter is bereavement — treat surviving relatives' details with discretion.

## Overlaps ("do both")
- Pairs with Find A Grave, SSDI/vital-records, and `[[rootsweb-2]]` — obituaries name the family and date the death; grave/vital records and trees corroborate and extend the genealogy. Do both to confirm and to build the associate graph.

## Trust & verifiability
`trust: trusted` — a reputable aggregator sourcing from newspapers and funeral homes, so the existence of a notice is reliable. The *content* is family-authored, so verify specific dates and relationships against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | legacy-com |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, associate, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
