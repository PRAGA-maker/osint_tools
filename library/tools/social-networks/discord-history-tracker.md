---
id: discord-history-tracker
name: Discord History Tracker
description: Use when you have access to a Discord server/DM and want to archive its messages for offline analysis — returns a searchable local copy of channels, authors and attachments.
url: https://dht.chylex.com/
category: social-networks
path:
- social-networks
bestFor: Saving Discord channel/DM history you can already see into a local, searchable archive before it's deleted.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
- associate
status: live
pricing: free
costNote: Free and open-source (browser script + offline viewer). No cost; you run it against channels your own account can access.
opsec: active
opsecNote: It runs through YOUR logged-in Discord session to read messages your account can see, so activity is tied to that account and automated scraping violates Discord's ToS (risking a ban). Use a dedicated sock-puppet account, only in servers it has legitimately joined, and never your real identity. It captures content, not covert access — it can't read anything your account can't already see.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known open-source tool (chylex). It faithfully saves the messages your account can view; the archive is as reliable as what you had access to.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- discord-search
- discordhistory
aliases:
- DHT
- dht.chylex.com
tags:
- discord
- chat-archive
- messaging
- evidence-preservation
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Discord History Tracker

> An open-source archiver that saves the Discord messages your account can see into a local, searchable file — capture the conversation before it's edited or deleted.

## When to use
You have legitimate access (via a sock-puppet or authorised account) to a Discord server or DM that matters to a case, and you want a durable, offline, searchable copy before messages are deleted or the server vanishes. DHT walks the channels your account can read and stores messages, authors, timestamps, and attachments into a database you view offline. Its OSINT value is evidence preservation and analysis: who said what, when, and who they interact with (`associate` links) inside a community.

## How to use it (`bestInteractionPattern`: web-manual)
1. Get DHT from https://dht.chylex.com/ (a browser script/console tool plus an offline viewer).
2. Log into Discord with a **dedicated sock-puppet** account that already has access to the target server/DM.
3. Run the tracker on the channel(s) to save messages, authors, timestamps, and attachments locally.
4. Open the saved archive in the offline viewer to read and search the history.
5. Pivot: commenter `username`s/IDs are `social-profile`/`associate` leads for cross-platform search; attachments feed image/metadata tools; the interaction graph reveals who's connected to whom.

## Inputs → Outputs
- **In:** access to a Discord server/DM (and, in analysis, a `username` to search the archive for)
- **Out:** local searchable message archive — `username`s, message text, timestamps, attachments, `associate` interaction links
- **Empty/negative result looks like:** nothing captured — your account can't see the channel (no access/permissions), or the channel is empty. It cannot retrieve messages your account isn't permitted to read.

## Gotchas & OpSec
- OpSec: **active and ToS-sensitive** — automated reading through your session breaches Discord's ToS and can get the account banned. Use only a burner account, only where it has legitimately joined, never your real login.
- It captures only what your account can already access; it is not a way to breach private servers.
- Archive promptly — the value is capturing content before it's deleted; you can't recover what's already gone.

## Overlaps ("do both")
- Pairs with `[[discord-search]]` (finding relevant servers/users to target) — use search/discovery to locate the community, then DHT to preserve and analyse its history offline.

## Trust & verifiability
`trust: community` — a mature open-source tool that saves genuine Discord content your account viewed. The archive is verifiable against the live channel while it exists; reliability is bounded only by what your account could see.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-history-tracker |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
