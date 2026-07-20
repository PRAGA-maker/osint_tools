---
id: coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k
name: 'Coronavirus Bailouts: Search Every Company Approved for Federal Loans Over $150k'
description: Use when you have a `name` or `employer-org` and want to check U.S. PPP/pandemic loans — returns employer-org, address, and associate (owner/business) links from ProPublica's loan database.
url: https://projects.propublica.org/coronavirus/bailouts/
category: public-records
path:
- public-records
bestFor: Tying a person or business to a U.S. PPP/pandemic-relief loan, with the business address, industry, and jobs reported.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free ProPublica public-interest database built on released SBA data; no account or payment required.
opsec: passive
opsecNote: Searching a published journalism/government dataset; no one is contacted. Only your own web request is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by ProPublica from official SBA Paycheck Protection Program disclosures — a reputable, sourced dataset.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nonprofit-explorer
- credibly-accused
- 527-explorer
- nursing-home-inspect
- parler-capitol-videos
- police-protest-videos
- the-nypd-files
aliases:
- ProPublica Coronavirus Bailouts
- PPP loan search
tags:
- public-records
- business-records
- financial-records
- ppp-loans
source: osint4all
lastVerified: '2026-07-20'
enrichment: full
---

# Coronavirus Bailouts: Search Every Company Approved for Federal Loans Over $150k

> ProPublica's searchable database of U.S. Paycheck Protection Program (PPP) and pandemic-relief loans — a way to link a person or business to federal money, an address, and an industry.

## When to use
You have a `name` or `employer-org` and want to check whether the subject or their business received PPP/pandemic-relief funds. A hit yields the business name, address, industry (NAICS), loan amount, lender, and jobs reported — corroborating that a person runs or is tied to a specific company at a specific location, and surfacing business associates behind a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://projects.propublica.org/coronavirus/bailouts/.
2. Search by business name (`employer-org`) or by a person's `name` (sole proprietors and self-employed filers often appear under their own name).
3. Read the record: business name, `address`, industry, loan amount/range, lender, and jobs retained.
4. Note the address and any linked business as `associate`/`employer-org` pivots.
5. Pivot: a business address feeds corporate-registry and people-search; the company name feeds [[nonprofit-explorer]] or state filings for officers/owners.

## Inputs → Outputs
- **In:** `name` (esp. sole proprietors) or `employer-org`
- **Out:** `employer-org` (business), `address`, `associate` (owner/company link), loan amount/lender/industry
- **Empty/negative result looks like:** no matching loan — the person/business didn't receive a covered loan (or it was under the $150k detailed-disclosure threshold in earlier data). Absence isn't proof of anything.

## Gotchas & OpSec
- Coverage is PPP/pandemic-relief only and reflects the SBA data as released — a snapshot, not a live registry.
- Business addresses may be a registered agent or home address for sole proprietors; verify before treating as a residence.
- Common business names collide; confirm with address/industry.
- OpSec: passive; published public-interest data.

## Overlaps ("do both")
- Pairs with [[nonprofit-explorer]] and state corporate registries: this shows the federal loan, those show the org's officers, filings, and finances.

## Trust & verifiability
`trust: trusted` — ProPublica journalism built on official SBA disclosures; authoritative as of the dataset's release, with ProPublica's documented caveats on data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | coronavirus-bailouts-search-every-company-approved-for-federal-loans-over-150k |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
