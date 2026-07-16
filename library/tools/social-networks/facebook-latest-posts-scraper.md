---
id: facebook-latest-posts-scraper
name: Facebook Latest Posts Scraper (Apify)
description: Use when you have a public Facebook page/profile URL (`social-profile`) and want its recent posts and comments in bulk — returns post/comment text, timestamps, URLs, engagement counts and author IDs as `metadata-exif`.
url: https://console.apify.com/actors/EtZ9lsiipPgKrQIi6
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting recent public Facebook posts and their comments (text, timestamps, likes/shares, author IDs) from one or many page URLs into structured JSON/CSV.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- social-profile
status: live
pricing: freemium
costNote: Runs on Apify. Requires a free Apify account; usage consumes platform credits — the free tier includes a monthly credit allowance, heavy scraping is paid. It is not a no-signup web tool.
opsec: active
opsecNote: Scraping runs from Apify's cloud IPs, not yours, which shields your address — but it is still automated collection against Facebook and may violate Facebook's ToS. Only target PUBLIC pages; the actor cannot and must not touch private/login-gated content. Your Apify account ties the job to your identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: community
trustNote: A third-party actor in the Apify marketplace (harvested via cyb-detective). Quality and upkeep depend on the individual actor author; verify current status and pricing on the actor page before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Apify Facebook posts scraper
- Facebook page posts scraper
tags:
- social-media
- facebook
- scraper
- apify
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- apify-s-google-maps-scraper
- dark-web-scraper
- facebook-latest-comments-scraper
- google-maps-scraper
- google-search-scraper
- instagram-hashtag-scraper
- instagram-scraper
- reddit-scraper
- twitter-scraper
- twitter-url-scraper
- youtube-scraper
---

# Facebook Latest Posts Scraper (Apify)

> An Apify marketplace actor that bulk-collects recent public Facebook posts and their comments from page URLs into structured data — for when copy-pasting posts by hand doesn't scale.

## When to use
You have one or more public Facebook page/profile URLs (`social-profile`) and want the recent posting and comment activity as structured data — to build a timeline, map who comments (candidate `associate`s via author IDs), or archive content before it disappears. Reach for this over manual scrolling when you need many posts, many pages, or repeatable extraction. It only works on **public** content.

## How to use it (`bestInteractionPattern`: api)
1. Create a free account at Apify and open the actor at https://console.apify.com/actors/EtZ9lsiipPgKrQIi6.
2. Configure input: paste one or more public Facebook page/post URLs and set limits (max posts, whether to include comments).
3. Run the actor (from the console UI or via the Apify API/SDK for automation). It executes on Apify's cloud.
4. Download the dataset (JSON/CSV): each record has post text, timestamp, post URL, likes/shares/comment counts, and comment text with author IDs.
5. Pivot: comment author IDs → resolve to profiles for an `associate` graph; timestamps → activity/timezone pattern; post content → geolocation/entity extraction.

## Inputs → Outputs
- **In:** `social-profile` (public Facebook page/profile/post URLs)
- **Out:** `metadata-exif` (post/comment timestamps, engagement counts, author IDs), plus `social-profile` links to commenters
- **Empty/negative result looks like:** an empty dataset — the target is private/login-gated, the URL is wrong, Facebook changed its markup and broke the actor, or a rate-limit blocked the run. Empty ≠ "no activity"; verify the page is public and the actor is current.

## Gotchas & OpSec
- **Account + credits:** not a click-and-go site — you need an Apify account and the run costs credits. Check the actor's live pricing/status page first.
- Facebook actively fights scraping; third-party actors break periodically. Treat brittleness as expected and confirm the actor is maintained.
- ToS/legal: automated scraping may breach Facebook's terms; restrict to public data and use lawfully.
- OpSec: runs from Apify IPs (shields yours) but ties the job to your Apify account; it is **active** automated collection.

## Overlaps ("do both")
- Pairs with `[[facebook-search-2]]` — SowSearch finds the right pages/posts; this actor then bulk-extracts them.
- Feed commenter author IDs into Facebook profile/ID resolvers to build an associate map.

## Trust & verifiability
`trust: community` — a marketplace actor whose reliability rests on its author; Facebook changes can silently break it. Spot-check a few extracted posts against the live page to confirm the data is current and accurate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-latest-posts-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login) |
