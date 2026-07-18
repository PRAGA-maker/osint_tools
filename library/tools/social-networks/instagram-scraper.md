---
id: instagram-scraper
name: Instagram Scraper (Apify)
description: Use when you have an Instagram `username`/`social-profile` and want its posts, stories, and commenters at scale — returns `username`s, `image`s, captions, and `geolocation` tags.
url: https://apify.com/jaroslavhejlek/instagram-scraper
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting an Instagram account's posts, stories, comments, and follower interactions via a hosted actor.
selectorsIn:
- username
- social-profile
selectorsOut:
- username
- image
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Runs on Apify's platform; free monthly platform credits cover light use, heavier runs consume paid compute units. No Instagram login of your own is required.
opsec: passive
opsecNote: The scrape runs from Apify's cloud infrastructure and residential proxies, not your IP, so it's passive toward the target and doesn't tie the activity to you. It only collects public data; scraping still violates Instagram's ToS, and Apify sees your job inputs.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: api
trust: community
trustNote: A popular, maintained third-party actor by jaroslavhejlek on the Apify marketplace; widely used but community-built, and Instagram anti-scraping changes can break or throttle it.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- instagram-hashtag-scraper
- facebook-latest-posts-scraper
- facebook-latest-comments-scraper
- twitter-scraper
- reddit-scraper
- youtube-scraper
- apify-s-google-maps-scraper
- dark-web-scraper
- google-maps-scraper
- google-search-scraper
- twitter-url-scraper
aliases:
- jaroslavhejlek/instagram-scraper
- Apify Instagram Scraper
tags:
- Social Media
- Instagram
- scraping
- apify
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Instagram Scraper (Apify)

> A hosted Apify actor that bulk-extracts an Instagram account's posts, stories, comments, and commenters — no login of your own required.

## When to use
You have an Instagram `username` or profile URL for a subject (or their associates) and need more than manual scrolling: a structured export of their posts, captions, tagged locations, images, and — crucially for network mapping — the `username`s of people who comment on and interact with them. Strong for enumerating a subject's social circle and geotagged activity when building a missing-persons or associate map.

## How to use it (`bestInteractionPattern`: api)
1. Create an Apify account and get your API token.
2. Open the actor (`jaroslavhejlek/instagram-scraper`), supply target profile URLs / `username`s and options (posts, comments, stories, result limits).
3. Run it from the Apify console, the API, or a client library; the actor scrapes from Apify's cloud + proxies.
4. Download the dataset (JSON/CSV): post captions, `image`/media URLs, tagged `geolocation`s, timestamps, and commenter `username`s.
5. Pivot: commenter/tagged usernames feed username-enumeration and cross-platform searches; geotags feed mapping.

## Inputs → Outputs
- **In:** Instagram `username`(s) or profile/post `social-profile` URLs.
- **Out:** posts with captions and `image` URLs, tagged `geolocation`s, commenter and tagged `username`s, follower/following interaction data.
- **Empty/negative result looks like:** a private account returns little/no post data; a run that returns only profile metadata usually means content is gated or Instagram throttled the actor.

## Gotchas & OpSec
- API key / account required: you need an Apify token and consume platform credits.
- Rate limits & breakage: Instagram actively fights scraping; runs can be throttled or return partial data, and the actor needs periodic updates.
- Private accounts: only public content is reachable — no login-walled data.
- OpSec: passive toward the target (runs from Apify infra), but scraping breaches Instagram ToS; ensure you're authorized.

## Overlaps ("do both")
- Pairs with `[[instagram-hashtag-scraper]]` (discover accounts by hashtag/place) and other Apify social actors (`[[twitter-scraper]]`, `[[facebook-latest-posts-scraper]]`) — this one owns the per-account deep pull.

## Trust & verifiability
`trust: community` — a well-known third-party Apify actor; data comes straight from public Instagram, but coverage/completeness depends on the actor keeping up with Instagram's defenses, so verify key findings against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → username, image, geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes |
