---
id: osint-framework-2
name: OSINT Framework
description: Use when you have any selector and want to discover which tools exist for it — a navigable directory tree that maps a data type (username, email, phone, image, etc.) to relevant resources.
url: https://osintframework.com/
category: search-engines
path:
- search-engines
bestFor: Discovering the right category of tool for a given selector by browsing a categorized resource tree.
selectorsIn:
- name
- username
- email
- phone
- domain
- ip-address
- image
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free, open web directory (also open-source on GitHub). No account.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing about a target — it only lists tools. OpSec depends entirely on which linked tool you then use; evaluate each leaf site separately.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The canonical, long-maintained OSINT resource tree (11k+ GitHub stars; osintframework.com). It is a curated index, not a data source; individual leaf links vary widely in quality.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- start-me
- osint-combine
- osint-framework
- osint-framework-3
aliases:
- osintframework.com
- lockfale/OSINT-Framework
tags:
- directory
- resource-tree
- meta-resource
source: gh-topic-footprinting
lastVerified: '2026-07-10'
enrichment: full
---

# OSINT Framework

> Not a lookup tool but a map of them — a browsable tree that, given a selector you hold, points you to the categories of tools built to work on it.

## When to use
You have a selector (a `username`, `email`, `phone`, `image`, `domain`, `ip-address`, `name`, or `social-profile`) and you're not sure which tool to reach for. OSINT Framework organizes hundreds of resources into an expandable tree by data type and task, so it's the fastest way to orient at the start of an investigation or to discover a category of tool you didn't know existed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osintframework.com/ (the interactive tree; also mirrored as the `lockfale/OSINT-Framework` GitHub repo you can self-host).
2. Expand the branch matching your selector (e.g. Username, Email Address, Images/Videos/Docs).
3. Drill into sub-branches (task-specific) and open the leaf links to candidate tools.
4. Treat each leaf as a starting point — assess the linked site's freshness, pricing, and trust yourself, since quality varies and some links rot.
5. Pivot: use it to plan a workflow (which selector → which tool category), then execute with the specific tools (many of which are catalogued here in this library).

## Inputs → Outputs
- **In:** any selector you hold (used to pick a branch)
- **Out:** a curated list of candidate tools/resources for that selector (not data about a person)
- **Empty/negative result looks like:** a branch with only stale or dead links — the framework is broad but not exhaustively maintained; supplement with other tool directories.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: **passive** — it exposes nothing about your target; risk lives entirely in the downstream tools you choose.
- Link rot: some leaves point to defunct or low-quality sites; verify before relying.

## Overlaps ("do both")
- Pairs with `[[start-me]]` — curated start.me OSINT pages cover overlapping ground with more human commentary.
- Pairs with `[[osint-combine]]` — task-oriented tools and guides that complement the raw directory tree.

## Trust & verifiability
`trust: trusted` — the framework itself is the canonical, long-standing OSINT index and is reliable as a discovery surface; the caveat is that the tools it links to are third-party and must each be judged on their own merits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-framework-2 |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, phone, domain, ip-address, image, social-profile → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
