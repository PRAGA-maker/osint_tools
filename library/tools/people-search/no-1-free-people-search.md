---
id: no-1-free-people-search
name: No.1 Free People Search
description: Use when you have a `name` and want a web-mention aggregation of that person (links, news, images, profiles) — returns `social-profile`s, related `name`s, and web references.
url: http://www.yasni.com/
category: people-search
path:
- people-search
bestFor: Aggregating public web mentions of a person's name into one profile view (links, news, images, social).
selectorsIn:
- name
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: freemium
costNote: Free to search and view aggregated mentions. Yasni also sells self-promotion "Exposé" profiles, but searching others is free.
opsec: passive
opsecNote: Yasni aggregates already-public web mentions; searching is passive and the subject is not notified. It does not require login. It only surfaces indexed public references — treat what it finds as leads to verify at the source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running name-based web aggregator (German-origin); it collates third-party mentions, so quality varies and same-name people are easily conflated.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Yasni
- yasni.com
tags:
- people-search
- name-aggregator
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# No.1 Free People Search

> Yasni — a name-centric web aggregator that pulls links, news, images, and profiles mentioning a person into one view.

## When to use
You have a subject's `name` and want a quick, broad sweep of their public web footprint — news mentions, links, images, and social profiles — gathered in one place, optionally narrowed by location, profession, or skill. Best as an early, low-effort reconnaissance step to surface leads and alternate profiles before deeper, source-specific work. Coverage skews to German/European and general web content.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.yasni.com/ and enter the `name`; optionally add a location/profession keyword to disambiguate.
2. Review the aggregated results: web links, news, images, and linked social profiles for that name.
3. Separate the true subject from same-name noise using the location/profession filters and corroborating details.
4. Open promising links at their source to verify — Yasni is an index, not the primary source.
5. Pivot: discovered `social-profile`s feed username/social OSINT; related `name`s (`associate`) feed people-search.

## Inputs → Outputs
- **In:** `name` (+ optional location/profession keyword)
- **Out:** aggregated `social-profile`s, web/news mentions, images, related `name`s (`associate`)
- **Empty/negative result looks like:** few or generic mentions — common for low-profile people or those with common names buried among namesakes. As an aggregator it conflates same-name individuals; a hit is a lead, not confirmed identity.

## Gotchas & OpSec
- Same-name conflation is the main failure mode; always disambiguate and verify at the source.
- Index freshness varies — some links are dead or dated.
- Skews European/German; thinner for other regions.

## Overlaps ("do both")
- Pairs with `[[pipl]]`-style and search-engine dorking approaches — Yasni gives a fast aggregated name view, while targeted searches and people-search resolve the specific individual and current details.

## Trust & verifiability
`trust: community` — a functional aggregator of public mentions; treat results as leads and confirm each against its original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | no-1-free-people-search |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, name, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
