---
id: bibliogram-art
name: Bibliogram.art
description: Use when you have an Instagram `username` and want to view their public profile/posts without an Instagram login — but this Bibliogram instance (and the project) is discontinued, so it returns nothing today.
url: https://bibliogram.art/
category: social-networks
path:
- social-networks
bestFor: Historically, viewing public Instagram profiles/posts anonymously via a privacy front-end — no longer functional.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: down
pricing: free
costNote: Was a free open-source front-end; the project is discontinued and public instances (including bibliogram.art) are offline, so there is nothing to use.
opsec: passive
opsecNote: Moot while offline. The historical appeal was anonymity — viewing Instagram without logging in or hitting Instagram directly. That benefit is gone; today anonymous Instagram viewing needs a different route.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Bibliogram was a legitimate open-source Instagram front-end, but the project was discontinued and instances were shut down after Instagram tightened access; this domain no longer serves a working viewer.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bibliogram
- bibliogram.art
tags:
- instagram
- front-end
- defunct
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Bibliogram.art

> A once-popular open-source Instagram front-end for anonymous profile viewing — the project is discontinued and this instance is offline, so it's documented here mainly so you don't waste time on it.

## When to use
Do not reach for this today. Bibliogram was a privacy front-end that let you view public Instagram profiles/posts without an account; the project has been discontinued and public instances (including bibliogram.art) are dead, largely because Instagram clamped down on unauthenticated access. It appears in older OSINT lists — recognize it as defunct and move to a working alternative.

## How to use it (`bestInteractionPattern`: web-manual)
1. The site (https://bibliogram.art/) no longer serves a working Instagram viewer — expect errors/timeouts, not results.
2. There is no functioning way to enter a `username` and get a profile here.
3. Pivot to a live route: a compartmentalized sock-puppet Instagram account for logged-in viewing, current Instagram-viewer front-ends (which also come and go), or reverse-image search on a known profile photo.

## Inputs → Outputs
- **In:** (historically) Instagram `username`
- **Out:** (historically) `social-profile`, post `image`s viewed anonymously
- **Empty/negative result looks like:** the domain is unreachable/erroring — treat any non-result as "tool is dead," and switch methods.

## Gotchas & OpSec
- It's down: don't rely on it, and don't assume a mirror under a new domain is safe or maintained.
- OpSec: the historical value (no Instagram login, no direct hit to Instagram) is exactly what you now have to reconstruct with a sock-puppet account and network isolation.

## Overlaps ("do both")
- Pairs conceptually with other Instagram-viewing front-ends and logged-in sock-puppet browsing — since Bibliogram is gone, those are where anonymous/low-attribution Instagram viewing now happens.

## Trust & verifiability
`trust: unverified` — the project is discontinued and the instance is offline; nothing it would return can be obtained or verified now, so treat it as a dead entry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bibliogram-art |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
