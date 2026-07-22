---
id: ora
name: ORA
description: Use when you have a set of `associate` links / `social-profile` connections and want to map and analyse the network — returns centrality, key actors and sub-groups.
url: http://www.casos.cs.cmu.edu/projects/ora/software.php
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a list of people-to-people (or people-to-place) connections into a visual social-network graph with metrics that surface the most-connected actors.
selectorsIn:
- associate
- social-profile
selectorsOut:
- associate
status: live
pricing: freemium
costNote: ORA-LITE is free from CMU CASOS (Windows only, capped at 2,000 nodes per entity class). The full ORA-PRO (PC/Mac, unlimited) is a paid product sold separately by Netanomics.
opsec: passive
opsecNote: Runs entirely offline on your own machine against data you have already collected — no queries leave the desktop, so nothing about the target is disclosed to a third party. OpSec risk is only in how you gathered the underlying relationship data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Developed and maintained by the CASOS centre at Carnegie Mellon University; a long-standing, peer-cited academic tool for dynamic network analysis.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- the-data-and-story-library
aliases:
- ORA-LITE
- ORA-PRO
- CASOS ORA
tags:
- social-network-analysis
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# ORA

> A CMU academic desktop tool for social-network and link analysis: feed it who-knows-whom and it ranks the key actors and clusters.

## When to use
You have already assembled a set of relationships — `associate`-to-`associate` links, `social-profile` follower/friend edges, or people-to-organisation ties — and you want to move past a hand-drawn diagram to see which node is the true hub, which sub-groups exist, and who bridges them. Useful late in a case when a subject's network is large enough that structure is not obvious by eye.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download ORA-LITE from the CASOS page (`http://www.casos.cs.cmu.edu/projects/ora/`); it is a Windows desktop install. Mac users need the paid ORA-PRO from Netanomics.
2. Prepare your network as a node list + edge list (CSV/DyNetML) — e.g. one row per `associate`→`associate` connection you have evidenced.
3. Import the data as a meta-network, then run the reports: centrality (degree/betweenness) to find the most-connected and the brokers, and grouping/clustering to find sub-communities.
4. Read the visualisation and the metric tables together — a high-betweenness node is the person whose removal would fragment the network.
5. Pivot: the surfaced key actor becomes a new subject to run through people-search and `social-profile` tools.

## Inputs → Outputs
- **In:** `associate` / `social-profile` relationship data you supply (node + edge lists)
- **Out:** ranked key actors, brokers, and clustered sub-groups (`associate` structure)
- **Empty/negative result looks like:** a flat graph where every node has similar centrality — meaning your data is too sparse or too uniform to reveal structure, not that the tool failed.

## Gotchas & OpSec
- ORA-LITE is Windows-only and capped at 2,000 nodes per entity class; large networks need ORA-PRO (paid).
- It analyses only what you import — garbage in, garbage out. Weakly-evidenced edges will produce confident-looking but false structure.
- OpSec: fully offline; no target data leaves your machine.

## Overlaps ("do both")
- Pairs with `[[the-data-and-story-library]]` for sourcing and structuring the underlying datasets before you model the network in ORA.

## Trust & verifiability
`trust: trusted` — maintained by Carnegie Mellon's CASOS centre and widely cited in academic network-analysis literature; results are reproducible from your own inputs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ora |
