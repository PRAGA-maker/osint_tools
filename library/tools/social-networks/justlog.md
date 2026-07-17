---
id: justlog
name: Justlog
description: Use when you have a Twitch `username` and a channel and want their chat history there — returns the user's logged messages (with timestamps), downloadable as text.
url: https://logs.ivr.fi/
category: social-networks
path:
- social-networks
bestFor: Retrieving a Twitch user's full chat-message history in a specific logged channel.
selectorsIn:
- username
selectorsOut:
- username
- name
status: live
pricing: free
costNote: Free public logs instance (the open-source Justlog by gempir). No account needed; results downloadable as TXT/JSON.
opsec: passive
opsecNote: You read an already-collected public chat log; the target isn't notified and you don't join the channel. Only channels the instance actively logs are available, and users can request opt-out. Passive; use a clean session for sensitive lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A public instance of the open-source Justlog logger. Logs are genuine captured Twitch chat, but coverage is limited to channels this instance logs and users can opt out, leaving gaps.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- twitch-tools
- sullygnome
aliases:
- logs.ivr.fi
- ivr logs
- gempir justlog
tags:
- twitch
- chat-logs
- messaging
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Justlog

> A public Twitch chat-log archive: give it a username and a channel and read everything that user has said there, exportable as text.

## When to use
Your subject uses Twitch and you want their words, not just their profile. Justlog (hosted at logs.ivr.fi) stores per-channel chat history, so you can pull a `username`'s full message log in a channel it tracks — useful for building a behavioural/timeline picture, catching self-identifying details a person dropped in chat (location, real name, other handles, plans), and preserving messages before they scroll away. It only covers channels the instance actively logs, so it's a targeted rather than universal source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://logs.ivr.fi/.
2. Enter the channel name and the target `username`.
3. Read the returned messages with timestamps; browse by date or search within the log.
4. Download the log as TXT/JSON to preserve it (the API supports programmatic pulls too).
5. Pivot: chat text often leaks a real `name`, location, or other handles → feed those to people/username search; timestamps place the person active at specific times.

## Inputs → Outputs
- **In:** `username` (Twitch) + a channel name
- **Out:** the user's logged chat messages (timestamps), plus any self-disclosed `name`/details in the text
- **Empty/negative result looks like:** "channel not logged" or "no messages" — the instance doesn't track that channel, the user never chatted there, or they've opted out. Absence isn't proof they don't use Twitch.

## Gotchas & OpSec
- Coverage is limited to channels this specific instance logs; a miss often just means the channel isn't tracked — try other logs instances.
- Users can request opt-out, creating gaps.
- OpSec: passive; you read stored logs without joining the channel or alerting anyone.

## Overlaps ("do both")
- Pairs with `[[sullygnome]]` / `[[twitch-tools]]` (channel/user analytics and activity) — those profile the account and its streaming history, while Justlog gives the actual chat content the person wrote.

## Trust & verifiability
`trust: community` — an open-source logger instance capturing real Twitch chat. Messages are genuine and timestamped (verifiable if the channel is public), but coverage gaps (unlogged channels, opt-outs) mean absence proves nothing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justlog |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
