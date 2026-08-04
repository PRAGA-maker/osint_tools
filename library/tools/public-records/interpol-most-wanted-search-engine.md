---
id: interpol-most-wanted-search-engine
name: Interpol Most Wanted Search Engine
description: Use when you have a `name` and want to check for an Interpol notice — returns wanted/notice hits with photo, physical description, and nationality where published.
url: https://cse.google.com/cse?cx=b1746754c83012613
category: public-records
path:
- public-records
bestFor: Screening a name against Interpol Red/Yellow Notice and most-wanted publications.
selectorsIn:
- name
selectorsOut:
- image
- physical-description
- name
status: live
pricing: free
costNote: Free Google Custom Search Engine scoped to Interpol/most-wanted sources; no account.
opsec: passive
opsecNote: Passive — you query a Google CSE over public notice pages; the subject is not contacted. Standard sock-puppet browsing hygiene applies if you don't want the searches tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An unofficial Google Custom Search Engine; the underlying data is Interpol's public notices, but a CSE's scope can drift or break. Cross-check against Interpol's official notice database.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Interpol wanted CSE
tags:
- wanted-persons
- law-enforcement
- public-records
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Interpol Most Wanted Search Engine

> A Google Custom Search Engine scoped to Interpol notices and most-wanted publications — a fast name-screen against internationally wanted persons.

## When to use
You have a `name` (or alias) and want to know whether the person is the subject of an Interpol notice or appears in most-wanted publications. Most directly relevant to fugitive/associate screening; for missing-persons work it also touches Interpol **Yellow Notices** (missing persons), making it a useful cross-check when a case may have an international dimension.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE: https://cse.google.com/cse?cx=b1746754c83012613.
2. Search the `name`/alias (try variant spellings and transliterations).
3. Review hits — notice pages typically carry a photo, physical description, nationality, and the offence/notice type.
4. **Confirm on the source of truth:** verify any hit against Interpol's official notices database (interpol.int → How we work → Notices), since a CSE can be stale or incomplete.
5. Pivot: a confirmed notice yields `image`, `physical-description`, and nationality to feed face-search and identity tools.

## Inputs → Outputs
- **In:** `name` / alias
- **Out:** `image` (mugshot/photo), `physical-description`, confirmed `name`/nationality from the notice
- **Empty/negative result looks like:** no results — meaning no matching notice was indexed, NOT proof the person has no notice (the CSE's coverage is unofficial and partial; confirm on interpol.int).

## Gotchas & OpSec
- It is an unofficial CSE: its index can drift or miss recent/removed notices — always corroborate on Interpol's official site.
- Notices are published in specific languages; search transliterations and native-script forms of the name.
- A notice is an allegation/record, not a conviction — handle findings carefully and lawfully.

## Overlaps ("do both")
- Pairs with sanctions/PEP screening (`[[opensanctions]]`, `[[openscreening]]`) — this covers wanted-person notices, those cover sanctions/PEP exposure; run both for a full "flags" pass.

## Trust & verifiability
`trust: community` — an unofficial search layer over authoritative Interpol data; treat hits as leads and verify each against Interpol's official notice database.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | interpol-most-wanted-search-engine |
| category | public-records |
| selectorsIn → selectorsOut | name → image, physical-description, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
