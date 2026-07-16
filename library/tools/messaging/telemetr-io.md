---
id: telemetr-io
name: Telemetrio (telemetr.io)
description: Use when you have a Telegram channel/`username` or a keyword and want channel analytics, post search and mention monitoring across millions of channels — returns social-profile, associated channels and post metadata.
url: https://telemetr.io/en/channels
category: messaging
path:
- messaging
bestFor: Searching and analysing public Telegram channels at scale — rankings, subscriber/reach stats, ad-creative intel, keyword post search and real-time mention tracking.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free tier exists but is tightly capped (≈1,000 requests/month, 5 verified channels, 7-day history; post-search and "Spy" mention-tracking heavily limited). Paid tiers (S/M/L/XL, roughly $25–$499/month) unlock deep post search, longer history and more trackings.
opsec: passive
opsecNote: You query Telemetrio's own index, not Telegram directly, so the target's channel is not notified of your interest. Create an account with a research email; avoid tying searches to a personal Telegram login.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Listed in Bellingcat's Online Investigation Toolkit and widely used by researchers; a reputable third-party Telegram analytics aggregator, though data is its own index rather than official Telegram output.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Telemetrio
- telemetr.io
tags:
- telegram
- Telegram
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- telemetrio
---

# Telemetrio (telemetr.io)

> A large-scale Telegram analytics and search engine — index of 10M+ channels with rankings, subscriber/reach stats, ad-creative history, keyword post search and real-time mention alerts.

## When to use
You have a Telegram channel handle (`username`), a person/organisation name, or a keyword, and you want to (a) find channels associated with them, (b) measure a channel's reach and audience, (c) search historical posts by keyword — including posts later deleted by the author — or (d) set a "Spy" alert that pings when your term is mentioned anywhere in the index. It is a channel-intelligence tool; the payoff is discovering and profiling public Telegram presences (`social-profile`) and their post `metadata`, not resolving a private individual's phone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://telemetr.io/en/channels and register a free account (needed for most search/analytics features).
2. Search a channel `username`, a `name`, or a keyword; browse the ranked channel list and open a channel page for subscriber growth, views, engagement rate and audience breakdown.
3. Use **Post Search** to find messages containing your keyword across indexed channels (deep search is paid-gated), and **Spy** to set real-time mention alerts.
4. Read the ad-creative section to see where a channel has advertised — a useful cross-link to related channels.
5. Extract the channel identity/links (`social-profile`) and post details (`metadata`); pivot handles and cross-referenced channels into further Telegram OSINT.

## Inputs → Outputs
- **In:** channel `username`, `name`/organisation, or keyword
- **Out:** `social-profile` (channels + links), `metadata` (post/engagement/audience data, ad history)
- **Empty/negative result looks like:** the channel/keyword is absent from the index or shows only a bare page — Telemetrio indexes *public channels*, so private groups and 1:1 chats will never appear.

## Gotchas & OpSec
- Free tier is genuinely limited (small request quota, 7-day history, minimal post-search); assume you'll hit the wall quickly and either ration queries or budget for a paid tier.
- Indexes public channels only — do not expect coverage of private groups, secret chats or individual user accounts.
- OpSec: passive against the target (you query Telemetrio, not Telegram); still use a sock-puppet account.

## Overlaps ("do both")
- Pairs with `[[teleteg]]` and Google-CSE-for-Telegram approaches — Telemetrio is strongest for analytics and deep post search, while link-search tools surface channels/handles it may rank lower; run both when mapping a target's Telegram footprint.

## Trust & verifiability
`trust: community` — a reputable, Bellingcat-listed aggregator, but figures are Telemetrio's own measurements; confirm any critical post by opening it in Telegram directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telemetr-io |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
