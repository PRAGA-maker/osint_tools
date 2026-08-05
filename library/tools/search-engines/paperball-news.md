---
id: paperball-news
name: Paperball.news
description: Use when you have a name or keyword and want to search today's German-language newspaper press for mentions — returns news articles/social-profile leads.
url: https://paperball.news/
category: search-engines
path:
- search-engines
bestFor: Keyword-searching current German daily newspapers in one pass.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free keyword news search; no account required.
opsec: passive
opsecNote: Passive — a third-party news search index. Your query is sent to Paperball's servers but never reaches the people named in the articles. Use a VPN/clean browser if the subject or region is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running German press meta-search (formerly paperball.de); it indexes reputable newspapers' current editions, but it is an aggregator layer, so verify hits on the original outlet.
missingPersonsRelevance: low
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
aliases:
- Paperball
- paperball.de
tags:
- news
- german-press
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Paperball.news

> A keyword search across the current issues of German daily newspapers — a fast way to sweep the German press for a name or event.

## When to use
Your subject has a German-language footprint and you want to know whether they, an associated organisation, or an event appears in today's German newspapers. Good for German missing-persons/appeal coverage, local reporting, and current-affairs mentions that broader search engines bury or translate poorly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://paperball.news/ (the site also answers on paperball.de).
2. Enter a keyword — a person's `name`, place, or organisation. German diacritics matter; try both `Müller` and `Mueller`.
3. Read the results: article headlines and links across German daily papers, drawn from their current editions.
4. Open promising hits on the original newspaper site to read the full article and capture the byline/date.
5. Pivot: an article naming your subject yields quotes, locations, associates, and journalist contacts (`social-profile` leads) to chase further.

## Inputs → Outputs
- **In:** `name` or keyword (German-language)
- **Out:** links to current German press articles; from those, `social-profile`/associate and location leads
- **Empty/negative result looks like:** no articles returned — the term is absent from today's indexed editions. Because Paperball covers current issues only with no archive, a blank result does NOT mean the subject was never in the German press; it means they are not in the current window.

## Gotchas & OpSec
- No archive: it searches current editions, so historical coverage will be missed — pair with an archive/newspaper database for older stories.
- German-only focus; near useless for non-German-language subjects.
- Coverage is limited to the papers it indexes, not the entire German press.
- OpSec: passive; only your query is exposed to the aggregator, never to the subject.

## Overlaps ("do both")
- Complement with a general news search and a newspaper-archive tool: Paperball catches the freshest German print/online editions, while archives and broader engines recover the back-catalogue Paperball drops.

## Trust & verifiability
`trust: community` — an established German press meta-search; treat it as a discovery layer and confirm every hit on the originating newspaper, whose reporting is the actual source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paperball-news |
