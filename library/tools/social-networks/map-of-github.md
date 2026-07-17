---
id: map-of-github
name: Map of Github
description: Use when you have a GitHub repository or topic and want to see related projects clustered by similarity — returns a visual map of neighboring repos to expand a technical footprint.
url: https://anvaka.github.io/map-of-github/
category: social-networks
path:
- social-networks
bestFor: Discovering repositories related to a known project by browsing a similarity-clustered map.
selectorsIn:
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free static visualization hosted on GitHub Pages; no account or key required.
opsec: passive
opsecNote: A pre-computed static map of public GitHub data; you are not querying GitHub live or touching any target. Fully passive, no attribution risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source hobby visualization by Andrei Kashcha (anvaka), built from public GitHub star/relationship data; it is an exploration aid, not an authoritative index.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- map-of-reddit
aliases:
- map of github
- anvaka map-of-github
tags:
- Social Media
- Github
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Map of Github

> A "city map" of GitHub where each repository is a point and similar projects cluster into neighborhoods — a way to explore what surrounds a project you already know.

## When to use
You have a known GitHub repository, topic, or a `username`'s notable project and want to discover adjacent projects, communities, and technologies clustered around it. In an investigation this is a lateral-discovery aid: from a subject's key repo you can spot the ecosystem it lives in, related maintainers, and thematically close projects that might tie back to the same person or group. It is a niche, exploratory tool — low direct relevance to person-finding, but occasionally useful for mapping a technical persona.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://anvaka.github.io/map-of-github/ and let the WebGL map load.
2. Use the search box to jump to a specific repository name; the map centers on it and shows its neighborhood.
3. Zoom/pan to read nearby repository labels — proximity encodes similarity (shared audiences/stars).
4. Click a repo to open its GitHub page and inspect maintainers, contributors, and linked accounts.
5. Pivot: interesting maintainers/repos feed GitHub profile inspection and username tools.

## Inputs → Outputs
- **In:** a GitHub repository name / project tied to a `username`
- **Out:** a visual cluster of related repositories, each linking to a GitHub `social-profile` / project `domain`
- **Empty/negative result looks like:** the repository isn't on the map (the dataset is a snapshot, not all of GitHub) — fall back to GitHub's own search and "used by"/dependents graph.

## Gotchas & OpSec
- Built from a point-in-time dataset, so very new or very small repos may be absent, and clustering reflects star/relationship data, not authorship links — proximity is thematic, not proof of a shared owner.
- Heavy WebGL map; it can be slow on low-end machines.
- OpSec: **passive** — a static pre-computed visualization; no live queries to GitHub or the target.

## Overlaps ("do both")
- Pairs with [[map-of-reddit]] (same author, same technique) when a subject's footprint spans both platforms and you want to map communities rather than individuals.

## Trust & verifiability
`trust: community` — an open-source hobby visualization from public GitHub data; treat it as a discovery/brainstorming aid and confirm any lead directly on github.com.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | map-of-github |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
