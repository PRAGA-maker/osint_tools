---
id: mediamister-com
name: mediamister.com (Find Instagram User ID)
description: Use when you have an Instagram `username` and want its permanent numeric user ID — returns the stable numeric ID that survives username changes.
url: https://www.mediamister.com/find-instagram-user-id
category: social-networks
path:
- social-networks
bestFor: Converting an Instagram @username into its numeric user ID (the stable identifier for scrapers and archive tools).
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: 100% free; no account or purchase, limited to ~10 lookups per day. (MediaMister sells growth services, but this ID tool is free.)
opsec: passive
opsecNote: The lookup runs server-side against Instagram's public data — searches are anonymous and the target is not notified. No login required; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free utility from a social-growth vendor; the numeric ID it returns is Instagram's real identifier and is accurate at time of query.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MediaMister Instagram User ID
- Find Instagram User ID
tags:
- instagram
- Instagram Related Sites
- user-id
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# mediamister.com (Find Instagram User ID)

> Turns an Instagram @username into its permanent numeric user ID — the stable identifier that keeps tracking an account even after it's renamed.

## When to use
You have an Instagram `username` and need its numeric user ID: the handle can change, but the numeric ID never does, so it lets you keep an account under surveillance after a rename and lets you feed ID-keyed scrapers, anonymous viewers, and archive tools. A quick, free first step in Instagram OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mediamister.com/find-instagram-user-id.
2. Paste the target Instagram username and submit (up to ~10/day).
3. Read the returned numeric user ID.
4. Pivot: use the ID with Instagram scrapers/OSINT tools that require IDs, anonymous story viewers, and any tool that must survive a username change; cross-reference against the handle's public profile.

## Inputs → Outputs
- **In:** Instagram `username`
- **Out:** numeric Instagram user ID (`social-profile` identifier)
- **Empty/negative result looks like:** "not found"/error — the handle is wrong, deleted, or banned. A miss isn't proof of no account; check spelling and variants. Private accounts still resolve to an ID (you just can't see their content here).

## Gotchas & OpSec
- ~10 lookups/day free-tier cap.
- Returns the ID only — not posts, followers, or owner identity.
- Passive; anonymous; no notification to the target.

## Overlaps ("do both")
- Pairs with `[[commentpicker-com-2]]` (TikTok IDs) and Instagram scrapers/anonymous viewers — this supplies the stable numeric ID those consume; the viewers then pull the actual content.

## Trust & verifiability
`trust: community` — a free vendor utility surfacing Instagram's own identifier. The numeric ID is authoritative; confirm the account is your subject via its public content, not the handle alone.
