---
id: global-monitoring-system-ecosolve
name: Global Monitoring System - ECOSOLVE
description: Use when investigating online illegal wildlife trade and you want AI-monitored market data across key countries — returns aggregated trafficking-ad trends, no personal selectors.
url: https://www.ecosolve.eco/dashboard
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Aggregated intelligence on online illegal wildlife markets (species, platforms, languages, geographies) from the GI-TOC ECO-SOLVE programme.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Public dashboard and Global Trend Reports are free; full national data-hub feeds are shared with law enforcement and partners, not open to the public.
opsec: passive
opsecNote: You read an aggregated research dashboard — you are not contacting traffickers or touching marketplace listings directly, so there is no target-facing exposure. If you then pivot to the underlying platforms/listings, treat that as separate active work with its own OpSec.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Global Initiative Against Transnational Organized Crime (GI-TOC), EU-funded, and listed in Bellingcat's toolkit; a credible institutional source.
missingPersonsRelevance: low
coverage:
- global
- br
- co
- th
- id
- ng
- za
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- ECO-SOLVE
- ECOSOLVE Global Monitoring System
- GI-TOC ECO-SOLVE
tags:
- bellingcat-toolkit
- environment-wildlife
- wildlife-crime
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Global Monitoring System - ECOSOLVE

> The GI-TOC ECO-SOLVE programme's AI-powered dashboard tracking online illegal wildlife markets across national data hubs — a thematic intelligence source for environmental-crime work.

## When to use
Domain-specific: reach for it when the case involves online illegal wildlife trade (IWT) — trafficking of species, wildlife products, or the marketplaces and networks behind them. The Global Monitoring System aggregates AI-detected trafficking ads across social media and e-commerce in key countries, giving you trend context (which species, platforms, languages, and geographies are active) to orient an investigation. It reports on markets, not individuals, so it returns no personal selectors.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ecosolve.eco/dashboard in a browser.
2. Browse the monitoring dashboard and the published Global Trend Reports for aggregated figures — ad counts, species, platforms, languages, and participating country data hubs (Brazil, Colombia, Thailand, Indonesia, Nigeria, South Africa, expanding over time).
3. Use the trend data to scope an investigation: which platforms and regions are hot for a given species, and how activity is shifting.
4. Pivot: the dashboard points you at the *markets*; run any individual-listing or seller follow-up on the underlying platforms with dedicated OSINT tooling and fresh OpSec.

## Inputs → Outputs
- **In:** none (you browse aggregated data by species/region/platform — not a personal selector)
- **Out:** aggregated wildlife-trafficking market trends and geographies (no personal selectors)
- **Empty/negative result looks like:** a species/region with no recorded ads simply isn't covered by the current data hubs — absence reflects monitoring scope, not absence of trade.

## Gotchas & OpSec
- It is **aggregate intelligence**, not a searchable index of individual sellers — it scopes and contextualises, it does not hand you targets.
- Coverage is limited to the countries with active data hubs and grows edition-by-edition; gaps are common outside those regions.
- OpSec: **passive** for the dashboard itself; any move onto the actual marketplaces is separate active work.

## Overlaps ("do both")
- Use alongside general marketplace/social-media investigation tools: ECO-SOLVE tells you *where and what* is trending in IWT, and those tools let you work individual listings and accounts on the platforms it flags.

## Trust & verifiability
`trust: trusted` — produced by GI-TOC (Global Initiative Against Transnational Organized Crime), EU-funded, and referenced in Bellingcat's investigation toolkit. Institutionally credible; figures are its own AI-assisted monitoring, so cite them as ECO-SOLVE estimates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | global-monitoring-system-ecosolve |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
