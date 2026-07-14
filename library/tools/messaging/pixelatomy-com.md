---
id: pixelatomy-com
name: Snow Stamp (Discord Snowflake → Timestamp)
description: Use when you have a Discord ID (`document-id` snowflake from a user, message, or channel) and want its exact creation date/time — returns the decoded UTC timestamp.
url: https://pixelatomy.com/snow-stamp/
category: messaging
path:
- messaging
bestFor: Decoding a Discord snowflake ID into the precise UTC creation timestamp of the account, message, or channel it belongs to.
selectorsIn:
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free browser tool; no account, no payment.
opsec: passive
opsecNote: Fully client-side/offline math — the snowflake is decoded locally and nothing is sent to Discord or the subject. No account or query is logged against the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple deterministic converter (Discord snowflakes embed a millisecond timestamp since the Discord epoch); the math is exact and verifiable, so results are reliable regardless of who hosts the page.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- regdatebot
aliases:
- Snow Stamp
- Discord snowflake to timestamp
- pixelatomy.com
tags:
- discord
- Discord Related Sites
- snowflake
- timestamp
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Snow Stamp (Discord Snowflake → Timestamp)

> A one-field converter that decodes a Discord snowflake ID into the exact UTC moment it was created — because every Discord ID embeds its own creation timestamp.

## When to use
You have a Discord `document-id` — a user ID, message ID, or channel ID (an 18–19 digit snowflake) — and want to know precisely when that object was created. Account creation dates help judge whether a persona is old or freshly minted; message/channel timestamps help build a timeline. Unlike estimate-based bots, this is exact math.

## How to use it (`bestInteractionPattern`: web-manual)
1. Enable Developer Mode in Discord and "Copy ID" on the user/message/channel to get the snowflake.
2. Open https://pixelatomy.com/snow-stamp/ and paste the snowflake ID.
3. Read the decoded creation date/time (UTC).
4. Pivot: an account-creation timestamp corroborates or contradicts a claimed history; message timestamps anchor a Discord activity timeline.

## Inputs → Outputs
- **In:** a Discord snowflake ID (`document-id`) for a user, message, or channel
- **Out:** the exact UTC creation timestamp encoded in that ID
- **Empty/negative result looks like:** no/garbled output — the value pasted isn't a valid snowflake (wrong length, non-numeric, or truncated); re-copy the ID.

## Gotchas & OpSec
- It decodes *creation* time only — not last-seen, not identity; it says nothing about who owns the account.
- Works for anything using Discord's snowflake scheme; it is not a Twitter/Snapchat decoder (those use different epochs).
- OpSec: fully passive — pure local computation, nothing touches Discord or the subject.

## Overlaps ("do both")
- Pairs with `[[regdatebot]]` (Telegram) as the equivalent age-check on a different platform, and with Discord-username/ID lookup tools that turn a handle into the snowflake you feed here.

## Trust & verifiability
`trust: community` — the conversion is deterministic and independently reproducible, so the timestamp is trustworthy regardless of the host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pixelatomy-com |
