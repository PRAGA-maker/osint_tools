---
id: teletracker
name: TeleTracker
description: Use when you have a Telegram channel/bot ID and want to harvest and archive its messages, media, and owner info — returns exported content and channel metadata.
url: https://github.com/tsale/TeleTracker
category: messaging
path:
- messaging
bestFor: Bulk-collecting and archiving a Telegram channel's messages, media, and bot/owner details for investigation.
selectorsIn:
- username
- device-id
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python); requires your own free Telegram API credentials (api_id/api_hash) and a bot token.
opsec: active
opsecNote: TeleGatherer/TeleViewer read channel content via the API (passive to members), but the toolkit also includes TeleTexter, which SENDS messages (including bulk) — an active, potentially attributable action. Downloading media pulls files to your disk. Use a dedicated sock-puppet Telegram account/API app, never send messages to a live target channel unless deliberate, and handle downloaded media with care.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source threat-intel toolkit (tsale/TeleTracker); code is inspectable and framed for analysts, but it uses the Telegram API under your credentials and includes messaging capability that carries real OpSec risk.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- TeleTracker
tags:
- telegram
- scraper
- threat-intel
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# TeleTracker

> A Python toolkit for investigating Telegram channels — gather and download all of a channel's messages and media, pull bot/owner info, and (with care) message channels — built for threat-intel analysts monitoring adversary comms.

## When to use
You have a Telegram channel or bot identifier tied to your investigation and want to capture its content before it disappears: full message history, all media (photos/videos/documents), and the bot/owner metadata. Telegram channels are volatile and often central to a subject's activity or a case's chatter; bulk export lets you archive and analyze offline for names, media (for reverse-image/EXIF), links, and posting patterns. Reach for it when a channel matters and manual scrolling won't scale.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/tsale/TeleTracker`; create a Telegram API app (api_id/api_hash) and a bot token, stored in a `.env`.
2. Run **TeleGatherer.py** (or TeleViewer.py) against the channel/chat ID to view messages, download media, and retrieve bot/owner info: `python TeleGatherer.py -t <BOT_TOKEN> -c <CHAT_ID>`.
3. Collect outputs: media in a `downloads/` folder, logs in `.txt` (readable) and `.json` (structured).
4. Analyze: extract owner/bot handles, member/forwarding patterns, links, and media for downstream EXIF/reverse-image work.
5. Avoid **TeleTexter.py** (message sending) unless you deliberately intend an active, attributable action.

## Inputs → Outputs
- **In:** a Telegram channel/bot ID (`username` / `device-id`-style identifier) + your API creds
- **Out:** `social-profile` (channel + owner/bot info), `metadata-exif` (downloaded media + message metadata), message archives
- **Empty/negative result looks like:** no messages/media or an auth error — the bot lacks access to that channel, the ID is wrong, or the channel is private/gone. Not proof of no activity; confirm access and the identifier.

## Gotchas & OpSec
- Human-in-the-loop: requires **Telegram API credentials + bot token** (api-key); technical setup.
- OpSec: **active** — reading is passive, but the bundled messaging tool sends messages; and bot access to a channel implies you (or your bot) joined it. Use sock-puppet infrastructure and don't send to live targets.
- Bots can only read channels they're permitted to; you can't silently vacuum an arbitrary private channel.

## Overlaps ("do both")
- Pairs with Telegram directory/discovery tools like `[[groupda]]` (find the channel) and other Telegram scrapers — those locate channels; TeleTracker archives and enriches a chosen one.

## Trust & verifiability
`trust: community` — an inspectable open-source toolkit using the official API under your own keys; output fidelity is good, but the messaging feature and bot-access requirements demand deliberate OpSec.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | teletracker |
| category | messaging |
| selectorsIn → selectorsOut | username, device-id → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
