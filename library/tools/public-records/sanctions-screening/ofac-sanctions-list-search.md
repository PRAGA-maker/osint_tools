---
id: ofac-sanctions-list-search
name: OFAC Sanctions List Search
description: Use when you have a `name` (person or `employer-org`) and want to check it against U.S. Treasury sanctions (SDN and consolidated lists) — returns matched records with program, list type and a confidence score.
url: https://sanctionssearch.ofac.treas.gov/
category: public-records
path:
- public-records
- sanctions-screening
bestFor: Authoritative free check of a name against U.S. OFAC sanctions lists.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free, official U.S. government tool; no account or payment.
opsec: passive
opsecNote: You submit a name to a U.S. Treasury server, which may log the query; nothing is sent to the subject. No login. Use standard sock-puppet browsing hygiene, though there's no target-facing exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the U.S. Treasury's Office of Foreign Assets Control; this is the authoritative primary source for OFAC designations.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ofac-specially-designated-nationals-search-united-states
- opensanctions-org
aliases:
- OFAC SDN Search
- sanctionssearch.ofac.treas.gov
tags:
- sanctions
- ofac
- kyc
- public-records
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# OFAC Sanctions List Search

> The U.S. Treasury's own sanctions search: type a name, see whether it matches the SDN or other OFAC lists, with a confidence score for near-matches.

## When to use
You have a subject `name` (individual or `employer-org`) and need an authoritative answer on whether they are subject to U.S. sanctions — on the Specially Designated Nationals (SDN) list or one of OFAC's consolidated non-SDN lists. This is the primary source (not a third-party aggregator), so a hit here is directly citable. Matched records also expose known aliases, addresses and linked entities useful for pivoting.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://sanctionssearch.ofac.treas.gov/.
2. Enter the `name` (optionally narrow by address, country, entity type, or program).
3. Set the **minimum name score** slider — lower it to catch misspellings/transliterations, raise it to cut noise.
4. Read the results table: matched name, address, type, sanctions program(s), SDN vs non-SDN designation, and confidence score.
5. Open a record for full detail (aliases, DOB, linked entities). Pivot: aliases/addresses/`associate` entities feed further searches; corroborate context via `[[opensanctions-org]]`.

## Inputs → Outputs
- **In:** `name` (person or `employer-org`), optionally address/country/program
- **Out:** matched OFAC records — `name` + aliases, `address`, sanctions program, list designation, confidence; linked `associate` entities
- **Empty/negative result looks like:** "no matches" at your chosen score threshold — the name isn't OFAC-listed; lower the score to be sure you're not missing a transliteration before concluding.

## Gotchas & OpSec
- Fuzzy matching means common names return possible matches — always confirm identity via DOB/address/program on the full record; a name match alone is not a designation.
- Covers OFAC (U.S.) programs only — use other sanctions sources (EU, UN, UK) for global coverage.
- OFAC explicitly warns this isn't a substitute for full due diligence.
- OpSec: passive; a federal server logs the query, but there's no target-facing exposure.

## Overlaps ("do both")
- Pairs with `[[opensanctions-org]]` and `[[ofac-specially-designated-nationals-search-united-states]]` — OFAC's own tool is authoritative for U.S. designations, while OpenSanctions aggregates OFAC with EU/UN/UK lists for worldwide coverage.

## Trust & verifiability
`trust: trusted` — the official U.S. Treasury/OFAC search; results are primary-source designations, so a confirmed match is directly citable (subject to verifying the matched record is actually your subject).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ofac-sanctions-list-search |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
