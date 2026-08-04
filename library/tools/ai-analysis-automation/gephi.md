---
id: gephi
name: Gephi
description: Use when you have a set of `associate`/entity relationships and want to visualize and analyze them as a network graph — returns clustered link-analysis charts revealing key nodes and communities.
url: https://gephi.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning relationship data (people, accounts, domains) into an interactive link-analysis graph to find central nodes and communities.
selectorsIn:
- associate
- name
- social-profile
- domain
selectorsOut:
- associate
status: live
pricing: free
costNote: Free and open-source (GPL); no account, no paid tier. Donation-supported.
opsec: passive
opsecNote: Gephi runs entirely on your own machine and does not contact any subject — analysis is fully offline once your data is loaded. Keep sensitive case graphs on an encrypted local disk; nothing is uploaded.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Long-established open-source project used by universities and cited in 10,000+ peer-reviewed papers; the software is reputable, though the analysis quality depends entirely on the data you feed it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- gephi
- gephi lite
tags:
- link-analysis
- network-graph
- visualization
- awesome-osint
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Gephi

> The standard open-source tool for network/link analysis: load your entities and relationships, and Gephi lays them out as a graph that exposes the central players and hidden communities.

## When to use
You have collected a web of relationships during an investigation — who talks to whom, which accounts share an operator, which domains resolve together — and a list is no longer enough to see the structure. Gephi turns that edge list into an interactive graph, runs centrality and community-detection algorithms, and visually surfaces the `associate` most connected to your subject, bridge nodes between groups, and clusters worth deeper investigation.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Gephi from https://gephi.org (Windows/macOS/Linux; or try Gephi Lite in-browser for small graphs).
2. Prepare your data as a nodes list and an edges list (CSV/GEXF) — e.g. nodes = people/accounts/domains, edges = "co-appears with", "follows", "resolves to".
3. Import via **File → Import spreadsheet** (or open a GEXF).
4. Run a layout (ForceAtlas 2) and statistics: Degree/Betweenness centrality to find key nodes, Modularity to detect communities; size/colour nodes by those metrics.
5. Read the graph: large/high-betweenness nodes are the connectors around your subject; distinct colour clusters are candidate sub-networks.
6. Pivot: an unexpectedly central `associate` becomes your next research target; export the graph (PNG/PDF/GEXF) for the case file.

## Inputs → Outputs
- **In:** an entity + relationship dataset (`name`/`social-profile`/`domain` nodes, `associate` edges)
- **Out:** an interactive network graph, centrality/community metrics, and the key `associate` links it reveals
- **Empty/negative result looks like:** a sparse, disconnected graph with no clusters — usually a sign your edge data is too thin; gather more relationships before drawing conclusions.

## Gotchas & OpSec
- Garbage in, garbage out: Gephi visualizes whatever edges you supply — it does not gather data. Build a clean, sourced dataset first.
- Large graphs (100k+ nodes) need RAM and layout tuning; start small.
- Fully local: a strong OpSec property — no case data leaves your machine.

## Overlaps ("do both")
- Complements data-collection/scraping tools and Maltego-style transforms — those gather the relationships; Gephi is where you analyse and visualize them at scale for free.

## Trust & verifiability
`trust: trusted` — a mature, widely-cited open-source project; the tool is dependable, so the reliability of any conclusion rests on the provenance of the edges you import, not on Gephi itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gephi |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | associate, name, social-profile, domain → associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
