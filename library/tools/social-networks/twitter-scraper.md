---
id: twitter-scraper
name: Twitter Scraper
description: Use when you have a Twitter/X `username` and want their full tweet history at scale — returns tweets, replies, retweets and thread data as structured JSON/CSV.
url: https://console.apify.com/actors/u6ppkMWAx2E2MpEuF
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting a Twitter/X account's tweets, replies and threads via an Apify actor without the official API's limits.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- name
- geolocation
status: live
pricing: freemium
costNote: Runs on Apify, which gives a small free monthly credit; heavy scraping is pay-per-result (roughly cents per 1,000 tweets). Requires a free Apify account and API token.
opsec: active
opsecNote: Scraping runs from Apify's infrastructure, not your IP, so the target isn't queried directly by you — but it is an unofficial extraction against X's terms and it touches X servers. Use a dedicated Apify account and avoid tying results to a real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: unverified
trustNote: A third-party Apify actor, not an official Twitter/X product; actors change, break, or get delisted as X alters its site, so verify output freshness each run.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- twitter-url-scraper
- twitter
- instagram-scraper
- reddit-scraper
- youtube-scraper
- apify-s-google-maps-scraper
- dark-web-scraper
- facebook-latest-comments-scraper
- facebook-latest-posts-scraper
- google-search-scraper
- instagram-hashtag-scraper
tags:
- Social Media
- Twitter
- scraper
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Twitter Scraper

> An Apify actor that acts as an unofficial Twitter/X API — feed it a handle and it returns that account's tweets, replies, retweets and threads as structured data, without the official API's cost and rate caps.

## When to use
You have a Twitter/X `username` for a subject or associate and need more than a manual scroll: the full timeline, replies (which often reveal relationships and location cues), quote-tweets, and thread context, exported to JSON/CSV for timeline reconstruction and network analysis. Best when you want to preserve an account's activity before it's deleted or protected.

## How to use it (`bestInteractionPattern`: api)
1. Create a free Apify account and get your API token (Settings → Integrations).
2. Open the actor in the Apify Console (or find an equivalent Twitter/X scraper in the Apify Store if this specific actor is unavailable).
3. Configure the input: target handle(s), and options for how many tweets, whether to include replies/retweets, and date range.
4. Run the actor from the console UI, or call it via the Apify API/SDK for automation.
5. Download the dataset (JSON, CSV, Excel) and review: tweet text, timestamps, engagement, any geotags, and linked accounts.
6. Pivot: mentioned/replied `username`s → associate mapping; geotags/place mentions → `geolocation`; posting times → routine/timezone analysis.

## Inputs → Outputs
- **In:** Twitter/X `username` or profile URL (`social-profile`)
- **Out:** tweets, replies, retweets, thread data, timestamps, engagement, and any embedded `geolocation` — as structured JSON/CSV
- **Empty/negative result looks like:** an empty dataset or an actor error — the account may be protected, suspended, or renamed, or X may have changed its site and broken the actor. Confirm the handle still exists and try a currently-maintained actor.

## Gotchas & OpSec
- Unofficial and fragile: X frequently changes its front end, so any scraper actor can break or be delisted; check that returned data is current, not cached.
- Costs money past the free credit tier; budget per-result pricing for large accounts.
- Terms-of-service and legal grey area: scraping X is against its ToS. Keep collection proportionate and lawful.
- OpSec: extraction comes from Apify's servers, but use a dedicated Apify account and don't log into X from the same identity.

## Overlaps ("do both")
- Pairs with `[[twitter-url-scraper]]` (targeted single-URL/thread extraction) and native `[[twitter]]` advanced search — use this actor for whole-timeline bulk, the others for pinpoint pulls.

## Trust & verifiability
`trust: unverified` — a community-built Apify actor with no official backing; treat its output as a convenience snapshot and confirm any decisive tweet against the live X page (and archive it) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, name, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login) |
