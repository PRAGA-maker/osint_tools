---
id: facebook-matrix
name: Facebook Matrix
description: Use when you have a Facebook numeric ID (user/page/place) and want to run advanced graph-style searches — returns URL/JSON formulas that surface friends, photos, posts, and tagged locations.
url: https://plessas.net/facebookmatrix
category: social-networks
path:
- social-networks
- facebook
bestFor: A reference of Facebook search formulas that turn a numeric ID into friend lists, photos, and location-tagged content.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: degraded
pricing: free
costNote: Free reference page; the techniques themselves need a (sock-puppet) Facebook login to run.
opsec: active
opsecNote: The formulas are just constructed URLs, but running them means browsing Facebook while logged in — which ties your account to the searches and can surface you to targets. Facebook has also killed or throttled many graph-search endpoints, so some formulas simply no longer return results. Always run from a sock-puppet account, never your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-maintained, widely-cited reference by Henk van Ess / Plessas of Facebook search techniques; the reference is authoritative, but Facebook's own changes mean not every formula still works.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- The Facebook Matrix
- Plessas Facebook Matrix
tags:
- facebook
- graph-search
- url-technique
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Facebook Matrix

> A maintained cheat-sheet of Facebook search "formulas" — recipes for building the search URLs (often via Base64-encoded JSON) that dig past Facebook's neutered search bar to reach friends, photos, posts, and places tied to a numeric ID.

## When to use
You have a Facebook numeric ID (user, page, group, or place — get it from `[[facebook-photos-by-id]]`, socid-extractor, or a lookup) and want to pull relationships and content Facebook's normal search won't give you: who someone's friends are, photos they're in, posts by/about them, content tagged at a location, or live streams from a place. Reach for it whenever a Facebook investigation stalls at the profile and you need the graph around it — recognizing that Facebook has broken some of these paths over time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://plessas.net/facebookmatrix and find the formula for what you want (e.g. "photos of user X", "friends of X", "posts at place Y").
2. Obtain the required numeric ID(s) for the target.
3. Build the search string per the formula — several require converting a JSON snippet to Base64 and inserting it (plus the ID) into a Facebook search URL.
4. Run it from a **sock-puppet Facebook login**. Read whatever the graph returns.
5. Pivot: friend lists → `associate`s; photos → reverse-image/face; tagged places → `geolocation`.

## Inputs → Outputs
- **In:** a Facebook numeric ID derived from a `username`/`name`/profile
- **Out:** `social-profile` connections, `image`s, `associate`s (friends), tagged locations/posts
- **Empty/negative result looks like:** the formula returns nothing or an error page — often because **Facebook deprecated that endpoint**, not because the target has no such data. Try a different formula and confirm the ID is correct before concluding.

## Gotchas & OpSec
- Human-in-the-loop: requires a **logged-in Facebook session** — use a sock puppet.
- OpSec: **active** — logged-in graph searches tie to your account and can surface you; never use your real identity.
- **Reliability is uneven** (`status: degraded`): Facebook has removed/limited many graph-search features since 2019, so treat the matrix as a menu of things to try, not guaranteed queries.

## Overlaps ("do both")
- Pairs with `[[facebook-photos-by-id]]` (resolve/collect IDs) and reverse-image/face tools — the matrix expands one ID into the surrounding graph; those confirm identity of what it surfaces.

## Trust & verifiability
`trust: trusted` — an authoritative, well-maintained technique reference; the caveat is entirely Facebook's own endpoint changes, so verify each formula still returns data rather than assuming.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-matrix |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
