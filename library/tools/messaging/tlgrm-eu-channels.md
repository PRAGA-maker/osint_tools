---
id: tlgrm-eu-channels
name: tlgrm.eu channels
description: Use when you have a topic or channel `name`/`username` and want to find public Telegram channels — returns channel `social-profile`s and links.
url: https://tlgrm.eu/channels
category: messaging
path:
- messaging
bestFor: Discovering public Telegram channels by topic/category or name as an entry point into Telegram-based communities and content.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free third-party directory; no account. Lists opt-in / submitted public channels, so coverage is partial.
opsec: passive
opsecNote: Browsing the directory is anonymous and does not touch Telegram or alert any channel. Opening a channel inside the Telegram app, however, is done from your account — use a sock-puppet Telegram account for actual viewing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An unaffiliated Telegram channel catalogue built from submissions; useful for discovery but not exhaustive and not an authoritative index of all channels.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-channels-list
aliases:
- tlgrm.eu
- tlgrm.eu channel directory
tags:
- bellingcat-toolkit
- telegram
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# tlgrm.eu channels

> A browsable third-party directory of public Telegram channels, organised by topic — a discovery layer for finding channels you can then read inside Telegram.

## When to use
You want to find public Telegram channels around a topic, region, or a suspected channel `name`/`username` — for example to locate the community a subject participates in, or to monitor a subject-relevant channel. Telegram has no strong native public search, so a directory like this helps you discover channels to then open in the app.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tlgrm.eu/channels.
2. Browse by category (Politics, News, Technology, etc.) or search for a channel name/keyword.
3. Read each listing: channel title, description, avatar, and the `t.me/...` link.
4. Pivot: open the channel from a **sock-puppet** Telegram account to read messages, members (where visible) and forwarded sources; feed distinctive channel/usernames into username-search and dedicated Telegram OSINT tools.

## Inputs → Outputs
- **In:** topic keyword, or channel `name`/`username`
- **Out:** channel `social-profile`s (title, description, `t.me` link)
- **Empty/negative result looks like:** no listing — the directory only holds submitted/opted-in channels, so many (especially private or niche) channels are absent. Absence here is weak evidence; search Telegram directly and other Telegram indexes.

## Gotchas & OpSec
- **Partial, submission-based coverage** — it misses most channels; don't treat it as a complete map of Telegram.
- Actual reading happens in Telegram, which ties to an account — always use a burner Telegram identity for viewing/joining.
- OpSec: directory browsing passive; in-app viewing is account-linked.

## Overlaps ("do both")
- Pairs with [[telegram-channels-list]] and other Telegram search indexes — each catalogues a different slice, so run several to widen discovery.

## Trust & verifiability
`trust: community` — an unofficial, community-built catalogue. Good for finding candidate channels; verify a channel's real content and ownership inside Telegram itself, not from the directory blurb.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tlgrm-eu-channels |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
