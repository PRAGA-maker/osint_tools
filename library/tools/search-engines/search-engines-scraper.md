---
id: search-engines-scraper
name: Search Engines Scraper
description: Use when you have a `name`, `username`, or `email` and want to sweep many engines at once — returns aggregated result URLs (`social-profile`, `document-id`) as CSV/JSON.
url: https://github.com/tasos-py/Search-Engines-Scraper
category: search-engines
path:
- search-engines
bestFor: Programmatically querying 10+ search engines (incl. Tor's Torch) for one term and collecting all result pages.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
- document-id
status: live
pricing: free
costNote: Free and open-source (MIT). Python library + CLI; no account or API key.
opsec: active
opsecNote: It scrapes search-engine result pages directly (not official APIs), so engines see automated traffic from your IP and may rate-limit, CAPTCHA, or block you — and scraping breaches some engines' ToS. Use a proxy/rotating IP for volume; the target person is never contacted, so it's passive toward them.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: python-lib
trust: community
trustNote: Open-source project by tasos-py; results are raw scraped SERP links, verifiable by opening them, but engine layout changes can break scrapers over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Search-Engines-Scraper
- search_engines python
tags:
- search engines
- serp-scraping
- automation
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Search Engines Scraper

> A Python library/CLI that queries Google, Bing, Yahoo, DuckDuckGo, Startpage, Brave, Mojeek, Ask, Dogpile, AOL and Torch (dark web) for one query and collects every result page into HTML/CSV/JSON.

## When to use
You have a selector — a `name`, `username`, `email`, or distinctive phrase — and want to cast a wide net across many engines at once instead of searching each by hand. Different engines index and rank differently, so a handle that's buried on Google may surface on Mojeek or Brave; the Torch backend even reaches some .onion content. It's the automation layer for the "search the person everywhere" step, giving you a de-duplicable list of URLs to triage.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install search-engines` (or clone the repo).
2. As a library:
   ```python
   from search_engines import Google
   results = Google().search('"Jane Q. Doe" Chicago')
   for r in results.links():
       print(r)
   ```
3. As CLI: `python search_engines_cli.py -e google,bing,brave,mojeek -q '"jane doe"' -o json,csv`.
4. Collect the output files and open the promising URLs.
5. Pivot: profile URLs feed social/username tools; document hits feed metadata extraction.

## Inputs → Outputs
- **In:** `name`, `username`, or `email` (any query string, with optional url/title/text filters)
- **Out:** aggregated result URLs — `social-profile` pages and `document-id`s — exported to HTML/CSV/JSON
- **Empty/negative result looks like:** engines returning zero links or a block/CAPTCHA page instead of results — the latter means you're rate-limited, not that nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: engines throttle automated scraping fast; expect CAPTCHAs and use proxies/delays for anything beyond a few queries.
- Scraping SERPs violates some engines' ToS — a legal/operational consideration, not just technical.
- Scrapers break when engines change their HTML; if one backend returns nothing, try another before concluding.

## Overlaps ("do both")
- Automates what you'd do manually with dorks from `[[dorks-collections-list]]`; feed it dork queries and let it fan them across engines.

## Trust & verifiability
`trust: community` — open-source and the output is raw SERP links you can open and verify; reliability depends on engines not changing layout, so treat empty backends as possibly-broken rather than authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-engines-scraper |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (rate-limit) |
