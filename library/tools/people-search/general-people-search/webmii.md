---
id: webmii
name: Webmii
description: Use when you have a `name` and want a web-footprint overview — returns a visibility score plus social profiles, images, videos and news mentions tied to that name.
url: https://webmii.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: Quick web-visibility overview of a name — aggregating profiles, images and news into one footprint view.
selectorsIn:
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free to use, no registration; searches public web data only.
opsec: passive
opsecNote: WebMii aggregates public search results — the subject is not contacted and nothing is posted. You disclose the searched name to WebMii; use a sock-puppet browser. Results are a convenience aggregation of the open web, not private data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A people-visibility aggregator that surfaces public web results by name; convenient for a first pass, but it's a third-party scraper of open sources with no verification of matches.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WebMii
- webmii.com
tags:
- people-search
- web-footprint
- name-search
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Webmii

> A name-to-footprint aggregator: type a name and get a visibility score with the social profiles, images, videos and news the open web associates with it.

## When to use
You have a `name` and want a fast, single-pane overview of that person's public web presence before diving deeper — what profiles, images, and news mentions exist, and how "visible" the name is. Good as an orientation step to spot obvious accounts and news, and to gauge whether you're dealing with a low-footprint private individual or a well-documented one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://webmii.com/ in a sock-puppet browser.
2. Enter the first and last `name`; add a keyword (city, employer, interest) to filter out same-name homonyms.
3. Read the aggregated results: a web-visibility score, `social-profile` links, `image`s, videos, and news mentions.
4. Disambiguate carefully — for common names, use the keyword filter and confirm each result actually refers to your subject.
5. Pivot: a surfaced profile feeds `[[user-searcher]]`/username tools; an image feeds `[[reverse-image-search]]`; a news mention gives dates/associates.

## Inputs → Outputs
- **In:** `name` (+ optional keyword)
- **Out:** visibility score, `social-profile` links, `image`s, videos, news mentions for the name
- **Empty/negative result looks like:** low/zero visibility and few links — a low-footprint or private person, a misspelled name, or a very common name diluting results. Absence is not proof of no presence; try a keyword.

## Gotchas & OpSec
- **Homonym risk:** results are name-matched, so a common name blends many people. Always filter and verify each hit belongs to your subject.
- It aggregates the open web — nothing here you couldn't find via search engines, just faster and pre-grouped.
- OpSec: **passive**; the site sees your query. Use a sock puppet.

## Overlaps ("do both")
- Pairs with general search engines (`[[naver-com]]` for Korea, Google/Bing) and username tools — WebMii gives a grouped first pass; run targeted searches and `[[user-searcher]]` to confirm and extend the specific profiles it surfaces.

## Trust & verifiability
`trust: unverified` — a third-party aggregator of public results with no match verification; treat every surfaced item as a candidate to confirm by opening the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webmii |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, name, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
