---
id: nation-master
name: Nation Master
description: Use when you need country-level context statistics (crime, economy, demographics) to frame an investigation — returns comparable national indicators across 200+ countries.
url: http://www.nationmaster.com/statistics
category: public-records
path:
- public-records
bestFor: Pulling and comparing national statistics (crime rates, demographics, economy, transport, etc.) to add context or baseline figures to a report.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to browse country statistics and comparisons.
opsec: passive
opsecNote: A reference/statistics site; you query country data, never a person. Fully passive with nothing disclosed about any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates public-domain international datasets; figures can be dated or drawn from older source years, so cite the underlying source/year for anything decisive.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- nationmaster.com
- NationMaster
tags:
- statistics
- reference
- public-records
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Nation Master

> A comparative statistics portal — 200+ countries across dozens of categories — for adding baseline national context to a case, not for finding individuals.

## When to use
You need background numbers to frame a report or sanity-check a claim: how a country compares on crime, GDP, internet usage, demographics or transport. This is context tooling — it will not identify a person, but it helps you reason about the environment around a case (e.g. plausibility of a statistic, regional baselines).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.nationmaster.com/statistics.
2. Browse or search a category (economy, crime, health, transport, etc.) and drill into a specific indicator.
3. Compare countries side-by-side or open a country profile for a rounded picture.
4. Note the source and year behind each figure before quoting it.
5. Use the numbers as context in your write-up; verify anything load-bearing against the primary source (World Bank, UN, national statistics office).

## Inputs → Outputs
- **In:** none (you pick a country/indicator)
- **Out:** comparable national statistics and country profiles
- **Empty/negative result looks like:** a missing or "no data" indicator for a country — the dataset simply doesn't cover it; find the primary source instead.

## Gotchas & OpSec
- Figures may be several years old and are only as good as the underlying source — always check the year.
- Context tool only; zero value for locating or profiling a specific person.
- OpSec: fully passive.

## Overlaps ("do both")
- Overlaps with primary statistical sources (World Bank, UN Data, Eurostat) — NationMaster is a convenient front-end, but cite the primary source for accuracy.

## Trust & verifiability
`trust: community` — a useful aggregator of public-domain data, but re-verify decisive numbers against the original statistical source and year.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nation-master |
