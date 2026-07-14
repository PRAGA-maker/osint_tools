---
id: telepahty
name: Telepathy
description: Use when you have a Telegram channel/group or `username` and want to map it — returns member lists (`associate`), archived messages, forwarded-message links, top posters and coordinate-based user finds.
url: https://github.com/proseltd/Telepathy-Community
category: messaging
path:
- messaging
bestFor: Archiving a Telegram channel/group and extracting membership, message history, forwarded-message networks and engagement metrics for analysis.
selectorsIn:
- username
- social-profile
- geolocation
selectorsOut:
- associate
- social-profile
- name
status: live
pricing: freemium
costNote: Community edition is free and open-source (MIT). An enterprise "Telepathy Pro" (prose.ltd) is paid. You must supply your own free Telegram API credentials (api_id/api_hash) from Telegram's developer portal.
opsec: active
opsecNote: It operates through a real Telegram account (your API credentials), so joining/archiving is attributable to that account and large scrapes can trip Telegram rate limits or bans. Use a dedicated sock-puppet Telegram number/account, throttle, and never your personal account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A well-known, actively developed open-source Telegram OSINT toolkit by Prose (proseltd); MIT-licensed and inspectable, with a commercial Pro tier for the maintained/enterprise version.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- regdatebot
aliases:
- Telepathy-Community
- Telepathy Community
- proseltd Telepathy
tags:
- telegram
- channel-archiving
- membership
- network-analysis
- cli
- python
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Telepathy

> The "swiss army knife" of Telegram OSINT — a Python CLI that archives channels, dumps member lists, maps forwarded-message networks and finds users by location.

## When to use
You have a Telegram channel/group (by `username`/link) or a user handle and need structured intelligence: who is in a group (`associate` lists), the full archived message history, which channels forward to which (influence/network mapping), the most active posters, and — powerfully — users near a set of `geolocation` coordinates. This turns an opaque Telegram community into CSVs and edgelists you can analyse.

## How to use it (`bestInteractionPattern`: cli)
1. Install the community edition from `https://github.com/proseltd/Telepathy-Community` (Python).
2. Register a Telegram app to get `api_id`/`api_hash`; authenticate with a sock-puppet Telegram account.
3. Run commands to archive a chat, scrape a member list, map forwards, or locate users by coordinates.
4. Read the outputs: CSVs, message databases, metadata files, and edgelists (import into Gephi for network graphs).
5. Pivot: member handles feed username/ID tools and `[[regdatebot]]` for account-age; forwarded-message maps reveal linked communities; coordinate finds surface local associates.

## Inputs → Outputs
- **In:** a Telegram channel/group/`username` (or `geolocation` coordinates for nearby-user search)
- **Out:** member `associate` lists, archived messages/media, forwarded-message links, top-poster metrics, `social-profile`/`name` data
- **Empty/negative result looks like:** empty exports or errors — the target is private and your sock-puppet isn't a member, membership visibility is restricted, or you hit Telegram rate limits; a null can mean access limits, not an empty group.

## Gotchas & OpSec
- Human-in-the-loop: needs your own Telegram API credentials and an authenticated account; that account is exposed by the activity.
- OpSec: **active** — joining and bulk-scraping are attributable and can get an account rate-limited or banned. Isolate the account, throttle, and expect Telegram countermeasures.
- Some features are in-progress in the community edition; the maintained feature set lives in the paid Pro version.

## Overlaps ("do both")
- Pairs with `[[regdatebot]]` and Telegram ID tools — Telepathy harvests the members and structure; per-account bots then age-check and enrich the handles it surfaces.

## Trust & verifiability
`trust: community` — an inspectable, MIT-licensed, actively maintained toolkit; outputs are as reliable as Telegram's own data, but respect that bulk collection is intrusive and rate-limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telepahty |
