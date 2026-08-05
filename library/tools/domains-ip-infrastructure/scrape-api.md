---
id: scrape-api
name: ScraperAPI
description: Use when you have a domain/URL you need to collect at scale and want a proxy API that rotates IPs, handles JS rendering and CAPTCHAs, and masks your origin — returns the target page's HTML/data without exposing your own IP.
url: https://www.scraperapi.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fetching pages at scale through rotating proxies (with JS render / anti-bot handling) while hiding your own IP.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Freemium — a free tier grants a limited monthly credit allowance; higher volume, geotargeting, and concurrency require a paid plan.
opsec: active
opsecNote: ScraperAPI fetches the target FROM ITS OWN proxy pool, so the target sees ScraperAPI's IP, not yours — good for masking origin during bulk collection. But ScraperAPI itself sees every URL you fetch and the returned content, so don't route a sensitive investigation through it, and read their data-retention terms. Bulk scraping is active and may breach a site's ToS.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: An established commercial scraping-proxy vendor; reliable as infrastructure, but a third party that sees your requests — trust it as a proxy, not with sensitive query data.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- ScraperAPI
- scraperapi.com
tags:
- web-scraping
- proxy
- Domain/IP/Links
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# ScraperAPI

> A proxy API for web scraping — it fetches target pages through rotating IPs (handling JS rendering and anti-bot defences) so you collect at scale without exposing your own address.

## When to use
When collection is the bottleneck: you need many pages from a `domain`, or a site blocks/rate-limits your IP, or requires JS rendering. Instead of building your own proxy rotation, you send the target URL to ScraperAPI and get back the rendered HTML from one of its IPs. Useful for bulk OSINT harvesting where origin-masking and anti-bot handling matter.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://www.scraperapi.com/ to get an API key (free tier available).
2. Make requests to their endpoint with your key and the target URL (plus options like `render=true` for JS, or geotargeting).
3. Receive the fetched page HTML/content and parse it in your pipeline.
4. Stay within your credit allowance; scale to a paid plan only if needed.
5. Pivot: parsed content → the selectors it contains (names, emails, links, `domain`s) → downstream OSINT tools.

## Inputs → Outputs
- **In:** a target `domain`/URL to fetch
- **Out:** the target page's HTML/content (from ScraperAPI's IP), i.e. `domain` content to parse
- **Empty/negative result looks like:** errors/blocks even through the proxy (hard anti-bot sites), or exhausted credits — reduce volume, enable rendering, or accept the site resists scraping.

## Gotchas & OpSec
- **Third party sees everything:** ScraperAPI logs the URLs you fetch and returns their content — don't route sensitive investigations through it; check retention terms.
- Requires an API key (human-in-the-loop registration).
- Free tier is limited; heavy use is paid. Bulk scraping may violate target ToS — know the rules.

## Overlaps ("do both")
- Overlaps other scraping-proxy services; combine with in-browser scrapers (`[[scrappy]]`, link dumpers) for small jobs and reserve the API for scale/anti-bot targets.

## Trust & verifiability
`trust: community` — a solid commercial proxy as infrastructure; trust it to fetch and mask origin, but treat it as a third party that sees your queries, and verify scraped data against the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrape-api |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | active |
| human-in-loop | yes (api-key) |
