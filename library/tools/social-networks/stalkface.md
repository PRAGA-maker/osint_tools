---
id: stalkface
name: StalkFace
description: Use when you have a Facebook `social-profile` (or numeric ID) and want prebuilt Facebook Graph-search queries for their photos, activity and connections — returns social-profile and image links.
url: https://stalkface.com/en/
category: social-networks
path:
- social-networks
bestFor: Generating ready-made Facebook Graph-search URLs (photos of, posts by, places visited) for a given profile.
selectorsIn:
- social-profile
- name
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free query generator; no account on StalkFace itself, but the generated links must be run while logged into Facebook.
opsec: active
opsecNote: StalkFace only builds URLs, but running them requires you to be logged into Facebook, and those searches execute against Facebook under YOUR account — attributable, and Facebook logs the activity. Use a sock-puppet Facebook account, never your real one. Do not send friend requests or interact.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party query builder for Facebook Graph search. Facebook deprecated much of Graph search in 2019, so many generated queries no longer return results; treat it as hit-or-miss.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Stalk Face
- stalkface.com
tags:
- facebook
- graph-search
- profile-investigation
source: osintambition-social
lastVerified: '2026-07-11'
enrichment: full
---

# StalkFace

> A Facebook Graph-search query builder — paste a profile and it generates the "photos of / posted by / visited" search URLs you'd otherwise hand-craft.

## When to use
You have a Facebook `social-profile` (ideally the numeric user ID) and want to pull structured views of their activity — photos they're tagged in, posts they authored, places they've checked into, and mutual connections — using Facebook's own Graph-search syntax without composing the URLs manually. Best treated as a convenience wrapper; because Graph search is heavily curtailed, verify each query actually returns data.

## How to use it (`bestInteractionPattern`: web-manual)
1. First get the target's numeric Facebook ID (many Graph queries need the ID, not the vanity name) — resolve it with an ID-lookup tool.
2. Open https://stalkface.com/en/ and enter the profile URL/ID.
3. It generates a set of clickable queries (photos-of, photos-by, posts, likes, places, friends, etc.).
4. Log into a **sock-puppet** Facebook account, then click a generated query. Read whatever Facebook returns.
5. Pivot: tagged photos feed reverse-image search and face work; check-in places feed geolocation; mutual friends feed the associate graph.

## Inputs → Outputs
- **In:** Facebook `social-profile` / numeric ID (optionally a `name`)
- **Out:** `social-profile` connections and `image` (tagged photo) result sets via Graph-search URLs
- **Empty/negative result looks like:** the generated query opens Facebook to an empty results page — expected for many query types since the 2019 deprecation; not proof the data doesn't exist, just that Graph search won't surface it.

## Gotchas & OpSec
- **Degraded:** Facebook removed most Graph-search capabilities in 2019; a large share of StalkFace's queries now return nothing. Don't interpret empty results as fact.
- Human-in-the-loop: queries only work while logged into Facebook — **use a sock-puppet account**, as the searches are attributable and logged.
- Privacy settings gate everything: a locked-down profile yields little regardless of query.

## Overlaps ("do both")
- Pairs with `[[app-fanpagekarma-com]]` and an ID-resolver — resolve the numeric ID first, use Fanpage Karma to find Pages, and StalkFace to probe an individual profile's tagged content.

## Trust & verifiability
`trust: unverified` — a third-party query builder with no guarantees; its usefulness is bounded by Facebook's shrinking Graph search and the target's privacy settings. Verify every query returns real data before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stalkface |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, name → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
