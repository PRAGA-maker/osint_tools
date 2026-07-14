---
id: gazettes-africa
name: gazettes.africa
description: Use when you have a `name`/`employer-org` and want to full-text search African government gazettes for official notices (directorships, name changes, estates, insolvencies) — returns name, employer-org, associate.
url: https://gazettes.africa/
category: public-records
path:
- public-records
bestFor: Full-text searching African official government gazettes for a person or company by name.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free, full-text searchable archive of official gazettes; no account required. A civic-tech project (Code for Africa / OpenUp lineage).
opsec: passive
opsecNote: Searching an archive of already-published official gazettes is fully passive — the subject is not notified. No login. Use a clean browser if the search itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Aggregates official government gazettes (primary-source legal notices) into a searchable archive; the source documents are authoritative, with the usual caveat that OCR/coverage completeness varies by country and period.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Gazettes Africa
- Open Gazettes
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- gazettes
- africa
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# gazettes.africa

> A free, full-text-searchable archive of African government gazettes — the official record where directorships, name changes, estates, insolvencies, and legal notices are published.

## When to use
You have a `name` or `employer-org` with an African connection and want to find them in official gazettes: company directorships and registrations, deceased-estate and probate notices, insolvencies, name/marriage notices, and government appointments. Gazettes are primary-source legal publications, so a hit is strong corroboration — of a business role, a death, a name change, or a relationship (`associate`) named in a notice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://gazettes.africa/ and use the full-text search.
2. Enter the subject `name` (try variants) or a company/`employer-org`.
3. Filter by country/jurisdiction and date where possible to cut noise.
4. Open matching gazette pages and read the notice in context — note co-parties, dates, addresses, and roles.
5. Pivot: a directorship links a person to a company and co-directors (`associate`); an estate notice yields relatives and dates; feed names into company registries and people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `name`, `employer-org` (company roles), `associate` (co-parties/relatives named in notices), dates/addresses in the notice
- **Empty/negative result looks like:** no matches — could be genuine absence, an OCR miss, or a country/period not yet digitised; try name variants and don't treat a miss as conclusive.

## Gotchas & OpSec
- Coverage and OCR quality vary by country and era — a negative isn't proof; try spelling variants.
- Notices are point-in-time legal records; interpret roles/relationships in their published context.
- OpSec: fully passive, primary-source public records.

## Overlaps ("do both")
- Pairs with national company registries and estate/probate indexes — gazettes surface the notice; registries and courts hold the fuller record.

## Trust & verifiability
`trust: trusted` — a searchable archive of authoritative official gazettes; the documents are primary-source, subject to digitisation/OCR completeness — verify the exact notice text on the source page.
