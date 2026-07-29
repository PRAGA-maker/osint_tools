---
id: violation-tracker
name: Violation Tracker
description: Use when you have an `employer-org` (or a company-linked person) and want its US regulatory/criminal penalty history — returns cases, agencies, penalties, and parent-company links.
url: https://violationtracker.goodjobsfirst.org/
category: documents-metadata
path:
- documents-metadata
bestFor: Looking up a company's record of US corporate misconduct — fines, settlements, and criminal cases since 2000.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free to search and view results. Bulk download of results and a few detail fields are reserved for subscribers; the on-screen investigative data is free.
opsec: passive
opsecNote: A public research database; you query Good Jobs First's servers, not any target. No login required and nothing is disclosed to the company being searched. Standard search-engine logging applies — use a clean session if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by the Corporate Research Project of Good Jobs First, a long-established non-profit; records are sourced from federal regulators, the DOJ, state AGs and local agencies, with citations to the originating action.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- opencorporates
- sec-edgar
aliases:
- Good Jobs First Violation Tracker
tags:
- corporate-records
- regulatory
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Violation Tracker

> A free searchable database of US corporate misconduct — 700,000+ civil and criminal cases from 450+ agencies, totalling over $1 trillion in penalties, indexed by company and parent.

## When to use
You are profiling an `employer-org` (or a person's employer/business) and want its enforcement history: environmental, safety, wage-and-hour, discrimination, fraud, bribery, banking, and consumer-protection cases. Good for corroborating that a business is real and active, understanding a company's risk profile, and surfacing the regulators and case citations that lead to fuller court/agency records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://violationtracker.goodjobsfirst.org/.
2. Basic search: type a company name in the search box. Use **Advanced Search** to filter by state, agency, offense group, industry, year range, or penalty amount.
3. Results list matching cases with company, penalty, year, agency, and offense type; the parent-company view aggregates subsidiaries under the ultimate owner.
4. Click a case for the detail page: agency, description, penalty, and a citation/source link to the originating enforcement action.
5. Pivot: the agency + case reference feeds direct regulator/court-record lookups; the parent-company mapping feeds `[[opencorporates]]` / `[[sec-edgar]]` for ownership and filings.

## Inputs → Outputs
- **In:** `employer-org` (company name) — or a `name` tied to a business
- **Out:** enumerated penalty cases, penalty amounts, enforcing `employer-org`/agency, parent-company `associate` links, case citations (often with a location/`address`)
- **Empty/negative result looks like:** "no results" — the entity has no US federal/state case in the database since 2000; try name variants, the parent company, or a subsidiary spelling before concluding a clean record.

## Gotchas & OpSec
- Coverage is US-only and starts in 2000; small/local matters below reporting thresholds may be absent. A "clean" result is absence-of-record, not proof of good conduct.
- Company naming varies (Inc./LLC/DBA); search parent and subsidiary variants. The parent-company rollup is the most reliable aggregate view.
- Downloading the full result set and a few fields require a subscription, but every case detail needed for an investigation is viewable free.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — Violation Tracker gives the enforcement/penalty history; OpenCorporates gives the corporate registration, officers, and structure. Do both to connect misconduct to the legal entity and its people.
- Combine with `[[sec-edgar]]` for public-company filings that contextualise large settlements.

## Trust & verifiability
`trust: trusted` — non-profit-maintained, sourced from primary government enforcement records with per-case citations you can follow to the original agency action. High reliability; still verify the specific citation for legal use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | violation-tracker |
