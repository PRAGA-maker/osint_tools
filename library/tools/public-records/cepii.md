---
id: cepii
name: CEPII
description: Use when you need international-economics datasets (trade flows, gravity, country geography) for context — returns free downloadable research databases.
url: http://www.cepii.fr/CEPII/en/welcome.asp
category: public-records
path:
- public-records
bestFor: Free, well-documented international-economics databases (bilateral trade, gravity models, country/geography data) for analytical context.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Open-access research databases (e.g. CHELEM, BACI, Gravity) with documentation; free, no account. As of July 2026 CEPII merged with OFCE into the Institut français d'économie (IFE).
opsec: passive
opsecNote: Passive, aggregate economic data — you query countries/flows, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by CEPII, France's leading international-economics research centre (now part of IFE, affiliated with Sciences Po); authoritative, well-documented datasets.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Centre d'Etudes Prospectives et d'Informations Internationales
- cepii.fr
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# CEPII

> France's international-economics research centre and its free databases — trade flows, gravity models and country geography for analytical context, not person-level records.

## When to use
Your case needs macro/international-economics context — bilateral trade between countries, gravity-model variables, country geographic/economic indicators. It supplies aggregate research datasets; it holds nothing about specific individuals or companies by name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.cepii.fr/CEPII/en/welcome.asp (now under the merged IFE/Sciences Po; content remains accessible).
2. Browse the databases section (e.g. CHELEM for world trade, BACI for bilateral trade, the Gravity dataset, GeoDist).
3. Download the dataset and its documentation; read the methodology notes before use.
4. Cite the specific database and version; combine with World Bank/national trade stats for corroboration.

## Inputs → Outputs
- **In:** a country/trade-flow question (not a personal selector)
- **Out:** downloadable international-economics datasets with documentation
- **Empty/negative result looks like:** a country/year outside a dataset's scope — check the dataset's documented coverage and pick the right database.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; nothing about a subject is entered.
- Datasets are aggregate and research-oriented — read the methodology; note the 2026 CEPII→IFE merger may relocate some pages over time.

## Overlaps ("do both")
- Complements World Bank and `[[world-bank-enterprise-surveys]]` trade/firm data: CEPII adds curated bilateral-trade and gravity datasets for deeper international-economics analysis.

## Trust & verifiability
`trust: trusted` — a leading research centre's well-documented datasets; authoritative within each database's stated methodology and coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cepii |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
