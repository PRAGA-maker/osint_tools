---
id: theaustralian-national-news
name: The Australian (national news)
description: Use when you have a `name` or `employer-org` linked to Australia and want national coverage — returns `associate`, `employer-org` and event context from published articles.
url: https://www.theaustralian.com.au
category: communities-forums
path:
- communities-forums
bestFor: Finding Australian national news coverage of a person, company, or case.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
status: live
pricing: freemium
costNote: A hard subscription paywall — a limited number of free articles, then subscription required. Search, headlines and standfirsts are free.
opsec: passive
opsecNote: Searching and reading a public news site leaks nothing about your subject. The paywall sets cookies and prompts sign-up; use a private window and decline. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Australia's main national broadsheet (News Corp Australia); an established paper of record, subject to its known editorial slant. Reliable secondary source.
missingPersonsRelevance: medium
coverage:
- au
aliases:
- The Australian
- theaustralian.com.au
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# The Australian (national news)

> Australia's national broadsheet — searchable for national coverage of people, companies, courts, and events across the country.

## When to use
Your subject has an Australian connection — lived, worked, went missing, was in court, or is tied to a company or event of national note in Australia. The Australian carries names, professional affiliations, court reporting, and business coverage that help confirm an `employer-org`, place a person in time, and identify `associate`s. Good national complement to state/local papers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.theaustralian.com.au and use site search, or run: `site:theaustralian.com.au "Full Name"`.
2. Read headlines/standfirsts (free) to gauge coverage and timeframe.
3. When the paywall blocks the article, read an archived copy (`web.archive.org`) or find the same story via other News Corp AU outlets and Google News.
4. Note the subject's role, employer, dates, and other named people.
5. Pivot: a confirmed employer/role feeds ASIC business and LinkedIn lookups; named associates feed people-search; a court reference feeds Australian court-record searches.

## Inputs → Outputs
- **In:** `name` / `employer-org` (Australia-linked)
- **Out:** `associate` (co-named figures), `employer-org`, event/date context
- **Empty/negative result looks like:** no article matches — the person wasn't covered nationally; try state papers (Sydney Morning Herald, The Age), the ABC, and Google News before concluding no coverage.

## Gotchas & OpSec
- Hard subscription paywall — plan to use archive.org or headline level, or a sister outlet carrying the same story.
- National broadsheet with a known editorial slant — separate reporting from opinion, and confirm facts against primary records.
- Australia-focused. Fully passive.

## Overlaps ("do both")
- Pairs with Australian state dailies and the ABC — this gives the national view, while state outlets add local detail one drops; run both to catch full coverage.

## Trust & verifiability
`trust: trusted` — an established national paper of record; treat articles as reliable secondary sourcing and confirm specifics (titles, dates, charges) against authoritative Australian records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | theaustralian-national-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
