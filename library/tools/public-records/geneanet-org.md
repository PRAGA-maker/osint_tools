---
id: geneanet-org
name: geneanet.org
description: Use when you have a `name` and want genealogical records — ancestors, relatives, birth/death dates and places — returns `associate` (family), `dob`, and `address`/place links.
url: https://en.geneanet.org/
category: public-records
path:
- public-records
bestFor: Genealogy research — family trees and vital records, especially strong for France and continental Europe.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: freemium
costNote: Free to search and to view much shared-tree and index data with a free account; a Premium subscription unlocks full record images, some collections, and advanced search filters.
opsec: passive
opsecNote: Passive — you search user-contributed trees and record indexes; living people are generally masked, and no subject is notified. A free account is needed for most detail; register with a sock-puppet identity for sensitive work. Geneanet (owned by Ancestry) logs searches.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A major, long-established genealogy platform; index data derives from official vital records, but user-submitted family trees are unverified and can contain errors or speculation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- Geneanet
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- genealogy
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# geneanet.org

> One of Europe's largest genealogy platforms: search a name and reconstruct the family tree — parents, siblings, spouses, dates and places — with particular depth in France.

## When to use
You have a `name` and need the family/ancestry dimension: relatives (`associate`), birth/marriage/death dates (`dob`) and the towns/`address` places tied to a lineage. Useful in missing-persons and identity work to corroborate a subject's relatives, find surviving family to contact, confirm a date of birth, or place a family geographically — especially for French/continental-European roots that US-centric tools miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.geneanet.org/ and register a free account (needed for most detail).
2. Search the `name` (add approximate year/place to narrow); Geneanet searches both user family trees and record indexes.
3. Open a matching individual to see linked relatives, life dates, and places; note living people are usually hidden/anonymised.
4. For full record images or premium collections, a Premium subscription is required.
5. Pivot: relatives feed `[[familytree]]` (US) / directory searches; a confirmed `dob` disambiguates other records; places narrow local searches.

## Inputs → Outputs
- **In:** `name` (+ optional year/place)
- **Out:** `associate` (parents, siblings, spouses, descendants), `dob`/life dates, associated place/`address`, confirmed `name` spelling/variants
- **Empty/negative result looks like:** no tree or index match — the family isn't documented on Geneanet (common for non-European lineages or very recent generations), or living-person masking hides them. Not proof of anything.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** required for detail; premium paywall for record images.
- OpSec: **passive** — user trees and indexes; register with a puppet account. Living individuals are deliberately masked.
- User-submitted trees are **unverified** — cross-check names/dates against primary vital records before treating as fact.

## Overlaps ("do both")
- Pairs with `[[familytree]]` — Geneanet is strongest on European ancestry and historical vital records; FamilyTreeNow covers current US relatives/addresses. Run both to bridge past and present.

## Trust & verifiability
`trust: community` — a major, reputable platform, but its family-tree layer is crowd-sourced and error-prone. Index data traces to official records; confirm critical dates/relationships against the primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geneanet-org |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
