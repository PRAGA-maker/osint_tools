---
id: stalkscan
name: Stalkscan
description: Use when you want to run Facebook Graph-search queries against a profile to surface photos, friends and likes — but the tool is defunct (Facebook removed Graph Search in 2019); historically returned social-profile, image, and associate links.
url: https://www.stalkscan.com
category: social-networks
path:
- social-networks
bestFor: (Historic) Generating Facebook Graph-search URLs to enumerate a profile's photos, friends, likes and interactions.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
- image
- associate
status: down
pricing: free
costNote: Was a free tool by Inti De Ceukelaire. Now offline (the domain no longer resolves), and its whole method died when Facebook removed Graph Search in mid-2019. Recorded so you recognise it and don't chase a dead technique.
opsec: active
opsecNote: When it worked, it built Facebook Graph-search URLs that YOU then opened while logged into Facebook — so queries ran under your account and were attributable. It was a sock-puppet-account activity, never your real profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A well-known and widely-recommended tool in its day (2017–2018), but Facebook's removal of Graph Search made it and every clone non-functional. The domain is now down.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- graph-tips
- intelligencex
- facebook-scanner
aliases:
- stalkscan.com
tags:
- facebook
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Stalkscan

> Once the go-to Facebook Graph-search front-end for enumerating a profile's photos, friends and likes — now **defunct**, because Facebook killed Graph Search in 2019 and the site is offline.

## When to use
Historically: to point at a Facebook profile and generate ready-made Graph-search queries (their photos, their friends' photos, places they've been tagged, pages they like, mutual connections). **This no longer works** — Facebook disabled Graph Search in mid-2019, and the stalkscan.com domain no longer resolves. This entry exists so you recognise the tool, understand why it and its clones are dead, and pivot to what still works on Facebook.

## How to use it (`bestInteractionPattern`: web-manual)
Historic procedure (no longer functional):
1. Paste a Facebook profile URL/ID into stalkscan.com.
2. It produced a menu of Graph-search links (photos of, photos by, friends, likes, places, comments).
3. You opened those links while logged into Facebook to see results.

Today, for the same goals on Facebook:
- Use manual Graph-search-style URL tricks where any still function (`[[graph-tips]]`), and dedicated FB search tools (`[[intelligencex]]`), understanding coverage is far more limited post-2019.
- Fall back to `[[dumpitblue-chromewebstore-google-com]]` to capture what a logged-in sock puppet can already see on the profile.

## Inputs → Outputs
- **In:** `social-profile` (a Facebook profile ID/URL)
- **Out:** `social-profile`, `image`, `associate` (friends/taggers) — historically
- **Empty/negative result looks like:** **always dead now** (domain down). Even the successor Graph-search tricks return far less than Stalkscan once did.

## Gotchas & OpSec
- **Defunct:** Graph Search is gone; no Stalkscan-style tool recovers the old breadth.
- Historically required a logged-in Facebook account — always a sock puppet.
- OpSec: active — queries ran under your account.

## Overlaps ("do both")
- Its spiritual successors — `[[graph-tips]]`, `[[intelligencex]]` — retain a fraction of the capability; combine them and set expectations low.
- Pair with `[[dumpitblue-chromewebstore-google-com]]` to preserve whatever a sock puppet can still view.

## Trust & verifiability
`trust: unverified` — a legitimate, once-celebrated tool now rendered non-functional by Facebook; recorded as **down** for situational awareness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | stalkscan |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile, image, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
