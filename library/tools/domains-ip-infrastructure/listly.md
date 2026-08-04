---
id: listly
name: Listly
description: Use when you have a data-rich web page and want its lists/tables extracted — returns the page's structured rows (names, links, contacts) as a spreadsheet.
url: https://chromewebstore.google.com/detail/listly-free-data-scraper/ihljmnfgkkmoikgkdkjejbkpdpbmcgeh
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click no-code scraping of lists, tables and cards from a web page into Excel/Google Sheets.
selectorsIn:
- domain
selectorsOut:
- name
- social-profile
- email
- phone
status: live
pricing: freemium
costNote: Free to use as a guest (no signup) for basic scraping; higher-volume, multi-page and cloud features are paid.
opsec: passive
opsecNote: The extension scrapes pages you already have open in your own browser, so your visit — not the extension — is what reaches the target site; apply your usual browsing OpSec. Multi-page/auto-scroll scraping generates lots of requests to the site, which can be noticeable, so throttle on sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Popular free web-scraper Chrome extension (~100k users, well rated); reliable for structured page data, but a commercial vendor's tool — review what it uploads if you enable cloud features.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Listly free data scraper
- listly
tags:
- Domain/IP/Links
- scraping
- data-extraction
- browser-extension
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Listly

> A no-code web scraper as a browser extension: click a list, table, or card on a page and Listly grabs every similar item into a spreadsheet — fast structured extraction for OSINT.

## When to use
You're looking at a page full of structured records — a member directory, a search-results list, a table of registrants, a set of profile cards — and want the data as rows rather than copying by hand. Listly extracts the repeating items (names, links, contact fields) into Excel/Google Sheets, and can follow links and page through multi-page lists, turning a directory into a workable dataset of `name`/`social-profile`/`email`/`phone` leads.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Listly - Free Data Scraper" from the Chrome Web Store (link above); you can run it as a guest without signing up.
2. Navigate to the page with the list/table/cards you want (apply your usual browsing OpSec first).
3. Click Listly and select a list/table/card — it auto-detects the other similar items on the page.
4. Enable multi-page/auto-scroll or "follow links" if you need detail from linked pages; then export to Excel/Google Sheets.
5. Pivot: the extracted `name`/`email`/`phone`/`social-profile` rows feed the matching selector tools in bulk.

## Inputs → Outputs
- **In:** a data-rich page on a `domain` (list/table/cards)
- **Out:** structured rows — `name`, `social-profile` links, `email`, `phone` where present
- **Empty/negative result looks like:** nothing detected — the content may be rendered as images, inside a canvas, behind infinite-scroll/login, or not actually repeating; try scrolling to load items or view-source extraction instead.

## Gotchas & OpSec
- Only grabs what's in the rendered DOM; images/canvas/login-walled data won't extract.
- Aggressive multi-page/auto-scroll scraping is noisy to the target site and may hit rate limits or ToS — throttle and scrape only what you're authorized to.
- Local extraction is passive to the extension; cloud features upload data, so review before enabling.

## Overlaps ("do both")
- Complements `[[google-chrome-webpage-regexp-search]]` — the regex extension pulls patterned strings from one page, Listly grabs whole structured lists across pages; use regex for ad-hoc selectors, Listly for tabular datasets.

## Trust & verifiability
`trust: community` — a widely-used, well-rated commercial extension; dependable for structured extraction, though the accuracy of scraped data is only as good as the source page, and cloud/upload features warrant a look before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | listly |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → name, social-profile, email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
