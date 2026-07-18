---
id: telemetry
name: Telemetry
description: Use when you have a `username`, `name`, keyword, or `phone` and want to find where it surfaces across public Telegram — returns `social-profile` channels/groups and message context.
url: https://www.telemetryapp.io/
category: messaging
path:
- messaging
bestFor: Full-text and channel search across 1M+ public Telegram channels and billions of messages.
selectorsIn:
- username
- name
- phone
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free account unlocks basic search; full-text search, CSV export, API access, and advanced analytics require a paid plan. Enough is free to check whether a selector appears in public Telegram.
opsec: passive
opsecNote: You query Telemetry's own index, not Telegram, so the target is not notified and you never join their channels. Sign up with a sock-puppet email. Reading a hit inside Telegram itself (rather than in Telemetry's viewer) can leak your account into view counts/membership — stay in Telemetry's UI while scoping.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial Telegram analytics product listed in Bellingcat's toolkit; index is large but coverage of public channels is partial and message data may lag. Treat hits as leads to confirm in Telegram.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- Telemetry.io
- telemetryapp.io
tags:
- bellingcat-toolkit
- telegram
- message-search
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# Telemetry

> A search engine and analytics layer over public Telegram — find every channel, group, and message where a name, handle, or keyword appears.

## When to use
You have a `username`, real `name`, `phone`, or a distinctive keyword (a company, a location, a callsign) and want to know whether — and where — it appears in public Telegram. Good for surfacing a subject's own channel, tracing a handle across communities, or monitoring a topic without manually joining dozens of groups.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.telemetryapp.io/ and sign up for the free tier (sock-puppet email).
2. Enter your query — a `username`, `name`, or keyword. Use boolean operators (AND, OR, wildcards, phrase quotes) and filters for channel, language, time range, and engagement.
3. Read the results: matching message content, the channel it came from, plus channel analytics (subscriber growth, forward/mention graphs).
4. To open a hit in Telegram, note the channel/message link — but scope from within Telemetry first to avoid leaking your Telegram account.
5. Pivot: a discovered channel or handle feeds Telegram-native tooling and username OSINT; a `phone` tied to a channel feeds phone lookups.

## Inputs → Outputs
- **In:** `username`, `name`, `phone`, or keyword
- **Out:** `social-profile` (Telegram channels/groups), `username`, message snippets, channel analytics
- **Empty/negative result looks like:** zero matching messages/channels, or only the free-tier preview with "sign up to unlock full search" — treat as "not in the indexed public set," not proof of absence (private/unindexed channels are invisible).

## Gotchas & OpSec
- Human-in-the-loop: account login is required for real search; the free tier is deliberately limited.
- Index is partial — Telemetry sees public channels it has crawled, not all of Telegram, and message data can lag.
- Stay in Telemetry's viewer while scoping; joining or opening channels from your real Telegram account is active and attributable.

## Overlaps ("do both")
- Pairs with other Telegram tooling in the [[messaging]] set — Telemetry is strongest for full-text message search, while ID/username resolvers and channel-membership tools cover pivots it does not.

## Trust & verifiability
`trust: community` — a commercial analytics product vetted into Bellingcat's toolkit. Reliable as a discovery index; always confirm a specific message or membership claim against the live Telegram source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telemetry |
| category | messaging |
| selectorsIn → selectorsOut | username, name, phone → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
