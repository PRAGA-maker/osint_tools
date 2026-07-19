---
id: lei-bloomberg-com
name: Bloomberg LEI Search
description: Use when you have an `employer-org` name or a Legal Entity Identifier (LEI) and want authoritative entity-registration detail — returns the LEI, legal name, registered address, and jurisdiction for a company/fund.
url: https://lei.bloomberg.com/search
category: public-records
path:
- public-records
bestFor: Looking up a company/fund's Legal Entity Identifier and registered legal name, address, and jurisdiction.
selectorsIn:
- employer-org
- document-id
selectorsOut:
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free LEI search (Bloomberg is an accredited LEI issuer/LOU); searching and viewing LEI records is free, though registering/renewing an LEI costs money.
opsec: passive
opsecNote: You query a public global LEI registry; no company is notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Bloomberg is an accredited Local Operating Unit in the Global LEI System (GLEIF); LEI records are standardized, validated entity data, authoritative for legal name/address/registration.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bloomberg LEI
- lei.bloomberg.com
tags:
- lei
- corporate
- entity-registration
- public-records
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- bloomberg
- bloomberg-business-news
- bloomberg-com
---

# Bloomberg LEI Search

> A free search over the Global LEI System via Bloomberg — resolve a company or fund to its Legal Entity Identifier and its validated legal name, registered address, and jurisdiction. An entity-identity anchor for the corporate side of an investigation.

## When to use
You have an `employer-org` name (or an LEI code, a `document-id`) tied to your subject — an employer, a company they own, or a fund named in filings — and want its authoritative, standardized identity: exact legal name, registered address, home jurisdiction, and the unique 20-character LEI that ties it together across financial datasets. Useful for disambiguating similarly-named companies and for pivoting into other financial/registry data keyed on LEI. Company-focused, so direct value for finding an individual is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lei.bloomberg.com/search.
2. Search by company name or LEI code.
3. Open the matching record for the legal name, registered `address`, jurisdiction, entity status, and registration/renewal dates.
4. Note the LEI — use it as the key to look the entity up in other GLEIF-linked datasets and regulatory filings.
5. Pivot: the registered address and legal name feed corporate-registry (OpenCorporates), sanctions, and filing searches; the LEI links to ownership/relationship data in the GLEIF system.

## Inputs → Outputs
- **In:** `employer-org` name or LEI (`document-id`)
- **Out:** LEI (`document-id`), validated legal `employer-org` name, registered `address`, and jurisdiction
- **Empty/negative result looks like:** no LEI record — many small/private entities never obtained an LEI (it's mainly required for entities in financial transactions), so absence is common and not meaningful for such companies; try OpenCorporates/national registries.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive** — a public global registry lookup.
- Coverage: only entities that have registered an LEI appear (financial-market participants, many funds/large firms); a lapsed LEI shows "expired/lapsed" status. Use GLEIF's own search too — the same data is available across accredited issuers.

## Overlaps ("do both")
- Pairs with OpenCorporates, GLEIF's global search, and national company registries — LEI search gives the standardized global identifier and validated core data; corporate registries give directors, filings, and ownership, and GLEIF adds parent/child entity relationships.

## Trust & verifiability
`trust: trusted` — Bloomberg is an accredited LEI issuer in the GLEIF-governed Global LEI System; records are validated, standardized entity data, cross-checkable against GLEIF and other issuers, so the identity fields are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lei-bloomberg-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, document-id → employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
