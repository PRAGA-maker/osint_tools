---
id: exhibit
name: Exhibit (SIMILE Widgets)
description: Use when you have structured case data (JSON/CSV) and want a filterable, mappable, timelined web view — an open-source framework for data-rich interactive pages.
url: http://www.simile-widgets.org/exhibit/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Publishing your own structured dataset as a searchable, faceted web page with maps and timelines.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open-source (BSD license); self-hosted, no account or payment.
opsec: passive
opsecNote: A local/self-hosted presentation framework — it renders data you already hold and contacts no subject. If you embed live map tiles, those tile requests go to the map provider; host offline or use a research network for sensitive datasets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Legacy MIT SIMILE project (copyright through ~2013), still online and BSD-licensed but effectively unmaintained; solid for what it does but expect no updates or support.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SIMILE Exhibit
- Exhibit
tags:
- infographics-and-data-visualization
- data-publishing
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Exhibit (SIMILE Widgets)

> A legacy but still-usable open-source framework (from MIT's SIMILE project) for turning a structured dataset into a filterable, mappable, timelined web page — no backend required.

## When to use
This is an analysis/presentation aid, not a discovery tool. Use it when you already have structured case data — a JSON/CSV of people, events, locations, dates — and want an interactive web view to explore it: facet-filter by attributes, plot points on a map, lay events on a timeline. Handy for making sense of, or briefing others on, a medium-sized dataset you assembled.

## How to use it (`bestInteractionPattern`: web-manual)
1. Prepare your data as JSON (Exhibit's format) or a supported CSV.
2. Create an HTML page that includes the Exhibit library and points to your data.
3. Declare views — a map, a timeline, tiles, a table — and facets (filter controls) for the fields you care about.
4. Open the page locally in a browser; filter, sort, and pivot through your data interactively.
5. Use the resulting view to spot clusters/gaps or to present findings.

## Inputs → Outputs
- **In:** your own structured dataset (JSON/CSV) — no external selector
- **Out:** an interactive, faceted, mapped/timelined web view of that data
- **Empty/negative result looks like:** a blank exhibit / broken view — usually malformed data JSON or a stale library path, not a lack of results.

## Gotchas & OpSec
- Effectively unmaintained (copyright ~2013); modern browser or map-tile API changes may need workarounds, and there's no support channel.
- It visualizes only data you supply — quality and provenance are entirely on your input.
- Self-hosting keeps sensitive data local; watch for outbound map-tile calls if that matters.

## Overlaps ("do both")
- Overlaps with modern data-viz/timeline tools — Exhibit is lightweight and self-contained, but for actively maintained faceting/mapping you may prefer a current library; use whichever your dataset and skills fit.

## Trust & verifiability
`trust: community` — a respected but frozen academic project; reliable for local visualization, yet unmaintained, so validate that it still renders correctly in your browser before depending on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | exhibit |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | (none) → (none) |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
