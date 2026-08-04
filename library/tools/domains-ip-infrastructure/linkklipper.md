---
id: linkklipper
name: Link Klipper (extract all links)
description: Use when you have a web page and want every link off it as data — returns all URLs on the page, filterable by extension/regex, exported to CSV/TXT.
url: https://chrome.google.com/webstore/detail/link-klipper-extract-all/fahollcgofmpnehocdgofnhkkchiekoo
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: One-click harvesting of every hyperlink on a page (profile, directory, search results) into a clean CSV for pivoting.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free Chrome extension; the developer states it runs entirely in the browser and sends no data to external servers.
opsec: passive
opsecNote: Link extraction runs locally on the page you already loaded — it makes no extra requests to the target, so it adds no footprint beyond your normal page visit. Anonymity depends only on how you loaded the page (VPN/sock puppet as needed).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: A popular, well-rated extension (tens of thousands of users) that operates locally; low risk since it only reads the DOM of the current page and exports links.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- linkKlipper
- Link Klipper - Extract all links
tags:
- link-extraction
- scraping
- csv-export
- browser-extension
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Link Klipper (extract all links)

> A one-click Chrome extension that scrapes every hyperlink off the current page and hands you a clean, filterable CSV/TXT — turning a wall of links into a workable dataset.

## When to use
You're on a link-dense page — a target's link-in-bio, a directory listing, a forum member page, a search-results page, a sitemap-like index — and you want all the outbound URLs as structured data instead of copying them one by one. Exporting the links lets you triage which `domain`s and `social-profile` URLs to chase, and regex/extension filters isolate exactly the kind you want (e.g. only social links, only PDFs).

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Link Klipper from the Chrome Web Store.
2. Load the page you want to harvest (behind a VPN/sock-puppet if the visit itself is sensitive).
3. Click the icon → **Extract All Links** (or use the Ctrl/Cmd+Shift+K selection mode to grab links from a specific page section).
4. Filter the results by file extension or a regular expression (e.g. limit to `instagram.com|linkedin.com|twitter.com`), then export to CSV/TXT.
5. Pivot: feed the exported `domain`s/`social-profile` URLs into your other tools — reverse-image, profile OSINT, DNS/WHOIS — in bulk.

## Inputs → Outputs
- **In:** the current web page (its `domain`/links)
- **Out:** all page links as CSV/TXT — `domain`s and `social-profile` URLs, filterable
- **Empty/negative result looks like:** few/no links exported — the page renders links via JavaScript after load (scroll/expand first) or genuinely has none; a near-empty export usually means dynamic content, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none beyond installing the extension.
- OpSec: **passive** — it only reads the already-loaded page's DOM and makes no extra requests to the target, so it adds no footprint; your exposure is just from having loaded the page.
- Dynamic pages: links injected after load or hidden behind "load more" won't be captured until they're actually in the DOM — expand/scroll first.

## Overlaps ("do both")
- Pairs with a crawler/scraper for multi-page harvests — Link Klipper is perfect for the *current* page, while a crawler follows links across a whole site; use Klipper for quick single-page grabs and a crawler for depth.

## Trust & verifiability
`trust: community` — a popular, locally-running extension that only reads and exports the page's own links; the output is trivially verifiable by inspecting the page.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkklipper |
