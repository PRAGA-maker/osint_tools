---
id: clearing-and-depository-services
name: CDS (Clearing and Depository Services)
description: Use when you need Canadian securities-market infrastructure info (participant lists, ISIN issuance, regulatory notices) — mostly institutional; limited public data and no consumer securities search.
url: https://www.cds.ca
category: search-engines
path:
- search-engines
bestFor: Reference for Canada's central securities depository — participant/member lists, ISIN issuance, and regulatory notices; not a person or company investigative search.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: The public pages (participant lists, regulatory documents, notices) are free; substantive clearing/depository services and data products require login or paid vendor agreements.
opsec: passive
opsecNote: Reading public corporate/regulatory pages is passive and touches no target. Nothing here queries or notifies an individual.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: CDS is Canada's central securities depository (part of TMX Group); its published participant lists and regulatory notices are authoritative, but the site is market infrastructure, not a searchable intelligence source.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- CDS
- Canadian Depository for Securities
- cds.ca
tags:
- toddington
- curated-directory
- specialty-search
- finance
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# CDS (Clearing and Depository Services)

> Canada's central securities depository — authoritative market infrastructure whose *public* footprint is limited to participant lists, ISIN issuance, and regulatory notices, not a consumer-facing securities or people search.

## When to use
Rarely, and only for financial-infrastructure context: you need to confirm whether an `employer-org` is a CDS participant/member, look up ISIN-related information, or read a regulatory notice affecting Canadian securities settlement. For investigating an individual, this offers essentially nothing — it is institutional plumbing, not a searchable database of holdings or beneficial owners.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cds.ca and browse the public sections — participant/member lists, ISIN services, regulatory documents, and notices.
2. Check whether a target financial `employer-org` appears as a CDS participant.
3. Read relevant regulatory notices/`document-id`s for context on a securities-market matter.
4. Recognise the limits: most substantive services and data products sit behind login or paid vendor agreements (via TMX Webstore).
5. Pivot: a confirmed participant org feeds corporate-registry and securities-regulator (e.g. SEDAR+) research, which is where actual filings and ownership live.

## Inputs → Outputs
- **In:** `employer-org` (a financial institution/participant name)
- **Out:** participant-membership confirmation, ISIN/regulatory `document-id` references, `employer-org` context
- **Empty/negative result looks like:** the org isn't a listed participant, or the data you want is gated behind login/paid products — there is no public search over securities holdings, trades, or individuals.

## Gotchas & OpSec
- Institutional infrastructure, not an investigative search tool — set expectations accordingly.
- Most useful data requires participant login or paid vendor agreements.
- For company filings/ownership, use securities regulators (SEDAR+) and corporate registries instead.

## Overlaps ("do both")
- Pairs with SEDAR+/securities-regulator filings and corporate registries — those hold the actual disclosures and ownership data; CDS only confirms depository-participant/infrastructure facts.

## Trust & verifiability
`trust: trusted` — an authoritative institution (TMX Group); its published lists and notices are reliable, but its investigative usefulness is minimal, so don't expect person- or holdings-level intelligence here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clearing-and-depository-services |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
