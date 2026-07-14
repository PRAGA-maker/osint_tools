---
id: osint-framework-3
name: OSINT Framework
description: Use when you have a selector type (`email`, `username`, `phone`, etc.) but not the right tool — returns a categorized directory tree pointing to specific OSINT resources for that data type.
url: https://osintframework.com/
category: search-engines
path:
- search-engines
bestFor: Browsing a categorized tree of OSINT resources by selector/goal to discover which specific tool to use next.
selectorsIn:
- email
- username
- phone
- name
selectorsOut: []
status: live
pricing: free
costNote: Free, open web directory; no account or payment.
opsec: passive
opsecNote: Just a static directory of links — browsing it touches only osintframework.com, not any target. The actual investigative queries happen on the destination tools, whose OpSec you must consider individually.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: A long-standing, widely referenced community directory (bookmarked in the Trace Labs VM; the taxonomy behind the gumshoe tool). It curates links, so quality depends on the destinations and some links go stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osintframework.com
- OSINT Framework
tags:
- directory
- meta-resource
- osint-framework
source: tracelabs-repos
lastVerified: '2026-07-13'
enrichment: full
---

# OSINT Framework

> The canonical tree-view directory of OSINT resources — start from the selector you hold (email, username, phone…) and it branches you to the specific tools for that data type.

## When to use
You have a selector — an `email`, `username`, `phone`, `name`, domain, IP, etc. — and want a map of *which* tools apply, not a single answer. OSINT Framework is a jumping-off point: expand the branch for your data type or investigation goal and it lists candidate resources to try. Use it to make sure you haven't overlooked a category of tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osintframework.com/.
2. Expand the top-level node matching your selector or objective (e.g. Username, Email Address, Telephone Numbers, Social Networks).
3. Drill down the sub-branches; each leaf links to a specific external tool/site (icons flag those needing registration, an install, or being URL-only).
4. Open the destination tools and run your actual query there.
5. Pivot: treat it as a checklist — cover each relevant branch so no tool class is missed for the selector you hold.

## Inputs → Outputs
- **In:** a selector type / investigation goal (`email`, `username`, `phone`, `name`, …)
- **Out:** a categorized list of destination tools (the framework itself returns links, not data about a subject)
- **Empty/negative result looks like:** a branch with only stale/dead links, or no branch for a very niche need — it is a curated map, not a live search, so it lags newer tools.

## Gotchas & OpSec
- It's a directory, not a search engine — it points, it doesn't query; the intelligence comes from the tools it links.
- Some links rot; cross-check with other tool lists (this library included) for current options.
- OpSec: browsing is passive; consider each destination tool's OpSec separately before using it.

## Overlaps ("do both")
- Complements this skill library and other curated tool lists — use OSINT Framework to discover a tool class, then this library's per-tool skills for how to actually run and interpret them.

## Trust & verifiability
`trust: trusted` — a well-established, community-standard directory; reliable as a map, though the destinations it lists vary in quality and freshness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-framework-3 |
