---
id: familysearch-research-wiki
name: Familysearch Research Wiki
description: Use when you have a `name` and a place/era and want to know which genealogical records exist and where to find them — returns pointers to record sets and relatives leads.
url: https://www.familysearch.org/en/wiki/Main_Page
category: search-engines
path:
- search-engines
bestFor: A free how-to guide (156k+ articles) that tells you what birth/marriage/death/census records exist for a given place and how to access them.
selectorsIn:
- name
selectorsOut:
- associate
- document-id
status: live
pricing: free
costNote: Completely free; content is Creative Commons (CC BY-SA). A free FamilySearch account is optional and only needed to reach some linked record images.
opsec: passive
opsecNote: Read-only reference reading; nothing is disclosed to any subject. Safe from any browser. The optional account is tied to FamilySearch (LDS) if you register.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by FamilySearch (a reputable genealogy non-profit) but community-edited; it's a research guide, so verify against the actual record sets it points to.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- family-search
- familysearch
- familysearch-org
- alabama-deaths
- colorado-statewide-marriage-index
- familysearch-2
- familysearch-births-and-baptisms-1972-1981-australia
- familysearch-deaths-and-burials-1816-1980-australia
- familysearch-free-family-trees-and-genealogy-archives-familysearch-org
- familysearch-guessing-a-name-variation
aliases:
- FamilySearch Research Wiki
- FamilySearch Wiki
tags:
- toddington
- curated-directory
- genealogy
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Familysearch Research Wiki

> A giant, free genealogy how-to guide: for a place and record type, it tells you what records exist and how to reach them.

## When to use
You're building a family/relatives picture around a `name` and need to know which records to chase in a given country/state/county and era — birth, marriage, death, census, church, immigration — and where those record sets live (which archive, which online collection, what's digitized). This is a research **guide**, not a search of individuals; it points you at the record sets you then query for actual people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familysearch.org/en/wiki/Main_Page.
2. Drill in by region/country (then state/county) or search a record type or place.
3. Read the article: what records exist for that place/era, coverage dates, holding archives, and links to online collections (FamilySearch and others).
4. Follow the links to the actual record set and search there for the individual (a free login may be needed for some images).
5. Pivot: records surfaced here yield `associate` relatives, `dob`/death dates and a record `document-id` to anchor an identity.

## Inputs → Outputs
- **In:** a `name` plus a place/era context (or a record-type question)
- **Out:** guidance to relevant record sets and repositories → pathways to `associate` (relatives) and record `document-id`s
- **Empty/negative result looks like:** an article that says few records survive/are digitized for that place/era — a real research constraint, not a tool failure.

## Gotchas & OpSec
- It's a **guide, not a database** — it won't return a person; it tells you where to look.
- Community-edited, so depth varies by region; corroborate with the primary record.
- Some linked images require a free FamilySearch login and may be access-restricted by locale.

## Overlaps ("do both")
- Pairs with `[[familysearch]]`/`[[family-search]]` record search and other genealogy databases — the wiki tells you which collection holds the record, those let you pull the record itself.

## Trust & verifiability
`trust: community` — from a reputable genealogy non-profit but crowd-edited; excellent for navigation, but always confirm findings in the underlying record set.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familysearch-research-wiki |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
