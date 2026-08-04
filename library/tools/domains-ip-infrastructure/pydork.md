---
id: pydork
name: PyDork
description: Use when you have a `name`, `username`, `domain` or `image` and want to automate dork queries across Google, Bing, DuckDuckGo, Baidu and Yahoo Japan — returns result URLs, domains and matching images from multiple engines at once.
url: https://github.com/blacknon/pydork
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Scripted, multi-engine search/dorking and image search from the CLI or as a Python library.
selectorsIn:
- name
- username
- domain
- image
selectorsOut:
- domain
- social-profile
- image
status: live
pricing: free
costNote: Free and open-source (MIT). No API keys — it scrapes the engines' web results directly.
opsec: active
opsecNote: Because it scrapes search engines rather than using official APIs, your IP issues automated queries that engines can rate-limit or CAPTCHA. Use a proxy/VPN and modest result counts; the targets you search are only disclosed to the search engines, not to any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community Python project (blacknon); scraper-based, so it breaks when engines change markup or throttle.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- py-dork
tags:
- dorking
- search-automation
- image-search
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# PyDork

> A CLI + Python library that runs the same search or dork across five engines and collects the results, with image-search and suggestion modes.

## When to use
You have a `name`, `username`, `domain`, or reference `image` and want to run advanced search queries (site:, intitle:, filetype: dorks) across several engines programmatically — useful for surfacing profiles, documents, cached pages or reused images that a single engine misses or has de-ranked.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install pydork`.
2. Text search across engines: `pydork search -n 20 -t google bing duckduckgo -- 'site:linkedin.com "Jane Doe"'`.
3. Image search: `pydork image -s -n 20 -t google yahoo -- 'Jane Doe'` (the `-s` flag uses Selenium for JS-rendered results).
4. Optionally pull page titles with `-T`, or import the `SearchEngine` class into a Python script for batch dorking.
5. Review the aggregated URLs/images and pivot: candidate `social-profile`/`domain` hits go to profile tools; matched images go to reverse-image workflows.

## Inputs → Outputs
- **In:** any search string built from a `name`, `username`, `domain`, or an `image` query term.
- **Out:** result URLs (`domain`, candidate `social-profile`), and image results/URLs when using image mode.
- **Empty/negative result looks like:** an empty result list or a CAPTCHA/rate-limit error from an engine — often throttling rather than a true zero; retry later or via proxy.

## Gotchas & OpSec
- **Scraper fragility:** no official APIs, so engine layout changes or bot-detection can break results without warning; keep it updated.
- Aggressive `-n` values trigger CAPTCHAs and temporary blocks; go slow and rotate IPs.
- Different engines rank/censor differently — run several (`-t`) to avoid one engine's blind spots.

## Overlaps ("do both")
- Pairs with account-enumeration like `[[slash]]` — pydork finds indexed mentions and documents by dork, while enumerators probe platforms directly; together they cover indexed and non-indexed footprints.

## Trust & verifiability
`trust: community` — a maintained open-source scraper; results are raw search hits, so treat each as a lead to open and verify rather than a vetted fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pydork |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | name, username, domain, image → domain, social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
