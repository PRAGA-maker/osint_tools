---
id: circos
name: Circos
description: Use when you have relational data (who-contacts-whom, wallet flows, co-occurrences) and want a circular link diagram to reveal the structure — a visualization tool for investigation findings.
url: http://circos.ca
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Rendering relationships/flows between many entities as a circular (chord) diagram to expose network structure.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Perl); an online table-viewer variant exists for quick charts without installing.
opsec: passive
opsecNote: Circos runs locally on data you already have — it visualizes, it does not query anything. Keep the input data (which may contain sensitive links/PII) on an encrypted volume; nothing is sent anywhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-established open-source visualization tool (originating in genomics, widely used for relational data); mature and stable, though configuration is text-file heavy.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- circos.ca
- Circos plot
tags:
- infographics-and-data-visualization
- network-visualization
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Circos

> A circular link-diagram engine — lay your entities around a ring and draw the connections between them to make network structure and flows visible at a glance.

## When to use
You've gathered relational data during an investigation — communication links between accounts, fund flows between wallets, co-occurrence of names across documents, travel between locations — and want a dense, readable picture of who/what connects to whom. Circos renders many-to-many relationships as a circular chord diagram, which handles more entities legibly than a sprawling node graph. It's a presentation/analysis layer, not a data source.

## How to use it (`bestInteractionPattern`: cli)
1. Install Circos (Perl) locally, or use the online table-viewer for a quick chord chart from a matrix.
2. Prepare your data: a list of entities (segments around the ring) and the weighted links between them.
3. Write the Circos config (karyotype + links + rules) — or paste a relationship matrix into the online viewer.
4. Generate the diagram; read the thickest/most-connected chords as the strongest relationships or largest flows.
5. Pivot: the visual hubs and clusters highlight which entities to investigate next; export the figure for the case report.

## Inputs → Outputs
- **In:** a relationship matrix / edge list you assembled (no live selector)
- **Out:** a circular chord diagram of the relationships (an analysis/communication artifact) — no direct selector output
- **Empty/negative result looks like:** a sparse or unreadable plot — usually too few links or a malformed config/matrix; fix the input data.

## Gotchas & OpSec
- **Steep config:** classic Circos is text-file driven with a learning curve; for a quick chart use the online table viewer or a simpler chord-diagram library (D3/plotly).
- Garbage-in-garbage-out: it faithfully draws whatever links you feed it — verify the underlying relationships are real, not artifacts of your collection.
- **Passive/offline:** keep sensitive relationship data on encrypted local storage; nothing is uploaded when run locally.

## Overlaps ("do both")
- A visualization endpoint for data gathered by other tools (blockchain flows from `[[blockexplorer]]`, contact graphs from social tooling); pairs with node-graph tools like Maltego — Circos for dense flow overviews, node graphs for exploratory pivoting.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source tool; it renders your data faithfully, so trust rests on the quality of the relationships you supply.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | circos |
