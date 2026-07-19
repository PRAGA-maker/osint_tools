---
id: naval-open-source-intelligence
name: Naval Open Source Intelligence
description: Use when you need curated open-source naval/maritime-military news and analysis — returns an actively updated feed of naval developments for domain context, not a people lookup.
url: https://nosi.org/
category: dark-web
path:
- dark-web
bestFor: A curated, actively updated feed of open-source naval and maritime-military news for subject-matter context and monitoring.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free to read; funded by its owner with no advertising, and an optional free email subscription for new posts.
opsec: passive
opsecNote: Reading a public news-aggregation blog is passive and touches no target. Subscribing by email reveals your address to the site owner — use a sock-puppet address if you subscribe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A single-curator naval-news aggregation (funded by Michael P. D'Alessandro); it points to primary open sources but is one person's editorial selection, so follow through to the underlying reporting.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- NOSI
- nosi.org
tags:
- toddington
- curated-directory
- naval
- maritime
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Naval Open Source Intelligence

> A long-running, actively updated one-curator feed of open-source naval and maritime-military news — useful as domain context or for monitoring a theatre, not for finding people.

## When to use
Your investigation touches naval or maritime-military matters — a vessel, a navy, a maritime incident, or an `employer-org` in the defence/maritime space — and you want curated open-source reporting to build background or monitor developments. NOSI aggregates and links naval news (US Navy, allied and adversary fleets, unmanned systems), giving you a running picture of a maritime topic and pointers to primary sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://nosi.org/ and browse the latest curated posts, or use the archives/reading list for a topic.
2. Follow each item through to its primary open source (news outlet, official release) — NOSI is an index, so verify at the source.
3. For ongoing monitoring, subscribe by email (use a sock-puppet address) to get new posts.
4. Use it to contextualise a maritime `employer-org`, incident, or region rather than to identify individuals.
5. Pivot: named organisations/vessels feed conventional org/vessel OSINT; incident locations feed `geolocation`/timeline work.

## Inputs → Outputs
- **In:** a maritime topic, vessel, or `employer-org` of interest
- **Out:** curated naval news linking to primary sources, yielding `employer-org` and `geolocation`/incident context
- **Empty/negative result looks like:** the topic isn't covered — it's a curated feed, not a searchable database of everything maritime; niche or non-military topics won't appear.

## Gotchas & OpSec
- It's news curation, not a people/vessel database — do not expect identifier lookups.
- One-person editorial selection; always follow through to the primary source before citing.
- OpSec: reading is passive; subscribing exposes your email.

## Overlaps ("do both")
- Pairs with AIS/vessel-tracking and defence-news databases — this gives curated narrative context, while vessel trackers and official registries give the hard data on specific ships.

## Trust & verifiability
`trust: unverified` — a reputable-seeming but single-curator aggregation; treat it as a well-organised pointer to primary sources, and verify anything important at those sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | naval-open-source-intelligence |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org → employer-org, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
