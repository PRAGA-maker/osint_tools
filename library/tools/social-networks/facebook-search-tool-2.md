---
id: facebook-search-tool-2
name: Facebook Search Tool
description: Use when you have a Facebook profile `username`/ID or a `name` and want to run advanced Graph-style queries (photos-of, photos-by, places, connections) — returns social-profile, image, and associate leads.
url: https://netbootcamp.org/facebook.html
category: social-networks
path:
- social-networks
bestFor: Building advanced Facebook Graph-search URLs from a profile ID to surface tagged photos, places, and connections that keyword search hides.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free web-based query builder from NetBootcamp; no payment. You must supply your own logged-in Facebook account to execute most generated queries.
opsec: active
opsecNote: The builder itself is passive, but every generated link opens inside Facebook under YOUR logged-in session — Facebook logs the query and it can surface you in the target's "people you may know". Always run generated queries from a dedicated sock-puppet Facebook account, never a real/attributable one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing OSINT training resource by Bob Brasich (NetBootcamp); it only assembles Facebook's own search URLs, so results come from Facebook, not a third-party scraper.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- find-facebook-id
- netbootcamp-org-websitetool-html
- netbootcamp-s-people-tool
aliases:
- NetBootcamp Facebook Search
- Facebook Graph Search Tool
tags:
- facebook
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Facebook Search Tool

> NetBootcamp's web form that assembles advanced Facebook Graph-search URLs from a numeric profile ID, reaching connections that Facebook's keyword box no longer exposes.

## When to use
You have a target's Facebook numeric profile ID (or a `username`/`name` you can resolve to one) and want to pivot into their graph: photos they are tagged in, photos they uploaded, places they visited, pages/groups they interact with, and friends/associates. Standard Facebook search only does keyword matching; this tool reconstructs the older Graph-search syntax (`/photos-of/`, `/photos-by/`, `/places-visited/`, etc.) so you can query relationships directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. First obtain the target's numeric Facebook ID (a vanity handle won't work for graph queries) — resolve it with [[find-facebook-id]] if you only have the profile URL.
2. Open https://netbootcamp.org/facebook.html and paste the numeric ID into the relevant field.
3. Pick the query type (photos of the person, photos by them, places, friends, etc.); the tool builds the corresponding facebook.com Graph URL.
4. Click through while logged into a **sock-puppet** Facebook account — most graph queries require an active session to return results.
5. Read the output on Facebook: tagged/uploaded `image`s, visited `places` (geolocation leads), and `associate` connections. Save/screenshot before Facebook rate-limits you.

## Inputs → Outputs
- **In:** Facebook numeric ID (from a `username`/`name`)
- **Out:** `social-profile` context, tagged/uploaded `image`s, `associate` connections and place/geolocation leads
- **Empty/negative result looks like:** Facebook returns "no results" or a blank graph page — often because the account's privacy settings block that graph dimension, not because the person is inactive. Try a different query type before concluding.

## Gotchas & OpSec
- Facebook has deprecated much of classic Graph search; some generated queries return nothing regardless of the target — this is a Facebook-side limitation, not a tool failure.
- Human-in-the-loop: you must be logged into Facebook. This is the OpSec-critical step — use a burner account, never your own.
- OpSec: **active** once you click through; Facebook logs the viewing account and may feed it into "people you may know" for the target.

## Overlaps ("do both")
- Pairs with [[find-facebook-id]] because that tool converts a vanity URL into the numeric ID this tool needs as input; run them in sequence.

## Trust & verifiability
`trust: community` — a well-known OSINT-trainer utility that only constructs Facebook's own URLs. Any result you see is served by Facebook itself, so verifiability is high; the tool adds no data of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-search-tool-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
