---
id: latinobarometro
name: Latinobarometro
description: Use when you need public-opinion/attitudinal data for a Latin American country — returns survey datasets on democracy, economy and society across 18 countries.
url: https://www.latinobarometro.org
category: public-records
path:
- public-records
bestFor: Country-level Latin American public-opinion data (democracy, trust, economy) for context on a place or population.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Datasets and an online analysis tool are publicly available (a free registration is typically needed to download microdata). Run by a non-profit with international backing.
opsec: passive
opsecNote: Passive, aggregate survey data — you query countries/topics, not an individual. No subject data is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by Corporación Latinobarómetro (Santiago, Chile), a long-running reference survey supported by UNDP/IDB/CAF and others; authoritative for its own methodology.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Latinobarómetro
- latinobarometro.org
tags:
- data-and-statistics
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Latinobarometro

> A long-running Latin American public-opinion survey (18 countries) — aggregate attitudinal context, not person-level records.

## When to use
Your case touches a Latin American country and you want authoritative context on public attitudes there — trust in institutions, democracy, economic sentiment, social values. It is aggregate survey data; it holds nothing about specific individuals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.latinobarometro.org.
2. Use the online analysis tool for quick cross-tabs, or register (free) to download the microdata for a given year/country.
3. Read the indicators for your country of interest and note the survey year (annual rounds, ~20,000 interviews across 18 countries).
4. Cite the specific year/question; pair with other regional data for corroboration.

## Inputs → Outputs
- **In:** a country/topic (not a personal selector)
- **Out:** aggregate public-opinion indicators and downloadable datasets
- **Empty/negative result looks like:** a country/year not in a given round — coverage is periodic; check the available years.

## Gotchas & OpSec
- Human-in-the-loop: none for the online tool; microdata download needs a free registration.
- OpSec: passive; nothing about a subject is entered.
- Survey data is aggregate and periodic — read as population-level context, not individual fact.

## Overlaps ("do both")
- Complements the UNDP `[[human-development-reports]]` and World Bank data: Latinobarómetro adds attitudinal/opinion depth for Latin America to those structural indicators.

## Trust & verifiability
`trust: trusted` — a reference regional survey with international institutional backing; authoritative within its survey methodology and coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | latinobarometro |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
