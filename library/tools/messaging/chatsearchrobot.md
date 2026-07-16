---
id: chatsearchrobot
name: ChatSearchRobot
description: Use when you have a Telegram group/channel `social-profile` or a topic `username`/keyword and want to discover similar or related Telegram communities — returns social-profile links to other group chats.
url: https://t.me/ChatSearchRobot
category: messaging
path:
- messaging
bestFor: Finding Telegram groups/channels similar to a known one, or by topic keyword.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Telegram bot; no payment required beyond having a Telegram account.
opsec: passive
opsecNote: You query the bot, not any target, so no subject is alerted. But the operator logs your searches — use a burner Telegram account if the communities you're mapping are sensitive, and remember that joining any group the bot surfaces is itself an active step that can expose your account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous Telegram discovery bot; the similarity ranking is opaque and results are best treated as a lead list, not an exhaustive index.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- ChatSearchRobot bot
tags:
- telegram
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# ChatSearchRobot

> A Telegram bot that surfaces related group chats and channels, letting you expand from one known community into the wider cluster around a subject or topic.

## When to use
You've found one Telegram group/channel your subject frequents (a `social-profile`), or you have a topic `username`/keyword, and you want to map the surrounding community graph — other groups on the same theme where the subject or their associates may also be active. Good for widening a Telegram footprint beyond a single known chat.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a Telegram account (Telegram Web is fine), open https://t.me/ChatSearchRobot and press Start.
2. Send the bot a known group/channel link or a topic keyword.
3. Read the returned list of similar/related group chats and channels.
4. Pivot: review each surfaced group's public members and message history for your subject or associates. Do NOT join sensitive groups from your real account — use a burner if you must enter one.

## Inputs → Outputs
- **In:** `social-profile` (a Telegram group/channel), or a topic `username`/keyword
- **Out:** `social-profile` (links to related Telegram groups/channels)
- **Empty/negative result looks like:** an empty or generic list — means the seed group/topic is too niche or private for the bot's index, not that no related communities exist.

## Gotchas & OpSec
- Human-in-the-loop: needs a logged-in Telegram account to interact with the bot.
- This is a discovery aid, not a member search — it points you at groups; the actual person-hunting happens once you inspect each group.
- OpSec: querying is passive, but joining any surfaced group is active and exposes your Telegram identity to that group's admins; compartmentalize with a burner.

## Overlaps ("do both")
- Pairs with broader Telegram-OSINT toolsets like `[[awesome-telegram-osint]]` and search bots such as `[[osint-tool-for-tg]]` — this one finds the groups, those help you enumerate and analyze the members inside them.

## Trust & verifiability
`trust: unverified` — an anonymous bot with an opaque ranking algorithm; use its output as a starting lead list and confirm relevance by inspecting the groups directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chatsearchrobot |
| category | messaging |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
