---
id: allyoucanread-com
name: AllYouCanRead.com
description: Use when you have a `geolocation` (country/region) and want the local newspapers and magazines that cover it — returns news-outlet `domain` links to search for local coverage of a person.
url: https://www.allyoucanread.com/
category: search-engines
path:
- search-engines
- news-search
bestFor: Finding the local and regional news outlets for a given country/region so you can hunt for local coverage of a missing person or event.
selectorsIn:
- geolocation
selectorsOut:
- domain
status: live
pricing: free
costNote: Free directory; no account or payment needed to browse.
opsec: passive
opsecNote: You are only browsing a directory and then visiting third-party news sites. Passive — the directory learns nothing about your target. Normal browsing hygiene applies when you follow through to the outlet sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running (since 2001) curated directory of world news media; a link index, not a data source, so quality risk is stale/dead links rather than bad facts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- allyoucanread
aliases:
- All You Can Read
tags:
- news-search
- media-directory
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# AllYouCanRead.com

> A browsable directory of newspapers and magazines worldwide, organized by country and region — the map from "where" to "which local outlets to search."

## When to use
You have a `geolocation` — the country, region or town connected to a case — and need to know which local newspapers, magazines and news sites cover that area. Local outlets often carry missing-person notices, obituaries and community news that never reach national aggregators or Google's front page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.allyoucanread.com/ .
2. Pick the relevant region (Africa, Asia, Europe, North/South America, Australia & Pacific) and then the specific country, or use the A–Z country dropdown.
3. Browse the listed publications for that area — the directory is organized by geography and topic rather than keyword search.
4. Read the output: the `domain` of each local/regional outlet.
5. Pivot: open those outlet sites directly and run their internal search (or a `site:` Google query against the domain) for the subject's name.

## Inputs → Outputs
- **In:** `geolocation` (country / region)
- **Out:** `domain` (local newspaper and magazine websites)
- **Empty/negative result looks like:** a sparsely-covered country with few or no listed outlets — fall back to a search engine or a country-specific media directory.

## Gotchas & OpSec
- It is a directory, not a search engine — you cannot query a person's name here; it only points you to outlets to search individually.
- Some listed links are stale or dead given the directory's age; verify each outlet still exists.
- OpSec: passive; nothing about your target is submitted to this site.

## Overlaps ("do both")
- Pairs with `[[allyoucanread]]` — the same media-directory listing under a sibling id; use whichever loads, then feed the outlet domains into a name search.

## Trust & verifiability
`trust: community` — a curated human-maintained link directory operating since 2001. It carries no facts of its own, so the only reliability concern is broken or outdated links.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | allyoucanread-com |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
