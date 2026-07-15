---
id: malta
name: Malta — MBR Company Registry
description: Use when you have a Maltese company `name`/`employer-org` or a person and want official registry data — returns registered company details, addresses and directors/officers from the Malta Business Registry.
url: https://registry.mbr.mt/ROC/index.jsp#companySearch.do?action=companyDetails
category: public-records
path:
- public-records
bestFor: Authoritative lookups of Maltese companies and their directors/officers via the national business registry.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: freemium
costNote: Basic company search (name, registration number, status, registered office) is free; full document extracts and detailed filings typically require registration and/or a fee.
opsec: passive
opsecNote: Official government registry lookup; you query the registry, not any individual, and no notification is sent. No login for the basic search. Maltese company records are public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Malta Business Registry (MBR), the statutory registrar of Maltese companies — the authoritative source for company registration data.
missingPersonsRelevance: high
coverage:
- mt
auth: none
api: false
localInstall: false
registration: false
aliases:
- Malta Business Registry
- MBR
- registry.mbr.mt
tags:
- companysites
- Company Related Sites
- company-registry
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Malta — MBR Company Registry

> Malta's official business registrar: the authoritative source for registered Maltese company details, registered offices and directors — useful given Malta's role as a corporate domicile.

## When to use
You have a Maltese company `name`/`employer-org` (or a registration number, or a person you think is a director) and want authoritative registry data: legal name, registration number, status, registered office `address`, and directors/officers (`associate` links). Malta is a common corporate-structuring jurisdiction, so this is valuable for untangling ownership tied to a subject and confirming a business connection.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the MBR registry — https://registry.mbr.mt/ (it redirects to the current register app). No login is needed for the basic company search.
2. Search by company `name` or registration number.
3. Read the record: legal name, registration number, status, registered office `address`, and listed directors/officers/secretary.
4. For full filings/annual returns/beneficial-ownership documents, expect to register and possibly pay — the free search confirms existence, status and officers.
5. Pivot: director names feed people-search and cross-registry checks; the registered office feeds mapping; the reg number feeds cross-border company databases.

## Inputs → Outputs
- **In:** company `name` / `employer-org` / registration number (optionally a person as director)
- **Out:** registered `employer-org` details, registered office `address`, directors/`associate`s, status
- **Empty/negative result looks like:** no matching company — meaning no Maltese registration under that name/number, not that the subject has no company elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: none for basic search; full document extracts are gated behind registration/fees.
- Registered office ≠ residence: a Maltese registered office is often a corporate-services provider's address, not where a director lives — treat it as a business, not home, address.
- OpSec: fully passive; an official public-registry lookup that never touches the subject.

## Overlaps ("do both")
- Pairs with cross-jurisdiction company aggregators and other national registries — this is the authoritative Maltese source, while aggregators link it to entities and officers in other countries.

## Trust & verifiability
`trust: trusted` — the MBR is Malta's statutory company registrar, so its data is authoritative; paid document extracts add depth (e.g. beneficial ownership) beyond the free record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | malta |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
