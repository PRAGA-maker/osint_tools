---
id: searchforchats
name: Searchforchats
description: Use when you have a keyword, topic or `name` and want to discover Telegram groups and channels about it — a Telegram catalog bot returning matching public group/channel social-profiles.
url: https://telegram.me/searchforchatsbot
category: messaging
path:
- messaging
bestFor: Finding public Telegram groups and channels by keyword — useful for locating communities tied to a person, place, or topic.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Telegram catalog bot. Requires a Telegram account to query it; no payment.
opsec: active
opsecNote: Active and account-bound — you interact with a third-party bot from a Telegram account, and joining any group it surfaces exposes your account to that group. Use a dedicated sock Telegram account and stay a passive lurker.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A community group/channel catalog bot (Russian-language, "Поиск чатов и каналов"). Its index is crowd/scrape-sourced and incomplete; results are discovery leads, not an exhaustive directory.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- reddit-com-2
- avtogram-bot
- datxpert
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- leak-osint
- oksearch
- pimeyes
- spyggbot
- unamer
aliases:
- searchforchatsbot
- Поиск чатов и каналов
tags:
- telegram
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Searchforchats

> A Telegram catalog bot that finds public groups and channels by keyword — a way into the communities around a person, place, or topic that Telegram's own search under-serves.

## When to use
Telegram's built-in search is weak at surfacing topical groups/channels. When you have a keyword, place, organisation, or `name` and want to find the Telegram communities discussing it — a town's local channel, a group tied to an employer or cause, a niche interest a subject follows — this bot returns matching public groups/channels to investigate. Best for building context and finding where a subject or their circle might congregate.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **sock** Telegram account, open https://telegram.me/searchforchatsbot and start the bot.
2. Send a keyword/topic/place (interface is Russian-language; keywords in the target's language work best).
3. Read the output: a list of matching public groups and channels (`social-profile`) with member counts.
4. Open promising groups/channels as a lurker; search within them for the subject's handle, name, or activity.
5. Pivot: usernames and messages inside a group feed handle enumeration and [[reddit-com-2]]-style Telegram user-ID resolution; group topics corroborate a subject's interests/location.

## Inputs → Outputs
- **In:** `name`/keyword/topic/place
- **Out:** `social-profile` (matching Telegram groups/channels)
- **Empty/negative result looks like:** few or no matches — the catalog is incomplete, so a null result doesn't mean no such community exists. Try alternate keywords and languages.

## Gotchas & OpSec
- The index is crowd/scrape-sourced and partial; treat it as discovery, not a complete directory.
- Human-in-the-loop: a Telegram account and manual review of results are required.
- OpSec: **active** — joining a surfaced group exposes your (sock) account to its members/admins. Lurk; don't post.

## Overlaps ("do both")
- Pairs with [[reddit-com-2]] (Telegram user-ID resolution) — this finds the groups a subject may inhabit, that technique pins down the durable numeric ID of accounts you spot inside them.

## Trust & verifiability
`trust: community` — an unofficial catalog bot with incomplete coverage. Use it to discover communities, then verify any subject link by observing the group directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchforchats |
| category | messaging |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
