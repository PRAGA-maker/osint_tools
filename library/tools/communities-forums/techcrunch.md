---
id: techcrunch
name: TechCrunch
description: Use when you have a `name` or `employer-org` in the startup/tech world and want coverage of funding, launches and people — returns `employer-org`, `associate` and timeline context.
url: https://techcrunch.com
category: communities-forums
path:
- communities-forums
bestFor: Tracing startup founders, executives, funding rounds, and company histories through tech-press coverage.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to read and search; ad-supported, no hard paywall on standard articles.
opsec: passive
opsecNote: Searching and reading a public news site transmits nothing about your subject. Fully passive; a private window avoids personalisation cookies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A leading, long-running technology/startup news outlet (Yahoo). Reliable secondary source for the tech and venture world, with the usual journalistic caveats.
missingPersonsRelevance: low
coverage:
- global
aliases:
- TechCrunch
- techcrunch.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# TechCrunch

> The dominant startup/tech news outlet — searchable for founders, executives, funding rounds, acquisitions, and company histories.

## When to use
Your subject is in the startup or technology world — a founder, executive, investor, or employee of a covered company. TechCrunch is especially strong on funding announcements and company launches, which name people, co-founders, investors, and dates. Use it to confirm an `employer-org`, establish a career/funding timeline, and map `associate`s (co-founders, backers, colleagues).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://techcrunch.com and use site search, or run: `site:techcrunch.com "Full Name"` / `"Company"`.
2. Read funding/launch pieces for co-founders, investors, roles, valuations, and dates.
3. If the subject is a journalist/contributor, open their author page to enumerate their coverage and beats.
4. Note the people and firms named alongside the subject and the article dates.
5. Pivot: a confirmed company feeds Crunchbase/registry lookups; co-founders/investors feed people-search; a funding date anchors a timeline.

## Inputs → Outputs
- **In:** `name` / `employer-org` (startup/tech)
- **Out:** `employer-org`, `associate` (co-founders, investors, colleagues), funding/career timeline
- **Empty/negative result looks like:** no article matches — the person/company wasn't covered; try Crunchbase, other tech press, and Google News before concluding no footprint.

## Gotchas & OpSec
- Tech/startup focus — a subject outside that world won't appear, so absence says little.
- Announcements reflect company PR at the time — verify that a role/round actually persisted against later sources.
- Fully passive — searching leaks nothing.

## Overlaps ("do both")
- Pairs with Crunchbase and company registries — TechCrunch gives the narrative and named people, those give the structured funding and corporate record; run both to confirm and enrich.

## Trust & verifiability
`trust: trusted` — an established outlet; reliable secondary sourcing for the tech world, with specifics (titles, amounts, dates) worth confirming against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | techcrunch |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
