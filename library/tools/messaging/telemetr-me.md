---
id: telemetr-me
name: telemetr.me
description: Use when you have a Telegram channel `username` or keyword and want channel analytics — returns subscriber stats, post history, growth, ad tracking and channel discovery (Russian-focused).
url: https://telemetr.me/
category: messaging
path:
- messaging
bestFor: Discovering and analysing Telegram channels (especially Russian-language) — stats, post search, and ad history.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier lets you browse the channel catalog and view basic stats; detailed analytics, audience analysis and API access require a paid subscription.
opsec: passive
opsecNote: Telemetr indexes public Telegram channels — you query its database, not Telegram directly, so no join or view is registered against your account and channel admins aren't alerted by your search. Use a sock-puppet browser; a paid account ties queries to your subscription identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large commercial Telegram-analytics service (8.7M+ channels indexed), Russian-market oriented; coverage is strongest for Russian-language public channels and thinner elsewhere.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Telemetr
- telemetr.me
tags:
- telegram
- Telegram
- channel-analytics
- russian
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# telemetr.me

> A Telegram channel analytics engine and catalog — search channels, read their post history, and track subscribers/ads across millions of (mostly Russian) public channels.

## When to use
You are investigating a Telegram presence and want to find channels by keyword/topic, analyse a known channel's reach and history, or search across billions of indexed posts — without joining channels from your own account. Especially strong for Russian-language Telegram, which dominates much conflict/fraud/disinfo OSINT. Use it to profile a channel a subject runs or frequents, and to search post content over time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telemetr.me/ in a sock-puppet browser (interface is primarily Russian — a translator helps).
2. Search by channel `username`/name, or by keyword to discover channels and posts on a topic.
3. Open a channel's profile: subscriber count and growth curve, posting frequency, view/engagement metrics, quality rating, and detected advertising posts.
4. Use post search to find where a phrase/name appears across indexed channels and history.
5. Pivot: a channel admin/handle feeds Telegram-native and `[[user-searcher]]` username pivots; ad posts link channels to advertisers; historical posts feed timeline analysis.

## Inputs → Outputs
- **In:** Telegram channel `username` / keyword
- **Out:** channel `social-profile` (stats, growth, post history, ad history), and post-search matches across channels
- **Empty/negative result looks like:** channel not in the catalog or no post matches — common for small, private, or non-Russian channels (weaker coverage). Absence means "not indexed here," not that the channel/post doesn't exist.

## Gotchas & OpSec
- **Russian-centric coverage** — excellent for RU-language public channels, patchier for other languages; complement with other Telegram tools for global coverage.
- Analytics reflect Telemetr's indexing/estimates, not Telegram's ground truth; treat metrics as approximate.
- OpSec: **passive** — you don't touch the channel from your account; keep the session a sock puppet.

## Overlaps ("do both")
- Pairs with TGStat, Telegram's native search, and phone/username checkers like `[[telegram-phone-number-checker]]` — different indexes cover different channels; run several for completeness, and use native Telegram (via sock puppet) to confirm live content.

## Trust & verifiability
`trust: community` — a large commercial analytics vendor; data is indexed/estimated, not authoritative. Verify key findings against the live channel (from a sock-puppet account) and a second analytics source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telemetr-me |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
