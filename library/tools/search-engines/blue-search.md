---
id: blue-search
name: Blue Search
description: Use when you want an alternative general web search engine (now rebranded GOOD, on the independent Brave index) to cross-check results a mainstream engine buries — returns web results toward `social-profile`, `domain`, `document-id`.
url: https://blue-search.org/
category: search-engines
path:
- search-engines
bestFor: A privacy-oriented alternative general web search that uses a non-Google/Bing index, useful for cross-checking mainstream results.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free, ad-free, non-profit-run search engine; no account required.
opsec: passive
opsecNote: Ad-free with no tracking or stored search history per its own policy, which is favourable for OSINT queries. Still run sensitive searches from a sock-puppet/logged-out session and avoid clicking straight through to target-controlled pages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Runs on the independent Brave search index (not Google/Bing); the operator rebranded from Blue Search to GOOD (good-search.org) as a B-Corp charitable search enterprise.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- GOOD Search
- good-search.org
- blue-search.org
tags:
- toddington
- curated-directory
- search-engines
- alternative-search
source: toddington-resources
lastVerified: '2026-07-20'
---

# Blue Search

> An alternative, privacy-oriented general web search engine (now rebranded "GOOD") built on the independent Brave index — worth a pass to cross-check what Google/Bing bury or omit.

## When to use
You've searched a `name`, `username`, or `domain` on mainstream engines and want a *different index* to catch results Google/Bing rank low or filter. Blue Search now 301-redirects to **good-search.org** (GOOD), a non-profit charitable search engine that draws on the independent Brave index rather than reselling Google/Bing results. A distinct index occasionally surfaces different pages — useful in a search-engine-diversity sweep. It's a general web engine, not a person finder, so relevance is low but non-zero for coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://blue-search.org/ (redirects to good-search.org).
2. Enter the subject `name`/`username` in quotes; add operators where supported.
3. Compare the top results against Google/Bing — note any pages the mainstream engines missed.
4. Follow promising links from a clean session.
5. Pivot: new `domain`s and `social-profile`s feed the rest of your footprint sweep.

## Inputs → Outputs
- **In:** `name`, `username`, `domain`, or keyword
- **Out:** general web results → `social-profile`, `domain`, `document-id` (indexed files)
- **Empty/negative result looks like:** thin or no results — the Brave index is smaller than Google's, so absence here is weak evidence; confirm against a larger engine.

## Gotchas & OpSec
- Smaller index than Google — treat it as a *supplement*, not a replacement; a miss here doesn't mean a page doesn't exist.
- The brand moved from Blue Search to GOOD; bookmarks to the old name still resolve.
- OpSec: its no-tracking stance is a plus for query privacy; still avoid clicking straight to target-controlled pages.

## Overlaps ("do both")
- Pairs with mainstream and other alternative engines — the point is index diversity: run the same selector across several so no single index's blind spot hides a result.

## Trust & verifiability
`trust: community` — a legitimate non-profit engine on an independent index; results are as reliable as the pages they point to, so verify each hit at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blue-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
