---
id: hitta-se
name: Hitta.se
description: Use when you have a `name` or `address` in Sweden and want the matching resident, phone, business, or map location — returns address, phone, geolocation and associate links.
url: https://www.hitta.se/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Looking up Swedish residents, phone numbers, addresses and businesses on a searchable map.
selectorsIn:
- name
- address
- phone
- geolocation
selectorsOut:
- address
- phone
- geolocation
- associate
- employer-org
status: live
pricing: free
costNote: Basic person, business and map lookups are free; some deep property/financial reports are behind a paid tier, but the core directory search costs nothing.
opsec: passive
opsecNote: Reading Hitta.se is passive — you query their public directory, not the subject's own infrastructure, so nothing is disclosed to the target. It is a Swedish-hosted commercial site; use a clean browser session if you want to avoid tying searches to your own IP, but no login is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running major Swedish directory (~4M weekly visitors) aggregating official Swedish population-register addresses and Bolagsverket company filings; data is authoritative for Sweden.
missingPersonsRelevance: medium
coverage:
- se
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- hitta-se-2
aliases:
- hitta
- hitta.se
tags:
- bellingcat-toolkit
- maps
- sweden
- people-search
source: bellingcat-toolkit
lastVerified: '2026-08-04'
enrichment: full
---

# Hitta.se

> Sweden's main public directory and map: turn a Swedish name or address into a resident's phone, address, neighbours and business links.

## When to use
You have a `name`, `phone`, or `address` located in Sweden and want to confirm the current `address`, find a `phone` number, place it on a map, or surface `associate`/`employer-org` links. Because Sweden's population and company registers are public, Hitta.se is one of the strongest first stops for locating a Swedish subject, their neighbours at an address, or a company's officers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.hitta.se/.
2. Choose the tab for what you have — "Personer" (people), "Företag" (businesses/companies), or "Kartor" (maps) — and enter the `name`, `phone`, or `address`.
3. Read the result card: a person hit shows registered `address`, any listed `phone`, age, and often people co-registered at the same address (household `associate` links). A company hit shows the registered office, board members, and financial summary.
4. Click the map/"Vägbeskrivning" view to pin the `geolocation` and see the street-level surroundings.
5. Pivot: a co-registered household member feeds relationship mapping; a company officer name feeds another person search; the address feeds `[[hitta-se-2]]` or a mapping tool.

## Inputs → Outputs
- **In:** `name`, `phone`, `address`, or `geolocation` (Sweden only)
- **Out:** `address`, `phone`, `geolocation`, household `associate`, `employer-org` (company officers)
- **Empty/negative result looks like:** "Inga träffar" (no hits) — the person may be ex-directory, outside Sweden, or spelled differently; try the variant tools before concluding absence.

## Gotchas & OpSec
- Sweden-only: a hit requires the subject to be in the Swedish registers. A blank result is not proof the person doesn't exist, only that they aren't in this dataset.
- The interface is in Swedish; the person/business/map tabs are the three things you need.
- Some property valuation and full financial reports are paywalled; the core directory lookup is not.
- Passive: no notification reaches the subject.

## Overlaps ("do both")
- Pairs with `[[hitta-se-2]]` — the sibling entry covers the same provider from a different angle; run both since Swedish directory sites (Hitta, Eniro, Ratsit) each miss records the others hold.

## Trust & verifiability
`trust: trusted` — Hitta.se is a large, established Swedish directory sourcing official population-register and company-registry data, so its address and company facts are authoritative for Sweden.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hitta-se |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name, address, phone, geolocation → address, phone, geolocation, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
