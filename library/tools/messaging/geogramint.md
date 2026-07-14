---
id: geogramint
name: Geogramint
description: Use when you have a `geolocation` (coordinates) and want to enumerate Telegram users/groups who have shared their location nearby — returns social-profile, associate, geolocation.
url: https://github.com/Alb-310/Geogramint
category: messaging
path:
- messaging
bestFor: Finding Telegram "People/Groups Nearby" at a chosen coordinate for geofenced Telegram recon.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- associate
- geolocation
status: live
pricing: free
costNote: Free, open source (GPL). Requires your own free Telegram API credentials (api_id/api_hash from my.telegram.org) and a Telegram account to authenticate the client.
opsec: active
opsecNote: You must log in with a real Telegram account (phone-verified), and the "Nearby" feature is reciprocal by design — using it can expose YOUR presence and account. Use a dedicated sock-puppet Telegram account and number, spoof/set the query coordinates deliberately, and never run it from your personal account.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool (Alb-310) built on the documented Telegram (Telethon) API; results are only as complete as who has enabled Telegram's opt-in "People Nearby" — a small, self-selected subset of users.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
aliases:
- Geogramint
tags:
- telegram
- geolocation
- kimi-2026
source: kimi-telegram
lastVerified: '2026-07-14'
enrichment: full
---

# Geogramint

> A Telegram geo-OSINT tool that queries the "People/Groups Nearby" feature at arbitrary coordinates — surfacing Telegram users and groups who've opted to broadcast their location.

## When to use
You have a `geolocation` (a specific coordinate — a last-known location, an address, an area of interest) and want to know which Telegram users or groups have made themselves discoverable "nearby" there. Useful for placing a subject who uses Telegram's location feature, or mapping local Telegram activity around a site. Note the hard limit: it only sees users who have *opted into* Telegram's People Nearby.

## How to use it (`bestInteractionPattern`: cli)
1. Get free Telegram API credentials (api_id/api_hash) at my.telegram.org and set up a **sock-puppet** Telegram account/number.
2. Clone https://github.com/Alb-310/Geogramint, install dependencies, and configure it with your API credentials (it also has a GUI mode).
3. Set the target latitude/longitude and run the scan.
4. Read results: nearby Telegram users (usernames/IDs, approximate distance → `geolocation`) and nearby groups (`associate` / community context).
5. Pivot: a discovered `username`/ID feeds Telegram-specific OSINT and username enumeration; nearby groups reveal local communities the subject may belong to.

## Inputs → Outputs
- **In:** `geolocation` (latitude/longitude)
- **Out:** `social-profile` (nearby Telegram users), `associate` (nearby groups), approximate `geolocation`/distance
- **Empty/negative result looks like:** no nearby users/groups — very common, because People Nearby is opt-in and sparsely used; absence says nothing about whether your subject is on Telegram.

## Gotchas & OpSec
- Human-in-the-loop: needs Telegram API keys and an authenticated account login.
- Only sees opt-in "Nearby" users — a small, self-selected slice; distances are approximate.
- OpSec (active): the feature is reciprocal — running it can reveal your own account/presence. Use a dedicated sock-puppet account and number; never your personal one.

## Overlaps ("do both")
- Pairs with other Telegram OSINT (username/ID lookup, group scrapers) — Geogramint finds who's *near a point*; those enrich *who they are*.

## Trust & verifiability
`trust: community` — a transparent open-source tool over Telegram's official API; the data is real but inherently partial (opt-in only) and locations are approximate — treat hits as leads to confirm.
