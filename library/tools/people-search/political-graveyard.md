---
id: political-graveyard
name: The Political Graveyard
description: Use when you have a `name` of a US political figure (or their relative) and want biographical and burial data — returns life dates, offices held, family links and cemetery/burial location.
url: http://politicalgraveyard.com/index.html
category: people-search
path:
- people-search
bestFor: Biographical, family and burial-location lookups for people who held or ran for US public office (and their kin).
selectorsIn:
- name
selectorsOut:
- associate
- address
- dob
status: live
pricing: free
costNote: Free to search and browse; no account or payment.
opsec: passive
opsecNote: A static public biographical database — searching contacts no one and leaves no trace with any subject. No account required. Records are historical/public-figure data, so PII sensitivity is low.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running, single-author labour-of-love database (Lawrence Kestenbaum) covering people connected to US politics. Well-known and broadly reliable for public figures, but hobbyist-maintained — corroborate specific facts.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Political Graveyard
- politicalgraveyard.com
tags:
- toddington
- curated-directory
- people-search
- biography
- burial
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# The Political Graveyard

> A niche but deep database of Americans connected to public office — the go-to for a politician's life dates, offices, family ties and, distinctively, where they're buried.

## When to use
You have a `name` that belongs to a US officeholder, candidate, or one of their relatives, and you want biographical anchoring: birth/death dates, positions held, party, and burial location. Its standout value is genealogical and burial data — it maps family relationships between political figures and pins cemetery locations, useful for confirming a death, dating a person, or bridging into a family tree. Only covers people with a political connection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://politicalgraveyard.com/ and use the name index / search.
2. Enter the `name`; open the matching biographical entry.
3. Read: life dates (`dob`/death), offices and dates, party, relatives cross-linked as `associate`s, and the cemetery/burial `address`.
4. Follow the family cross-links to related political figures.
5. Pivot: burial location feeds Find A Grave / obituary corroboration; relatives feed people-search and genealogy; dates anchor other record searches.

## Inputs → Outputs
- **In:** `name` (must have a US political connection)
- **Out:** `dob`/death dates, offices held, family `associate` links, burial `address` (cemetery)
- **Empty/negative result looks like:** no entry — the person never held/sought office and isn't a relative of someone who did, so they're simply out of scope. Absence here is expected for ordinary people, not meaningful.

## Gotchas & OpSec
- Scope is strictly political figures (and kin) — it is NOT a general people-search; most subjects won't appear.
- Single-hobbyist maintained; broadly reliable but corroborate specific dates/relationships.
- Coverage skews historical; very recent figures may be thin.

## Overlaps ("do both")
- Pairs with Find A Grave, Wikipedia and obituary sources — Political Graveyard uniquely ties political families together and records burials, while those add breadth and recency.

## Trust & verifiability
`trust: community` — a respected, long-standing hobbyist database; treat it as a strong lead source for public figures and confirm individual facts against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | political-graveyard |
| category | people-search |
| selectorsIn → selectorsOut | name → associate, address, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
