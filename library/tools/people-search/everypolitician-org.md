---
id: everypolitician-org
name: Everypolitician.org
url: http://everypolitician.org
category: people-search
path:
- people-search
description: Use when you have a `name` of a politician/office-holder and want structured political data — returns party, terms, positions and links (`social-profile`, `associate`).
bestFor: Looking up an elected/appointed official's structured record — party, offices held, terms — across many countries from open, Wikidata-linked data.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
- name
status: degraded
pricing: free
costNote: Free and openly licensed (Creative Commons); data is community-built on Wikidata. It is a bulk/open dataset rather than a polished live search, and currency varies.
opsec: passive
opsecNote: Passive read of open, published political data; nothing is disclosed to the subject and no login is required. These are public figures, so relevance/sensitivity is low.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large open, Wikidata-derived dataset of politicians; coverage is broad but community-maintained and can be dated or incomplete, so confirm current office against an official source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- EveryPolitician
- everypolitician.org
tags:
- people-search
- political-data
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- every-politician
- everypolitician
---

# Everypolitician.org

> An open, Wikidata-linked dataset of politicians worldwide — structured party/term/office records for hundreds of thousands of office-holders across most countries.

## When to use
You have a `name` you believe belongs to an elected or appointed official and want their structured political record: party, the positions they've held, term dates, and links out (Wikidata, official pages, sometimes social). Best for disambiguating "is this the politician of that name?", building a public-figure timeline, or seeding an associate/party network. It only covers people in public office, not private individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open everypolitician.org and browse by country, or use the linked data/Wikidata to query a `name`.
2. Locate the person's entry: party, offices, term dates, and identifiers.
3. Follow the Wikidata/official links for authoritative current status and further biography.
4. Because the dataset can lag, confirm any "current office" claim against an official/parliament source.
5. Pivot: party colleagues feed `associate` mapping; linked Wikidata feeds richer biography; official pages feed contact/`social-profile`.

## Inputs → Outputs
- **In:** `name` (of an office-holder)
- **Out:** party, positions/terms, `associate` (party/colleagues), links to `social-profile`/official pages
- **Empty/negative result looks like:** no entry — the person isn't in the dataset (never in covered office, too local, or a coverage gap). Given the data can be dated, absence is weak evidence; a stale entry may also miss a recent office.

## Gotchas & OpSec
- **Degraded/currency risk:** community-built on Wikidata, coverage and freshness vary; treat term/office data as needing confirmation against an official source.
- Public-figures only — useless for ordinary private individuals.
- OpSec: fully passive open data; nothing disclosed to the subject.

## Overlaps ("do both")
- Pairs with Wikidata/Wikipedia and official parliament registers — EveryPolitician gives the structured cross-country skeleton; those confirm current, authoritative detail.

## Trust & verifiability
`trust: community` — a genuine open dataset with broad reach, but community/Wikidata-sourced and potentially dated, so verify current office and key facts against an authoritative government source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | everypolitician-org |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
