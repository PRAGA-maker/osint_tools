---
id: twiiter-trending-archive
name: Twitter Trending Archive
description: Use when you have a date, place, or keyword and want to know what was trending on Twitter/X — returns historical trending topics by day and country, and when a keyword trended (a timeline/`geolocation` context signal).
url: http://archive.twitter-trending.com/
category: social-networks
path:
- social-networks
bestFor: Reconstructing what was trending on Twitter on a given day/country, or finding when a keyword hit the trends.
selectorsIn:
- name
status: live
pricing: freemium
costNote: Free web access to the trending archive; no account needed for the core lookups.
opsec: passive
opsecNote: Passive — you're browsing an aggregate archive of public trending data, not touching any individual's account. Nothing about your query reaches a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party archive of Twitter/X trending topics; useful for context, but coverage/completeness by country and date is not independently guaranteed.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- archive.twitter-trending.com
- Twitter trending history
tags:
- Social Media
- Twitter
- trends
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Twitter Trending Archive

> A searchable history of Twitter/X trending topics — see what a country was talking about on a specific date, or find when a name or hashtag broke into the trends.

## When to use
This is a **context and timeline** tool, not a person-lookup. Reach for it when you need to (a) understand what was dominating public conversation in a country on the day something happened, or (b) find *when* a specific `name`, hashtag, or keyword trended — which can date an event, corroborate a claim, or reveal that a subject's handle/topic spiked at a particular moment. It anchors social activity to a place and a date.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://archive.twitter-trending.com/.
2. To browse by date: pick a day and a country (or worldwide) to see the ranked trends that were active then.
3. To search a term: enter the keyword/hashtag/name and see the dates and countries where it trended.
4. Read the ranking/timing to place the topic in a location and timeframe.
5. Pivot: a keyword's trend date narrows when to search a subject's timeline (e.g. with `[[tweet-machine]]`); the country context supports a `geolocation` hypothesis.

## Inputs → Outputs
- **In:** a date + country, or a keyword/hashtag/`name`
- **Out:** ranked historical trending topics for that day/country, or the dates/countries a term trended (timeline + `geolocation` context)
- **Empty/negative result looks like:** no entries for the date/term — the archive didn't capture that country/day, or the term never reached the public trends (a niche handle usually won't).

## Gotchas & OpSec
- Trends are **aggregate public sentiment**, not tied to any one account — this contextualises activity, it does not identify individuals.
- Country/date coverage is uneven; a gap is an archive limitation, not evidence nothing trended.
- Only topics that reached the *trends* appear; most people and posts never trend, so absence is expected and uninformative about an individual.

## Overlaps ("do both")
- Pairs with `[[tweet-machine]]` and Wayback searches — this tells you *when/where* a topic was hot, those let you pull the specific accounts and posts from that window.

## Trust & verifiability
`trust: unverified` — a third-party trending archive; treat its timeline as a strong lead to corroborate against the actual dated posts rather than as a complete record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twiiter-trending-archive |
| category | social-networks |
| selectorsIn → selectorsOut | name → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
