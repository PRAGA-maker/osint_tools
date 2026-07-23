---
id: linkscope-client
name: LinkScope Client
description: Use when you have any selector and want to build a visual link-analysis graph across OSINT sources — a free, Maltego-style desktop tool that resolves entities into connected entities.
url: https://github.com/AccentuSoft/LinkScope_Client
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free open-source link-analysis/graphing of OSINT entities and their connections (a Maltego alternative).
selectorsIn:
- name
- email
- username
- domain
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open source (AGPL-3.0); desktop installers for Windows/Linux or run from source. No license fee.
opsec: passive
opsecNote: OpSec depends on the resolutions you run — passive lookups (WHOIS, search) leak nothing to the target, but any resolution that actively probes a host or hits an authenticated API carries that API/probe's exposure. Route active resolutions through a VPN and use sock-puppet API keys.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source graph-OSINT client by AccentuSoft; modular and extensible, with quality depending on which resolution modules you use and the sources they query.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- LinkScope
- AccentuSoft LinkScope
tags:
- other-tools
- link-analysis
- graph
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# LinkScope Client

> A free, open-source link-analysis desktop tool — a Maltego-style graph where entities (names, emails, domains, IPs) are resolved into connected entities, letting you build and visualise an investigation.

## When to use
You have one or more selectors and want to grow and *visualise* the connections between them rather than tracking them in notes. Reach for LinkScope when an investigation has enough moving parts that a graph helps — pivoting an email to accounts, a domain to infrastructure, a name to associates — and you want a free alternative to Maltego. It runs resolutions (modules) that take an entity's attributes and return linked entities, drawing the network as you go.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the desktop client (Windows/Linux installer) or run from source (Python).
2. Create a graph and drop in your starting entities (e.g. an `email`, `domain`, `username`).
3. Run resolutions on an entity to expand it into connected entities; chain resolutions to grow the graph.
4. Use the timeline, map, and screenshot features to organise findings; add custom modules for sources you need.
5. Pivot: the graph itself is the workspace — export findings, and feed high-value nodes (a confirmed `social-profile`, an `associate`) into dedicated tools for depth.

## Inputs → Outputs
- **In:** starting selectors — `name`, `email`, `username`, `domain`, etc.
- **Out:** a connected graph of resolved entities — `social-profile`s, `associate`s, infrastructure — with map/timeline views
- **Empty/negative result looks like:** a resolution returning no new entities (source had nothing, or an API key/module is missing/misconfigured) — the graph simply doesn't grow on that branch.

## Gotchas & OpSec
- Output quality = module quality: results depend entirely on which resolution modules you install and the sources/API keys behind them.
- OpSec varies per resolution — passive ones are safe, active/probing ones expose you; know what each module does and route active ones through a VPN with sock-puppet keys.
- It's a framework, not a data source; it's only as good as the tools you wire into it.

## Overlaps ("do both")
- A free counterpart to Maltego and `[[spiderfoot]]`-style automation — use LinkScope for interactive, visual pivoting and a broad automated scanner for breadth; feed each other's findings.

## Trust & verifiability
`trust: community` — a capable open-source graphing client; because it aggregates other sources via modules, verify individual resolved entities against their original source before treating a graph edge as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkscope-client |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, email, username, domain → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
