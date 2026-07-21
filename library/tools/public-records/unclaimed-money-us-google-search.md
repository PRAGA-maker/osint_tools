---
id: unclaimed-money-us-google-search
name: '"unclaimed money" US - Google Search'
description: Use when you have a `name` (and maybe last-known `address`) and want to locate a person via US unclaimed-property/asset databases — returns confirmation of a claim tied to a `name`/`address` and a state to pursue.
url: https://www.google.com/search?q=%22unclaimed+money%22
category: public-records
path:
- public-records
bestFor: Using a Google entry point to reach US state unclaimed-property databases and check whether a subject has unclaimed funds tied to a name and address.
selectorsIn:
- name
- address
selectorsOut:
- address
- name
status: live
pricing: free
costNote: Free — a Google search plus free state unclaimed-property portals (never pay a "finder" service to search).
opsec: passive
opsecNote: Passive — searching public asset databases by name. The subject is not notified. Standard search hygiene applies; nothing is disclosed to the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: This entry is a search-technique launcher, not a data source; trust the official state treasury/unclaimed-property sites it leads to, and distrust paid "asset locator" middlemen.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- unclaimed money search
- unclaimed property search
tags:
- property
- public-records
- people-search
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# "unclaimed money" US - Google Search

> A saved Google query as an on-ramp to US **unclaimed-property** databases — a people-finding angle: funds owed to a person are indexed by name and last-known address, which can confirm a state and locality to pursue.

## When to use
You have a `name` (ideally with a last-known state or `address`) and want another way to place or trace someone. US states hold billions in unclaimed property (old bank accounts, refunds, insurance, wages) searchable *free* by name. A hit links a name to an address and a state — useful both to corroborate identity/locality and, in missing-persons work, to find where someone last had financial ties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start from the Google search, but go straight to the authoritative aggregators: **MissingMoney.com** (multi-state, endorsed by NAUPA) and each relevant **state treasurer / unclaimed-property** site.
2. Search the subject's `name`; add middle initial or known city to disambiguate.
3. For each state the person lived in, repeat on that state's official portal (MissingMoney doesn't cover every state).
4. Read matches: name + last-known address + holder + amount range.
5. Pivot: a returned `address` is a datable locality lead; a holder (former bank/employer) is an `employer-org`/relationship lead.

## Inputs → Outputs
- **In:** `name` (+ optional `address`/state)
- **Out:** confirmation of a claim tied to a `name` + last-known `address` and the state holding it
- **Empty/negative result looks like:** no matches in searched states — weak evidence (no unclaimed property, or it's in a state you didn't check); search additional states individually.

## Gotchas & OpSec
- **Never pay a finder** — official state searches are free; paid "asset locators" just charge for public data.
- Common names return many matches; use middle initial/city to confirm it's your subject.
- Coverage is US only and state-by-state; MissingMoney aggregates most but not all states.
- OpSec: passive; the subject learns nothing.

## Overlaps ("do both")
- Pairs with general people-search and address-history tools — unclaimed-property gives an independent, official name↔address link that can corroborate (or contradict) what a people-search returns.

## Trust & verifiability
`trust: community` — this file is a technique launcher; rely on the official state/NAUPA (MissingMoney) sources it points to, whose records are authoritative, and ignore paid intermediaries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unclaimed-money-us-google-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
