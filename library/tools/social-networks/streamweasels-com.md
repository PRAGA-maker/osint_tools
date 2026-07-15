---
id: streamweasels-com
name: streamweasels.com
description: Use when you have a Twitch `username` and want its permanent numeric Twitch user/channel ID — returns the stable `device-id`-style ID that survives display-name changes, for reliable API queries and cross-referencing.
url: https://www.streamweasels.com/tools/convert-twitch-username-%20to-user-id/
category: social-networks
path:
- social-networks
bestFor: Converting a Twitch username to its permanent numeric channel/user ID (which does not change when the streamer renames).
selectorsIn:
- username
selectorsOut:
- device-id
- social-profile
status: live
pricing: free
costNote: Free web tool, no login; it calls the Twitch API server-side to do the lookup.
opsec: passive
opsecNote: The conversion is a public Twitch API read done by StreamWeasels' server; the Twitch user is not notified and nothing is posted. Passive. Your query goes to a third-party site, so use a research browser if attribution matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: StreamWeasels is an established vendor of Twitch/YouTube embed tools; this converter is a widely-referenced free utility. The ID it returns comes straight from Twitch's API, so it is verifiable and reliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- matthewcassinelli-com
- trevorfox-com-2
aliases:
- StreamWeasels Twitch Channel ID Converter
- Twitch username to user ID
tags:
- twitch
- Twitch Related Sites
- id-lookup
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# streamweasels.com — Twitch Channel ID Converter

> Turns a Twitch handle into its permanent numeric channel ID — the stable key you need to keep tracking a streamer through renames and to query the Twitch API.

## When to use
You are following a Twitch account and need its numeric channel/user ID rather than the display handle. Twitch usernames can be changed, but the numeric ID is permanent — pinning it lets you re-find the account after a rename, detect that a "new" channel is the same person, and query Twitch API endpoints (VODs, clips, followers) that require the ID, not the name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the StreamWeasels "Convert Twitch Username to User ID" tool (https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/).
2. Enter the target Twitch `username`.
3. Click **Convert Username to ID** — it queries the Twitch API and returns the numeric channel/user ID.
4. Record the ID as the durable identifier for that account.
5. Pivot: feed the ID into Twitch API queries or third-party Twitch tools (VOD/clip history, follower lists) to reconstruct activity and timelines.

## Inputs → Outputs
- **In:** a Twitch `username`
- **Out:** the account's permanent numeric channel/user ID (a `device-id`-style identifier) and the confirmed `social-profile`
- **Empty/negative result looks like:** a nonexistent or banned/renamed handle returns no ID — if the handle recently changed, you may need the current name; if the account was deleted, no ID resolves.

## Gotchas & OpSec
- Resolves current handles; a since-renamed or deleted account won't map cleanly — capture the ID while the account is live.
- The numeric ID is the durable anchor; the handle is not — always store the ID for longitudinal tracking.
- OpSec: **passive** — a normal Twitch API read via the vendor's server; no notification to the target.

## Overlaps ("do both")
- Same "recover a durable ID from a handle/URL" pattern as `[[matthewcassinelli-com]]` (Mastodon account ID) and `[[trevorfox-com-2]]` (LinkedIn post timestamp) — use whichever matches the platform in hand.

## Trust & verifiability
`trust: community` — an established Twitch-tools vendor; the returned ID comes directly from Twitch's own API, so it is authoritative and independently checkable (you can confirm the same ID via the Twitch API yourself).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | streamweasels-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
