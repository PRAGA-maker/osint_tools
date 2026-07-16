---
id: pockettube
name: PocketTube
description: Use when you have a set of YouTube channels (`social-profile`/`username`) to monitor and want them grouped, deduped and watched in one feed — returns an organized, exportable view of channel activity.
url: https://chromewebstore.google.com/detail/pockettube-youtube-subscr/kdmnjgijlmjgmimahnillepgcgeemffb
category: social-networks
path:
- social-networks
bestFor: Organizing and monitoring many YouTube channels/subscriptions into topical groups and a single activity feed for ongoing surveillance of accounts of interest.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to install and use; developers accept voluntary Patreon / "Buy Me a Coffee" support. No mandatory paywall.
opsec: active
opsecNote: A browser extension that runs inside your logged-in YouTube/Google session and syncs collections via your Google Drive — so monitoring is tied to a real Google account. Use a dedicated sock-puppet Google account, never a personal one, when tracking subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Established third-party extension (200k+ users, ~4.6 stars); a UI layer over YouTube, not a data provider, so it surfaces only what YouTube already shows you.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- PocketTube YouTube Subscription Manager
tags:
- Social Media
- YouTube
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# PocketTube

> A YouTube subscription manager browser extension — turns a sprawl of subscribed channels into named groups and a single, filterable activity feed useful for monitoring accounts over time.

## When to use
You are tracking a cluster of YouTube channels (`username`/`social-profile`) — a subject's own channel plus related accounts — and want them organized into groups, deduplicated, and surfaced in one "deck" feed so you can watch for new uploads without checking each channel by hand. It is a monitoring/organization aid, not a discovery or attribution tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install PocketTube from the Chrome Web Store (or its Firefox/mobile builds) into a browser signed into a dedicated sock-puppet Google account.
2. Subscribe to the channels of interest, then in PocketTube sort them into named collections/sub-groups with custom icons.
3. Use "Deck mode" for a TweetDeck-style multi-column view of the latest videos per group; filter/sort by duration, activity and date.
4. Read the output: a consolidated feed of channel activity (`social-profile`); optionally export the subscription list to CSV.
5. Pivot: feed the channel handles/CSV into username lookups and cross-platform searches; use the CSV as a durable record of who you were monitoring.

## Inputs → Outputs
- **In:** `username` / `social-profile` (YouTube channels you subscribe to)
- **Out:** `social-profile` (organized channel activity feed), plus a CSV export of the subscription set
- **Empty/negative result looks like:** groups with no recent uploads simply show an empty feed — it does not find new channels for you.

## Gotchas & OpSec
- It only organizes channels you subscribe to from your own account — it is not a scraper or a way to see private data. Everything shown is already visible to that Google account.
- OpSec: **active** — it lives in a logged-in Google session and syncs via Google Drive. Subscribing to a subject's channel is visible to Google (and can affect recommendations); always use a throwaway account, never your own.
- Free tier is ample; ignore the donation prompts.

## Overlaps ("do both")
- Complements dedicated YouTube OSINT lookups (channel-id/upload-date tools): PocketTube handles ongoing monitoring and grouping, while those extract metadata from a single video/channel.

## Trust & verifiability
`trust: community` — a mature, well-reviewed third-party extension. It presents only YouTube's own data, so there is no independent-data-quality risk beyond trusting the extension with your (sock-puppet) session.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pockettube |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
