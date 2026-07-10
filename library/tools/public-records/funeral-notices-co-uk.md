---
id: funeral-notices-co-uk
name: funeral-notices.co.uk
description: Use when you have a `name` and want a UK death/funeral notice — returns date of death, location, funeral details and named family members.
url: https://funeral-notices.co.uk/national
category: public-records
path:
- public-records
bestFor: Searching UK funeral and death notices to confirm a death and harvest family/associate links.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- address
- name
status: live
pricing: free
costNote: Free to browse and search notices and leave tributes; placing a notice has paid options (public vs funeral-director rates).
opsec: passive
opsecNote: You search a public notices archive — no notification reaches anyone. Notices are published by families and funeral directors and are inherently public. Use a sock-puppet browser; the subject matter is bereavement, so handle surviving-relative details with discretion.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large UK funeral-notices aggregator (5M+ notices) fed by newspapers and funeral directors; the notices come from vetted publishers, though family-submitted detail can vary.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Funeral Notices
- funeral-notices.co.uk
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- obituaries
- death-records
- uk
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# funeral-notices.co.uk

> The UK counterpart to obituary search — 5M+ funeral and death notices you can search by name to confirm a death and map the surviving family.

## When to use
You have a `name` connected to the UK and need to know whether the person has died, or you want to mine a death/funeral notice for the family network around a subject. A found notice can resolve a missing-person case (confirming a death with date and place) or, when the subject is alive, name relatives as mourners — living `associate`s you can pivot to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://funeral-notices.co.uk/national in a sock-puppet browser.
2. Search by deceased `name`; narrow by region (North West, Scotland, Wales, etc.) or local newspaper if known.
3. Open the matching notice.
4. Read it for: date of death/age (`dob` context), location/`address` clues, funeral arrangements and funeral director, and named family (`associate`s — spouse, children, siblings), often with locations.
5. Pivot: named survivors feed people-search; a confirmed death date closes a whereabouts question; the funeral director can hold further detail.

## Inputs → Outputs
- **In:** `name` (+ optional region/newspaper)
- **Out:** date of death, age/`dob`, location/`address`, funeral details, family `associate`s
- **Empty/negative result looks like:** no matching notice — the person may be alive, the family didn't publish, or the notice appeared only in an unindexed outlet. Absence is weak evidence, not proof of life.

## Gotchas & OpSec
- Coverage is broad for the UK but not total — many deaths have no published notice, or only in local titles not indexed here. Cross-check with `[[legacy-com]]`, national records, and local newspapers.
- Family-submitted detail can be imprecise; corroborate dates/relationships.
- OpSec: **passive** and public, but bereavement is sensitive — treat surviving relatives' details discreetly.

## Overlaps ("do both")
- Pairs with `[[legacy-com]]` (broader/US obituaries), UK death-record indexes, and `[[rootsweb-2]]` — notices name the family and date the death; official records and trees corroborate and extend the genealogy. Do both to confirm and to build the associate graph.

## Trust & verifiability
`trust: community` — a reputable aggregator sourcing from newspapers and funeral directors, so the existence of a notice is reliable; the content is family-authored, so verify specific dates/relationships against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | funeral-notices-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → dob, associate, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
