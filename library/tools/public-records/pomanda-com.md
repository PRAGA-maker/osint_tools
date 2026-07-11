---
id: pomanda-com
name: Pomanda
description: Use when you have a company `name`, a director `name`, or an `address` in the UK and want company intelligence and officer links — returns registered address, officers/associates and company (employer-org) records.
url: https://pomanda.com/
category: public-records
path:
- public-records
bestFor: UK company and director intelligence — profiles, financials estimates, officers and registered addresses.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
- associate
status: live
pricing: freemium
costNote: Free tier gives basic company/officer profiles and search; detailed financials, valuations and full reports require a paid subscription or per-report purchase.
opsec: passive
opsecNote: Company/officer records are public (built on Companies House plus Pomanda's own data). Searching is passive and does not notify anyone. A free account may be needed for some detail; use a research account, not personal identity, if registering.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial UK business-intelligence aggregator built substantially on Companies House data plus modelled estimates. Officer/company facts trace to authoritative sources; Pomanda's financial estimates are modelled, not filed figures.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- pomanda.com
tags:
- companysites
- company-records
- corporate-intelligence
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Pomanda

> A UK company-intelligence aggregator — search a company or director and get profiles, officers, registered addresses and financial estimates, layered on top of Companies House data.

## When to use
You have a UK company `name`, a director/officer `name`, or a registered `address`, and you want to map a person's corporate footprint: which companies they run or are officers of, co-directors (`associate`), and registered addresses. A strong route from a person to their business interests and a service/registered address, useful for locate and due-diligence work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pomanda.com/ and search by company name, director name, or address.
2. Open a company or officer profile to read registered address, officers/directors, incorporation details, and Pomanda's estimated financials.
3. From a person's profile, enumerate their appointments and co-officers to build an `associate`/network map.
4. Some detail and reports require a paid tier — decide whether the free profile already answers your question.
5. Pivot: cross-check officer facts against Companies House (authoritative), feed a registered/service address into people-search, and use co-director links to expand the network.

## Inputs → Outputs
- **In:** company `name`, director `name`, or `address`
- **Out:** registered `address`, `employer-org` (company records), officer `name`s, co-officer `associate` links, and (paid) financial estimates
- **Empty/negative result looks like:** no matching company/officer — the person may have no UK company role, or the name is spelled differently; common names return multiple officers to disambiguate by DOB-month/address.

## Gotchas & OpSec
- **Estimates vs filings:** Pomanda models financials/valuations — those are estimates, not filed accounts. For authoritative figures use Companies House.
- Paywall gates deeper reports; the free profile is often enough for officer/address links.
- UK scope; overseas directorships won't appear.
- OpSec: passive, public-record based; register with a research identity if needed.

## Overlaps ("do both")
- Pairs with Companies House (`[[companies-house]]`-style official registry) — Pomanda is a friendlier search/aggregation layer; Companies House is the authoritative filing source. Do both: discover on Pomanda, confirm on Companies House.

## Trust & verifiability
`trust: community` — a commercial aggregator. Officer/company/address facts derive from authoritative Companies House data (verify there); Pomanda's own financial estimates are modelled and should be treated as indicative only.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pomanda-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
