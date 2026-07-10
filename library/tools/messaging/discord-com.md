---
id: discord-com
name: discord.com
description: Use when you have a Discord `username` (or `phone` for verification signals) and want to view the profile, servers and linked accounts — returns a `social-profile` with connections.
url: https://discord.com/
category: messaging
path:
- messaging
bestFor: Working a subject's Discord presence directly — profile, user ID, mutual servers, and linked third-party accounts.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to use; a free account is required to view profiles, join servers, or see connections. Discord Nitro (paid) is unrelated to OSINT use.
opsec: active
opsecNote: Reading a public profile is low-touch, but Discord is inherently interactive — joining the subject's server, sending a friend request, or DMing is ACTIVE and visible to them/admins. Always use a sock-puppet account, never your real one. Your account (and its ID) is visible when you join a shared server.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Discord itself is the authoritative source for its own account data, but all user-generated content (names, bios, connections) is self-reported and can be faked.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Discord
- discord.com
tags:
- discord
- Discord Related Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# discord.com

> The Discord platform itself — where you actually work a subject's account: profile, permanent user ID, mutual servers, and linked third-party accounts (Steam, Spotify, Reddit, etc.).

## When to use
You have a Discord `username`/user ID (or a `phone` and want to test verification signals) and need to investigate the account directly: display name and history, the permanent numeric user ID, avatar, "Connections" to other platforms, and which mutual servers you share. Discord connections in particular can hand you linked accounts on Steam, Reddit, Spotify, Twitch, and more — strong identity pivots. Plan the pivots first with the attack-surface map in `[[osint-github-com]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a **sock-puppet** Discord account at https://discord.com/.
2. Open the target profile (via a shared server or a resolvable user ID): read display name, note the permanent user ID (right-click → Copy ID with Developer Mode on), avatar, and the "Connections" tab for linked platforms.
3. Check mutual servers for context and associates; read their public messages in shared servers.
4. Stay read-only — do not friend, DM, or interact (that's active and attributable).
5. Pivot: linked "Connections" feed `[[sherlock]]`/manual review on those platforms; the avatar feeds reverse-image/face tools; reused handle feeds `[[namechk]]`.

## Inputs → Outputs
- **In:** Discord `username`/user ID (or `phone` for verification-signal testing)
- **Out:** `social-profile` (Discord profile), permanent user ID, avatar, linked "Connections" (other platforms), mutual servers
- **Empty/negative result looks like:** an unresolvable handle, a bare profile with no connections, or no shared servers — the account is private/inactive, or you can't reach it without a mutual server. Handles are non-unique historically; confirm via the numeric ID.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — a Discord account is required; use a puppet.
- OpSec: **active** — joining servers/interacting is visible to the subject and admins, and your account/ID is exposed in shared servers. Stay read-only; never use a real account.
- User-set fields (name, bio, connections) can be faked; the permanent user ID is the reliable anchor.

## Overlaps ("do both")
- Pairs with `[[osint-github-com]]` (Discord attack-surface map — plan the pivots) and `[[sherlock]]`/`[[namechk]]` (spread linked handles) — Discord is the live platform; those structure and extend the investigation.

## Trust & verifiability
`trust: unverified` — Discord is authoritative for its own account data, but everything user-set is self-reported. Anchor identity on the numeric user ID and corroborate connections on their own platforms.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-com |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
