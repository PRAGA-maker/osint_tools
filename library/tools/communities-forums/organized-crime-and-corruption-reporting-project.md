---
id: organized-crime-and-corruption-reporting-project
name: OCCRP
description: Use when you have a `name` or `employer-org` possibly tied to crime/corruption and want investigative coverage and record datasets — returns linked persons, companies, and documented associations.
url: https://www.occrp.org/en
category: communities-forums
path:
- communities-forums
bestFor: Investigative reporting and the OCCRP Aleph archive of leaks, company registries, and court records for cross-border corruption research.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- name
status: live
pricing: freemium
costNote: News reporting is free to read; the Aleph data archive is free to search, but some datasets/document access require a free vetted account (journalists/researchers) via manual review.
opsec: passive
opsecNote: Reading articles and searching Aleph is read-only; subjects are not notified. Requesting elevated Aleph access reveals your identity/affiliation to OCCRP under their vetting. Use care handling data on living private individuals surfaced in leaks.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: OCCRP is a globally recognized investigative-journalism nonprofit; reporting is professionally sourced, and Aleph aggregates primary records (registries, leaks, court filings).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- aleph-occrp
- opencorporates
- offshoreleaks-icij
- data-occrp-org
- occrp-aleph
- occrp-org
- the-pegasus-project-occrp
- visual-investigative-scenarios
- investigative-dashboard
aliases:
- OCCRP
- Aleph
- Organized Crime and Corruption Reporting Project
tags:
- investigative-journalism
- corruption
- leaks
- company-information
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# OCCRP

> A global investigative-journalism network and, via its Aleph platform, a searchable archive of leaks, corporate registries, and court records — used to connect names and companies to documented crime and corruption.

## When to use
You have a `name` or `employer-org` that may be tied to fraud, organized crime, sanctions, or political corruption, and you want both narrative coverage and primary records. OCCRP's articles document who-did-what-with-whom, and its **Aleph** search engine indexes hundreds of datasets — leaked databases, company registries, court filings, watchlists — so a single name can surface directorships, shell companies, and associates across jurisdictions that ordinary search misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the newsroom at https://www.occrp.org/en for the `name`/`employer-org` to find any investigative coverage and the reporters behind it.
2. Go to Aleph (`https://aleph.occrp.org`) and search the same selector across its aggregated datasets.
3. Read the Aleph entity/document hits: linked companies, officers, addresses, and the source dataset for each — note which are leaks vs official registries.
4. For deeper/document-level access to restricted datasets, request a vetted account (manual review of your journalist/researcher status).
5. Pivot: company links → `[[opencorporates]]`; offshore entities → `[[offshoreleaks-icij]]`; named associates → people-search.

## Inputs → Outputs
- **In:** `name`, `employer-org`
- **Out:** `associate` (linked people/entities), `employer-org` (companies/directorships), `name` confirmations, supporting documents
- **Empty/negative result looks like:** no articles and no Aleph entity hits — the subject isn't in OCCRP's coverage or indexed datasets; this is common for private individuals with no corruption nexus and is not exculpatory.

## Gotchas & OpSec
- Aleph mixes authoritative registries with leaked data of varying reliability — always check each hit's source dataset before treating it as fact.
- Full access to some datasets requires OCCRP vetting (manual review); the public tier still searches a large amount.
- OpSec: **passive** for reading/searching; requesting elevated access identifies you to OCCRP. Handle personal data from leaks responsibly and lawfully.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (structured company registries) and `[[offshoreleaks-icij]]` (offshore entity leaks) — Aleph aggregates broadly, while those give authoritative or specialized depth, so cross-check entity links across all three.

## Trust & verifiability
`trust: trusted` — OCCRP is a leading investigative nonprofit and Aleph surfaces primary records; nonetheless, verify individual Aleph hits against their underlying source, since leaked datasets vary in accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | organized-crime-and-corruption-reporting-project |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
