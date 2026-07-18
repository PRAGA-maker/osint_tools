---
id: socialdata-api
name: SocialData API
description: Use when you have a `username` or `name` and want Twitter/X profile and tweet data programmatically — returns social profiles, posts, and follower relationships.
url: https://socialdata.tools/
category: social-networks
path:
- social-networks
bestFor: Pulling Twitter/X user profiles, tweets, followers, and search results via API without the official (expensive) X API.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Pay-as-you-go at ~$0.20 per 1,000 tweets/users fetched, no subscription; a free trial with credits (no credit card) lets you evaluate it. Effectively metered rather than free.
opsec: passive
opsecNote: Passive toward the subject — SocialData fetches from X on its servers, so your IP never touches the target's profile and no view/notification reaches them. Your queries and API key are, however, logged by SocialData; treat it as a third party handling your target list.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: unverified
trustNote: Third-party unofficial X data reseller; reliability tracks X's anti-scraping countermeasures and the vendor's own stability, neither of which is guaranteed.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- twitter-advanced-search
aliases:
- socialdata.tools
- SocialData
tags:
- twitter
- api
- data-access
source: osintambition-social
lastVerified: '2026-07-18'
enrichment: full
---

# SocialData API

> A pay-as-you-go REST API that returns Twitter/X profiles, tweets, and follower graphs without the official X API's cost or gatekeeping.

## When to use
You have a `username` (or a `name` to search) on Twitter/X and want structured data — profile fields, tweet history, followers/following, or search results — pulled programmatically for enrichment or monitoring. It is useful when you need to script collection across many handles, or when the official X API's price/access is a blocker. In a missing-persons workflow, it lets you snapshot a subject's X presence and network (`associate` links via followers/mentions) at scale.

## How to use it (`bestInteractionPattern`: api)
1. Register at https://socialdata.tools/ and obtain an API key (free trial credits available, no card required).
2. Call the REST endpoints (documented on the site): user-by-username, user tweets, followers/following, and tweet/keyword search.
3. Pass the subject `username` (or a search query for a `name`) and parse the JSON — profile bio, location, join date, tweet objects, and relationship lists.
4. Watch usage: billing is per tweet/user object returned (~$0.20/1,000), so scope queries tightly.
5. Pivot: followers/mentions surface `associate` handles; profile bio/location and linked URLs feed username-enumeration and geolocation tools.

## Inputs → Outputs
- **In:** `username` (or `name` via search)
- **Out:** `social-profile` (X profile + tweets), `associate` (followers/following/mentions)
- **Empty/negative result looks like:** an empty result set or "user not found" — the handle may be suspended, deleted, renamed, or private; a 4xx/quota error means billing/key issues, not that the subject is absent.

## Gotchas & OpSec
- Human-in-the-loop: requires an API key and a funded/trial account.
- It is metered, not free — treat "freemium" as trial-plus-usage-billing and budget queries.
- As an unofficial reseller it is exposed to X's anti-scraping changes; expect occasional gaps or downtime, and corroborate anything critical against the live profile.
- OpSec: passive toward the target, but you are handing your target handles to a third-party vendor that logs them.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` — use X's own advanced search for precise manual queries and verification, and SocialData when you need the same data structured and at scale via API.

## Trust & verifiability
`trust: unverified` — a commercial third-party scraper of X data; provenance is only as good as X's live data and the vendor's fidelity, so verify key findings directly on X.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialdata-api |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
