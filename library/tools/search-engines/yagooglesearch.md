---
id: yagooglesearch
name: yagooglesearch
description: Use when you have a `name`/`username`/query and want to script Google results without getting 429-blocked — returns result URLs programmatically.
url: https://github.com/opsdisk/yagooglesearch
category: search-engines
path:
- search-engines
bestFor: Automating Google dork/search result collection in Python with human-like pacing and back-off to dodge rate-limiting.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free and open source; pip-installable Python library. No API key (it scrapes the web UI).
opsec: active
opsecNote: This programmatically queries Google from your IP — Google sees automated traffic and may serve CAPTCHAs or HTTP 429 blocks. Use a dedicated/proxied IP and consider the library's proxy support; heavy use can get an IP temporarily blocked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Well-known open-source library by opsdisk (also behind pagodo); actively used in dorking pipelines.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- metagoofil
- pagodo-passive-google-dork
aliases:
- yagooglesearch
- yet another google search
tags:
- google-dorking
- search-automation
- python-lib
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# yagooglesearch

> A Python library for scripting Google searches that behaves like a human — randomised pacing plus 429 back-off — so your dorking pipeline isn't instantly blocked.

## When to use
You want to automate Google result collection — running many dorks, or searching a `name`/`username`/`email` at scale — without the near-instant rate-limiting that naive scrapers hit. yagooglesearch wraps Google web search with human-like delays, user-agent rotation, and exponential back-off on HTTP 429, returning result URLs you can pipe onward. It's search automation; missing-persons value is indirect (bulk-finding pages, profiles, and documents mentioning a subject).

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install yagooglesearch`.
2. Query in Python:
   ```python
   import yagooglesearch
   client = yagooglesearch.SearchClient('"John Smith" site:linkedin.com', max_search_result_urls_to_return=50)
   urls = client.search()
   ```
   Tune `minimum_delay_between_paged_results_in_seconds`, proxy, and result count to stay under the radar.
3. Read the returned list of result URLs; feed them to your own parser.
4. Pivot: it's the search engine behind dorking tools — pair with `[[pagodo-passive-google-dork]]` to run a dork list, or with `[[metagoofil]]` to then harvest documents from the discovered domains.

## Inputs → Outputs
- **In:** a Google query string (a `name`, `username`, dork, or `site:` filter)
- **Out:** a list of result URLs (surfacing `social-profile`s, `domain`s, documents)
- **Empty/negative result looks like:** an empty list plus 429/CAPTCHA warnings in logs — usually means Google has throttled your IP, not that there are no results; slow down, switch proxy/IP, and retry.

## Gotchas & OpSec
- Google actively fights automation — even with back-off, a hot IP gets CAPTCHA'd; budget proxies and patience.
- It scrapes the HTML UI, so Google layout changes can break parsing until the library updates.
- OpSec: **active** — the traffic originates from your IP and looks bot-like; use a disposable/proxied egress, never your attributable connection.

## Overlaps ("do both")
- It's the querying engine under `[[pagodo-passive-google-dork]]` (dork runner) and pairs with `[[metagoofil]]` (document harvesting) — use yagooglesearch to *find* URLs, the others to *act* on them.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source library; results are literally Google's, so trust the source ranking but verify each hit, and expect breakage when Google changes its markup.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yagooglesearch |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | active |
| human-in-loop | no |
