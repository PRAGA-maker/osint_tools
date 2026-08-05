---
id: 1st-headlines
name: 1st Headlines
description: Use when you have a topic, place, or event and want a fast cross-source view of current news headlines — returns links to stories across many outlets and regions (no subject PII).
url: http://www.1stheadlines.com
category: search-engines
path:
- search-engines
bestFor: Scanning breaking-news headlines across many outlets and regions from one page.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, ad-supported news aggregator; no account required.
opsec: passive
opsecNote: You browse a public headline aggregator — nothing you do reaches any subject. Only your own reading is visible to the site; use a sock-puppet browser if the topic itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 1997) headline aggregator that links out to primary outlets; it curates links, so verify any claim at the originating source.
missingPersonsRelevance: low
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- 1stheadlines.com
tags:
- news
- headlines
- news-aggregator
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# 1st Headlines

> A long-running news-headline aggregator: it pulls breaking headlines from major outlets (CNN, BBC, NYT, Fox, and more) and organises them by source, topic, and region so you can scan the coverage landscape at a glance.

## When to use
An investigation surfaces a place, event, organisation, or topic and you want a quick, cross-outlet read of what is being reported now — for example checking whether a location or incident tied to a case is in the news, or comparing how different outlets and regions cover it. It aggregates and links to primary stories rather than reporting itself, so it is a discovery lens, not a source of subject data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.1stheadlines.com (no login).
2. Browse by source, category (business, health, sports, technology), or geography (US states, cities, countries), or scan the updated headline lists.
3. Read the headlines and click through to the originating outlet for the full story.
4. Pivot: a relevant story feeds targeted searches on the named people/places; the geographic breakdown helps localise coverage of an event.

## Inputs → Outputs
- **In:** a topic/place/event you browse toward (no subject PII entered)
- **Out:** links to current news stories across outlets and regions
- **Empty/negative result looks like:** the aggregator surfaces only mainstream headlines — a niche local event may not appear, so treat absence here as "not in the majors," not "no news."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — a public aggregator; it leaks nothing about your subject.
- It only links to what major outlets publish; for hyper-local or non-English coverage, go to regional news search instead.

## Overlaps ("do both")
- Pairs with Google News and regional/local news search — this gives a fast multi-outlet snapshot, those give depth and local coverage it misses; run both when news context matters.

## Trust & verifiability
`trust: community` — a durable aggregator (operating since 1997) that curates links to primary outlets. Trust the outlet it links to, not the aggregator's framing; always confirm a claim at the source article.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 1st-headlines |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
