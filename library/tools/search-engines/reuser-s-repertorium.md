---
id: reuser-s-repertorium
name: Reuser's Repertorium
description: Use when you need a vetted starting point of OSINT sources for a country, registry or topic — returns curated links to people, registry, map and search tools.
url: http://rr.reuser.biz/
category: search-engines
path:
- search-engines
bestFor: A veteran-curated directory of OSINT sources (registries, maps, people, country-specific tools) to seed an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free public reference site; no account or payment.
opsec: passive
opsecNote: A static link directory — browsing it touches only Reuser's site, not any subject. Fully passive. Note it is served over plain HTTP, so treat the connection as unencrypted (fine for reading a public list).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Arno Reuser, a pioneering professional OSINT practitioner; a long-respected, hand-curated reference rather than an automated harvest.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Reuser's Repertorium
- rr.reuser.biz
tags:
- tool-collection
- repertorium
- reference
- directory
source: ultimate-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Reuser's Repertorium

> Arno Reuser's long-running, hand-curated directory of OSINT sources — a trusted map of *where to look* for registries, maps, people and country-specific tools when starting a case.

## When to use
You're at the start of an investigation (often into a specific country, registry type, or data domain) and want a vetted list of the right sources rather than raw search results. The Repertorium is a reference index, not a lookup engine: you don't enter a selector, you browse it to discover authoritative registries, map services, people-search sources and specialist databases curated by a veteran practitioner. Use it to fill coverage gaps — especially for jurisdictions your usual toolset is thin on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://rr.reuser.biz/ (plain HTTP — expect an unencrypted static site).
2. Browse the categorized sections (by country, source type, and topic) to find candidate sources for your target.
3. Follow the outbound links to the actual registries/tools and run your selector there.
4. Treat it as a jumping-off directory: its value is curation and breadth, not doing the search itself.
5. Pivot: each linked source is the real tool — bring the leads it points you to back into your selector-based workflow.

## Inputs → Outputs
- **In:** none directly — it's a browse-and-discover directory, not a query tool
- **Out:** curated links to third-party OSINT sources (registries, maps, people, country-specific databases)
- **Empty/negative result looks like:** a category with sparse or aged links — like any directory it can contain dead outbound links; verify a linked source still works before relying on it.

## Gotchas & OpSec
- It's a directory, not a search engine — no selector goes in; don't expect results *about a person* from the site itself.
- Served over HTTP and updated by hand, so some outbound links may be stale or moved.
- OpSec: passive; nothing you look up here reaches a subject.

## Overlaps ("do both")
- Complements other OSINT link collections and framework directories — cross-reference several curated lists, since each veteran maintainer surfaces sources the others miss.

## Trust & verifiability
`trust: trusted` — curated by a well-known professional OSINT trainer; the *curation* is authoritative, but each linked third-party source carries its own reliability that you must judge on arrival.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reuser-s-repertorium |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
