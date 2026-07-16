---
id: obituaries-from-newspapers-north-america
name: Legacy.com Obituaries (North America)
description: Use when you have a `name` and want obituary/death notices — returns death dates, hometowns and named surviving relatives from North American newspaper obituaries.
url: https://www.legacy.com/
category: public-records
path:
- public-records
bestFor: Finding a person's obituary to confirm a death and harvest family members, hometown and life details from newspaper death notices.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- geolocation
- name
status: live
pricing: free
costNote: Searching and reading obituaries is free; Legacy aggregates death notices from thousands of North American newspapers.
opsec: passive
opsecNote: You search published obituaries; no living person is contacted. Obituaries name living relatives, though — treat that family data responsibly and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Legacy.com is the main aggregator of US/Canada newspaper obituaries; notices are family-submitted, so details are usually accurate but occasionally incomplete or with variant spellings.
missingPersonsRelevance: high
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- billiongraves-com
- legacy
- legacy-com
aliases:
- Legacy.com
- newspaper obituaries
tags:
- toddington
- genealogy
- obituaries
- death-records
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Legacy.com Obituaries (North America)

> The main aggregator of US and Canadian newspaper obituaries — search a `name` to confirm a death and mine the notice for surviving relatives, hometown, and biographical detail.

## When to use
You have a `name` and want to confirm whether the person (or a relative) has died, and to extract the rich family/biographical data obituaries carry. Death notices routinely list the deceased's hometown, birth/death dates, workplace, and — crucially — **named surviving family members** (spouse, children, siblings, sometimes their cities). That makes obituaries one of the best sources for mapping a family network and anchoring a person to a place, whether the subject is the deceased or a listed relative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the `name` at https://www.legacy.com/ (add a state/city or date if known); also try Google `site:legacy.com "<name>"`.
2. Open the obituary: read death/birth dates, hometown, and the list of surviving/predeceased relatives with their locations.
3. Note the newspaper and funeral home (both are geographic/timeline anchors).
4. Extract each named relative as a fresh lead.
5. Pivot: relative `associate` names + cities feed people-search; the hometown is a `geolocation` anchor; confirm burial/dates via `[[billiongraves-com]]`.

## Inputs → Outputs
- **In:** `name`
- **Out:** `dob`/death dates, named family `associate`s (often with cities), hometown `geolocation`, and confirmed `name`
- **Empty/negative result looks like:** no obituary — the person may be living, have no published notice, or be recorded under a variant name/another aggregator; absence isn't proof of anything.

## Gotchas & OpSec
- Coverage is **North America** and depends on the newspaper publishing to Legacy; a missing notice is common.
- Notices are family-written — usually accurate but can omit estranged relatives or use nicknames/variant spellings.
- OpSec: passive, but obituaries expose **living** relatives — handle that data responsibly.

## Overlaps ("do both")
- Pairs with `[[billiongraves-com]]` — the obituary gives family/biography; the grave record adds GPS burial location and headstone dates. Do both to confirm a death and map the family.

## Trust & verifiability
`trust: community` — a comprehensive aggregator of family-submitted notices; generally reliable, but corroborate critical dates/relationships against a register or grave record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | obituaries-from-newspapers-north-america |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, associate, geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
