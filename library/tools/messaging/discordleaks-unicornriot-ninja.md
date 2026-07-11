---
id: discordleaks-unicornriot-ninja
name: discordleaks.unicornriot.ninja
description: Use when you have a `username` (or keyword) and want to find them inside leaked far-right Discord chat logs — returns the messages, server/channel context and linked `social-profile` behind that handle.
url: https://discordleaks.unicornriot.ninja/discord/server/
category: messaging
path:
- messaging
bestFor: Searching a huge archive of leaked extremist Discord chats by username, server, or keyword.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public research database published by the Unicorn Riot media collective. No account or payment.
opsec: passive
opsecNote: You search a static leaked-data archive hosted by Unicorn Riot — no query reaches the subject or Discord. It is passive. Note the archive is sensitive investigative material about specific named individuals; handle findings responsibly and be aware some subjects actively monitor coverage of these leaks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by Unicorn Riot, an established non-profit investigative media collective. The messages are primary leaked material, but attribution of a handle to a real person is the journalists' analysis — verify before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- discord-com
aliases:
- Unicorn Riot DiscordLeaks
- DiscordLeaks
tags:
- discord
- Discord Related Sites
- leaks
- extremism
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# discordleaks.unicornriot.ninja

> Unicorn Riot's searchable archive of hundreds of thousands of messages leaked from white-supremacist and neo-Nazi Discord servers — searchable by user, server, or keyword.

## When to use
You have a `username`, handle, or distinctive phrase and want to know whether it appears in the corpus of extremist Discord chat logs Unicorn Riot obtained (many after Charlottesville). A hit surfaces the person's messages, the servers/channels they operated in, who they talked to, and often self-disclosed details (location, real name, other handles) — a rich `social-profile` pivot when investigating a subject connected to these communities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discordleaks.unicornriot.ninja.
2. Search by `username`/handle, by keyword, or browse the indexed servers (hundreds of far-right servers are catalogued).
3. Open matching channels/messages — each shows the author handle, timestamp, server/channel, and message text.
4. Read for self-disclosures: linked accounts, first names, cities, employers, other platforms mentioned in-context.
5. Pivot: a real name or secondary handle feeds people-search and username tools; an admitted location feeds `geolocation`; cross-reference the same handle on `[[discord-com]]` and other platforms.

## Inputs → Outputs
- **In:** `username`/handle or keyword
- **Out:** `social-profile` context — messages, server/channel membership, associates, and any self-disclosed identity details
- **Empty/negative result looks like:** no messages returned — the handle/keyword isn't in this specific corpus (which is limited to the servers Unicorn Riot leaked). It says nothing about the person's activity elsewhere on Discord.

## Gotchas & OpSec
- Human-in-the-loop: none for searching, but heavy analytical judgement is required — a handle in a leak needs corroboration before you attribute it to a specific living person.
- OpSec: **passive** — a static archive; nothing reaches the subject. But this is sensitive, adversarial-community data; treat conclusions carefully and consider the legal/ethical frame of your investigation.
- Scope is limited to the servers Unicorn Riot published; absence is not exoneration.

## Overlaps ("do both")
- Pairs with live `[[discord-com]]` investigation — the leak archive gives historical, deep context on a handle, while current Discord (mutual servers, profile, connections) shows present activity. Together they bracket a subject's Discord footprint past and present.

## Trust & verifiability
`trust: community` — published by a reputable investigative outlet, and the messages are primary source material. The one caveat: mapping a chat handle to a real identity is interpretive; confirm with independent evidence before acting on an attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discordleaks-unicornriot-ninja |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
