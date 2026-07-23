---
id: news-search-engine
name: News Search Engine (Google CSE)
description: Use when you have a `name`, `employer-org`, or event and want it searched across a curated set of news sites at once — returns news mentions with dates and named people.
url: https://cse.google.com/cse?cx=013991603413798772546:fvmtax6anhd
category: search-engines
path:
- search-engines
bestFor: One-box searching of a preset list of news outlets via a Google Custom Search Engine.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- address
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account. Coverage is fixed by the CSE's site list and can drift over time.
opsec: passive
opsecNote: Passive news search; the subject is never contacted. Queries go to Google — use a clean browser for sensitive names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine; results are Google's, but the outlet list is set by an unknown curator and may be stale or narrow.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-news
- google-advanced-search
aliases:
- News Search CSE
tags:
- news
- custom-search-engine
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# News Search Engine (Google CSE)

> A preset Google Custom Search Engine scoped to a curated list of news outlets — a quick way to search many news sites at once, useful but limited by whoever configured the site list.

## When to use
You want news coverage of a `name`, `employer-org`, or event, restricted to journalism sites rather than the whole web. This CSE searches a fixed set of outlets in one box, which can cut noise — but because the outlet list is curated by a third party and may be dated, treat it as *one* news lens, not comprehensive coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE link (https://cse.google.com/cse?cx=013991603413798772546:fvmtax6anhd).
2. Enter the `name`/`employer-org`/event; use quotes and `AND`/`OR` to focus.
3. Read hits for dated coverage, named individuals (`associate`s), quoted locations (`address`), and affiliations.
4. Note the outlets returned — if they look narrow or dated, treat coverage as partial.
5. Pivot: named people → people-search; then re-run on `[[google-news]]` for broader, current coverage.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or event keyword
- **Out:** news articles from the CSE's outlet list, with dates, named people (`associate`), and locations (`address`)
- **Empty/negative result looks like:** no hits — the story isn't covered by the CSE's outlet set (not proof it's unreported); widen to Google News.

## Gotchas & OpSec
- The outlet list is fixed and opaque; a Custom Search Engine can silently narrow or degrade over time — never treat a blank result as "no news exists."
- Results are still Google's index of those sites — this is a scoping wrapper, not an independent archive.
- OpSec: passive; queries go to Google.

## Overlaps ("do both")
- Pairs with `[[google-news]]` (broad, current, all outlets) and `[[google-advanced-search]]` (roll your own `site:` list) — use this for a quick scoped pass, then Google News to be sure you haven't missed coverage.

## Trust & verifiability
`trust: community` — a third-party-configured CSE over Google's index; the articles are authentic, but the curated outlet list is unverified and possibly stale, so confirm breadth with a general news search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | news-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
