---
id: annualreports-com
name: AnnualReports.com
description: Use when you have a public-company `employer-org` name or ticker and want its annual/proxy reports — returns downloadable filings naming officers, directors and addresses.
url: https://www.annualreports.com/
category: public-records
path:
- public-records
- annual-reports
bestFor: Locating and downloading a public company's annual reports, proxy statements, and sustainability reports in one place.
selectorsIn:
- employer-org
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free to search and download; no account required. Aggregates publicly filed corporate reports.
opsec: passive
opsecNote: You download public corporate filings from a third-party aggregator — the target company isn't contacted and nothing ties the query to you. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator of publicly filed reports. The underlying documents are official company filings; the aggregator's role is convenience, so confirm a report against the company/regulator for anything critical.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Annual Reports
tags:
- corporate-records
- annual-reports
- public-records
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# AnnualReports.com

> A free, searchable library of public companies' annual reports, proxy statements, and sustainability reports — a fast route to the people and details a company discloses.

## When to use
You have a public-company `employer-org` (name or ticker) connected to a subject and want its corporate disclosures. Annual and proxy reports name executives and board members, list headquarters and registered `address`es, describe subsidiaries and business relationships, and can corroborate a person's role or connection to an organisation. Reach for it when profiling a company or verifying someone's stated employment/directorship.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.annualreports.com/ and search by company name or ticker (or browse by industry/sector).
2. Open the company's page and download the relevant report(s): annual report, proxy statement, sustainability report, across available years.
3. Read for people and structure: named officers/directors (`name`/`associate` links), headquarters/registered `address`, subsidiaries, and material relationships.
4. Compare years to build a timeline of leadership and structural change.
5. Pivot: named executives feed people-search and professional-network lookups; the registered address feeds corporate-registry searches for the full legal entity.

## Inputs → Outputs
- **In:** public-company `employer-org` (name/ticker)
- **Out:** downloadable reports → named officers/directors (`name`, `associate`), company `address`, structure
- **Empty/negative result looks like:** no reports — the company is private, foreign-listed, or not covered here; absence isn't proof it doesn't file (check the relevant regulator, e.g. SEC EDGAR/Companies House).

## Gotchas & OpSec
- Public companies only: private firms and many non-US/UK listings won't appear — use the relevant regulator's filing system instead.
- It's an aggregator: for legally authoritative filings, confirm against the primary source (SEC EDGAR, Companies House, the company's investor-relations page).
- Reports are periodic snapshots — leadership/addresses may have changed since the latest one.
- OpSec: fully passive download of public documents.

## Overlaps ("do both")
- Complements primary regulator databases (SEC EDGAR / Companies House) — AnnualReports.com is the convenient front door; the regulator is the authoritative, complete record.

## Trust & verifiability
`trust: community` — a convenience aggregator of official filings. The documents themselves are authoritative company disclosures; for anything decisive, verify the same report against the primary regulator or the company directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | annualreports-com |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
