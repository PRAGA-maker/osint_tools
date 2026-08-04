---
id: unicorn-riot-discord-leaks
name: 'Unicorn Riot: Discord Leaks'
description: Use when you have a `username`/`name` possibly tied to far-right groups — searches leaked Discord chats and returns messages, `associate` links and `social-profile` handles.
url: https://discordleaks.unicornriot.ninja/discord/
category: public-records
path:
- public-records
bestFor: Searching a large archive of leaked far-right/neo-Nazi Discord servers by user, server, channel or keyword.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: free
costNote: Free and publicly searchable; no account required.
opsec: passive
opsecNote: Searching the archive is passive against the individuals in it — you query Unicorn Riot's site, not any live target, so subjects are not tipped off. Your own queries reach Unicorn Riot's servers; use a sock-puppet browser/VPN if you don't want the search associated with you. The content is extremist material — handle with care and appropriate legal/ethical framing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Unicorn Riot, an established non-profit media organisation, as investigative data journalism; the leaks are real chat exports, though usernames are self-chosen and identity linkage requires corroboration.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- discordleaks
- discordleaks-unicornriot-ninja
aliases:
- DiscordLeaks
- Unicorn Riot DiscordLeaks
tags:
- extremism
- leaks
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Unicorn Riot: Discord Leaks

> A searchable archive of hundreds of thousands of messages from white-supremacist and neo-Nazi Discord servers, published by Unicorn Riot — a way to place a username or handle inside documented extremist communities.

## When to use
You have a `username`, handle, or `name` and want to know whether it appears in the far-right Discord servers Unicorn Riot obtained (many post-Charlottesville). The archive lets you read a user's actual messages, see which servers/channels they were active in, and surface the other handles they interacted with — useful for corroborating an ideological affiliation, mapping a network, or attributing a persona.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discordleaks.unicornriot.ninja/discord/ (ideally in a sock-puppet browser).
2. Use general search, advanced search, or the dedicated user search to query a `username`/`name` or a keyword.
3. Browse by server/channel to understand context; open user profiles to see their message history.
4. Read the messages and note co-occurring handles.
5. Pivot: co-occurring `username`s feed [[associate]] mapping and username enumeration; a matched handle feeds cross-platform social-profile searches.

## Inputs → Outputs
- **In:** `username`/handle or `name` (or a keyword)
- **Out:** matching messages, the user's `social-profile` (Discord handle) and server/channel activity, and `associate` handles they interacted with
- **Empty/negative result looks like:** no matches — the handle isn't in these particular leaked servers (a bounded, historical dataset), or the person used a different name there; absence is not exoneration.

## Gotchas & OpSec
- **Handles ≠ identities:** a Discord username is self-chosen; linking it to a real person requires independent corroboration, and name collisions are real.
- **Bounded, historical dataset:** it covers specific leaked servers at specific times — not all of Discord, and not current.
- Sensitive/extremist content with legal and ethical weight; document your methodology and handle findings responsibly.

## Overlaps ("do both")
- Pairs with cross-platform username tools and breach/leak search — this proves presence and context in specific communities; those extend the handle across other platforms.

## Trust & verifiability
`trust: trusted` — a reputable media non-profit publishing primary-source chat exports; the messages are authentic, but the analytical leap from handle to person is yours to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unicorn-riot-discord-leaks |
| category | public-records |
| selectorsIn → selectorsOut | username, name → social-profile, associate, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
