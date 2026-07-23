---
id: tableau-public
name: Tableau Public
description: Use when you have tabular investigation data (or want to search others' published dashboards) and need interactive visual analysis — returns shareable charts and, via search, third-party datasets tied to a name/employer-org.
url: https://public.tableau.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free interactive dashboards for exploring your own case data, plus a searchable gallery of others' published vizzes.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free tier of Tableau (Salesforce). The catch — everything you publish to Tableau Public is PUBLIC and searchable; there is no private save.
opsec: passive
opsecNote: Analyzing data locally in Tableau Public Desktop is passive, but PUBLISHING is not — saved workbooks are world-visible and indexed. Never publish case data, PII, or anything that reveals your subject or your interest. Treat it as a public broadcast.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Operated by Tableau/Salesforce; the platform is legitimate, though individual user-published dashboards are unverified third-party content.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- Tableau
tags:
- infographics-and-data-visualization
- data-analysis
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Tableau Public

> The free, public-only edition of Tableau: build interactive dashboards from your data, and mine the gallery of dashboards other people have already published.

## When to use
Two distinct cases. (1) You have a spreadsheet of investigation data — call logs, transactions, timelines, geodata — and want to explore it visually to spot patterns. (2) You want to search the Tableau Public gallery, where analysts, journalists, and companies publish dashboards that sometimes embed spreadsheets referencing a `name` or `employer-org`. It is an analysis/visualization tool, not a people-search engine.

## How to use it (`bestInteractionPattern`: desktop-app)
1. For analysis: download Tableau Public Desktop (free, needs a free account to save), connect your CSV/Excel, and drag fields onto the canvas to build charts.
2. Keep it local — do NOT click Publish for anything sensitive; Tableau Public has no private save.
3. For discovery: go to public.tableau.com and use the gallery search / your favorite web search with `site:public.tableau.com "term"` to find dashboards mentioning a target org, place, or dataset.
4. Open a found viz, then **Download** its underlying data if the author left it enabled — this can expose an embedded source spreadsheet.
5. Pivot: an exposed dataset → normal records analysis; a company dashboard → the org's own reporting.

## Inputs → Outputs
- **In:** your own tabular data, or a search `name`/`employer-org`/topic for the gallery.
- **Out:** interactive charts you build, and third-party published dashboards (sometimes with downloadable source data referencing an `employer-org`).
- **Empty/negative result looks like:** a gallery search with no relevant vizzes, or a found dashboard whose author disabled data download — you see the picture but can't pull the numbers.

## Gotchas & OpSec
- **Everything you publish is public and indexed** — this is the single biggest footgun; never publish case material.
- Free account (login) is required to save/publish; pure viewing/search needs no account.
- Gallery data quality is entirely on the (unverified) author; corroborate before trusting figures.

## Overlaps ("do both")
- Complements generic link-analysis/mindmap tools: Tableau is for quantitative pattern-finding in tabular data, while diagramming tools handle entity-relationship mapping.

## Trust & verifiability
`trust: trusted` for the platform (Salesforce-operated); individual published dashboards are unverified user content — always trace figures to their stated source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tableau-public |
