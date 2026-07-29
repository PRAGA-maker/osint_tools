---
id: linkscope
name: LinkScope
description: Use when you have any selector (name, email, domain, username) and want a free Maltego-style link-analysis graph that runs resolutions and visualizes connections — returns associate, social-profile, domain and email leads.
url: https://accentusoft.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free, open-source visual link-analysis (entity graphs + automated "resolutions") for OSINT investigations — a Maltego alternative.
selectorsIn:
- name
- email
- domain
- username
selectorsOut:
- associate
- social-profile
- domain
- email
status: live
pricing: free
costNote: Free and open source (AccentuSoft/LinkScope-Client on GitHub); GPL-licensed. Runs locally as a desktop/Docker app. Some resolutions need their own API keys.
opsec: active
opsecNote: Mixed — the graph tool is local, but individual resolutions actively query external services (WHOIS, social sites, search engines, APIs) from your machine, so those leave footprints on the queried services. Route through a proxy/VPN, use sock-puppet API keys, and know which resolutions touch a target directly before running them at scale.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source project (AccentuSoft); a capable Maltego-style tool, but community-maintained — verify each resolution's data source and quality.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- LinkScope
- LinkScope Client
- AccentuSoft
tags:
- other-tools
- link-analysis
- graph
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# LinkScope

> A free, open-source link-analysis platform — build an entity graph, run automated "resolutions" that pull related data, and watch a subject's connections unfold visually. A Maltego alternative you fully control.

## When to use
You're running a multi-step investigation and want to see relationships as a graph rather than a pile of notes: drop in a starting entity (`name`, `email`, `domain`, `username`, phone, etc.), run resolutions to expand it (WHOIS, social lookups, breach data, search), and let LinkScope link the results into a navigable map of associates, accounts, and infrastructure. Best when pivots are numerous and the connections between them are the point — mapping a person's or organization's footprint end to end.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install from https://accentusoft.com/ or the GitHub repo (desktop app or Docker); launch it.
2. Add a starting entity to the canvas (e.g. an email or domain).
3. Add API keys for any resolutions that need them (search engines, breach/social APIs).
4. Right-click the entity → run resolutions; new linked entities appear on the graph. Iterate outward.
5. Pivot: follow high-degree nodes (a shared email/phone linking many accounts) → they're your strongest leads; export the graph for reporting.

## Inputs → Outputs
- **In:** any starting selector — `name`, `email`, `domain`, `username`, phone, etc.
- **Out:** an expanding graph of linked entities — `associate`s, `social-profile`s, `domain`s, `email`s and their relationships
- **Empty/negative result looks like:** a resolution returns no child entities — the source had no data, or the resolution needs an API key/credentials; a bare graph means your resolutions aren't finding links, not that none exist.

## Gotchas & OpSec
- Human-in-the-loop: many useful resolutions require you to supply API keys.
- **Active** — resolutions query external services (and sometimes the target) from your machine; proxy them and use sock-puppet keys.
- Data quality varies per resolution; verify high-stakes links at the source.

## Overlaps ("do both")
- Direct alternative to Maltego CE and SpiderFoot — LinkScope is free/open-source and self-hosted; use SpiderFoot for automated breadth, LinkScope for interactive graph pivoting.

## Trust & verifiability
`trust: community` — capable open-source link-analysis tool; the graph is only as reliable as each resolution's source, so confirm decisive links independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkscope |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, email, domain, username → associate, social-profile, domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (api-key) |
