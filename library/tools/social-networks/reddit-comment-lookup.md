---
id: reddit-comment-lookup
name: Reddit Comment Lookup
description: Use when you have a Reddit `username` and want to search that account's comment history (by keyword or in bulk) to profile interests, location tells, and associates — returns social-profile, associate, geolocation leads.
url: https://randomtools.io/reddit-comment-search/
category: social-networks
path:
- social-networks
bestFor: Keyword-searching or bulk-reading a Reddit user's comment history to build a behavioural profile.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- geolocation
status: live
pricing: free
costNote: Free to use, unlimited queries per the site; no account required.
opsec: passive
opsecNote: Reads Reddit's public comment data via the site, not through your own logged-in Reddit account, so the target sees nothing. Still use a sock-puppet browser; the tool operator can log which usernames you probe.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free third-party utility (randomtools.io) that queries recent/cached Reddit data, not live — so it can miss the newest comments and deleted content; corroborate against Reddit directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Reddit comment search
- randomtools reddit search
tags:
- reddit
- social-search
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- find-my-facebook-id
---

# Reddit Comment Lookup

> A free keyword-and-username search over Reddit comment history — mine a target's comments for the location tells, routines, and connections a profile page hides.

## When to use
You have a Reddit `username` and want to read or keyword-search everything they've commented — Reddit users routinely leak their city, employer, schedule, relationships, and interests in comment threads that the profile view buries. Use it to build a behavioural picture, find self-disclosed `geolocation` clues, and surface subreddits/users they interact with (`associate`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://randomtools.io/reddit-comment-search/ in a clean/sock-puppet browser.
2. Enter the Reddit `username`. Either add keywords (e.g. a city name, employer, "I live", "my wife") to target disclosures, or leave keywords blank to pull the full comment history.
3. Read the returned comments; note self-disclosures of place, work, relationships, and the subreddits they frequent.
4. Cross-check anything important against the live profile at `reddit.com/user/<username>` — the tool uses recent/cached data and can lag or miss deletions.
5. Pivot: subreddit patterns and named `associate`s feed further Reddit/social OSINT; a stated city/employer feeds people-search.

## Inputs → Outputs
- **In:** `username` (+ optional keywords)
- **Out:** matching comments → `geolocation`/interest/`associate` disclosures, confirmation of an active `social-profile`
- **Empty/negative result looks like:** no comments returned — could mean a comment-light or shadowbanned account, a typo'd username, or data the cache hasn't picked up; confirm on Reddit directly.

## Gotchas & OpSec
- Uses recent/cached data, not live — newest comments and deleted ones may be absent; always verify key finds on Reddit itself.
- Self-disclosed location/employment is a claim, not proof — corroborate before relying on it.
- OpSec: passive; run through your own logged-out session, not the target's, and use a throwaway browser.

## Overlaps ("do both")
- Pairs with Reddit-native history viewers and [[redective]]-style Reddit analytics, and with username-enumeration tools that carry the handle to other platforms.

## Trust & verifiability
`trust: community` — a free community utility surfacing genuine public Reddit comments; the comments are real, but its cached index can lag, so treat gaps as inconclusive and verify against live Reddit.
