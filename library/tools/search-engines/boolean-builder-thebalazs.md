---
id: boolean-builder-thebalazs
name: Boolean Builder theBalazs
description: Use when you have a name/keywords and want a ready-made Google X-Ray query to find someone's profiles — returns a search string that surfaces social-profile hits.
url: https://docs.google.com/spreadsheets/d/1v27Oybrv9H5sn3MMD76clLp2B4mwhA7OtUkfQzlNu8w/edit#gid=940516593
category: search-engines
path:
- search-engines
bestFor: Generating copy-paste Google Boolean/X-Ray search strings without memorising operator syntax.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public Google Sheet; make your own copy to edit inputs (no account needed to view).
opsec: passive
opsecNote: The sheet itself only builds a string and touches nobody. OpSec risk lives in *running* the resulting query on Google against the target's name — do that from a clean/sock-puppet session, since it is a live search about your subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known sourcing-community X-Ray helper (Balázs Paróczay); it is a query-construction convenience, not a data source — the results come from Google, so trust attaches to what Google returns.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- theBalazs Boolean Builder
- X-Ray search builder
tags:
- Tools for Google
- boolean-search
- sourcing
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Boolean Builder theBalazs

> A Google Sheet that assembles Google X-Ray (`site:`) and Boolean search strings for you — fill the cells, copy the query, paste it into Google.

## When to use
You want to find a person's profiles on a specific platform (LinkedIn, Facebook, GitHub, etc.) but don't want to hand-write `site:` + Boolean operator strings. Feed the subject's `name`, `username`, employer, or location terms and the sheet outputs a ready query that X-Rays the target site through Google. A technique multiplier for people-search, not a database.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Google Sheet URL; File → Make a copy (or download) so you can edit the input cells.
2. Fill the input fields — target site/platform, keywords (`name`, job title, company, `username`), and any include/exclude terms.
3. The sheet concatenates these into a valid Google query (e.g. `site:linkedin.com/in "Jane Roe" (Berlin OR "GmbH X")`). Copy the generated string.
4. Paste it into Google (from a clean/sock-puppet browser) and review the SERP for matching `social-profile` pages.
5. Iterate: loosen or tighten the Boolean terms in the sheet and re-run; swap the `site:` target to sweep other platforms.

## Inputs → Outputs
- **In:** `name`, `username`, employer/location keywords, and a target site
- **Out:** a copy-paste Google X-Ray query that, when run, surfaces `social-profile` links
- **Empty/negative result looks like:** the sheet always produces a string; "empty" happens downstream — running the query returns no relevant SERP hits, meaning the person isn't indexed on that site under those terms. Broaden the Boolean or try a different platform before concluding absence.

## Gotchas & OpSec
- The sheet builds a query; it finds nothing on its own. All data quality/coverage limits are Google's (indexing gaps, `site:` operator quirks, region-personalised results).
- Overly strict Boolean (too many ANDs/quotes) yields zero hits; start broad, then narrow.
- OpSec: building is passive, but running the query is a live Google search about your subject — use a clean session and avoid logging patterns that tie many target searches to one account.

## Overlaps ("do both")
- Pairs with any people-search or profile-enumeration tool: use this to craft precise Google X-Ray sweeps, then feed the profile URLs it finds into username/social enrichment tools for deeper detail.

## Trust & verifiability
`trust: community` — a respected sourcing-community helper for query construction; it adds no data, so verifiability rests entirely on the Google results the generated string returns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boolean-builder-thebalazs |
