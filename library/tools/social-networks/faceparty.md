---
id: faceparty
name: FaceParty
description: Use when you have a `name` or `username` possibly tied to an older UK internet user and want to check for a legacy FaceParty profile — returns `social-profile`, photos, and stated interests.
url: https://www.faceparty.com
category: social-networks
path:
- social-networks
bestFor: Checking one of the UK's oldest social/dating networks for a legacy profile under a name or handle.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: degraded
pricing: free
costNote: Free to browse and register a basic profile; some contact/messaging features have historically been paid. It is a legacy niche network with a small, aging user base.
opsec: active
opsecNote: Viewing member profiles may require a logged-in account, and browsing/messaging can be visible to members. Register and browse only from a sock-puppet account with disposable email; never use an attributable identity on a live dating-style site.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running but niche UK social/dating site with a controversial history; still resolving as live but low-traffic, so profile coverage is thin and identity claims are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Faceparty
tags:
- toddington
- curated-directory
- social-media
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# FaceParty

> One of the UK's oldest social/dating networks (est. 2000) — a long-tail place to check for a legacy profile under an older name or handle.

## When to use
You have a `name` or `username` for someone who was an active UK internet user in the 2000s and you want to check for a legacy FaceParty profile — old photos, stated age/interests, and handle reuse that can bridge to other platforms. Best treated as a long-tail, low-yield check for older subjects, not a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.faceparty.com in a sock-puppet browser.
2. Use Browse Members / search by the target `username` or `name` (registration with a disposable account may be required to view profiles).
3. Read any matching profile for photos (`image`), stated age/location, and interests.
4. Pivot: reuse a distinctive handle across `[[whatsmyname-python]]`/`[[spy]]`; feed profile photos into reverse image / face search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (FaceParty profile), `image` (profile photos), stated demographics/interests
- **Empty/negative result looks like:** no matching member — likely because the person never used FaceParty or the small, aging user base simply doesn't include them. Given the network's low traffic, absence here means very little.

## Gotchas & OpSec
- Legacy, low-traffic network with a controversial past (notably purging over-36 users in 2008) — coverage is thin and skewed to older UK users.
- Profile viewing/messaging can require login and be visible to members — active footprint; always sock-puppet.
- Identity claims are self-reported and unverified.

## Overlaps ("do both")
- Pairs with other legacy-network checks (`[[myspace-com]]`, Bebo/Friends Reunited archives) and username sweeps — old handles reused across these are strong cross-links for an older subject.

## Trust & verifiability
`trust: unverified` — a niche legacy site with self-reported profiles. Any hit is a lead to corroborate elsewhere, not evidence on its own.
