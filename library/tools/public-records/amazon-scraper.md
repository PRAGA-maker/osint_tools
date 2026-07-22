---
id: amazon-scraper
name: Amazon Scraper
description: Use when you have Amazon product/search URLs and want structured listing and review data pulled to disk — returns associate leads (reviewer names, sellers) and metadata.
url: https://github.com/scrapehero-code/amazon-scraper
category: public-records
path:
- public-records
bestFor: Bulk-extracting Amazon product details, seller info, and reviews (with reviewer names) from a list of URLs into JSONL for offline analysis.
selectorsIn:
- name
- username
selectorsOut:
- associate
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python). A paid, browser-based commercial version exists on the ScrapeHero Marketplace, but this repo's scrapers are free to run yourself.
opsec: passive
opsecNote: Scraping runs from your own machine against Amazon's public pages; the target person is never contacted. Amazon may rate-limit or block scraping IPs and can log your requests — run from a throwaway IP/proxy, throttle requests, and respect Amazon's terms. It reads public listing/review data only.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: unverified
trustNote: A ScrapeHero tutorial-grade open-source scraper; minimally maintained (few commits) and dependent on Amazon's page structure, so selectors can break when Amazon changes its HTML.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- scrapehero-code/amazon-scraper
tags:
- Tender/shipment information search
- Amazon
- scraper
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Amazon Scraper

> A free Python scraper that pulls structured Amazon product, seller, and review data (including reviewer display names) from a list of URLs into JSONL — a data-collection technique for turning Amazon pages into analysable records.

## When to use
You have Amazon product or search-result URLs — a subject's wishlist items, a seller/storefront they run, or products whose reviews you want to mine — and you need the data in structured form rather than clicking through pages. Review scraping surfaces reviewer display names and profile links (potential `associate`/handle leads), and seller pages surface business names; product data supports commercial-link and lifestyle inference.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/scrapehero-code/amazon-scraper and install the Python requirements (uses `requests` + `selectorlib`).
2. Add the target Amazon product/search URLs to the tool's input text file(s).
3. Run the product scraper and/or the search-results scraper.
4. Read the JSONL output: product name, price, description, images, variants, and reviews (with reviewer names) — for search runs, the list of matching products/sellers.
5. Pivot: reviewer display names/handles become `username`/`associate` leads for username-search tools; seller/business names feed company-records lookups.

## Inputs → Outputs
- **In:** Amazon product/search URLs (optionally tied to a `name`/`username` you're investigating)
- **Out:** `associate` (reviewer names, seller/storefront links), listing `metadata-exif`/attributes in JSONL
- **Empty/negative result looks like:** empty JSONL or "Uh oh"/blocked responses — usually Amazon rate-limiting or an HTML change that broke the selectors, not a true "no data". Re-run with a proxy/delay or update the selectorlib template.

## Gotchas & OpSec
- Fragile: it depends on Amazon's current HTML; when Amazon changes layout the selectors break until updated.
- Rate-limiting/ToS: Amazon actively throttles scrapers and scraping may violate its terms; throttle, proxy, and stay within public data.
- Tutorial-grade: minimal maintenance; expect to patch selectors yourself.

## Overlaps ("do both")
- Pairs with username-search tools — this harvests reviewer/seller handles at scale, those resolve each handle to the subject's other accounts.

## Trust & verifiability
`trust: unverified` — an open-source tutorial scraper, not an authoritative source; its output is only as reliable as the live Amazon pages it reads, which you can re-scrape and eyeball to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | amazon-scraper |
| category | public-records |
| selectorsIn → selectorsOut | name, username → associate, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
