---
id: netsplit-de
name: netsplit.de
description: Use when you have a topic, keyword, or channel name and want to find the IRC communities that discuss it — returns channel names, networks, topics, and user counts.
url: https://netsplit.de/channels/search.php
category: communities-forums
path:
- communities-forums
- irc-search
bestFor: Passively discovering active IRC channels and networks by keyword, plus network size/health stats.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public IRC search/statistics site; no account or payment.
opsec: passive
opsecNote: Passive — you search netsplit.de's own crawled index, not the live IRC networks, so your query never touches a server the subject is on and generates no join/whois against them. Actually joining a discovered channel to observe users would be an active step done elsewhere.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running independent IRC statistics service that crawls ~500 networks for public channel lists and user counts; data is as current as its last crawl, not real-time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- netsplit.de IRC search
- irc.netsplit.de
tags:
- irc
- communities
- channel-search
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# netsplit.de

> A search engine and statistics tracker for ~500 IRC networks — find which channels (and thus which communities) exist around a topic or handle, without touching the networks yourself.

## When to use
You want to locate the IRC communities tied to a subject's interests, a project, a nickname, or a niche topic — technical support rooms, hobbyist channels, or scene communities that don't show up in normal web search. netsplit.de indexes public (non-private) channel names and topics across hundreds of networks, so it's a passive first step for scoping *where* to look before deciding whether to enter a channel and observe. Also handy for gauging a network's size/activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://netsplit.de/channels/search.php (or the channel search at `/channels/`).
2. Enter a keyword, topic, or candidate channel/handle. The engine matches against channel **names and topics** across ~500 networks.
3. Read results: channel name, the network it's on, current/typical user count, and the topic line.
4. Optionally open a network's statistics page (`/networks/statistics.php?net=<network>`) for size and health over time.
5. Pivot: a promising channel + network tells you where to (carefully, and separately) connect and observe; a distinctive channel/topic can corroborate a community a subject belongs to.

## Inputs → Outputs
- **In:** a keyword, topic, or channel/nick fragment (`username`-style handle)
- **Out:** matching channels with network, user count, and topic — pointers to a `social-profile`-equivalent community presence
- **Empty/negative result looks like:** no matches means no *public* channel name/topic indexed for that term — private/secret channels and per-user presence are invisible here, so absence is not proof.

## Gotchas & OpSec
- **Index, not live:** results reflect netsplit.de's last crawl, so counts and channels can lag; a channel may have moved or gone quiet.
- It searches channel names and topics, **not** who is currently in a room — to see users you must join the channel yourself, which is an active step to plan separately (use a sock-puppet client, expect your nick/host to be visible).
- Private, keyed, and secret channels are excluded by design.

## Overlaps ("do both")
- Complements username-enumeration tools — those find a handle's web accounts, while netsplit.de finds the IRC rooms/communities around a topic or nick that web-focused tools miss.

## Trust & verifiability
`trust: community` — an established, independent IRC-statistics project crawling real network data; the channel/network facts are verifiable by connecting, but figures are crawl-time snapshots rather than live truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netsplit-de |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
