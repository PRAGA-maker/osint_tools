---
id: outwit
name: OutWit Hub
description: Use when you have a `domain`/URL (a page, listing, or profile set) and want to extract structured data or media at scale — turns web pages into tables/exports; a free Light edition covers small jobs.
url: http://www.outwit.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Point-and-click extraction of structured data, links, images, and contacts from web pages into tables/CSV.
selectorsIn:
- domain
selectorsOut:
- email
- image
- social-profile
status: live
pricing: freemium
costNote: OutWit Hub Light is free and fully usable for small jobs (capped at a few hundred rows, no automation, no dynamic-page scraping). Pro/Expert/Enterprise editions (from ~€69) unlock automation, higher limits, and macros.
opsec: active
opsecNote: This is a desktop scraper that fetches target pages directly from your machine and IP — every crawl is a real visit the target's server can log. Run it behind a VPN/proxy and a sock-puppet browser identity when the target is sensitive, and keep request rates polite to avoid tripping rate limits or bans.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-established commercial scraping tool (OutWit SARL) with a free Light tier; widely used in OSINT/journalism for structured extraction.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- OutWit Hub
- OutWit
- outwit.com
tags:
- web-scraping
- data-extraction
- desktop-app
- other-tools
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# OutWit Hub

> A desktop point-and-click scraper: give it a URL and it pulls the links, images, contacts, and tabular data off the page into exportable structures — the free Light edition handles small jobs.

## When to use
You have a `domain` or a set of URLs — a directory, a listing site, a profile page, a forum thread — and need the data off it in structured form rather than by hand. OutWit Hub "auto-explores" a page and separates out emails, images, links, and repeating data rows, which is useful for harvesting contacts, media, or associate lists during an investigation without writing a scraper.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install OutWit Hub (Light is free) for Windows/macOS/Linux from http://www.outwit.com.
2. Enter or navigate to the target URL inside the app.
3. Use the left-panel extractors — "data", "links", "images", "email", "tables", or a custom scraper — to pull the elements you want (`selectorsOut`).
4. Export the results to CSV/Excel. For multi-page automation, "dig" through pagination, or dynamic pages, you need a Pro key.

## Inputs → Outputs
- **In:** `domain` / URL(s) to scrape
- **Out:** `email`, `image`, `social-profile` links, plus generic tabular data and hyperlinks — exported to CSV/Excel
- **Empty/negative result looks like:** the auto-extractors find no structured rows on a JS-heavy page — the Light edition can't render dynamic content, so it may return an empty grid where a Pro/headless-browser tool would succeed.

## Gotchas & OpSec
- Human-in-the-loop: none, but the free Light edition caps extraction size and blocks automation and dynamic-page scraping.
- OpSec: **active** — crawls originate from your machine/IP and hit the target's server; use a proxy/VPN + sock puppet for sensitive targets and throttle to avoid bans.
- Respect robots/terms and rate limits; aggressive scraping is attributable and can get an IP blocked.

## Overlaps ("do both")
- Complements code-based scrapers and headless-browser tools when Light can't handle dynamic pages, and pairs with email-verification tools to validate the addresses it harvests.

## Trust & verifiability
`trust: community` — a mature, widely-used commercial tool with a genuine free tier. The tool is reliable; the *data* it returns is only as trustworthy as the scraped source, so verify extracted emails/links independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | outwit |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → email, image, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
