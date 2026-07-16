---
id: statistics-and-data
name: UNODC Data Portal
description: Use when you have a country/region context and want aggregate crime, homicide, drug, trafficking, or prison statistics — returns country-level figures, NOT individual person records.
url: https://dataunodc.un.org
category: public-records
path:
- public-records
bestFor: Country-level base rates and context on homicide, trafficking, drugs, and prison populations to frame an investigation.
selectorsIn:
- address
selectorsOut: []
status: live
pricing: free
costNote: Free UN public data portal; no account required. Data is downloadable (CSV/Excel) and cite-able.
opsec: passive
opsecNote: Reading aggregate UN statistics reveals nothing about any subject and involves no personal query. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official United Nations Office on Drugs and Crime data portal — authoritative, but statistical/aggregate only.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- UNODC dataUNODC
- data.unodc.org
- UN Office on Drugs and Crime statistics
tags:
- court
- inmate
- statistics
- context
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- un-comtrade-database
- un-data
- un-security-council-consolidated-list
- unstats-social-indicators
---

# UNODC Data Portal

> The UN's crime-and-drugs statistics portal: country-level context and base rates, not a record of any individual.

## When to use
You need *context*, not an identity. Given a country or region tied to a case, this portal supplies the base rates and structural facts an investigator uses to frame a missing-persons or trafficking scenario: intentional-homicide rates, human-trafficking victim/flow data, drug seizures, prison populations, and criminal-justice indicators. Use it to judge how plausible a scenario is or to support a report — never expect it to name a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dataunodc.un.org (it redirects to data.unodc.org).
2. Pick a topic (homicide, trafficking in persons, drugs, prison/prisoners, corruption, firearms) or open a country profile.
3. Filter by country, year, and indicator; read or download (CSV/Excel) the aggregate figures.
4. Use the numbers as context/citations — e.g. trafficking flows for a region, or homicide trends — and pivot to actual person-level sources (national registries, court records) for individuals.

## Inputs → Outputs
- **In:** a country/region (`address`-level context)
- **Out:** aggregate statistics only — no personal selectors. This tool does not return `name`, `dob`, or `document-id` despite the original harvested tags.
- **Empty/negative result looks like:** a country with no reported data for an indicator (common for under-reporting jurisdictions). Missing data reflects reporting gaps, not zero incidence.

## Gotchas & OpSec
- This is a **statistics** resource, not a people search — do not treat it as a record lookup. Its OSINT value is framing and citation, not identification.
- Country coverage and recency vary widely; many indicators lag several years and depend on national reporting.
- OpSec: fully **passive** and anonymous.

## Overlaps ("do both")
- Pairs with regional court/inmate and trafficking-victim registries — UNODC gives the aggregate picture, those give the individual records that actually identify people.

## Trust & verifiability
`trust: trusted` — an official UN data portal with documented methodology and downloadable, citable datasets; authoritative for aggregate figures.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | statistics-and-data |
| category | public-records |
| selectorsIn → selectorsOut | address → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
