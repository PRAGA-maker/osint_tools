---
id: chart-js
name: Chart.js
description: Use when you have structured findings (timelines, frequencies, link counts) and want to render them as clean web charts — an open-source JS library for visualizing OSINT data in reports.
url: https://www.chartjs.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning collected data into shareable charts inside an HTML report or dashboard.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (MIT license); runs entirely client-side, no account or server.
opsec: passive
opsecNote: Runs locally in your own page/browser — nothing is transmitted, so no case data leaves your machine unless you host the report somewhere. Safe for sensitive datasets when kept local.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Widely used, well-maintained open-source charting library with a large community; it renders your data and holds none of its own.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- chartjs
- chart.js
tags:
- infographics-and-data-visualization
- reporting
- data-viz
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Chart.js

> A free, open-source JavaScript charting library — feed it your collected data and it draws clean line/bar/network/pie charts for reports and dashboards.

## When to use
You've gathered data during an investigation — a timeline of posts, frequency of contacts, activity by hour, counts of linked domains — and want to present it visually in an HTML report or internal dashboard rather than a raw table. Chart.js is the rendering layer: it doesn't collect anything, it makes your own findings legible and shareable.

## How to use it (`bestInteractionPattern`: python-lib / web)
1. Get the docs and examples at https://www.chartjs.org (and the GitHub repo).
2. Include the library in an HTML page (via a bundled/local copy — keep it offline for sensitive work) and add a `<canvas>` element.
3. Format your data as JSON arrays (labels + datasets) — e.g. export from a Python/pandas step to feed the chart config.
4. Choose a chart type (line for timelines, bar for frequencies, scatter/bubble for correlations) and configure axes, tooltips and colors.
5. Open the page locally to render; embed the result in your report. Pivot: pair with a static-report generator so charts sit alongside your written findings.

## Inputs → Outputs
- **In:** your structured data (no OSINT selector — this is a presentation tool)
- **Out:** rendered charts/graphs (no OSINT selector)
- **Empty/negative result looks like:** a blank canvas or console error — usually malformed data or a missing element, not a data-collection failure. It only visualizes what you give it.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must structure the data yourself; garbage-in/garbage-out.
- OpSec: **passive** and local — nothing leaves your machine when run offline, which makes it safe for sensitive datasets. If you publish the HTML anywhere, the underlying data ships with it, so scrub before sharing.
- It's a dev library, not a point-and-click app; expect to write a little HTML/JS or generate it from a script.

## Overlaps ("do both")
- Complements data-collection tooling — those gather selectors and links; Chart.js turns the resulting tallies and timelines into visuals for the final report.

## Trust & verifiability
`trust: trusted` — a mature, popular open-source library; it faithfully renders whatever data you supply and stores nothing itself, so verifiability rests on your source data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chart-js |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
