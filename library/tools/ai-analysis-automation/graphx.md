---
id: graphx
name: GraphX
description: Use when you have a very large relationship dataset (millions of edges) and want to compute graph analytics — Apache Spark's distributed graph engine (a library, no selectors of its own).
url: http://spark.apache.org/graphx
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Distributed, large-scale graph computation (PageRank, connected components, community detection) on huge relationship datasets.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Apache 2.0), part of Apache Spark; cost is the compute cluster you run it on.
opsec: passive
opsecNote: GraphX runs on your own Spark cluster over data you already hold, making no external calls about any subject. The exposure is entirely operational — bulk relationship data on shared/cloud compute must be secured; process sensitive data on infrastructure you control.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: Apache Spark is a mature, widely-used open-source project under the Apache Software Foundation; GraphX is a first-party Spark component.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- Spark GraphX
- Apache Spark GraphX
tags:
- infographics-and-data-visualization
- graph-analytics
- big-data
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
relatedTools:
- apache-tika
---

# GraphX

> Apache Spark's distributed graph-computation engine — the heavy-machinery option for running analytics over relationship graphs too large to fit one machine.

## When to use
Your investigation has produced a graph at a scale that breaks desktop link tools — millions of nodes/edges from bulk telecom records, large breach corpora, or blockchain transaction graphs — and you need to *compute* over it: rank the most central actors (PageRank), find connected components (who clusters with whom), or detect communities. GraphX distributes that computation across a Spark cluster. It is analytics infrastructure requiring engineering effort, not a point-and-click OSINT lookup, and it finds nothing on its own.

## How to use it (`bestInteractionPattern`: python-lib)
1. Stand up Apache Spark (locally for small jobs, or a cluster for real scale).
2. Load your relationship data into Spark and build a graph (GraphX in Scala, or GraphFrames from PySpark).
3. Run algorithms — PageRank, connected components, triangle count, label propagation for communities.
4. Export the computed metrics (centralities, cluster ids) back to your dataset.
5. Pivot: high-centrality nodes and cross-cluster bridges become priority targets; visualize the reduced result in a lighter tool like `[[vis-js]]`.

## Inputs → Outputs
- **In:** a large edge/vertex dataset (yours)
- **Out:** computed graph metrics (centrality scores, component/cluster labels) — analytics, no personal selectors
- **Empty/negative result looks like:** a job that runs but yields uninformative uniform scores — often a data or graph-construction problem (wrong edge direction, disconnected graph), not a finding.

## Gotchas & OpSec
- Human-in-the-loop: none at runtime, but substantial setup — you need Spark and data-engineering skill; overkill for small graphs.
- OpSec: passive and self-hosted; the risk is operational (securing bulk sensitive data on your compute), not target-facing.
- Scala-first; from Python most people use GraphFrames rather than raw GraphX.

## Overlaps ("do both")
- Pairs with `[[vis-js]]` and `[[apache-tika]]` — GraphX crunches the graph at scale and Tika helps extract entities from documents to build it; Vis.js renders the distilled result for human review.

## Trust & verifiability
`trust: trusted` — a first-party Apache Spark component from a mature, well-governed open-source project; results are as reliable as your input graph and algorithm choice, both of which you control and can re-run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | graphx |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
