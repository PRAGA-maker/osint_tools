---
id: data-visualization-catalogue
name: The Data Visualization Catalogue
description: Use when you have investigation data to present and want to pick the right chart type — returns a reference of 80+ visualization methods indexed by the analytical function they serve.
url: https://datavizcatalogue.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Choosing how to visualise link-analysis, timeline, or distribution data when writing up an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Catalogue is free to browse; the site also sells optional icon sets, but nothing needed for reference use is paywalled.
opsec: passive
opsecNote: Purely a reference site — you browse chart descriptions, you never submit case data. No target contact and nothing to leak.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independently maintained reference by designer Severino Ribecca; widely cited in data-viz teaching. Not an OSINT data source — a methods catalogue.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- datavizcatalogue
- DataViz Catalogue
tags:
- infographics-and-data-visualization
- reference
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# The Data Visualization Catalogue

> A browsable reference of 80+ chart types, indexed by what each one is *for* — pick the correct visualization instead of defaulting to a bar chart.

## When to use
Reach for this at the write-up/analysis stage, not the collection stage. When you have investigation data — a network of associates, an activity timeline, a geographic distribution, a set of proportions — and need to decide how to render it so the pattern is legible to a reader or reviewer. It is a design aid, not a data source; it surfaces no records about any person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://datavizcatalogue.com.
2. Use **Search by Function** (e.g. "Analyse relationships", "Show change over time", "Compare proportions") to narrow to fitting chart types, or **View by List** to browse all methods.
3. Open a method to read what it shows, when to use it, and its limitations, with a worked example.
4. Apply the choice: e.g. a link chart / node-link diagram for associate networks, a timeline for activity, a choropleth for geographic spread.
5. Pivot: implement the chosen chart in your reporting tool of choice.

## Inputs → Outputs
- **In:** none (reference only — you bring the analytical question, not a selector)
- **Out:** none (guidance on visualization method, not data about a subject)
- **Empty/negative result looks like:** N/A — it is a static catalogue; there is no query that "fails."

## Gotchas & OpSec
- This is a methods reference, not an intelligence tool — it will not find or enrich anything about a person.
- Fully passive: nothing you type leaves your browser as a query about a target.
- Some polished assets (icon sets) are for sale; the core catalogue you need is free.

## Overlaps ("do both")
- Complements any link-analysis or mapping tool in the library — those produce the data; this helps you present it well. No direct data overlap.

## Trust & verifiability
`trust: community` — a respected independent reference by Severino Ribecca, useful for methodology; it makes no data claims about individuals, so there is nothing to verify against a source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | data-visualization-catalogue |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
