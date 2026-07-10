---
id: discordleaks
name: DiscordLeaks
description: Use when you have a `name`, `username`, or keyword and want to search leaked messages from white-supremacist / neo-nazi Discord (and RocketChat/Skype) servers — returns matching chat messages with handles and context.
url: https://discordleaks.unicornriot.ninja/
category: people-search
path:
- people-search
bestFor: Attributing a person/handle to activity inside leaked extremist chat servers.
selectorsIn:
- name
- username
selectorsOut:
- username
- name
- social-profile
status: live
pricing: free
costNote: Free public research database published by the Unicorn Riot nonprofit; donations requested but not required.
opsec: passive
opsecNote: Passive — you search an archived leak, not any live server or the subject. Nobody is notified. Still, treat findings as sensitive and legally/ethically fraught; corroborate before attributing a real identity to a chat handle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by Unicorn Riot, an established investigative nonprofit; the leak is a genuine, widely-cited dataset, but chat handles are pseudonymous — attribution to a real person requires independent evidence.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Unicorn Riot DiscordLeaks
- discordleaks.unicornriot.ninja
tags:
- bellingcat-toolkit
- people
- extremism
- leaked-chats
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# DiscordLeaks

> Unicorn Riot's searchable archive of hundreds of thousands of messages leaked from 290+ white-supremacist and neo-nazi Discord servers (plus RocketChat/Skype) — a keyword/handle search into extremist chat activity.

## When to use
You have a `username`, `name`, or keyword and are investigating possible ties to organised extremist communities — a common thread in threat, radicalisation, and some missing-person cases. Searching a handle here can reveal a person's messages, the servers they were active in, and other handles they interacted with, building out an extremist-network picture that live Discord (private, ephemeral) won't give you.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discordleaks.unicornriot.ninja/.
2. Search by `username`, real `name`, or keyword (server names, locations, slogans).
3. Read matching messages with their sender handle, server/channel, and timestamp.
4. Map the handle's activity: which servers, who they replied to (more `username`s), what they disclosed (locations, meetups, real-name slips).
5. Pivot: run recovered handles through username enumeration (`[[snoop]]`, `[[gaddr]]`); a real-name or location slip inside a message becomes a hard lead to corroborate elsewhere.

## Inputs → Outputs
- **In:** `name` / `username` / keyword
- **Out:** matching chat messages, sender `username`s, server/channel context, interacting handles (`social-profile`/`associate` leads), occasional self-disclosed real `name`s
- **Empty/negative result looks like:** no messages match — meaning the handle/name isn't in *this* leak (which is specific to certain servers and a point in time). Absence is not exoneration and not full coverage of Discord.

## Gotchas & OpSec
- Handles are pseudonymous: a match is chat activity by a handle, NOT proof of a named individual. Never attribute to a real person without independent evidence.
- The dataset is bounded (specific servers, mostly post-Charlottesville era) — it doesn't cover Discord broadly or recent activity.
- Content is extremist and disturbing; handle findings responsibly and mind legal/ethical constraints on use.
- Passive; searching leaves no trace with the subject.

## Overlaps ("do both")
- Pairs with username enumerators `[[snoop]]` / `[[gaddr]]` to trace a recovered handle onto other platforms.
- Complementary to `[[wayback-machine-2]]` and other leak/breach sources when corroborating a handle-to-person link.

## Trust & verifiability
`trust: community` — a genuine, well-documented leak published by a credible nonprofit, but the core caveat is attribution: the data reliably shows what a *handle* said, not who owns it. Treat every identity link as a hypothesis to prove with independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discordleaks |
| category | people-search |
| selectorsIn → selectorsOut | name, username → username, name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
