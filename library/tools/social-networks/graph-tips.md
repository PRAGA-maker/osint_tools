---
id: graph-tips
name: Graph.tips
description: Use when you have a Facebook profile (`name`/`username`/numeric ID) and want to run Graph-Search-style queries on their photos, posts, friends, and check-ins — returns social-profile activity and associates.
url: https://graph.tips/
category: social-networks
path:
- social-networks
bestFor: Building Facebook search queries (photos of, posts by, friends of, places visited) around a target profile.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- associate
- geolocation
status: degraded
pricing: free
costNote: Free and open (by @sowdust). No account of its own; it just generates the Facebook search URLs you run while logged into Facebook.
opsec: active
opsecNote: The generated queries execute inside Facebook under YOUR logged-in session, so Facebook attributes the searches to whatever account you use — always use a well-worn sock-puppet Facebook account, never your real one. The target is not directly notified, but aggressive querying of one profile is visible to Facebook and can trip anti-scraping defenses.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community reconstruction of Facebook Graph Search after Facebook deprecated it in 2019; many query types no longer work, so treat it as partial and often broken.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- graph.tips
- Graph Tips
- Facebook Graph Search
tags:
- facebook
- graph-search
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Graph.tips

> A survivor of the Facebook Graph Search era — a query builder that (partially) reconstructs "show me photos of / posts by / friends of / places visited by" a target profile.

## When to use
You have a Facebook subject — a `name`, `username`, or best of all their numeric profile ID — and want to interrogate their footprint: tagged photos, posts, the friends list, pages liked, places checked into. Even with Facebook's post-2019 restrictions, the queries that still work can surface associates (`associate`), locations (`geolocation`), and images that aren't obvious from the profile page.

## How to use it (`bestInteractionPattern`: web-manual)
1. First get the target's **numeric Facebook ID** (many Graph queries need it, not the vanity username) — a lookup helper or the profile's page source gives it.
2. Open `https://graph.tips/` and pick a query type (photos of, posts by, friends, check-ins, etc.), entering the ID/name.
3. It builds a Facebook search URL — run it **while logged into a sock-puppet Facebook account**.
4. Read what Facebook returns; note that many query types now return nothing (deprecated) — try several.
5. Pivot: friends → associate mapping; check-in places → geolocation/timeline; tagged photos → reverse-image.

## Inputs → Outputs
- **In:** `name` / `username` / numeric Facebook ID
- **Out:** `social-profile` activity, `image` (tagged photos), `associate` (friends), `geolocation` (check-ins)
- **Empty/negative result looks like:** Facebook returns no results for a query — often because that query type was deprecated, or the target's privacy hides it. A null result is weak evidence given how much Graph Search was gutted.

## Gotchas & OpSec
- Degraded: Facebook killed most of Graph Search in 2019; expect many queries to be dead. Don't read absence as fact.
- Human-in-the-loop: queries run under a Facebook login — use a sock puppet; your real account would be attributable and at risk.
- OpSec: **active** — the searching happens inside Facebook as your account.

## Overlaps ("do both")
- Pairs with other Facebook ID/lookup helpers and reverse-image tools — Graph.tips builds the queries; you still need an ID resolver up front and reverse-image to exploit the photos it surfaces.

## Trust & verifiability
`trust: community` — an open community rebuild of a deprecated feature; genuinely useful when a query works, but partial and frequently broken, so verify anything it returns directly on Facebook.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | graph-tips |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image, associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
