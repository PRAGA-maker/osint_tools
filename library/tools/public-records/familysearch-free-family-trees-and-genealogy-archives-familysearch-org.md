---
id: familysearch-free-family-trees-and-genealogy-archives-familysearch-org
name: FamilySearch • Free Family Trees and Genealogy Archives — FamilySearch.org
description: Use when you have a `name` and want family/genealogy records — returns relatives (`associate`), birth/marriage/death dates (`dob`) and historical documents from the world's largest free genealogy archive.
url: https://www.familysearch.org/en
category: public-records
path:
- public-records
bestFor: Free global genealogy research — family trees plus billions of indexed historical vital records.
selectorsIn:
- name
selectorsOut:
- associate
- dob
- name
- address
status: live
pricing: free
costNote: Free, run by a non-profit (The Church of Jesus Christ of Latter-day Saints). A free account/login is required to view most records and trees; no payment.
opsec: passive
opsecNote: You search historical/genealogical records and user-contributed trees; nothing reaches a living subject. Passive. A free account ties searches to an email — use a sock-puppet address. Be aware living persons are largely masked in shared trees for privacy.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: One of the largest and most reputable genealogy archives in the world. Indexed historical records are authoritative; user-submitted family trees are community-contributed and can contain errors — verify against the source documents.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- freebmd-org-uk
- ancestry
- alabama-deaths
- colorado-statewide-marriage-index
- family-search
- familysearch
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-guessing-a-name-variation
- familysearch-org
- familysearch-research-wiki
aliases:
- FamilySearch
- familysearch.org
tags:
- genealogy
- family
- vital-records
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# FamilySearch • Free Family Trees and Genealogy Archives — FamilySearch.org

> The world's largest free genealogy archive — billions of indexed historical records plus a shared family tree, for reconstructing a subject's family and lineage at no cost.

## When to use
You have a `name` and want to build out the person's family and history: relatives (`associate`s — parents, siblings, spouses, children), birth/marriage/death dates (`dob`), and links to scanned source documents (census, vital, church, immigration records) from around the world. Indispensable for genealogical/heir tracing, distinguishing same-name individuals by family context, and corroborating a historic identity — and it's free where Ancestry is paywalled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register (free) and sign in at https://www.familysearch.org/en.
2. Use **Search → Records** for indexed historical documents by `name` (+ dates/places), or **Family Tree** to explore the shared collaborative tree.
3. Open record hits: names, dates, places, and often a scanned image of the original document; note the source citation.
4. Follow relationships in the tree to map relatives, but treat user-submitted tree data as claims to confirm.
5. Pivot: dates/places feed other vital-record indexes (`[[freebmd-org-uk]]` for England & Wales); relatives feed people-search; a source document confirms a `dob`/`address`.

## Inputs → Outputs
- **In:** `name` (+ dates/places to narrow)
- **Out:** `associate`s (family relationships), `dob`/vital dates, historical `address`/place, confirmed `name`, and scanned source documents
- **Empty/negative result looks like:** no matching records/tree entries — the person may be too recent (living people are privacy-masked), the record not yet indexed, or a name variant. Absence isn't proof; try spellings, places, and related collections.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** (free) required to view most records — set up a sock-puppet account.
- OpSec: **passive** — historical records; living individuals are deliberately hidden in shared trees for privacy, so this is weak for *current* details and strong for lineage/history.
- User-contributed trees carry errors and duplications; always drop to the cited source document before trusting a date or relationship.

## Overlaps ("do both")
- Pairs with `[[freebmd-org-uk]]` (England & Wales civil index) and `[[ancestry]]` (broader/commercial records + trees) — FamilySearch is the free global backbone; regional indexes and Ancestry add depth and records it lacks. Cross-check trees against primary documents across all three.

## Trust & verifiability
`trust: trusted` — a highly reputable archive; its *indexed historical records* are authoritative, while its *shared trees* are community-built and error-prone. Verify any consequential fact against the linked original document rather than the tree summary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-free-family-trees-and-genealogy-archives-familysearch-org |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, dob, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
