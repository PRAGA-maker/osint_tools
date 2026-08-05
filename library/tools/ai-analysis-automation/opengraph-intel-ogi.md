---
id: opengraph-intel-ogi
name: OpenGraph Intel (OGI)
description: Use when you have a seed selector (`domain`, `ip-address`, `email`, `username`) and want to build and enrich a visual link-analysis graph via transforms — returns connected entities and relationships.
url: https://github.com/khashashin/ogi
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Building a Maltego-style visual link-analysis graph and enriching entities with pluggable transforms.
selectorsIn:
- domain
- ip-address
- email
- username
selectorsOut:
- domain
- ip-address
- email
- social-profile
status: live
pricing: free
costNote: Free and open source (AGPL-3.0); self-host locally or via Docker. A hosted instance (ogi.khas.app) offers optional paid "Supporter" tiers, but self-hosting is fully free.
opsec: active
opsecNote: Transforms query external data sources (DNS, WHOIS, certificate transparency, social media) about your entities — some of those queries touch the target's infrastructure. Self-host and route through a proxy/VPN for sensitive investigations rather than using the shared cloud instance.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: An open-source link-analysis framework by developer khashashin; auditable, but transform quality varies since community transforms wrap third-party sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OGI
- ogi.khas.app
tags:
- other-tools
- link-analysis
- graph
- maltego-alternative
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OpenGraph Intel (OGI)

> An open-source visual link-analysis framework — a self-hostable Maltego alternative: drop in a seed entity, run transforms that pull from DNS, WHOIS, certificate transparency, and social media, and watch the relationship graph grow.

## When to use
You have one or more seed selectors (a `domain`, `ip-address`, `email`, or `username`) and want to pivot outward visually, letting relationships between infrastructure and identities emerge as a graph rather than a list. OGI is the tool when the investigation has enough moving parts that a link chart clarifies it, and you want a free, self-hosted alternative to commercial link-analysis suites.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy from `https://github.com/khashashin/ogi` — Docker locally, or open the hosted instance at ogi.khas.app (self-host for anything sensitive).
2. Add a seed entity (domain, IP, email, username) or import an existing graph (JSON/CSV/GraphML).
3. Run transforms on entities to enrich them — built-in and community transforms query DNS, WHOIS, cert-transparency logs, and social media; use the CLI to search/install/manage transforms.
4. Read the graph: new connected entities and edges. Export in multiple formats.
5. Pivot: promising nodes (a new domain, a linked account) become seeds for further transforms or handoff to specialist tools.

## Inputs → Outputs
- **In:** seed `domain` / `ip-address` / `email` / `username`, or an imported graph
- **Out:** an enriched graph of connected entities (`domain`s, `ip-address`es, `email`s, `social-profile`s) and their relationships
- **Empty/negative result looks like:** transforms return no new edges — either the entity is genuinely isolated or the relevant transform/source is missing; try additional transforms before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none required, but you choose which transforms to run and must self-host for privacy.
- OpSec: **active** — transforms make outbound queries, some against the target's own infrastructure. Self-host and proxy for sensitive work; do not run those through the shared cloud instance.
- Output quality tracks the transforms: community transforms wrap third-party sources of varying reliability — verify key edges at their primary source.

## Overlaps ("do both")
- Pairs with the classic transform sources it wraps (WHOIS, crt.sh, DNS tools) and with commercial link-analysis suites — OGI orchestrates and visualises, the primaries give authoritative single-dimension data; confirm decisive links directly.

## Trust & verifiability
`trust: community` — open source and auditable, but a graphing/orchestration layer over third-party data. Trust the graph's structure; verify each edge against the source its transform queried before treating a link as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opengraph-intel-ogi |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain, ip-address, email, username → domain, ip-address, email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | active |
| human-in-loop | no |
