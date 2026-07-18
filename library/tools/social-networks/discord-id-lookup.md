---
id: discord-id-lookup
name: Discord ID Lookup
description: Use when you have a Discord user/snowflake ID (`device-id`) and want the account's public identity — returns `username`, avatar, and exact account-creation timestamp.
url: https://discord.id/
category: social-networks
path:
- social-networks
bestFor: Resolving a raw Discord snowflake ID into a username, avatar, and account age.
selectorsIn:
- device-id
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free, no login. Reads only public data exposed by Discord's API.
opsec: passive
opsecNote: You query discord.id (or Discord's public API via it), never the target's account — the user is not notified and you do not join any server. No sock puppet needed to read, but avoid then messaging/friending the resolved account from an attributable Discord identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Unofficial third-party tool that wraps Discord's public user endpoint. The creation-date decode (baked into the snowflake) is deterministic and reliable; username/avatar reflect live public profile data and can change.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- discord.id
- Discord Snowflake Lookup
tags:
- discord
- id-resolution
- snowflake
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Discord ID Lookup

> Turn a raw Discord snowflake ID into a real identity — username, avatar, and the exact moment the account was created.

## When to use
You have a Discord user ID (an 17–19 digit snowflake, e.g. pulled from a message export, a moderation log, or a leaked database dump) and need to attach a public identity to it. The snowflake encodes the account-creation timestamp, so this both names the account and dates it — useful for judging whether an account is aged/established or freshly made, and for pivoting a bare ID into a username you can chase across platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Enable Developer Mode in Discord (or take the ID from your source) so you have the numeric user ID.
2. Open https://discord.id/ and paste the ID into the lookup field.
3. Read the result: current `username`/global name, avatar image, and the decoded account-creation date/time.
4. Save the avatar and username as pivots — reverse-image the avatar, and run the username through cross-platform account checkers.
5. Pivot: the username feeds username OSINT; the avatar feeds face/image search; the creation date corroborates or contradicts a claimed timeline.

## Inputs → Outputs
- **In:** `device-id` (Discord user/snowflake ID)
- **Out:** `username` (+ global display name), `social-profile` avatar image, account-creation timestamp
- **Empty/negative result looks like:** "user not found" / an error for a malformed or non-user ID (server and message IDs are also snowflakes but resolve differently) — a valid user ID always returns at least the creation date, since that is decoded from the number itself.

## Gotchas & OpSec
- Usernames and avatars are mutable — a match is current-state, not a permanent identifier; the immutable signal is the ID and its creation date.
- A snowflake can be a user, server, message, or channel ID; only user IDs return a profile here.
- Passive to read, but do not friend/DM the resolved account from an attributable identity — that is active and notifies the owner.

## Overlaps ("do both")
- Pairs with other Discord tooling in the [[social-networks]] set and with cross-platform username checkers — this resolves the ID, they spread the resulting username across the rest of the web.

## Trust & verifiability
`trust: community` — an unofficial wrapper around Discord's public API. The creation timestamp is mathematically reliable; treat the live username/avatar as a snapshot to confirm before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-id-lookup |
| category | social-networks |
| selectorsIn → selectorsOut | device-id → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
