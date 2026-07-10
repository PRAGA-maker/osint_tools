---
id: biographies-net
name: Biographies.net
url: https://www.biographies.net
category: people-search
path:
- people-search
description: Use when you have a `name` of a notable-ish person and want a biographical summary — returns birth/death `dob`, profession, family `associate`s and life-story facts.
bestFor: Getting a quick biographical sketch (dates, profession, family, notable facts) for a public or semi-public figure.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- name
status: live
pricing: free
costNote: Free to search and read; a free account is only needed to contribute or favourite entries. Part of the STANDS4 reference network.
opsec: passive
opsecNote: Passive read of a public biography database; nothing is disclosed to the subject and no login is needed to search. It only holds notable/semi-notable people, so it will not touch a private individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A collaboratively-edited reference site in the STANDS4 network; entries are aggregated/user-contributed, so treat facts as leads to corroborate rather than authoritative records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Biographies.net
- STANDS4 Biographies
tags:
- toddington
- curated-directory
- people-search
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Biographies.net

> A free, collaboratively-edited biography database — a fast sketch of a notable or semi-notable person's dates, profession, family and life story.

## When to use
You have a `name` for someone with at least a modest public profile and want a quick biographical baseline: birth/death years, profession, family members, and notable life facts. Useful for confirming which "John Smith" you're dealing with, seeding a timeline, or picking up family `associate` names — but it only covers people who have some notability, not private individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.biographies.net.
2. Search the `name` (or browse by profession/alphabet).
3. Read the entry: birth/death dates, profession category, family details, and the biographical narrative.
4. Treat facts as starting points — cross-check dates and relations against primary sources.
5. Pivot: a confirmed `dob` disambiguates same-name people elsewhere; family `associate` names feed genealogy/people-search; profession feeds targeted searches.

## Inputs → Outputs
- **In:** `name`
- **Out:** `dob` (birth/death), profession, family `associate`s, verified `name`/notable facts
- **Empty/negative result looks like:** no entry — extremely common, because only people with some public notability are covered. A miss means "not notable enough to be listed here," not that the person doesn't exist.

## Gotchas & OpSec
- Coverage is limited to notable/semi-notable figures; useless for ordinary private individuals.
- Entries are user-contributed and can be thin or inaccurate; corroborate before relying on any fact.
- OpSec: fully passive, no login to read, nothing disclosed to the subject.

## Overlaps ("do both")
- Pairs with Wikipedia and `[[familysearch-2]]` — Biographies.net gives a quick sketch, while those provide deeper sourcing and family records to verify it.

## Trust & verifiability
`trust: community` — a collaboratively-edited STANDS4 reference site; convenient for a first sketch but aggregated/user-supplied, so every fact should be confirmed against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | biographies-net |
| category | people-search |
| selectorsIn → selectorsOut | name → dob, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
