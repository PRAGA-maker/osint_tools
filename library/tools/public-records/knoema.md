---
id: knoema
name: Knoema
description: Use when you need authoritative statistics to contextualise a place, sector or claim — returns curated public datasets, indicators and visualizations by country and topic.
url: https://knoema.com
category: public-records
path:
- public-records
bestFor: Pulling country/sector statistics and indicators to ground-truth or contextualise an investigative claim.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free to browse and visualize public datasets; advanced data-hub/enterprise features are paid, and some datasets prompt for a free account.
opsec: passive
opsecNote: A public data-aggregation platform — you look up statistics, not people; nothing about a subject is submitted. Standard browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial data aggregator (an Eldridge business) that republishes third-party official statistics; reliable as a convenient front-end, but cite the original source and check the dataset's date.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- knoema.com
tags:
- data-and-statistics
- open-data
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Knoema

> A data-aggregation platform that gathers official statistics from thousands of sources into browsable, visualizable datasets — use it to contextualise a place, industry or claim, not to look up a person.

## When to use
Your case needs a factual backdrop: economic, demographic, energy, agriculture or trade figures for a country or region, or an indicator to sanity-check a claim ("is that export volume plausible?"). Knoema consolidates public datasets from national statistics offices, the World Bank, the UN and others into one searchable interface with charts, saving you from hunting each primary source separately. It returns aggregate data, not person-level records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://knoema.com and search by topic, indicator, or country.
2. Open a dataset; read the values and note the *original* source and reference year shown on the page.
3. Visualize or download the series as needed; some datasets may prompt for a free account.
4. Pivot: cite and, for anything load-bearing, verify against the original source (World Bank, national statistics office, etc.).

## Inputs → Outputs
- **In:** topic / indicator / country (no personal selector)
- **Out:** curated datasets, indicators, time series and visualizations
- **Empty/negative result looks like:** a dataset that is stale, discontinued, or thinner than the primary source — Knoema mirrors upstream data and can lag, so check the date.

## Gotchas & OpSec
- Human-in-the-loop: occasionally a free account for certain datasets/downloads.
- OpSec: passive — a statistics lookup; no subject interaction.
- Provenance: it re-hosts third-party data; always attribute and verify the original source, and mind the reference year.

## Overlaps ("do both")
- Pairs with primary open-data portals (World Bank, UN, national statistics offices) because Knoema is a convenient aggregator, but the authoritative figure and latest revision live at the source.

## Trust & verifiability
`trust: community` — a commercial aggregator of official data; convenient and generally accurate, but cite and cross-check the underlying source for anything that matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
