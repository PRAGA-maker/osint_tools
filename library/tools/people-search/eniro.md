---
id: eniro
name: Eniro
description: Use when you have a Swedish `name` (or `phone`/`address`) and want the person's registered address, phone and household — returns `address`, `phone`, `name`.
url: https://www.eniro.se/
category: people-search
path:
- people-search
bestFor: Swedish people, phone and address directory (the local Yellow/White Pages) with map integration.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- address
- phone
status: live
pricing: free
costNote: Free to search people, phone numbers and addresses; Sweden's open population data makes basic lookups unusually rich at no cost.
opsec: passive
opsecNote: Passive — Eniro draws on Sweden's openly published population/address data; the subject is not notified. No account is required for basic search. Your queries hit Eniro's servers (logged); use a clean browser for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established Swedish directory built on official open population data; coverage of Swedish residents is strong, though listings can lag moves and some people restrict their data.
missingPersonsRelevance: high
coverage:
- se
auth: none
api: false
localInstall: false
registration: false
aliases:
- eniro.se
- Swedish Yellow Pages
tags:
- bellingcat-toolkit
- people
- sweden
- directory
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- eniro-sweden
---

# Eniro

> Sweden's phone/address directory — thanks to the country's open population data, a name often yields a current address, phone, age and household map in seconds.

## When to use
You have a Swedish `name` (or a `phone`/`address` to reverse) and want to locate the person: registered `address`, landline/mobile `phone`, approximate age, and often who else lives at the address (household). Sweden's uniquely open personal data makes Eniro one of the highest-yield free people tools for any Swedish subject in a locate or missing-persons trace.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.eniro.se/ and choose the "Person" search (or search a `phone`/`address` to reverse-lookup).
2. Enter the `name`; results list matching people with town, age, and address.
3. Open a person for full `address`, `phone`, age, and a map; note co-residents at the address (household `associate` leads).
4. Reverse a number/address by entering it directly.
5. Pivot: names/addresses feed Nordic company registers and `[[geneanet-org]]`; a phone feeds messaging-app checks.

## Inputs → Outputs
- **In:** Swedish `name`, `phone`, or `address`
- **Out:** registered `address`, `phone`, age, map location, household co-residents (`name`/associate)
- **Empty/negative result looks like:** no match or a name-only entry — the person restricted their data, isn't Swedish-resident, or recently moved. Sweden-specific; useless for non-Swedish subjects.

## Gotchas & OpSec
- Human-in-the-loop: none — open public search.
- OpSec: **passive** — open population data, subject not notified; queries logged by Eniro.
- Sweden-only. Listings can be dated; a few individuals opt to hide details. Verify a current address before relying on it.

## Overlaps ("do both")
- Pairs with `[[geneanet-org]]` (family history) and Nordic business registers — Eniro nails the current Swedish address/phone; the others add relatives and corporate links.

## Trust & verifiability
`trust: community` — a reputable directory over official open data, but not real-time. Confirm addresses/phones against a second source for time-sensitive work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eniro |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → name, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
