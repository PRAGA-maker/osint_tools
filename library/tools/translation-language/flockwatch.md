---
id: flockwatch
name: FlockWatch
description: Use when you have a corpus of collected social-media text (tweets/Reddit) and want it to surface trending or associated terms/usernames to expand your collection keywords — returns new terms/usernames to track, not personal identity data.
url: https://github.com/sjacks26/flockwatch
category: translation-language
path:
- translation-language
bestFor: Auto-discovering new keywords/terms/usernames to add to an ongoing social-media data collection.
selectorsIn:
- username
selectorsOut:
- username
status: live
pricing: free
costNote: Free, open-source Python tool on GitHub; you run it against your own collected data (and supply any collection API keys separately).
opsec: passive
opsecNote: FlockWatch analyses text you have already collected — it does not touch a target, so it's passive. OpSec risk lives in the collection step it feeds (your Twitter/Reddit scraper), not here. Keep collected data secured; it may contain personal information.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An academic/community research tool (by sjacks26) for social-media data collection workflows; small and auditable, but research-grade rather than productised.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- flock watch
tags:
- socmint
- keyword-discovery
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# FlockWatch

> A Python tool that mines a collection of social-media posts for trending/associated terms — so your keyword list grows with the conversation instead of going stale.

## When to use
When you're running a longitudinal social-media collection (a Twitter/Reddit dataset around a topic, event, or community) and want to keep your search terms current. FlockWatch scans the text you've gathered and reports terms and `username`s that are trending or frequently co-occurring, which you feed back into your collector to widen coverage. It's a keyword-discovery aid for SOCMINT, not a person-lookup.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/sjacks26/flockwatch and install its Python dependencies.
2. Point it at your existing collected dataset and configure the term-frequency/trend thresholds.
3. Run it on a schedule; it outputs newly-trending terms and associated usernames.
4. Review the suggestions and add the useful ones to your collector's tracking list.
5. Pivot: newly-surfaced `username`s → profile lookups and cross-platform username tooling.

## Inputs → Outputs
- **In:** a corpus of collected social posts (with seed `username`s/terms)
- **Out:** newly-trending terms and `username`s to add to collection
- **Empty/negative result looks like:** no new terms above threshold — your collection has plateaued, or thresholds are too strict; adjust or accept coverage is saturated.

## Gotchas & OpSec
- It needs an **existing dataset** — it doesn't collect data itself; pair it with a Twitter/Reddit collector.
- Research-grade tooling: expect setup effort and check it works with current data formats/APIs.
- The sensitive step is the collection it feeds; secure that data and mind platform ToS/legalities.

## Overlaps ("do both")
- Works downstream of a social-media collector and upstream of profile-analysis tools: collector → FlockWatch (find terms) → username/profile OSINT.

## Trust & verifiability
`trust: community` — a small open-source research tool; it only summarises your own data, so trust comes from reading the code, and its suggestions are leads to weigh, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | flockwatch |
| category | translation-language |
| selectorsIn → selectorsOut | username → username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
