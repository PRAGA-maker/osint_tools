---
id: discord-bot-list
name: Discord Bot List
description: Use when you are investigating a Discord community and want to identify or vet a bot seen in a server — returns bot profiles, owner handles, invite metadata, and server counts.
url: https://discord.bots.gg/
category: communities-forums
path:
- communities-forums
- discord-servers
bestFor: Identifying and profiling a Discord bot (its owner, description, and reach) encountered while mapping a server.
selectorsIn:
- username
- device-id
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free public directory; browsing requires no account, though listing your own bot needs a Discord login.
opsec: passive
opsecNote: Browsing the public directory is passive and enumerates only publicly listed bots — no interaction with the target's server or account is required. Actually inviting a listed bot into a server you control is a separate, more active step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run bot directory (discord.bots.gg); listings are self-submitted by bot developers, so descriptions and stats are unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- discord.bots.gg
- DBGG
tags:
- discord
- bot-directory
source: arf-seed
lastVerified: '2026-07-20'
enrichment: full
---

# Discord Bot List

> A public directory of Discord bots — useful for putting a name, owner, and reach to a bot you've seen operating inside a server you're mapping.

## When to use
You are investigating a Discord community (server) as part of building out a subject's online footprint, and you encounter a bot — a moderation, logging, or utility bot — that you want to identify or vet. discord.bots.gg lets you look the bot up by name to see its description, developer/owner handle, GitHub link (if any), and how many servers it runs in. This is a niche pivot: it profiles *bots*, not people, so its direct missing-persons value is low. It matters mainly for understanding how a target community is instrumented or for reaching a bot's owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://discord.bots.gg/.
2. Search by the bot's name or browse by category.
3. Open the bot's listing to read its description, owner/developer handle, prefix, server count, and any linked source repo or support server.
4. If present, follow the developer's linked profile or support server to reach the human behind the bot.
5. Programmatic option: the site exposes an API for querying listed bots at scale.

## Inputs → Outputs
- **In:** a bot `username`/name (or bot application ID, `device-id`)
- **Out:** bot description, owner/developer `username`, support-server / `social-profile` links, server-count metadata
- **Empty/negative result looks like:** no listing — the bot may simply be unlisted or private, which is common; absence here says nothing about the bot's legitimacy.

## Gotchas & OpSec
- This indexes **bots, not members** — do not expect to find a person by searching here.
- Listings are self-submitted and unvetted; server counts and descriptions can be inflated.
- OpSec: browsing is passive; inviting a bot into a server is a distinct active action with its own footprint.

## Overlaps ("do both")
- Pairs with general Discord server-discovery/enumeration tools — those map the community and its members; this identifies the automation running inside it.

## Trust & verifiability
`trust: community` — a developer-submitted directory with no independent verification of listing accuracy; treat owner links as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-bot-list |
| category | communities-forums |
| selectorsIn → selectorsOut | username, device-id → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
