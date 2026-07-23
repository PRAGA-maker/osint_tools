---
id: username-availability
name: Username Availability
description: Use when you have a `username` and want to know if it's claimed/held on Twitch (including by suspended or deleted channels) — returns a taken/available signal.
url: https://cactus.tools/twitch/username
category: social-networks
path:
- social-networks
bestFor: Checking whether a Twitch handle is claimed, including by suspended or deleted channels that Twitch's own search hides.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free, no account needed; rate-limited to ~20 lookups/minute.
opsec: passive
opsecNote: "You query cactus.tools, not Twitch's account for the subject, so the target is not contacted or notified. cactus.tools logs your lookups; use a sock-puppet session if the handle you're checking is sensitive."
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Unofficial third-party Twitch tool (cactus.tools); it reads Twitch's public API for handle status and is not affiliated with Twitch. As of its own site notice it has intermittently reported the checker as non-functional, hence status degraded.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- check-channel-badges
- check-twitch-follow-length
- twitch-following
aliases:
- cactus.tools Twitch username
- Twitch username availability
tags:
- twitch
- username-check
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Username Availability

> An unofficial Twitch handle checker that reports whether a `username` is claimed — and, unlike Twitch's search box, flags handles held by suspended or deleted channels.

## When to use
You have a candidate `username` and want to know if it exists on Twitch. Its edge over just visiting `twitch.tv/<name>` is that it surfaces handles that are *claimed but not publicly searchable* — suspended, banned, or deleted channels, and previous-partner reservations — which matters when you're checking whether a subject once held a handle. It is a narrow, single-platform check, so missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cactus.tools/twitch/username in a sock-puppet browser.
2. Enter the `username` (4–25 chars, alphanumeric/underscore, must start with a letter or number).
3. Read the availability signal: "unavailable/taken" means the handle is claimed (possibly by a hidden/suspended channel); "available" means no channel currently holds it.
4. Cross-check a "taken" result by opening `twitch.tv/<username>` directly — if that 404s but this says taken, the channel is likely suspended/deleted.
5. Pivot a confirmed handle into the sibling tools for channel details.

## Inputs → Outputs
- **In:** `username`
- **Out:** taken/available status; corroborates existence of a `social-profile` on Twitch (incl. hidden channels)
- **Empty/negative result looks like:** "available" — the handle is unclaimed on Twitch. Note this is availability, not identity: a taken handle isn't necessarily your subject's.

## Gotchas & OpSec
- **Status is degraded:** cactus.tools has posted notices that the checker is intermittently non-functional. If it errors or stalls, fall back to visiting the Twitch URL directly.
- Rate-limited (~20/min); it reflects Twitch's public data, so a handle freed and re-registered will read accordingly.
- Unofficial tool — treat a lone signal as a lead and confirm on Twitch itself.

## Overlaps ("do both")
- Pairs with the same-provider cactus.tools suite — [[check-channel-badges]], [[check-twitch-follow-length]], [[twitch-following]] — which enrich a confirmed handle with channel/follower detail once this establishes the handle exists.

## Trust & verifiability
`trust: community` — a useful but unofficial, intermittently-down third-party tool. Always confirm a "taken" result against Twitch directly, since suspended-channel detection is exactly where an unofficial reader can drift out of date.
