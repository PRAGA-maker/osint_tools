---
id: cyprus
name: Cyprus Company Registry (Companies Section)
description: Use when you have a company `name`, officer `name` or registration number tied to Cyprus and want official corporate records — returns `employer-org`, registered `address`, and director/officer `name`s.
url: https://www.companies.gov.cy/en/company-lifecycle/search-for-company-information
category: public-records
path:
- public-records
bestFor: Searching the official Cyprus government business registry to link a person to Cypriot companies, directorships, and registered addresses.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free to search basic company information (name, number, status, registered office, officers). Certified copies or full filed documents may carry a government fee.
opsec: passive
opsecNote: Public registry search; neither the company nor its officers are notified. Queries hit a Cyprus government site — use a puppet browser/IP if you don't want your address tied to the search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Department of Registrar of Companies and Intellectual Property, Republic of Cyprus — the authoritative source for Cypriot corporate records.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cyprus Registrar of Companies
- companies.gov.cy
- Cyprus company search
tags:
- companysites
- company-related-sites
- public-records
- corporate-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- gov-cy
---

# Cyprus Company Registry (Companies Section)

> The Republic of Cyprus's official corporate registry — the authoritative way to tie a person to Cypriot companies, directorships, and registered addresses.

## When to use
You have a `name` (person or company) or a registration number with a Cyprus nexus and want to establish corporate connections: which companies a person directs or owns, the registered office `address`, and co-officers. Cyprus is a common offshore/holding jurisdiction, so this is high-value for financial, asset-tracing, and identity investigations where a subject may be hidden behind a Cypriot entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.companies.gov.cy/en/company-lifecycle/search-for-company-information (English interface).
2. Search by company `name`/registration number, or use the officer/organisation search to find entities linked to a person's `name`.
3. Open a matching company to read: registration number, status (active/struck-off), registered office `address`, and the list of directors/secretary (`name`s → `associate` links).
4. For an authoritative filing (annual return, incorporation docs), request the certified/paid copy if needed.
5. Pivot: co-directors → `associate` mapping; registered address → address/property cross-checks; company name → sanctions/leak databases (OpenCorporates, ICIJ Offshore Leaks).

## Inputs → Outputs
- **In:** `name` (person or company), `employer-org`, registration number, or `address`
- **Out:** `employer-org` (linked companies), `address` (registered office), `name` (directors/officers/secretary), plus status and incorporation date
- **Empty/negative result looks like:** "no results" — the entity may be dissolved beyond the searchable window, spelled/transliterated differently (Greek↔Latin), or simply not Cypriot. Try alternate transliterations and partial matches.

## Gotchas & OpSec
- Transliteration: Cypriot names appear in both Greek and Latin scripts; a miss on one spelling can hide records — try both.
- Nominee directors are common in Cyprus; a listed officer may be a corporate-services nominee, not the real controller — corroborate.
- OpSec: **passive** — public record, no notification.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]`-style aggregators and the ICIJ Offshore Leaks database — the official registry is authoritative and current; aggregators add cross-jurisdiction links and historical/leaked data.

## Trust & verifiability
`trust: trusted` — first-party government registrar, so the corporate facts are authoritative. Only caveat is nominee structures that obscure beneficial ownership; the registry shows the record of filing, not necessarily the real controller.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyprus |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
