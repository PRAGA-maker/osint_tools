---
id: bing-news
name: Bing News
description: Use when you have a `name`, org, or event and want news coverage as a second engine to Google — returns news articles, dates, and outlets that corroborate or add to a subject's record.
url: http://www.bing.com/news
category: search-engines
path:
- search-engines
bestFor: A second-opinion news search whose index and ranking differ from Google, surfacing articles Google buries.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
status: live
pricing: free
costNote: Free; no account required for news search.
opsec: passive
opsecNote: A normal search query to Microsoft — passive, and nothing is sent to your subject. Use a clean/sock-puppet session and consider a VPN if you don't want the searches tied to you; searches may be logged and personalised.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Microsoft's first-party news aggregator; the index is authoritative as a search surface, though the underlying articles vary in reliability and must be judged individually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- bing
- bing-creations
- bing-images
- bing-ip-search
- bing-maps
- bing-microsoft-translator
- bing-translate
- bing-videos
- bing-webmaster-tools
- see-it-search-it
aliases:
- Bing News
tags:
- news
- search-engine
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Bing News

> Microsoft's news search as a deliberate second engine: run the same subject you searched on Google here, because a different index surfaces different articles.

## When to use
You're building a person's or organisation's public record and want news coverage — arrests, accidents, obituaries, business mentions, local reporting on a missing person. Always worth running alongside Google News: Bing's crawl, regional weighting, and ranking differ, so it routinely surfaces local or older articles Google ranks away. Search a `name` (with a place/qualifier) or an `employer-org`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bing.com/news.
2. Search the `name` in quotes plus a disambiguator (town, employer, "missing"); or search the org.
3. Use the date filter to focus on a relevant window; scan outlets and datelines.
4. Compare against Google News results — treat non-overlapping articles as the payoff.
5. Pivot: named relatives/associates, locations, and dates in articles become new selectors and timeline anchors.

## Inputs → Outputs
- **In:** `name` (+ qualifier) or `employer-org`
- **Out:** news articles with outlet, date, and snippet (corroborating `name`/context)
- **Empty/negative result looks like:** no relevant hits or only namesakes — the person has no news footprint under that spelling, or your query needs a stronger disambiguator.

## Gotchas & OpSec
- Passive search, but log searches to a research profile, not your personal Microsoft account.
- Common names return namesakes — always qualify and verify the article is about *your* subject.
- The engine is authoritative as an index; the articles themselves are only as trustworthy as their outlet.

## Overlaps ("do both")
- Explicitly a "do both" with Google News and `[[bing]]` web search — different indexes, so run the same query across all and merge; local-paper hits often appear in only one.

## Trust & verifiability
`trust: trusted` — a first-party Microsoft search surface; reliable as a discovery tool, but assess each returned article's source independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bing-news |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
