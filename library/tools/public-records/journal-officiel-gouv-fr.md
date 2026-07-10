---
id: journal-officiel-gouv-fr
name: journal-officiel.gouv.fr (Associations)
description: Use when you have a French association `name`, person, or `address` and want the official register — returns declared non-profit associations, their `address`, purpose, and officers (`associate`).
url: https://www.journal-officiel.gouv.fr/pages/associations-recherche/?sort=cronosort&disjunctive.source
category: public-records
path:
- public-records
bestFor: Searching France's official register of declared associations (non-profits) for a body's existence, address, and officers.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free official French government (Journal Officiel / DILA) search; no account needed.
opsec: passive
opsecNote: Searching a public official register is passive and does not notify anyone. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party French government publication (Direction de l'information légale et administrative); the register of declared associations is authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pappers-fr
- infogreffe-fr
aliases:
- Journal Officiel Associations
- JOAFE
- journal-officiel.gouv.fr
tags:
- companysites
- Company Related Sites
- france
- associations
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# journal-officiel.gouv.fr (Associations)

> France's official gazette search for declared associations (non-profits) — confirm a French association exists and pull its registered address, stated purpose, and the officers behind it.

## When to use
Your subject is linked to a French association (club, charity, NGO, community body) and you want the official record: the association's `name`, registered `address`, declared purpose, and — via publication notices — the officers who founded or run it (`associate`). This ties a person to an organisation and location, and can reveal a network of co-officers. (For commercial companies, use the company registries instead.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Journal Officiel Associations search (journal-officiel.gouv.fr, associations-recherche).
2. Search by association `name`, `address`/locality, or keyword; sort by date as needed.
3. Open a matching declaration/notice: it shows the association's name, registered office `address`, object/purpose, and dates.
4. Read officer-change and creation notices for named officers (`associate`).
5. Pivot: officer names feed people-search; for a French *company* rather than an association, pivot to `[[pappers-fr]]` / `[[infogreffe-fr]]`.

## Inputs → Outputs
- **In:** association `name`, `address`, or `employer-org` keyword
- **Out:** association `name`, registered `address`, purpose, and officers (`associate`)
- **Empty/negative result looks like:** no matching association — check spelling, or the body may be a company (not an association) or unregistered/informal; absence here doesn't rule out other French registries.

## Gotchas & OpSec
- Covers **associations** (loi 1901 non-profits), not commercial companies — use `[[pappers-fr]]`/`[[infogreffe-fr]]` for firms.
- Officer detail comes from publication notices, which vary in completeness by era.
- French-language interface and records.
- OpSec: passive; an official public register, no notification.

## Overlaps ("do both")
- Complements `[[pappers-fr]]` and `[[infogreffe-fr]]` (French companies) — a subject's French footprint may span both associations and companies; check each.

## Trust & verifiability
`trust: trusted` — a first-party French government publication, so association records are authoritative. Officer completeness depends on the notices published; corroborate individuals via people-search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | journal-officiel-gouv-fr |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
