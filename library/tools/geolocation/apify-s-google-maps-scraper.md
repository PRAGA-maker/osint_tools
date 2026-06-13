---
id: apify-s-google-maps-scraper
name: Apify's Google Maps Scraper
description: Use when you need to bulk-extract Google Maps place data (names, addresses, phone numbers, reviews, coordinates) around a location or for a business a person is tied to.
url: https://apify.com/compass/crawler-google-places
category: geolocation
path:
- geolocation
bestFor: Scraping Google Maps/Places results at scale into structured records (address, phone, coordinates, reviews).
selectorsIn: [name, address, geolocation, employer-org]
selectorsOut: [address, phone, geolocation, employer-org, social-profile]
status: live
pricing: freemium
costNote: Pay-per-result, billed roughly from ~$1.50 per 1,000 scraped places; an Apify free monthly platform credit lets you run small jobs, but large pulls and contact/email enrichment add-ons cost extra.
opsec: active
opsecNote: Scrapes Google Maps via Apify's infrastructure, not yours, so your IP is not exposed to Google; but it does query Google's live servers (active toward Google, not toward the person). Reviewer profiles you collect are real accounts — handle as you would any social pivot.
humanInLoop: true
humanInLoopReason: [account-login, payment-wall-partial, api-key]
bestInteractionPattern: api
trust: community
trustNote: Maintained by Compass (a vetted Apify "actor" author) on the official Apify marketplace; widely used, but it scrapes Google Maps which can break when Google changes its UI.
missingPersonsRelevance: medium
coverage: [global]
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: [bing-maps, baidu-maps, batchgeo]
aliases: [crawler-google-places, google-maps-scraper]
tags: [scraper, google-maps, places, apify]
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# Apify's Google Maps Scraper

> A hosted Apify "actor" that scrapes Google Maps/Places at scale, returning structured business records — names, addresses, phone numbers, coordinates, hours, and review text with reviewer profiles.

## When to use
You have a `name`, business/`employer-org`, `address`, or a search area (`geolocation`) and want every matching Google Maps place as structured data instead of clicking through the map by hand. In a missing-persons context: enumerate businesses around a last-known location, pull a workplace's listing (phone, hours, reviews), or collect reviewer accounts that may tie back to a person of interest. It bypasses Google's ~120-result-per-view cap by automating scroll/search.

## How to use it (`bestInteractionPattern`: api)
1. Create an Apify account (free tier available) and open the actor at https://apify.com/compass/crawler-google-places.
2. Configure the input: search terms (e.g. "auto repair"), and/or Google Maps URLs, place IDs, plus a location string or a GeoJSON polygon for a custom search area.
3. Run from the web console for a one-off, or call it programmatically with the Apify API / Node/Python client (`apify-client`) using your API token for automation.
4. Read the dataset output (JSON/CSV/Excel): each row is a place with `name`, `address`, `phone`, website, `geolocation` (lat/long), ratings, and review text incl. reviewer names/profiles (`social-profile`).
5. Pivot: feed phone numbers to a phone-lookup tool, reviewer profile links to social tooling, and coordinates to `[[bing-maps]]`/`[[baidu-maps]]` for imagery.

## Inputs -> Outputs
- **In:** `name`, `address`, `geolocation`, `employer-org` (as search terms / area)
- **Out:** `address`, `phone`, `geolocation`, `employer-org`, `social-profile` (reviewer accounts)
- **Empty/negative result looks like:** zero items in the dataset (too-narrow area or zero matches), or rows missing phone/website (Google simply has no such field for that place).

## Gotchas & OpSec
- Human-in-the-loop: requires an Apify login and an API token; beyond the free monthly credit you must pay per result, and contact/email enrichment is a paid add-on.
- Cost can run away on broad areas — bound the search with a small polygon or a tight result limit first.
- Scrapes Google's live data, so results can degrade if Google changes its layout; the actor is updated to keep pace but verify a sample by hand.
- Data is only as current as Google's listings; closed businesses and stale phone numbers appear.

## Overlaps ("do both")
- Pairs with `[[batchgeo]]` to plot the extracted addresses on a shareable map.
- Pairs with `[[bing-maps]]` / `[[baidu-maps]]` to add imagery/Street-level context to each coordinate.

## Trust & verifiability
`trust: community` — official Apify marketplace actor by Compass, a recognized author; reliable and maintained, but it is a third-party scraper of Google Maps, so treat extracted fields as leads and confirm critical ones (phone, address) independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | apify-s-google-maps-scraper |
| category | geolocation |
| selectorsIn → selectorsOut | name, address, geolocation, employer-org → address, phone, geolocation, employer-org, social-profile |
| pricing / cost | freemium (pay-per-result) |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial, api-key) |
