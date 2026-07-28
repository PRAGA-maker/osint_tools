---
id: startpage-parser
name: Startpage Parser
description: Use when you have a `name` or `username` and want to bulk-scrape web search results without tripping Google's rate limits — returns candidate `domain` and `social-profile` links.
url: https://github.com/knassar702/startpage-parser
category: search-engines
path:
- search-engines
bestFor: Programmatically harvesting large volumes of search-result links for a query without proxies or CAPTCHAs.
selectorsIn:
- name
- username
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free, open-source (pip-installable) Python library; no API key or account.
opsec: passive
opsecNote: Queries go to Startpage.com, which proxies Google and does not require login or reveal your identity to the sites in the results. You are not touching the target directly — only reading indexed pages. Run from a sock-puppet IP if you are scraping at volume, since Startpage may still throttle a single address.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Community project by a single GitHub author (knassar702); useful but unaudited, so verify links it returns before acting on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- startpage scraper
tags:
- Search engines
- Universal search tools
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Startpage Parser

> A tiny Python library that scrapes Google-quality results through Startpage.com, so you can automate name/username searches without CAPTCHAs or proxies.

## When to use
You have a `name`, `username`, or any pivot string and want to pull *many* result links programmatically — e.g. iterating dozens of query permutations across pages — rather than clicking through a browser. Because Startpage relays Google's index but is far less aggressive about blocking bots, this lets you script bulk collection where hitting Google directly would get you rate-limited.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install startpage-parser` (or clone the repo and `pip install -r requirements.txt`).
2. In Python:
   ```python
   from startpage import Search
   task = Search()
   results = task.search("\"Jane Doe\" Springfield", page=1)
   ```
3. Read the returned dict — each result carries `title`, `link`, and `description`. Iterate `page=1..N` to walk deeper.
4. Pivot: feed the discovered `domain`/`social-profile` links into profile- and breach-oriented tools, or re-query with refined operators.

## Inputs → Outputs
- **In:** `name` / `username` (any search string; supports quotes and operators)
- **Out:** `domain`, `social-profile` (result title + link + snippet per hit)
- **Empty/negative result looks like:** an empty results dict/list for that page — means Startpage returned no hits (or you have paged past the last result), not that the person doesn't exist.

## Gotchas & OpSec
- No human-in-the-loop, but Startpage's HTML can change; if the parser suddenly returns nothing, the selectors may have drifted — check for an updated release.
- OpSec is **passive**: results come via Startpage, which anonymizes the click-through, so the target sites never see you. Still rotate IPs for high-volume runs to avoid Startpage-side throttling.
- Results mirror Google's index, so they carry Google's biases and blind spots — corroborate with a second engine.

## Overlaps ("do both")
- Pairs with manual Google dorking and other search scrapers because the same query surfaces different results per engine; Startpage covers the Google index without the block risk.

## Trust & verifiability
`trust: unverified` — a single-maintainer community tool with no formal audit; the *data* it returns is Google's, but treat the scraper itself as best-effort and confirm any link before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | startpage-parser |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → domain, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
