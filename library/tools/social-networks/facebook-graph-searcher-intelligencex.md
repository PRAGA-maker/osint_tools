---
id: facebook-graph-searcher-intelligencex
name: Facebook Graph Searcher (Intelligence X)
description: Use when you have a Facebook numeric ID (or `name`/`username`) and want ready-made Facebook search/URL queries — returns constructed links to photos, friends, places, and check-ins.
url: https://intelx.io/tools?tab=facebook
category: social-networks
path:
- social-networks
bestFor: Auto-generating Facebook "graph"-style query URLs (photos of, places visited, friends, likes) from a target's Facebook profile ID.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: The query-builder tool is free and needs no login. (Intelligence X's paid search product is separate; this particular utility is free.)
opsec: active
opsecNote: The generator itself just builds URLs (passive), but the moment you open a generated link you are browsing the target's Facebook — do that only while logged into a sock-puppet Facebook account, never your real one, since profile views and friend/photo enumeration happen under whatever account you use.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A free utility from Intelligence X (intelx.io), a reputable OSINT vendor. Its usefulness is limited by Facebook itself — Graph Search was gutted in 2019, so many generated queries no longer return results.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- intelligence-x
- intelligence-x-person-tools
- intelligencex
- intelx-io
- intelligence-x-2
- intelligence-x-telegram-search
- intelligencex-linkedin-search
aliases:
- IntelX Facebook tools
- Facebook ID search
tags:
- facebook
- graph-search
- intelx
source: osintambition-social
lastVerified: '2026-07-18'
enrichment: full
---

# Facebook Graph Searcher (Intelligence X)

> A free query-builder that turns a Facebook profile's numeric ID into ready-made search URLs — photos of the person, places they visited, their friends, likes, and check-ins.

## When to use
You have a target's Facebook profile (and can get its numeric ID) and want to enumerate their activity by category without hand-crafting each URL. The tool pre-writes the `facebook.com/search/...` and profile-section links (photos-of, places-visited, friends, pages-liked) so you can jump straight to each facet. Use it as a fast pivot menu once you've located a subject's Facebook account and want to systematically pull photos, associates, and location history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get the target's **numeric** Facebook ID (paste the profile URL/username into an ID-lookup; vanity usernames need converting to the numeric ID).
2. Open https://intelx.io/tools?tab=facebook and enter the numeric ID (or name/`username` where supported).
3. The tool generates a set of clickable queries — "photos of", "photos by", "places visited", "friends", "pages liked", "check-ins", etc.
4. Open each link **from a sock-puppet Facebook login** to view results (see OpSec).
5. Treat non-returning links as expected — Facebook disabled much of Graph Search in 2019 (see Gotchas).
6. Pivot: photos → reverse-image/face tools; friends → `associate`s; places/check-ins → `geolocation` timeline.

## Inputs → Outputs
- **In:** Facebook numeric ID (derived from `name`/`username`/profile URL)
- **Out:** constructed Facebook query links leading to the target's `social-profile` facets (photos, friends, places)
- **Empty/negative result looks like:** a generated link that opens Facebook but returns nothing — usually because that Graph Search feature was deprecated, the content is privacy-restricted, or you're not logged in; it rarely means the data never existed.

## Gotchas & OpSec
- **Facebook killed classic Graph Search in 2019** — many queries this builds no longer function; the still-useful ones are the direct profile-section links (photos, friends where visible).
- **Active on click**: viewing a target's Facebook is done under your account — always use a sock-puppet, never your real profile.
- Human-in-the-loop: you need a Facebook login to see most results; privacy settings hide much of it.
- The tool only builds URLs — it holds no data of its own.

## Overlaps ("do both")
- Pairs with `[[intelligence-x-person-tools]]` and Facebook-ID lookup utilities — resolve the numeric ID first, use this to fan out queries, and feed photos/associates into reverse-image, face, and people-search tools.

## Trust & verifiability
`trust: community` — a free utility from a reputable OSINT vendor; it merely constructs queries against Facebook, so verify every result on Facebook itself, and expect deprecated features to fail silently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-graph-searcher-intelligencex |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
