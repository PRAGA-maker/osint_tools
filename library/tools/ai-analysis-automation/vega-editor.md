---
id: vega-editor
name: Vega Editor
description: Use when you have investigation data and want a quick interactive chart/graph — returns rendered Vega/Vega-Lite visualizations from a JSON spec, in-browser.
url: https://vega.github.io/editor/#/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Prototyping charts and node-link/network graphs from your own data using Vega/Vega-Lite specs, entirely in the browser.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source online editor hosted by the Vega project (University of Washington IDL). No account.
opsec: passive
opsecNote: The editor runs client-side in your browser; specs and data you paste are processed locally and not uploaded, unless you explicitly use the Gist share feature. Avoid the share/export-to-Gist option with sensitive data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official editor for the well-established open-source Vega/Vega-Lite visualization grammars, maintained by the UW Interactive Data Lab.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Vega-Lite editor
- vega.github.io editor
tags:
- data-visualization
- charts
- analysis
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Vega Editor

> The official in-browser playground for Vega/Vega-Lite: paste a JSON spec plus your data and get an interactive chart or network graph back instantly.

## When to use
You've collected structured investigation data — a timeline, a table of transactions, a set of relationships between `associate`s — and want to *see* it as a chart, timeline, or node-link graph to spot patterns. Vega Editor renders Vega and Vega-Lite specifications live, letting you iterate on a visualization without installing anything. It's an analysis/presentation aid, not a data source; missing-persons relevance is low (visualizing case data you already have).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vega.github.io/editor/#/.
2. Choose Vega-Lite (simpler, declarative) or Vega (lower-level, more control) from the mode selector.
3. Paste or edit a JSON spec; inline your data under `"data": {"values": [...]}` or point to a URL. Start from the built-in Examples menu and adapt.
4. The chart renders in the right pane and updates as you edit; use the export menu to save SVG/PNG or share.
5. Pivot: export the graphic for a report, or move the finished spec into an embedded Vega-Lite view in your own page/notebook.

## Inputs → Outputs
- **In:** a Vega/Vega-Lite JSON spec + your own dataset (no library selectors — you supply arbitrary data)
- **Out:** a rendered, interactive visualization (exportable as SVG/PNG)
- **Empty/negative result looks like:** a blank canvas plus a red spec-error message — almost always a malformed spec or a field name that doesn't match your data; fix the JSON and it re-renders.

## Gotchas & OpSec
- It visualizes data you provide — it collects nothing itself.
- There's a learning curve to the grammar; lean on the Examples gallery and start with Vega-Lite.
- OpSec: data stays client-side unless you use the Gist share feature — don't share sensitive case data that way.

## Overlaps ("do both")
- Complements dedicated link-analysis tools (Maltego, Gephi) for relationship graphs and general chart libraries — Vega Editor is the fast, no-install option for a one-off custom visualization from raw JSON.

## Trust & verifiability
`trust: trusted` — the official editor for a mature, widely-used open-source visualization project; it's a rendering tool, so correctness depends entirely on the data and spec you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vega-editor |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
