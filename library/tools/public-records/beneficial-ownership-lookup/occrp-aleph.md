---
id: occrp-aleph
name: OCCRP Aleph
description: Use when you have a person `name` or company `employer-org` and want to cross-reference them across leaks, corporate registries and public records — returns matching entities, documents and `associate` links.
url: https://aleph.occrp.org/
category: public-records
path:
- public-records
- beneficial-ownership-lookup
bestFor: Searching a person or company across hundreds of investigative datasets, leaks and official registers at once.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
- document-id
status: live
pricing: free
costNote: Free to search the public datasets. A free account unlocks cross-referencing, alerts/tracking and uploading your own documents; some sensitive collections are restricted to vetted journalists.
opsec: passive
opsecNote: You query OCCRP's aggregated archive, not the subject — passive, no signal to the target. Register with a professional/sock-puppet account; be aware OCCRP may log searches, and restricted datasets require a genuine journalist vetting.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Organized Crime and Corruption Reporting Project, a respected investigative journalism network; datasets are sourced/curated and provenance is documented per collection.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Aleph
- OCCRP Data
tags:
- public-records
- leaks
- corporate-registry
- beneficial-ownership
- investigative
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- investigative-dashboard
- occrp-org
- organized-crime-and-corruption-reporting-project
- the-pegasus-project-occrp
- visual-investigative-scenarios
---

# OCCRP Aleph

> A search engine over hundreds of investigative datasets — leaks, corporate registries, court records, sanctions lists — that cross-references a person or company against all of them at once.

## When to use
You have a person `name` or company `employer-org` and want to know whether they appear anywhere in the world's aggregated investigative data: offshore leaks, national company registers, procurement records, court filings, sanctions and watchlists. Aleph surfaces matching entities, the source documents, and — with cross-referencing — links to `associate`s, `address`es, and directorships.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://aleph.occrp.org/ and search the `name` or `employer-org` (public datasets need no login).
2. Register a free account to unlock cross-referencing, saved searches, alerts, and document upload; request access to restricted collections only if you are a vetted journalist.
3. Filter by dataset, country, schema (Person, Company, etc.); open matching documents and entity profiles.
4. Pivot: entity profiles link officers/`associate`s, registered `address`es and `document-id`s — follow those into national registers and people-search. Use "cross-reference" to match your uploaded list against every dataset.

## Inputs → Outputs
- **In:** person `name` or company `employer-org` (optionally an uploaded document/entity list)
- **Out:** matching entities, source documents (`document-id`), linked `associate`s and `address`es
- **Empty/negative result looks like:** no hits — the subject isn't in the currently indexed collections (coverage is deep but uneven by country); absence is not exoneration.

## Gotchas & OpSec
- Human-in-the-loop: full power (cross-referencing, restricted datasets) needs an account and, for sensitive collections, journalist vetting.
- Coverage varies hugely by country and dataset freshness — a miss in Aleph doesn't mean a miss in the source register.
- Matches can be namesakes; confirm identity with corroborating selectors before drawing conclusions.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]`-style company registries and `[[eu-consolidated-corporate-registers]]` — Aleph finds the entity across everything; the primary register confirms the authoritative, current record.

## Trust & verifiability
`trust: trusted` — maintained by OCCRP, a leading investigative-journalism organisation; each collection carries provenance, so you can trace a hit back to its source document.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | occrp-aleph |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
