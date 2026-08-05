---
id: headlinespot
name: HeadlineSpot
description: Use when you have a place, topic, or industry and want a curated directory of news sources covering it — returns links to local/regional/subject newspapers to search next.
url: http://www.headlinespot.com
category: search-engines
path:
- search-engines
bestFor: Finding the right local or subject-specific news outlets to search for a person or event.
selectorsIn:
- name
- address
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free directory; no account.
opsec: passive
opsecNote: Passive — it is a static directory of links, so browsing it exposes nothing about your target. OpSec matters at the next step, when you actually search a named person on the outlets it points you to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A veteran StartSpot Network news portal (online since 1999); it is a hand-curated link directory rather than a data source, and some listed links have rotted with age, so expect dead entries.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- HeadlineSpot.com
tags:
- news
- directory
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# HeadlineSpot

> A hand-curated index of thousands of US and international news sources, sorted by metro area, state, country, industry, and subject — a map to *which* outlet to search, not a search engine itself.

## When to use
You need local or specialised journalism about a subject — a missing-persons appeal in a particular US metro, coverage of an event in a given country, or trade-press reporting on an industry — and you want to find the right outlets to query. HeadlineSpot points you to the papers; you then search each for your `name` or `address`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.headlinespot.com (the server intermittently rate-limits/503s bots; retry from a browser).
2. Browse by the axis that matches your lead: US metro area (56), US state (50), country (59), industry (27), or topic.
3. Follow the listed source links to the actual news outlets covering that place/subject.
4. On each outlet, run the outlet's own search for your subject's `name`, location, or event.
5. Pivot: an article naming your subject yields quotes, associates, locations, and journalist contacts (`social-profile` leads) to pursue.

## Inputs → Outputs
- **In:** a place/topic (from your subject's `address` or context) or a `name` to search on the outlets it lists
- **Out:** a shortlist of relevant news outlets, and — after searching them — article links and `social-profile` leads
- **Empty/negative result looks like:** a category with only dead or irrelevant links (the directory has aged), or no outlet listed for a niche locale — fall back to a broader news search or a current-edition aggregator.

## Gotchas & OpSec
- It is a directory, not a search engine: it never returns articles directly, only sources to go search yourself.
- Age shows — the network dates to 1999 and some links are stale or gone; verify each outlet is still live.
- Server sometimes returns 503 to automated fetches; access via a normal browser.
- OpSec: passive at the directory level; be deliberate when you then search a named subject on individual outlets.

## Overlaps ("do both")
- Pairs with a live news search (a current-edition aggregator or general engine): HeadlineSpot tells you *which* local outlets exist for a region, while an aggregator sweeps current headlines across many at once.

## Trust & verifiability
`trust: community` — a curated but ageing link directory; the value is the outlet list, and authority rests with the individual newspapers it points to, not with HeadlineSpot.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | headlinespot |
