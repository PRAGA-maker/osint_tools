---
id: telemetrio
name: Telemetrio
description: Use when you have a Telegram channel name, keyword, or forwarded post and want to search across a large catalog of channels — returns social-profile links, associated channels, and post history.
url: https://telemetr.io/
category: messaging
path:
- messaging
bestFor: Searching and analysing public Telegram channels — keyword search across posts, channel discovery, and forwarding-network mapping.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free plan covers 1,000 requests/month, 5 verified channels, and 7 days of post history; paid tiers extend limits, history depth, and API access.
opsec: passive
opsecNote: You query Telemetrio's own scraped catalog, not Telegram directly, so the target is not notified and never sees your identity. Registration ties activity to your account — use a sock-puppet email if you want to keep the investigation compartmentalised.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Listed in Bellingcat's Online Investigation Toolkit; a commercial Telegram-analytics vendor widely used by journalists and OSINT analysts. Data quality is good for public channels but the vendor's index, not an authoritative source.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- telemetr-io
aliases:
- telemetr.io
- Telemetr
tags:
- bellingcat-toolkit
- telegram
- channel-analytics
source: bellingcat-toolkit
lastVerified: '2026-07-21'
enrichment: full
---

# Telemetrio

> Commercial Telegram analytics engine — a searchable index of hundreds of thousands of public channels with post-level search, rankings, and forwarding-network analysis.

## When to use
You have a Telegram `username`/channel handle, a `name`, or a keyword and want to find the channels where a subject posts, is discussed, or is forwarded. Because Telegram itself has weak native search, Telemetrio's crawled catalog is the pivot: search a keyword to discover channels mentioning a person, trace a viral post back to its origin channel, or map which channels forward one another (an `associate` network).

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://telemetr.io/ (a sock-puppet email is fine).
2. Use the search box for keyword search across channel posts — including recently deleted posts, which on the free tier are limited to the last 7 days.
3. Open a channel's analytics page for subscriber trends, post reach, and the list of channels it forwards from / is forwarded to — that forwarding graph reveals the channel's network.
4. Set up keyword or channel monitoring to get alerts on new mentions of a name; deleted mentions can flag censorship or a subject scrubbing their trail.
5. Pivot: origin channels and admin handles feed back into direct Telegram lookups and username tooling.

## Inputs → Outputs
- **In:** `username` (channel handle) or `name`/keyword.
- **Out:** `social-profile` (channel pages, admin/handle links), `associate` (forwarding-network channels), post history and reach metrics.
- **Empty/negative result looks like:** a keyword returns no channels, or a handle isn't in the index — Telemetrio only sees channels it has crawled, so absence is not proof the channel doesn't exist, especially for small/private ones.

## Gotchas & OpSec
- Human-in-the-loop: the free tier caps requests (1,000/month) and history (7 days) — pace queries and prioritise, or the quota stops you mid-investigation.
- OpSec: **passive** — queries hit Telemetrio, not the target's channel, so there is no direct footprint. Keep the account on a sock-puppet identity.
- Coverage is Telegram-wide but skews to Russian/CIS and news channels; niche or brand-new channels may be missing or thinly indexed.

## Overlaps ("do both")
- Pairs with `[[telemetr-io]]` — the same provider suite; use both together to cross-check channel analytics and search coverage rather than trusting one index alone.

## Trust & verifiability
`trust: community` — a commercial vendor endorsed by the Bellingcat toolkit and standard in Telegram OSINT. Its numbers and post archive are reliable for public channels, but treat it as a third-party index: confirm a critical post or handle against Telegram directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telemetrio |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
