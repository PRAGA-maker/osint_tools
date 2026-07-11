---
id: zesty-facebook-search
name: Zesty Facebook Search
description: Use when you have a Facebook profile `name`/`username` (or numeric profile ID) and want to build Graph-Search-style query URLs to surface a target's photos, friends and tagged content — returns social-profile, image and associate leads.
url: http://zesty.ca/facebook
category: social-networks
path:
- social-networks
bestFor: Constructing Facebook Graph-Search URLs (photos of, friends of, places visited) from a profile ID.
selectorsIn:
- name
- username
- social-profile
selectorsOut:
- social-profile
- image
- associate
status: degraded
pricing: free
costNote: Free single-page helper; no account or payment needed to generate the URLs. The Facebook queries it links to require a logged-in Facebook session to run.
opsec: active
opsecNote: The generator itself is a passive client-side form, but the URLs it produces run searches against Facebook — typically while you are logged in. Use a sock-puppet Facebook account, never your real one, or the target's network graph can surface you as a viewer/searcher.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party helper page hosted on a personal domain (zesty.ca); it stores nothing and only assembles facebook.com URLs, but it is not affiliated with Facebook.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Zesty Facebook Graph Search
- zesty.ca/facebook
tags:
- facebook
- graph-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Zesty Facebook Search

> A one-page URL builder that rebuilds the old Facebook Graph Search syntax — feed it a profile ID and it hands you clickable "photos of X", "friends of X", "places X checked into" links.

## When to use
You have a confirmed Facebook profile (a `username` or, better, the numeric profile ID) for the subject and you want to enumerate their photos, friend/associate graph, tagged locations or interests without manually crafting Graph Search URLs. It turns "I have their profile" into a set of pivot queries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** Facebook account (Graph queries return nothing when logged out).
2. Get the target's numeric profile ID first (Graph queries key off the ID, not the vanity name) — e.g. via `[[lookup-id-com]]` / `findmyfbid`-style tools, or view-source on their profile.
3. Open http://zesty.ca/facebook, paste the ID/username into the relevant field, and pick a query type (photos of, photos liked/commented, friends, places, employers, etc.).
4. Click the generated URL — it opens the search on facebook.com. Read the results as `image`/`associate`/`social-profile` leads.
5. Pivot: friend lists feed `associate` mapping; tagged photos feed reverse-image search (`[[pimeyes-com]]`); check-in places feed `geolocation`.

## Inputs → Outputs
- **In:** `name` / `username` / numeric Facebook profile ID
- **Out:** links that surface `image` (photos of/by the target), `associate` (friends, commenters, tagged people), `social-profile` corroboration
- **Empty/negative result looks like:** the generated Facebook page shows "No results" — since Facebook deprecated much of Graph Search, many query types now return nothing even for real, active profiles. Absence here is NOT evidence the person has no photos/friends.

## Gotchas & OpSec
- **Degraded by design:** Facebook dismantled classic Graph Search around 2019; several query permutations this tool builds no longer work. Treat working queries as a bonus, not a guarantee.
- Human-in-the-loop: you must be logged into Facebook for any query to run — use a research account, never your own.
- OpSec: this is **active** reconnaissance against Facebook. Repeated searches from one account can trip rate limits or friend-suggestion leakage; rotate sock puppets.

## Overlaps ("do both")
- Pairs with a numeric-ID resolver like `[[lookup-id-com]]` because Zesty needs the profile ID to build reliable queries.
- Pairs with `[[pimeyes-com]]` — Zesty finds the photos, reverse face search identifies who else they appear with.

## Trust & verifiability
`trust: community` — a personal-domain helper that only assembles Facebook URLs client-side (nothing is logged), but it is unofficial and its query templates rot as Facebook changes its search backend.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zesty-facebook-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, social-profile → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
