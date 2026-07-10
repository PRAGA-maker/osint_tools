---
id: cyndi-s-list
name: Cyndi's List
description: Use when you have a `name` and a research locale and want to find the right genealogy database or record collection to search next — returns pointers to sources that yield `associate`, `dob`, and death records.
url: https://www.cyndislist.com
category: public-records
path:
- public-records
bestFor: A categorised directory of 300,000+ genealogy websites and record collections, used to find which database to search for a given place or record type.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
status: live
pricing: free
costNote: Free directory, funded by donations; some sites it links to are themselves paid or subscription (Ancestry, Findmypast, etc.).
opsec: passive
opsecNote: Browsing a link directory is passive and reaches nothing about the subject. OpSec exposure only begins when you follow a link into an actual records site — apply that site's precautions there, not here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A well-established, 25+ year genealogy directory (Cyndi Ingle) widely cited by researchers and libraries; it is a curated index of links, not a data source itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rootsweb-2
- usgenweb-archives-united-states
- findmypast
aliases:
- Cyndi's List of Genealogy Sites
- cyndislist.com
tags:
- genealogy
- family
- directory
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Cyndi's List

> The librarian's card-catalogue of online genealogy: 300,000+ curated links across 200+ categories, used to find the right record collection for a given place, surname, or record type.

## When to use
You have a `name` and a research locale or record type (a US county, a UK parish, "cemetery records", "orphan records", "immigration"), and you don't yet know which database holds what you need. Cyndi's List is the starting index: browse to the relevant category and it hands you the specialist sites to search. It is a **navigation aid**, not a database — it points you at where the records live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cyndislist.com.
2. Browse by category (place, record type, or surname) or use the site's alphabetical index; 232 categories are cross-referenced like a library catalogue.
3. Pick the collections that match your locale/record type and follow the links out to those sites.
4. Search the subject `name` on the destination site (some are free, some subscription).
5. Pivot: the destination records yield relatives (`associate`), birth/death dates (`dob`), and name confirmations that feed the rest of your family-tree work.

## Inputs → Outputs
- **In:** `name` plus a research locale/record-type to guide category selection
- **Out:** (indirectly, via the sites it links) `associate`, `dob`/death dates, `name` confirmations
- **Empty/negative result looks like:** Cyndi's List itself always returns categories; a "dead end" is really a linked site that has no record — evaluate coverage on the destination, not here.

## Gotchas & OpSec
- Human-in-the-loop: none here; it is browse-and-click. The linked sites may impose their own logins/paywalls.
- It holds **no records itself** — do not treat a Cyndi's List category page as evidence; it only routes you to sources.
- Some links are stale (the web churns); if a destination is dead, note the collection name and search for its current home.
- OpSec: passive at the directory; adopt the destination site's precautions once you click through.

## Overlaps ("do both")
- Use alongside `[[usgenweb-archives-united-states]]` and `[[rootsweb-2]]` — Cyndi's List helps you discover which of the many collections (including those two) to hit for a given place.
- Points you toward subscription giants like `[[findmypast]]` when free sources run out.

## Trust & verifiability
`trust: trusted` — a long-running, well-regarded curated directory. Trust applies to it being a faithful index; the reliability of any given record is a property of the destination site, which you must judge separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyndi-s-list |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
