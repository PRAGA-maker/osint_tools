---
id: sowdust-fb-search
name: Sowdust FB search (SOWsearch)
description: Use when you have a `name`/`username` and want to build Facebook search URLs for people, posts, photos-by-location and mutual friends — returns Facebook profiles, images and associates, no FB login to build the query.
url: https://sowdust.github.io/fb-search
category: social-networks
path:
- social-networks
bestFor: Constructing precise Facebook graph-search query URLs (people, posts, photos by location, mutual friends) without Facebook's native search.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Completely free and open-source; building the query needs no account, though opening the resulting Facebook search may prompt a Facebook login.
opsec: active
opsecNote: The query builder itself is passive and needs no login, but executing the generated URL runs the search on Facebook under whatever session you have. Use a sock-puppet Facebook account/browser; Facebook logs the search and any profile you open.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project by @sowdust; cited across multiple OSINT lists. Now redirects from the old GitHub Pages URL to sowsearch.info. Dependent on Facebook's current, shifting search behaviour.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SOWsearch
- sowsearch.info
- Facebook graph search
tags:
- facebook
- graph-search
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Sowdust FB search (SOWsearch)

> @sowdust's Facebook query builder — enter what you're looking for and it generates the exact Facebook search URL for people, posts, photos-by-location, videos, events and mutual friends. Now hosted at **sowsearch.info**.

## When to use
You have a `name`/`username` and want to filter Facebook the way native search won't let you: people by city/school/employer/mutual-friends, photos by uploader or by location, posts containing a keyword within a date range, or events at a place. It shows you *how* the query is constructed (educational) and hands you a ready URL — ideal when you want repeatable, tweakable Facebook searches for a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool — it now lives at https://sowsearch.info (the old `sowdust.github.io/fb-search` redirects there).
2. Choose the search type (People, Posts, Photos, Videos, Events, Pages, Top) and fill the optional filters (city, school, employer, mutual friends, location, date range).
3. The tool builds the corresponding Facebook search URL; open it (in a sock-puppet Facebook session) to see results.
4. Pivot: profiles → associate mapping; location-tagged photos → geolocation; keyword posts → activity timeline.

## Inputs → Outputs
- **In:** `name` / `username` (+ city, school, employer, mutual friends, location, date)
- **Out:** `social-profile` (Facebook profiles/pages), `image` (photos by uploader/location), `associate` (mutual friends, co-tagged people)
- **Empty/negative result looks like:** Facebook returning nothing, a login/permission wall, or trimmed results — often a reflection of Facebook's tightened graph-search, not true absence. Adjust filters and retry.

## Gotchas & OpSec
- Building the URL is safe and login-free, but **running** it queries Facebook under your session — use a sock puppet (`account-login` human-in-loop), never your real account.
- Facebook regularly changes which query patterns still resolve; expect some search types to break intermittently.
- Author's caution: don't paste ID values from untrusted sources.

## Overlaps ("do both")
- Pairs with [[graph-tips-fb-search]] (graph.tips, same author) — run both; when Facebook breaks one query style the other often still works, and they expose slightly different filter sets.

## Trust & verifiability
`trust: community` — a well-regarded open-source tool, but it only generates queries against Facebook; the data and its completeness are Facebook's. Confirm every hit on the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sowdust-fb-search |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
