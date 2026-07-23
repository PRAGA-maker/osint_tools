---
id: check-channel-badges
name: Check channel badges
description: Use when you have a Twitch `username` and want to see that channel's custom sub/bit badges — returns `social-profile` corroboration and evidence of a monetised, established channel.
url: https://cactus.tools/twitch/badges
category: social-networks
path:
- social-networks
bestFor: Listing the subscriber and bit-cheer badges configured on a Twitch channel.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool, part of the cactus.tools Twitch utility collection; no account needed.
opsec: passive
opsecNote: Reads Twitch's public badge data via the channel name — you never authenticate or interact with the target, so no signal reaches them. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Twitch tool by "Alex" (cactus.tools); it surfaces public Twitch data, so accuracy tracks Twitch's own API.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cactus.tools twitch badges
tags:
- social-networks
- twitch
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
relatedTools:
- check-twitch-follow-length
- twitch-following
- username-availability
---

# Check channel badges

> A quick lookup of a Twitch channel's custom badges — a small corroboration signal that a handle is a real, established, monetised channel.

## When to use
You have a Twitch `username` and want to confirm the channel exists and gauge its maturity. Custom subscriber-tenure badges and bit-cheer badges indicate an affiliate/partner channel with paying subscribers — useful for corroborating that a handle is genuinely active rather than a fresh throwaway, and for noting badge tiers when comparing accounts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cactus.tools/twitch/badges.
2. Enter the target Twitch channel `username` and click "Check badges".
3. Read the returned badge set — subscriber-month badges, bit badges, and any custom art. A rich badge set = an established, monetised channel; the default/empty set = new or non-affiliate.
4. Pivot: confirmed channel feeds other cactus.tools checks (`[[check-twitch-follow-length]]`, `[[twitch-following]]`) and general username enumeration across platforms.

## Inputs → Outputs
- **In:** `username` (Twitch channel)
- **Out:** `social-profile` corroboration + the channel's configured badge tiers
- **Empty/negative result looks like:** channel not found (invalid handle) or only Twitch's global default badges (channel not affiliate/partner or has no custom badges).

## Gotchas & OpSec
- Badges reflect monetisation status, not identity — a busy channel with no custom badges is still valid.
- It only reads public Twitch data; nothing here confirms the human behind the channel.

## Overlaps ("do both")
- Pairs with `[[check-twitch-follow-length]]` and `[[twitch-following]]` — same-suite tools that add follow-age and following-list context to the same handle.

## Trust & verifiability
`trust: community` — an independent utility surfacing Twitch's own public badge data; reliable as far as Twitch's API is, but adds no identity attribution on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-channel-badges |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
