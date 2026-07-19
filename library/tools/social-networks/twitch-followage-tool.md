---
id: twitch-followage-tool
name: Twitch Followage Tool
description: Use when you have a Twitch `username` and want the full list of channels that account follows, with follow dates — returns `social-profile` links and a follow timeline.
url: https://streamscharts.com/tools/followage
category: social-networks
path:
- social-networks
bestFor: Pulling every channel a Twitch user follows, with the date each follow started, to map interests and social graph.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The followage lookup is free and needs no account; Streams Charts also sells broader paid analytics, but this tool is not gated.
opsec: passive
opsecNote: Streams Charts reads Twitch's public follow data; the target is not notified and nothing links the query to you. Run from a sock-puppet browser as normal hygiene, but this is a low-risk passive lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Streams Charts is an established third-party streaming-analytics site. Follow data reflects Twitch's public API; accuracy depends on Twitch exposing it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- streamscharts-com
aliases:
- Streams Charts Followage
- Twitch followage
tags:
- Social Media
- Twitch
- social-graph
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Twitch Followage Tool

> A free Streams Charts utility that turns a Twitch username into the complete, dated list of channels that account follows.

## When to use
You have a Twitch `username` for a subject and want to understand their interests and social connections. The list of who they follow — plus when they followed each — can reveal communities, favourite streamers, friends, and a rough activity timeline, all useful for building a picture of an online persona or corroborating identity across platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://streamscharts.com/tools/followage.
2. Enter the target's Twitch `username` in the input box and submit.
3. Read the table: each row is a channel they follow, with follow length (years/months/days) and the "Followed at" date.
4. Sort to extract signal — by "Followed at" (oldest follows hint at early interests), or by follower count (their most-followed / mainstream picks).
5. Pivot: notable followed channels and follow-timing can corroborate an account's owner, link to Discord/other communities, or match a known associate's channel.

## Inputs → Outputs
- **In:** Twitch `username`
- **Out:** dated list of followed channels (`social-profile` links) = interest/social-graph signal
- **Empty/negative result looks like:** no results / "user not found" — the username is wrong or the account's follow list is private/hidden, not proof they follow nothing.

## Gotchas & OpSec
- Depends on Twitch exposing follow data; if the account hides follows or Twitch restricts the endpoint, the list is empty or partial.
- Reflects a moment in time — follows can be added/removed; re-check for changes.
- OpSec: passive, no notification to the target.

## Overlaps ("do both")
- Pairs with `[[streamscharts-com]]` — this tool maps who a user follows; the broader Streams Charts profile covers a channel's own stats, VODs, and audience.

## Trust & verifiability
`trust: community` — a third-party analytics site, not Twitch itself. The follow data is authentic public Twitch data, but treat completeness as best-effort and confirm key links directly on Twitch.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitch-followage-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
