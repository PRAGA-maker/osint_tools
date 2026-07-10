---
id: pappers-fr
name: Pappers.fr
description: Use when you have a `name` or French company and want directorships, officers, beneficial owners, and registered addresses — returns employer-org links, associates, address, and partial dob.
url: https://www.pappers.fr/
category: public-records
path:
- public-records
bestFor: Mapping a person to French company directorships/officers, or a company to its officers and owners.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
- dob
status: live
pricing: freemium
costNote: Free search and basic company/officer data; official filings (statutes, accounts) and bulk API access are paid.
opsec: passive
opsecNote: Reads official public French registry data; searches are anonymous and do not notify anyone. Business addresses/officer data are public record.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates authoritative French open data (INSEE/SIRENE, RCS/BODACC, INPI); the underlying records are official, though Pappers is a private reseller of that open data.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- societe-com
- opencorporates
- companies-house
aliases:
- pappers.fr
tags:
- companysites
- Company Related Sites
- france
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Pappers.fr

> A French company-registry search built on official open data — pivots between a person and the French companies they run, own, or direct.

## When to use
You have a subject `name` with French business ties (or a French `employer-org`) and want to establish their corporate footprint: which companies they are an officer/director of, co-directors (associates), registered/business addresses, and their partial date of birth (French officer records publish month/year). Excellent for placing a person via their company address and mapping their business network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pappers.fr/.
2. Search by person name (dirigeant) to list their mandates, or by company name/SIREN to list its officers and owners.
3. Read the result: company identity (SIREN/SIRET, address, status), officer list with roles and birth month/year, and beneficial owners.
4. For official documents (statutes, annual accounts) or bulk work, use the paid tiers/API.
5. Pivot: a business address feeds location work; co-directors feed an associate map; the partial DOB disambiguates a common name.

## Inputs → Outputs
- **In:** `name` (dirigeant) or `employer-org` (company/SIREN)
- **Out:** `employer-org` (companies/mandates), `name`, `address` (registered/business), `associate` (co-officers/owners), `dob` (month/year)
- **Empty/negative result looks like:** no mandates — the person may have no French company role, use a name variant, or hold only foreign entities. Absence isn't proof of no business activity.

## Gotchas & OpSec
- Human-in-the-loop: none for search; filings/API are paywalled.
- OpSec: **passive**; official public record, no alerts.
- Reseller caveat: data mirrors official sources but can lag the primary registry slightly; verify recent changes against INPI/BODACC.

## Overlaps ("do both")
- Pairs with `[[societe-com]]` — alternate French company-data source to cross-check officers and addresses.
- Pairs with `[[opencorporates]]` and `[[companies-house]]` — follow the person's directorships beyond France into other jurisdictions.

## Trust & verifiability
`trust: trusted` — surfaces authoritative French open data (SIRENE/RCS/BODACC/INPI); reliable for corporate links, with the only caveat being reseller lag versus the primary registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pappers-fr |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address, associate, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
