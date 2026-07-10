---
id: facebook-matrix-2
name: The Facebook Matrix
description: Use when you have a Facebook numeric UID or profile (`username`/`name`) and want ready-made search-URL templates to pull photos, friends, places and check-ins — returns social-profile, image and associate links.
url: https://docs.google.com/spreadsheets/d/15dd0qscdydwvtwkc9zfzk1j8rzmvzarxtu9hrm34dnu/edit
category: social-networks
path:
- social-networks
bestFor: A copy-paste cheat-sheet of Facebook graph-search-style URL templates for enumerating a target's photos, friends, likes, places and activity.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free public Google Sheet; no account needed to view. You still need Facebook access (usually a logged-in account) to run most of the URLs.
opsec: active
opsecNote: The spreadsheet itself is passive to read, but the URL templates are executed against Facebook while logged in — Facebook logs those queries and can surface you in "people you may know" to the target. Run every template from a sock-puppet Facebook account on a clean browser/IP, never your real profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community-maintained OSINT reference spreadsheet (widely shared in the OSINT community); techniques degrade as Facebook removes Graph Search endpoints, so some rows may be stale.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Facebook Matrix
- Facebook search matrix
tags:
- facebook
- reference
- cheat-sheet
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# The Facebook Matrix

> A community cheat-sheet of Facebook search-URL templates — plug a target's numeric UID into a row and it returns the photos, friends, places, likes or check-ins that Facebook's own UI hides.

## When to use
You have a Facebook target — ideally their numeric user ID (UID), or at least a profile/`name` you can resolve to one — and you want to systematically enumerate their footprint: photos they're tagged in, mutual friends, places visited, pages liked, comments made. Facebook removed most of Graph Search from its UI, but many underlying URL patterns still work; this spreadsheet collects them so you don't have to remember the syntax.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Google Sheet (read-only) at the URL.
2. Resolve your target to a numeric UID first (via a UID-lookup tool or `findmyfbid`-style service) — most templates key off the UID, not the vanity name.
3. Copy a template row (e.g. "photos of", "friends", "places visited", "videos tagged"), substitute the UID, and open the resulting URL in a **logged-in sock-puppet** Facebook session.
4. Read the results — tagged `image`s, `associate` friend lists, visited `places`/geolocation, liked pages.
5. Pivot: friends become new `name`/UID leads; place/check-in data feeds geolocation; tagged photos feed reverse-image search.

## Inputs → Outputs
- **In:** Facebook numeric UID (from a `username`/`name`)
- **Out:** `social-profile` (activity views), `image` (tagged photos), `associate` (friends/interactions), plus places/check-ins
- **Empty/negative result looks like:** a template that returns nothing or an error page — often because Facebook has deprecated that endpoint or the target's privacy settings block it, NOT proof the data doesn't exist.

## Gotchas & OpSec
- **Decaying techniques:** Facebook continually removes Graph Search endpoints; expect a fraction of rows to be dead and cross-check with other Facebook tools.
- Requires the numeric UID for most rows — resolve it first.
- **Active OpSec:** you're querying Facebook while logged in. Always use a puppet account; a real account risks exposing you to the target via mutual-connection algorithms.

## Overlaps ("do both")
- Pairs with UID-lookup tools and `[[graph-tips-fb-search]]`-style Facebook search builders — those generate individual queries, while this is the broad menu; use a UID resolver first, then this matrix, then verify hits.

## Trust & verifiability
`trust: community` — a crowd-maintained reference, accurate when written but subject to Facebook's changes; treat empty results as "endpoint may be dead", and confirm findings directly on the profile where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-matrix-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
