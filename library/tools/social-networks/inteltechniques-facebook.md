---
id: inteltechniques-facebook
name: IntelTechniques Facebook Tool
description: Use when you have a Facebook `username`/`social-profile` or numeric ID and want to run structured Facebook lookups (ID resolution, friend/photo/post searches) from one query-builder — returns `social-profile` links and Facebook search URLs.
url: https://inteltechniques.com/tools/Facebook.html
category: social-networks
path:
- social-networks
bestFor: A pre-built panel of Facebook search shortcuts (resolve profile↔numeric ID, then query friends, photos, posts, places, likes) that assembles the URLs Facebook no longer exposes.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free tool by Michael Bazzell / IntelTechniques. Note the online tools have been retired/moved before and are now distributed mainly as an offline HTML download; availability of the hosted page varies.
opsec: active
opsecNote: The generated links execute inside your logged-in Facebook session, so results and profile visits are tied to whatever account you use. Use a sock-puppet Facebook account and browser profile — never your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Michael Bazzell (IntelTechniques), a well-known OSINT author. It is a query-builder — the data comes from Facebook, not IntelTechniques — and Facebook changes frequently break individual queries.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- IntelTechniques Facebook search
- Bazzell Facebook tool
tags:
- facebook
- social-networks
- xray-search
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# IntelTechniques Facebook Tool

> Michael Bazzell's Facebook search panel: paste a profile or numeric ID and it builds the friend/photo/post/place queries Facebook killed off in its own UI.

## When to use
You have a Facebook `username` or profile URL (`social-profile`) and want to go deeper than Facebook's search box allows — resolve the account to its stable numeric ID, then enumerate friends, tagged photos, posts, check-ins/places, and likes via pre-built query links. Reach for it when mapping a subject's Facebook footprint and network in a missing-person or identity investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the tool — either the hosted page at https://inteltechniques.com/tools/Facebook.html or, more reliably, the offline HTML tools package Bazzell distributes (the online versions have been retired before).
2. Log into a **sock-puppet** Facebook account in a clean browser profile (the generated links only work while authenticated).
3. First resolve the target to a **numeric Facebook ID** (the tool has a username→ID field); many downstream queries need the numeric ID, not the vanity handle.
4. Use the ID in the panel's query fields — friends, photos of, photos by, posts, places visited, pages liked — each button opens the corresponding Facebook search URL in your session.
5. Read the results on Facebook; record the numeric ID as your durable reference.
6. Pivot: friends list → `associate` graph; tagged photos → face/reverse-image; check-ins → geolocation.

## Inputs → Outputs
- **In:** `username`/`social-profile` (Facebook handle or URL), or numeric ID
- **Out:** `social-profile` (resolved profile, friends, photo/post/place result pages), the stable numeric ID
- **Empty/negative result looks like:** a Facebook "no results" page or a query link that lands on a generic search — because Facebook constantly changes its internals, some panel queries are dead at any given time. Empty means "this query shape is broken/blocked today," not "nothing exists."

## Gotchas & OpSec
- **Facebook breakage:** individual queries (friends, some photo searches) frequently stop working as Facebook changes its backend — expect partial functionality and try multiple approaches.
- The hosted page may be **retired**; the offline download is the resilient option.
- OpSec: **active** — every query runs in your Facebook session and every profile you open is a logged visit. Puppet account only.

## Overlaps ("do both")
- Overlaps heavily with `[[facebook-search-2]]` (SowSearch) — both build Facebook queries; run both since they break in different places.
- Feed the resolved numeric ID and photos into reverse-image/face tools and friend-graph mapping.

## Trust & verifiability
`trust: community` — from a respected OSINT author, but it's a query-builder over Facebook's own (fast-changing, partly broken) search; verify every hit directly on Facebook.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-facebook |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
