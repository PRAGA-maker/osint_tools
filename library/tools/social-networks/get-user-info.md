---
id: get-user-info
name: Get User info
description: Use when you have a VKontakte `username`/screen-name or numeric ID and want profile fields — returns the VK `social-profile` (name, city, photo, counters) via the users.get API.
url: https://api.vk.com/method/users.get
category: social-networks
path:
- social-networks
bestFor: Resolving a VK screen-name or user ID to a structured profile record via the official VK API method.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: The API method is free, but VK now requires a valid access token (service or user) to call it.
opsec: passive
opsecNote: A read-only API call against VK's servers — the target isn't notified. Your access token and IP identify the caller to VK, so use a sock-puppet VK app/token and a clean IP; never use a personal token for target lookups.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: The genuine first-party VKontakte API endpoint; returned fields are authoritative VK profile data, not a scrape.
missingPersonsRelevance: medium
coverage:
- global
- ru
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- VK users.get
- api.vk.com users.get
tags:
- vk
- russia
- api
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- community-search
- people-search-results-vk
- vk
- vk-com
- vk-com-2
- vk-community-search
- vk-people-search
---

# Get User info

> The VK `users.get` API method: turn a VKontakte screen-name or numeric ID into a structured profile record — name, city, photo, and account counters — straight from VK.

## When to use
You have a VK `username`/screen-name (e.g. `id12345` or a vanity name) or numeric ID and want its canonical profile fields programmatically, or to resolve a screen-name to a stable numeric ID for further VK OSINT. Faster and more structured than scraping the profile page, and it lets you batch many IDs at once and request specific fields (city, bdate, last_seen, photo, counters).

## How to use it (`bestInteractionPattern`: api)
1. Get a VK access token — register a sock-puppet VK app and obtain a service or user token (required; anonymous calls are rejected).
2. Call the method, e.g.:
   `https://api.vk.com/method/users.get?user_ids=SCREENNAME&fields=city,bdate,photo_max,last_seen,counters&access_token=TOKEN&v=5.199`
3. Read the JSON: `id`, `first_name`, `last_name`, and any requested fields.
4. Pivot: the resolved numeric `id` feeds VK friends/groups/photo tools; `city`/`last_seen`/photo corroborate identity and activity.

## Inputs → Outputs
- **In:** VK `username`/screen-name or numeric ID (`user_ids`), optional `fields`
- **Out:** structured `social-profile` — `name`, id, and requested fields (city, photo, counters, last seen)
- **Empty/negative result looks like:** an empty array or an error object (`error_code`) — invalid/deleted/banned user, a privacy-restricted field, or a missing/expired token; a `5` error means the token is bad.

## Gotchas & OpSec
- Human-in-the-loop: **a token is mandatory** since VK tightened the API — no token, no data. Some fields (bdate, last_seen) are hidden by the user's privacy settings even with a token.
- Respect rate limits (≈3 calls/sec per token); batch `user_ids` (up to ~1000) instead of looping.
- OpSec: passive to the target, but VK sees your token — always use a sock-puppet app/token.

## Overlaps ("do both")
- Pairs with VK friends/community/photo tools (e.g. [[vk-com]], [[sn-radar-vk-photo-search]]): this resolves and enriches the account, those map its social graph and geotagged media.

## Trust & verifiability
`trust: trusted` — it's VK's own API, so returned fields are authoritative. The only caveats are access (token required) and privacy-gated fields, not data quality.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | get-user-info |
