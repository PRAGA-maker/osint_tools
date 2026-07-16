---
id: wink
name: Wink People Search (via iTools)
description: Use when you have a `name` and want a launcher that fires a people/social search across the web from one box — returns social-profile, associate.
url: http://itools.com/tool/wink-people-search
category: people-search
path:
- people-search
bestFor: A quick one-box launcher for name-based people/social search, hosted on the iTools tool directory.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
- address
status: degraded
pricing: free
costNote: Free to use the iTools launcher; any downstream people-search site it hands off to may itself gate results behind a paywall.
opsec: passive
opsecNote: The launcher just builds and fires a search query; you touch the destination search engine, not the subject. Use a sock-puppet browser as the query and any resulting clicks can be logged by the destination sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: iTools is a long-standing third-party directory of search tools; the original standalone Wink people-search engine is defunct, so this now functions as a query launcher rather than its own database.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Wink
- iTools Wink People Search
tags:
- people-search
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- people-search
---

# Wink People Search (via iTools)

> A name-search launcher on the iTools directory — the standalone Wink engine is gone, but the box still fires a people/social query for you.

## When to use
You have a `name` and want a fast starting point that runs a people/social-network search from a single box, alongside iTools' other people-search launchers (Spokeo, Yahoo, Canada411, etc.). Treat it as a convenience entry point, not an authoritative database — the value is the iTools people-search hub, not a proprietary Wink index (which no longer exists).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the iTools Wink People Search page in a sock-puppet browser.
2. Type the subject's `name` (add a city/state to cut noise) and run the search.
3. Read what comes back:
   - The launcher hands off to web/social results — scan for matching `social-profile` links, associated people (`associate`), and location/`address` hints.
   - If the specific Wink box is dead, use the other launchers listed in the iTools people-search section (they point at live engines).
4. Pivot: promising profiles feed username-enumeration and reverse-image tools; a candidate address feeds property/voter records.

## Inputs → Outputs
- **In:** `name` (optionally + location)
- **Out:** `social-profile`, `associate`, `address` (as surfaced by the destination engines)
- **Empty/negative result looks like:** the box errors or returns nothing — the Wink engine is retired, so fall back to the sibling iTools launchers or a mainstream people-search tool rather than concluding the person is absent.

## Gotchas & OpSec
- **Degraded:** the original Wink service shut down; this is a directory launcher, and the specific Wink hand-off may no longer resolve. The surrounding iTools people-search hub remains useful.
- Results quality depends entirely on the destination engine — verify anything it surfaces at the source.
- OpSec: passive toward the subject; destination sites may log your queries, so stay behind a puppet identity/IP.

## Overlaps ("do both")
- Pairs with dedicated people-search tools (Spokeo/TruePeopleSearch-style) — this is only a launcher, so run the real engine directly for structured, current results.

## Trust & verifiability
`trust: community` — iTools is a reputable third-party tool directory, but it aggregates other engines and no longer runs its own Wink index; corroborate every hit at the underlying source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wink |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
