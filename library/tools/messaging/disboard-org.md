---
id: disboard-org
name: Disboard (Discord Server Directory)
description: Use when you have a keyword, community name, or `username` and want to find public Discord servers around it — returns listed servers with invite links, member counts, tags, and descriptions.
url: https://disboard.org/servers
category: messaging
path:
- messaging
bestFor: Discovering public Discord servers by keyword/tag/community name, with invite links and member counts.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; no account needed to search and follow invite links.
opsec: passive
opsecNote: Browsing Disboard is passive and touches no target. The exposure comes when you JOIN a server — do that only from a sock-puppet Discord account, since your profile becomes visible to members and admins.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known third-party Discord server listing site; it indexes servers that opt in to be listed, so coverage is partial and self-selected, not exhaustive.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Disboard
- disboard.org
tags:
- discord
- Discord Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Disboard (Discord Server Directory)

> The largest public Discord server directory — a keyword-and-tag search that turns a topic, community name, or handle into a list of joinable servers with invite links and member counts.

## When to use
You have a keyword, community/brand name, or a `username` that might name a server, and you want to find the public Discord communities connected to it — e.g. locating a subject's community, a topic-based group, or a server tied to a handle. Discord itself has no global search, so a directory like Disboard is the main discovery route for public servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://disboard.org/servers and search by keyword/tag, or browse categories.
2. Read the listings: server name, description, tags, member count, and a "Join" invite link.
3. Shortlist servers relevant to your subject/topic; note member counts and descriptions for context.
4. Join only from a **sock-puppet** Discord account; do not use your real identity.
5. Pivot: inside a server you can observe members and usernames (`social-profile`), which feed username enumeration and Discord-specific lookups.

## Inputs → Outputs
- **In:** keyword / community name / `username`
- **Out:** listed Discord servers with invite links, member counts, tags → server/community `social-profile`s
- **Empty/negative result looks like:** no listed servers — the community may be private/invite-only (not listed) or simply not on Disboard; absence is not proof it doesn't exist.

## Gotchas & OpSec
- Opt-in coverage: only servers that choose to list appear; many communities are unlisted.
- Join risk: the real OpSec cost is joining — your Discord profile is exposed to admins/members; use a throwaway account.
- Discovery, not profiling: it finds servers, not individuals; person-level work happens after you're inside.

## Overlaps ("do both")
- Pairs with Discord username/OSINT tools and with `[[google-cse-for-telegram-links]]`-style directory searches — Disboard finds the Discord communities, other tools profile the accounts within them.

## Trust & verifiability
`trust: community` — a third-party opt-in directory; listings are genuine servers but coverage is partial, so don't treat an empty search as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disboard-org |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
