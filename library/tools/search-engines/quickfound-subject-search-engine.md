---
id: quickfound-subject-search-engine
name: QuickFound Subject Search Engine
description: Use when you want a topic to browse curated reference links and subject search portals — a directory site grouping news/science/history/biography resources; returns `domain`s of topical sources (little direct people-search value).
url: http://quickfound.net
category: search-engines
path:
- search-engines
bestFor: A retro subject directory that points you to reference sites and topical search portals (news, science, history, biography) rather than searching people directly.
selectorsIn:
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free ad-supported reference directory; no account.
opsec: passive
opsecNote: Passive — you browse a static directory of links, transmitting nothing about a subject. Following an outbound link carries only that link's normal footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent reference/link directory (Quicksand Foundation); it curates outbound links, not personal data — an index, not an authority.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- QuickFound
- Quick News
tags:
- toddington
- curated-directory
- search-engines
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# QuickFound Subject Search Engine

> An old-school subject directory — pick a topic and it hands you curated reference links and topical search portals; useful for background reading, not for finding a specific person.

## When to use
You want to explore reference material or topical search portals around a subject area (history, science, biography, news) — QuickFound organises links by category and embeds subject-specific search boxes. It is a jumping-off directory, not a people-search engine; expect `domain`s of resources, not personal records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://quickfound.net and pick a subject section (e.g. Biography, History, SciTech, News).
2. Use the embedded topical search box, or follow the curated links on the page.
3. Read the output: a curated set of outbound reference `domain`s and topical searches.
4. Pivot: use a relevant reference/biography link as a lead, then do the actual searching on that destination or a dedicated people tool.

## Inputs → Outputs
- **In:** a topic (or a `name` as a query into an embedded topical search)
- **Out:** `domain`s of reference/search resources for that subject
- **Empty/negative result looks like:** sparse or dated links — the directory is old, so some outbound links may be stale; treat it as a starting index only.

## Gotchas & OpSec
- Dated, ad-heavy directory; some links rot. It aggregates other sites' search boxes rather than holding its own index.
- Minimal direct value for locating an individual.
- Human-in-the-loop: none. OpSec: passive.

## Overlaps ("do both")
- Overlaps with any curated OSINT link list — use QuickFound only when you need topical reference sources, and pair it with a real search engine for the actual lookup.

## Trust & verifiability
`trust: community` — an independent link directory; verify any destination on its own site, and expect some dead links given the site's age.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | quickfound-subject-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
