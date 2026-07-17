---
id: every-politician
name: EveryPolitician
description: Use when you have a politician's `name` and want their offices and affiliations — returns `employer-org`, positions and linked identifiers across 250+ countries.
url: https://everypolitician.org/
category: public-records
path:
- public-records
- us-political-records
bestFor: Looking up an office-holder's positions, party and terms from a global Wikidata-backed database.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free and openly licensed (Creative Commons); data is browsable and downloadable in bulk with no account.
opsec: passive
opsecNote: A static, openly published reference database; the subject is never contacted and there is no query trail beyond the host's logs. Public-figure data only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built on Wikidata and now maintained by OpenSanctions; a well-documented open-data project, though ultimately community-sourced.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- everypolitician
- everypolitician-org
aliases:
- Every Politician
- everypolitician.org
tags:
- political-records
- open-data
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# EveryPolitician

> A global, openly licensed database of political office-holders — 700k+ politicians across 250+ countries — for turning a public figure's `name` into their positions, party and term history.

## When to use
You have the `name` of a legislator, minister, judge or senior official (anywhere in the world) and want their structured record: which office(s) they hold or held, party affiliation, term dates, and cross-links to Wikidata and other identifiers. Useful for confirming a public figure's identity and role, disambiguating people with the same name by office, and finding the `employer-org` (chamber/body) and named colleagues that place them in a network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://everypolitician.org/ and search or browse by country, then person.
2. Open the politician's record: read positions held, party, term dates and the linked Wikidata identifier.
3. For scale, use the bulk data downloads / API to pull an entire legislature at once.
4. Note that coverage is uneven — some countries/terms are richer than others because entries derive from Wikidata contributions.
5. Pivot: follow the Wikidata link for more identifiers (official pages, social handles), and feed the office `employer-org` and colleague `name`s into further lookups.

## Inputs → Outputs
- **In:** `name` (a political office-holder)
- **Out:** `employer-org` (governing body/office), positions/terms, `associate` colleagues and linked identifiers
- **Empty/negative result looks like:** no record — the person is not (or not yet) in Wikidata as an office-holder, or holds a local role below the project's coverage. Absence is not proof they hold no office.

## Gotchas & OpSec
- OpSec: **passive** — public-figure reference data; nothing reaches the subject.
- Wikidata-derived, so completeness and freshness vary by country; verify current office against an official source.
- It covers *office-holders* — private citizens and candidates who never held office generally will not appear.

## Overlaps ("do both")
- Pairs with national parliament/registry sites and Wikidata directly — EveryPolitician gives the normalised cross-country view; official sources give the authoritative current status.

## Trust & verifiability
`trust: trusted` — a mature open-data project (Wikidata-backed, OpenSanctions-maintained). Because it is community-sourced, confirm decisive facts against the office's official record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | every-politician |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
