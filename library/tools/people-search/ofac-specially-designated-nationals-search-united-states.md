---
id: ofac-specially-designated-nationals-search-united-states
name: OFAC Sanctions List Search (SDN)
description: Use when you have a `name` and want to check the US Treasury sanctions/SDN list — returns match with aliases, `address`es, `dob`, and linked entities (`associate`).
url: http://sdnsearch.ofac.treas.gov
category: people-search
path:
- people-search
bestFor: Screening a person or entity against the US Treasury OFAC Specially Designated Nationals and consolidated sanctions lists — with fuzzy name matching and rich identifiers.
selectorsIn:
- name
selectorsOut:
- address
- associate
- dob
status: live
pricing: free
costNote: Free official US government tool; no account. (The current endpoint is sanctionssearch.ofac.treas.gov; the older sdnsearch host redirects there.)
opsec: passive
opsecNote: Searching the public sanctions list does not notify anyone and is a routine compliance action. It's a US government site — use a puppet browser/IP if you don't want the query tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Department of the Treasury's Office of Foreign Assets Control — the authoritative source for US sanctions designations.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- OFAC SDN search
- Sanctions List Search
- sanctionssearch.ofac.treas.gov
tags:
- sanctions
- people-search
- compliance
- watchlist
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# OFAC Sanctions List Search (SDN)

> The US Treasury's official sanctions screening tool — check whether a name is a Specially Designated National, with fuzzy matching and a wealth of identifiers (aliases, addresses, DOB, linked entities).

## When to use
You have a `name` (person, company, vessel, or aircraft) and need to know whether they're under US sanctions — essential in due-diligence, fraud, financial-crime, and high-risk missing-person contexts. A hit is not just a yes/no: OFAC entries bundle aliases, dates of birth, passport/ID numbers, addresses, and linked designated entities, which are strong identifying and network leads. The built-in fuzzy matching (adjustable similarity threshold) catches transliteration and spelling variants.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the OFAC Sanctions List Search (sdnsearch.ofac.treas.gov → sanctionssearch.ofac.treas.gov).
2. Enter the `name`; optionally set the minimum-name-score slider lower to catch alias/transliteration variants, and filter by list, program, or type.
3. Read each result: primary name + AKAs, entity type, sanctions program, `address`es, `dob`, ID/passport numbers, and remarks linking to `associate` entities.
4. Confirm a match carefully using the secondary identifiers (DOB, address, ID) — common names produce weak matches you must adjudicate.
5. Pivot: linked entities/vessels → corporate registries and network mapping; addresses/ID numbers → further record checks; alias set → search those names elsewhere.

## Inputs → Outputs
- **In:** `name` (person or entity)
- **Out:** `address`, `dob`, `associate` (linked designated entities), plus aliases, sanctions program, and ID/passport numbers
- **Empty/negative result looks like:** "no matches" (or only low-score fuzzy matches) — the name isn't on OFAC's lists. That does not clear them under other regimes (UN, EU, UK OFSI); screen those separately for full coverage.

## Gotchas & OpSec
- **US lists only:** OFAC ≠ global. Also check UN, EU, and UK sanctions lists (and Interpol notices) for a complete picture.
- Fuzzy matching means low-score "hits" can be coincidental — adjudicate with DOB/ID, don't over-flag.
- OpSec: **passive** — public compliance data; no notification.

## Overlaps ("do both")
- Pairs with EU/UN/UK sanctions search and PEP/watchlist aggregators (OpenSanctions) — run all for cross-regime coverage.
- Feed linked entities into corporate registries (`[[company-information-service-gov-uk]]`, `[[cyprus]]`).

## Trust & verifiability
`trust: trusted` — first-party US government authority for its own designations. Confirm a candidate match against the entry's secondary identifiers before treating it as your subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ofac-specially-designated-nationals-search-united-states |
| category | people-search |
| selectorsIn → selectorsOut | name → address, associate, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
