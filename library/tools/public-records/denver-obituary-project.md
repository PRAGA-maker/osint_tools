---
id: denver-obituary-project
name: Denver Obituary Project
description: Use when you have a `name` of someone who may have died in Colorado (outside Denver) between the 1970s and 1990 and want their obituary — returns an index entry pointing to the published obituary.
url: https://history.denverlibrary.org/research-tool/denver-obituary-project
category: public-records
path:
- public-records
bestFor: Locating Colorado (non-Denver) obituaries from ~1970s–1990 to confirm a death and pull family/biographical detail.
selectorsIn:
- name
selectorsOut:
- name
- associate
- dob
status: live
pricing: free
costNote: Free research tool hosted by Denver Public Library; no account or payment to search the index.
opsec: passive
opsecNote: Searching a library obituary index contacts no one and is fully passive. Records are historical (pre-1990), so living-person PII exposure is minimal. Use a sock-puppet browser only if you care about not logging searches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hosted by the Denver Public Library (Western History/Genealogy); an authoritative library research index. It is an INDEX of ~50,000 obituaries — you may need to retrieve the full obituary from the cited source.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Denver Public Library Obituary Project
- Colorado obituary index
tags:
- toddington
- curated-directory
- specialty-search
- obituaries
- genealogy
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Denver Obituary Project

> A Denver Public Library index of roughly 50,000 Colorado obituaries from the 1970s to 1990 (statewide, excluding Denver itself) — a targeted way to confirm an older Colorado death and its family detail.

## When to use
You have a `name` and reason to think the person died in Colorado outside Denver between the 1970s and 1990. This index locates the obituary, which confirms the death and typically yields age/`dob`, locality and surviving relatives (`associate`). Best for cold cases, deceased-relative research to extend a family tree, and confirming a death that predates the big online obituary aggregators.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://history.denverlibrary.org/research-tool/denver-obituary-project.
2. Search the index by `name` (surname; try variants).
3. Read the index entry and note the source citation (newspaper/date) it points to.
4. Retrieve the full obituary from the cited source if the index alone doesn't carry the detail you need (library staff can help).
5. Pivot: named survivors are `associate` leads; age/date approximates a `dob`; locality narrows other Colorado record searches.

## Inputs → Outputs
- **In:** `name`
- **Out:** index entry → obituary confirming death, approximate `dob`/age, family `associate`s, locality
- **Empty/negative result looks like:** no entry — the person died in Denver proper (explicitly excluded), outside the 1970s–1990 window, outside Colorado, or the name is spelled differently. Absence is scope-limited, not proof of life.

## Gotchas & OpSec
- Scope is narrow: Colorado, ~1970s–1990, and explicitly EXCLUDES Denver itself — use other tools for Denver deaths or other eras.
- It's an index; the full obituary may require pulling the cited newspaper.
- Spelling/transcription variance — try name variants.

## Overlaps ("do both")
- Pairs with Find A Grave, newspapers.com obituary searches and the Colorado state death index — this index uniquely covers a specific Colorado window; the others add Denver, other eras and full text.

## Trust & verifiability
`trust: trusted` — a public-library research index; authoritative as a finding aid, with the caveat that it points to obituaries you may need to retrieve in full.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | denver-obituary-project |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
