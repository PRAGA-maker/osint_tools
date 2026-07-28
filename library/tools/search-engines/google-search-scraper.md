---
id: google-search-scraper
name: Apify Google Search Scraper
description: Use when you have a query and a target `geolocation`/language and want structured Google SERP data at scale (organic, ads, related) — returns domains and geolocation-scoped results.
url: https://apify.com/apify/google-search-scraper
category: search-engines
path:
- search-engines
bestFor: Programmatically harvesting Google SERPs (organic + ads + related) for a query across chosen country/language/location.
selectorsIn:
- geolocation
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Runs on Apify's platform; a free monthly credit tier exists, heavier use consumes paid credits. Requires an Apify account and API token.
opsec: active
opsecNote: Scraping runs from Apify's cloud, not your IP, which shields you from Google — but Apify sees your queries and results. Don't put case-sensitive query strings through a third-party cloud you wouldn't trust with them; use a sock-puppet Apify account for sensitive work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: A first-party Apify-maintained actor on a reputable scraping platform; output quality is good but it's a commercial cloud tool, and Google SERP structure changes can affect results.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- apify-s-google-maps-scraper
- dark-web-scraper
- facebook-latest-comments-scraper
- facebook-latest-posts-scraper
- google-maps-scraper
- instagram-hashtag-scraper
- instagram-scraper
- reddit-scraper
- twitter-scraper
- twitter-url-scraper
- youtube-scraper
aliases:
- Apify Google SERP scraper
tags:
- google
- serp
- scraping
- automation
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Apify Google Search Scraper

> A cloud actor that runs Google searches at scale and returns structured SERP data — organic results, ads and related queries — with country/language/location targeting.

## When to use
You need Google search results as structured data (JSON/CSV), in volume, and optionally as they'd appear from a specific country, language or `geolocation` — for bulk dorking, monitoring, or feeding results into a pipeline. Unlike a manual search or a fragile scraper, this runs on Apify's infrastructure and handles rotation for you. Use it when the job is "many queries → structured, location-scoped results," not a one-off lookup.

## How to use it (`bestInteractionPattern`: api)
1. Create an Apify account, get your API token, and open the `apify/google-search-scraper` actor.
2. Configure input: query terms, `countryCode`/language, and location; set result depth.
3. Run via the console, API, or client library; retrieve the dataset (organic results, ads, related queries, positions).
4. Extract `domain`s/URLs and metadata from the dataset for downstream tooling.
5. Pivot: feed harvested URLs into capture/enrichment tools; pair with the sibling Apify actors (Maps, social scrapers) for cross-source collection.

## Inputs → Outputs
- **In:** query terms + `geolocation`/country/language
- **Out:** structured SERP data — `domain`s, URLs, titles, snippets, ad and related-query blocks, scoped to the chosen location
- **Empty/negative result looks like:** an empty/short dataset or a run error — the query may be too narrow, credits exhausted, or Google markup changed; check the run log.

## Gotchas & OpSec
- OpSec: **active** scraping, but from Apify's cloud (shields your IP from Google); Apify itself sees your queries — use a sock-puppet account for sensitive terms.
- Costs credits beyond the free tier; large jobs need budgeting.
- SERP structure drifts; validate the output schema periodically and watch for partial results.

## Overlaps ("do both")
- Part of the Apify scraper family (`[[google-maps-scraper]]`, `[[reddit-scraper]]`, `[[twitter-scraper]]`, `[[instagram-scraper]]`, …) — do both to collect the same target across SERPs, maps and social platforms in one pipeline.

## Trust & verifiability
`trust: community` — a first-party actor on a reputable commercial platform; results are reliable but it's a paid cloud tool subject to Google's changing SERP format.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-search-scraper |
| category | search-engines |
| selectorsIn → selectorsOut | geolocation → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | active |
| human-in-loop | yes (api-key) |
