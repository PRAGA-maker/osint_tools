---
id: companies-house
name: Companies House
description: Use when you have a `name` or company name and want UK corporate ties — returns company officers, registered `address`es, dates of birth (partial), and filing history.
url: https://find-and-update.company-information.service.gov.uk/
category: public-records
path:
- public-records
- kyc-aml-tools
bestFor: Resolving a person to the UK companies they direct/own, and a company to its officers, addresses, and filings — the authoritative free UK corporate registry.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- dob
- employer-org
- associate
status: live
pricing: free
costNote: Free official UK-government register; full search, officer records, and filing documents are free. A free API key is available for bulk/programmatic use.
opsec: passive
opsecNote: You search a public government register; no subject is notified. Only Companies House sees your query. Registered addresses and partial DOBs are published by law — use them as leads, not as private data you've "obtained."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official UK Companies House register — authoritative for UK company data. Caveat: filings are self-reported by companies and not all are verified, so individual details can be false or outdated.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- opencorporates
- companies-house-api
- uk-persons-of-significant-control
aliases:
- Companies House
- find-and-update.company-information.service.gov.uk
- UK company register
tags:
- kyc-aml
- corporate-records
- uk
- public-records
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Companies House

> The UK's official free company register — the canonical way to tie a person to the UK companies they run and to unwrap a company's officers, addresses, and filings.

## When to use
You have a person's `name` and want to know which UK companies they're a director, secretary, or person-with-significant-control of — or you have a company name and want its officers, registered office, and history. Companies House publishes directors' names, service (and sometimes residential) addresses, partial dates of birth (month/year), nationality, and every filing. For a missing-persons or subject workup, a directorship links a person to addresses, co-directors (`associate`s), and a paper trail of activity dates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://find-and-update.company-information.service.gov.uk/.
2. Search a person's name (use the **officers** search) or a company name/number.
3. For a person: open their officer record to see every UK appointment, each with role, appointed/resigned dates, DOB (month/year), and the address used.
4. For a company: read **People** (officers + PSCs) and **Filing history** (accounts, confirmation statements, address changes) — filings often reveal earlier addresses and correspondents.
5. Pivot: co-directors are `associate` leads; addresses feed people-search/property tools; run the same names through `[[opencorporates]]` for cross-border corporate links.

## Inputs → Outputs
- **In:** `name` (officer search) or `employer-org`/company name.
- **Out:** officer `name`s, `address`es (registered/service), partial `dob`, `employer-org` links, and `associate` (co-officers/PSCs).
- **Empty/negative result looks like:** no officer/company matches — the person holds no UK appointment under that spelling (try variants/middle names), or the entity isn't UK-registered. Absence isn't proof of no business ties (they may be overseas or use a different name).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a public register; nobody is alerted. The data is lawfully public, but handle addresses/DOBs responsibly.
- Self-reported: companies file their own data and Companies House historically did limited verification, so names/addresses/DOBs can be fabricated or stale (a known money-laundering weakness). Corroborate before asserting identity.
- Name collisions are common; confirm you have the right individual via DOB/address consistency across appointments.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` — OpenCorporates aggregates registries across many jurisdictions and links networks; use it to extend a UK lead internationally and to graph officer relationships.
- Feeds property and people-search tools via the addresses it exposes.

## Trust & verifiability
`trust: trusted` — the authoritative UK source, so the *existence* of an appointment/filing is reliable. The *content* of filings is self-declared and only lightly verified, so treat individual details as strong leads to corroborate, not proven fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | companies-house |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address, dob, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
