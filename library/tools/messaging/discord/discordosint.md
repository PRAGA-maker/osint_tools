---
id: discordosint
name: DiscordOSINT
description: Use when you have a Discord `username`/user-ID/server and want the current method and toolchain — returns a curated guide of Discord investigation techniques and tools (a reference, not a lookup).
url: https://github.com/husseinmuhaisen/DiscordOSINT
category: messaging
path:
- messaging
- discord
bestFor: Learning the current Discord investigation workflow and finding the right tool for user-ID, server, and message intelligence.
input: Manual review of documentation and linked resources
output: Investigation guidance, resource links, and workflow references
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open GitHub repository (curated reference). No account; browse or clone.
opsec: passive
opsecNote: Reading the repo is passive and reveals nothing. The Discord techniques it describes are often ACTIVE (joining servers, resolving IDs, scraping) — each downstream action has its own footprint and can expose a puppet account; assess before executing.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known community-maintained Discord OSINT resource collection; a curated directory, not a vetted tool — verify each linked tool independently.
missingPersonsRelevance: high
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
- husseinmuhaisen DiscordOSINT
tags:
- discord
- catalog
- socmint
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# DiscordOSINT

> The reference map for investigating Discord: how to turn a username/ID/server into intelligence, and which tools do each step.

## When to use
Your subject has a Discord presence — a `username`, a numeric user-ID, or a server they frequent — and you need the current, correct methodology rather than guessing. Discord OSINT is fiddly (snowflake IDs, server enumeration, message search, invite tracking) and the tooling shifts; this repo consolidates the techniques and points to the tools that still work. Use it to plan the approach before touching a live server.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/husseinmuhaisen/DiscordOSINT and read the README sections relevant to your selector (user-ID resolution, server intel, message/invite tools).
2. Note the recommended technique and the specific tool(s) linked for it.
3. **Verify the tool** is still live and understand its footprint before running it — Discord actions are often active.
4. Execute the chosen technique in a controlled, sock-puppet Discord environment.
5. Pivot: a resolved user-ID/snowflake yields creation date and cross-server presence; a linked handle feeds broader username mapping.

## Inputs → Outputs
- **In:** a Discord selector you already hold (`username` / user-ID / server) — the repo tells you what to do with it
- **Out:** methodology + tool pointers that lead to `social-profile` and account intelligence — guidance, not data
- **Empty/negative result looks like:** dead links or outdated methods. Curated lists rot and Discord changes fast; treat entries as candidates to verify, and cross-check dates.

## Gotchas & OpSec
- This is a *reference*, not a tool — its value is orientation; the real (and often active) work happens in the tools it links.
- OpSec: reading is passive, but joining servers / resolving IDs / scraping is **active** and can burn a puppet account — plan the footprint first.
- Discord's ToS and rate limits apply to the downstream tools; automated collection can get accounts banned.

## Overlaps ("do both")
- Pairs with the general `[[social-media-osint-tools-collection]]` catalog and Discord snowflake/ID resolvers — this repo scopes the Discord method, those provide breadth and the specific ID-to-timestamp conversions.

## Trust & verifiability
`trust: community` — a popular community resource, but inclusion isn't vetting; confirm each linked tool's legitimacy and current status before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discordosint |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
