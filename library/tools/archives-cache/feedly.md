---
id: feedly
name: Feedly
description: Use when you want to continuously monitor news sites, blogs and RSS feeds about a subject or topic in one place — returns a deduplicated, searchable stream of new posts.
url: http://www.feedly.com
category: archives-cache
path:
- archives-cache
bestFor: Standing up a monitoring dashboard of RSS/news/blog feeds to track ongoing coverage of a person, org or topic.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier covers a limited number of feeds/boards; Pro/Enterprise add AI ("Leo") filtering, more feeds, search and alerts.
opsec: passive
opsecNote: Aggregating public feeds is passive — you read published content, the subject sees nothing. Your feed list and reading live in a Feedly account, so use a dedicated investigative account rather than a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-established commercial RSS aggregator (Feedly Inc.); it relays publishers' own feeds, so content authority is the underlying source's.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- feedly-rss-reader
aliases:
- Feedly RSS
tags:
- web-monitoring
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Feedly

> A hosted RSS/news aggregator for building a monitoring dashboard — subscribe to the feeds that matter to a case and watch new coverage arrive in one deduplicated stream.

## When to use
An investigation needs ongoing awareness rather than a one-off search: you want to know when a person, company, location or topic is mentioned in news, blogs or niche publications. Feedly lets you collect the relevant RSS/news feeds into boards and scan new items as they publish, so you catch fresh coverage without re-searching daily.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a (dedicated) account at https://feedly.com and log in.
2. Add sources: paste site URLs or RSS feeds, or search Feedly's directory for relevant outlets, then organise them into topic "feeds"/boards.
3. Scan the aggregated stream; use search (paid) to query across your subscriptions and set keyword alerts.
4. Save/annotate items to boards for evidence; export or share as needed.
5. Pivot: named entities, dates and links in new articles feed name/domain/geolocation searches; use the API (paid tiers) to pull items programmatically.

## Inputs → Outputs
- **In:** RSS/news/blog feed URLs and topic keywords (monitoring setup, not a target selector)
- **Out:** a deduplicated, chronological stream of new posts from your sources
- **Empty/negative result looks like:** a source that publishes rarely shows no new items — that's genuinely no new coverage, not a failure; broaden your feed list if the stream is too quiet.

## Gotchas & OpSec
- Human-in-the-loop: an account is required; the free tier caps feeds/boards and withholds search/alerts.
- Feedly only surfaces sources that expose feeds — sites without RSS need a feed-generator or a different monitor.
- OpSec: passive reading of public content; keep the monitoring account separate from your identity.

## Overlaps ("do both")
- Pairs with `[[feedly-rss-reader]]` and dedicated web-change monitors — Feedly is strong on feed-native publishers, while change-detection tools cover pages that have no RSS at all.

## Trust & verifiability
`trust: trusted` as an aggregator — Feedly faithfully relays publishers' feeds; the credibility of any item is that of its original source, which you should still assess.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | feedly |
