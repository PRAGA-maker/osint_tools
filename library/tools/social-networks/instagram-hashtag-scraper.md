---
id: instagram-hashtag-scraper
name: Instagram Hashtag Scraper
description: Use when you have an Instagram hashtag and want every post tagged with it — returns usernames, captions, image URLs and location leads as CSV/JSON.
url: https://console.apify.com/actors/reGe1ST3OBgYZSsZJ
category: social-networks
path:
- social-networks
bestFor: Bulk-collecting all posts under an Instagram hashtag to surface the accounts, images and locations behind an event or topic.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
- image
- geolocation
status: live
pricing: freemium
costNote: Runs on Apify's platform; a free Apify account includes monthly usage credits enough for small runs, larger scrapes consume paid credits (usage-based).
opsec: active
opsecNote: The actor pulls public Instagram data from Apify's own infrastructure/IPs, so your IP isn't exposed to Instagram — but you must trust Apify with the run and results, and scraping Instagram breaches its ToS. Use a dedicated Apify account, never your personal Instagram login, and don't seed it with private/investigation-revealing hashtags.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: community
trustNote: Third-party Apify Store actor, not an Instagram product; reliability tracks Instagram's anti-scraping changes and the actor author's upkeep.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- apify-s-google-maps-scraper
- dark-web-scraper
- facebook-latest-comments-scraper
- facebook-latest-posts-scraper
- google-maps-scraper
- google-search-scraper
- instagram-scraper
- reddit-scraper
- twitter-scraper
- twitter-url-scraper
- youtube-scraper
aliases:
- Apify Instagram Hashtag Scraper
tags:
- Social Media
- Instagram
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Instagram Hashtag Scraper

> An Apify actor that dumps every post under a given Instagram hashtag into a structured table — turning a hashtag into a list of accounts, images and places to investigate.

## When to use
You have a hashtag tied to your subject — an event they attended, a cause, a hometown tag, a fan/community tag, or a hashtag they coined — and you want the full set of posts using it so you can find *who* is posting and *where*. Good for mapping the crowd around an event a missing person was last seen at, or for finding a subject's own posts when they tag consistently. It's a bulk-collection step, not a targeted person lookup.

## How to use it (`bestInteractionPattern`: api)
1. Sign in to Apify (free account) and open the actor at the URL above.
2. In the input, enter one or more hashtags (without the `#`) and set a results limit (start small to conserve credits).
3. Run it via the console UI or the Apify API; wait for the run to finish.
4. Download the dataset as CSV/JSON/XLS: each row has the poster's `username`, caption, other hashtags, post URL, image dimensions/URLs and (when present) tagged location.
5. Pivot: each `username` → profile/account research; `image` URLs → reverse-image and face search; a tagged `geolocation` → mapping; co-occurring hashtags → widen the sweep.

## Inputs → Outputs
- **In:** an Instagram hashtag (keyword; enter as `username`-style handle without `#`)
- **Out:** `username`, `social-profile` (post/profile links), `image` URLs, `geolocation` (tagged place), plus captions and comment counts
- **Empty/negative result looks like:** an empty dataset or an error run — the hashtag has no public posts, Instagram rate-limited/blocked the scrape, or the actor needs an update; retry with a smaller limit or a different hashtag.

## Gotchas & OpSec
- Human-in-the-loop: requires an Apify account login; runs can fail when Instagram changes anti-scraping defences.
- OpSec: **active** collection of a platform's data. Apify's IPs do the fetching (shielding yours from Instagram), but you're trusting Apify with the job and results, and this violates Instagram's ToS. Keep it off your real accounts.
- Only public posts are returned; private accounts and hashtag-hidden content won't appear. Watch credit spend on popular hashtags.

## Overlaps ("do both")
- Pairs with `[[instagram-scraper]]` (profile/post-level once you have a username) and `[[google-maps-scraper]]` for location context — the hashtag scraper finds the accounts, the profile scraper drills into each one.

## Trust & verifiability
`trust: community` — a third-party Apify actor, not an Instagram service; treat its output as raw collected data to verify against the live posts, and expect breakage as Instagram evolves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instagram-hashtag-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile, image, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login) |
