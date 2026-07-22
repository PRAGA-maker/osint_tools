---
id: commentpicker-com-2
name: commentpicker.com (TikTok ID Finder)
description: Use when you have a TikTok `username` and want its permanent numeric user ID plus account stats — returns the numeric ID, account creation date, follower/video counts, and username-change date.
url: https://commentpicker.com/tiktok-id.php
category: social-networks
path:
- social-networks
bestFor: Converting a TikTok @username into its stable numeric user ID and pulling account metadata (creation date, counts).
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free tool; no account required for the TikTok ID lookup.
opsec: passive
opsecNote: The lookup runs server-side against TikTok's public data — the target is not notified and never sees you. No login needed; standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely used free giveaway/utility site; the TikTok ID/stat data it returns comes from TikTok's public endpoints and is generally accurate at time of query.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- CommentPicker TikTok ID Finder
- TikTok User ID Finder
tags:
- tiktok
- TikTok Related Sites
- user-id
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- commentpicker-com
- find-my-facebook-id-2
- instagram-user-id
- youtube-channel-id
---

# commentpicker.com (TikTok ID Finder)

> Turns a TikTok @username into its permanent numeric user ID — the stable identifier that survives username changes — plus account creation date and stats.

## When to use
You have a TikTok `username` and need its underlying numeric user ID: unlike the handle, the numeric ID never changes, so it lets you keep tracking an account even after the subject renames it, and lets you correlate the account across tools/APIs that key on IDs. The account creation date and username-change date are also strong identity/timeline signals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://commentpicker.com/tiktok-id.php.
2. Enter the target TikTok username (with @) and run the lookup.
3. Read the output: numeric user ID, account creation date, follower/following/video/like counts, and last username-change date.
4. Pivot: use the numeric ID with TikTok scrapers/APIs and archive tools that require an ID; use the creation/username-change dates to corroborate identity and build a timeline.

## Inputs → Outputs
- **In:** TikTok `username`
- **Out:** numeric user ID (`social-profile` identifier), account creation date, follower/video counts, username-change date
- **Empty/negative result looks like:** "user not found" or an error — the handle is wrong, the account is deleted/banned, or private-restricted. A miss isn't proof the person has no TikTok; check handle spelling and variants.

## Gotchas & OpSec
- Only resolves public accounts; deleted/banned handles won't resolve.
- Stats are point-in-time snapshots, not history.
- Passive; no login or notification to the target.

## Overlaps ("do both")
- Pairs with TikTok scraper/quick-search tools — this gives the stable numeric ID those tools consume, and the creation date to anchor a timeline.

## Trust & verifiability
`trust: community` — a free utility surfacing TikTok's own public data. The numeric ID is authoritative; verify the account is your subject by its content, not the handle alone.
