---
id: discord-me
name: Discord.me
description: Use when you have a `username` or topic and want to find public Discord servers a subject may frequent — returns server listings with categories, member counts, and invites.
url: https://discord.me/
category: social-networks
path:
- social-networks
bestFor: Browsing/searching a public Discord server directory by category or topic to locate communities of interest.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search and browse; paid "sponsored" placement exists only for owners promoting their own server.
opsec: passive
opsecNote: Searching the directory queries Discord.me, not any target. Joining a discovered server via its invite is active and puts you in the member list — do that only from a sock-puppet Discord account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running public Discord server directory; listings are owner-submitted and promotional, so member counts and descriptions are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- top-gg
aliases:
- Discord Me
- discord.me
tags:
- discord
- community-directory
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Discord.me

> A public directory of Discord servers organized by category (gaming, anime, community, roleplay, and 60+ topics) — search or browse to find communities and their invite links.

## When to use
You want to locate the Discord communities tied to a subject's interests, handle, or a topic you're tracking. Discord.me turns a `username` or theme into a list of joinable public servers, which is a starting point for finding where a person participates before observing from a sock-puppet. It's a second directory to run alongside Top.gg, since the two index overlapping-but-different sets of servers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discord.me/ and use the search box or browse by category/tag.
2. Search a topic, community name, or `username` associated with your subject.
3. Read each listing: category, tags, member count, "recently bumped" activity, and the invite link.
4. Note any owner/staff handles or linked accounts shown in the description.
5. Join only from a sock-puppet Discord account if you need to observe inside (see OpSec).
6. Pivot: a server owner/handle → `social-profile`/username enumeration; a community → its public membership for further leads.

## Inputs → Outputs
- **In:** `username`, community `name`, or topic
- **Out:** server listings, categories, member counts, invite links, owner/staff `social-profile` hints
- **Empty/negative result looks like:** no matching servers — the community isn't listed here (many servers list nowhere or only on other directories); not proof it doesn't exist.

## Gotchas & OpSec
- Covers only opted-in servers — a small slice of all Discord; combine with other directories.
- Listings are owner-submitted marketing; member counts and descriptions are unverified.
- Passive while browsing; **joining** a server exposes you in its member list — always use a sock-puppet account.

## Overlaps ("do both")
- Pairs with `[[top-gg]]` — the other major Discord directory; run both because each surfaces servers the other omits.

## Trust & verifiability
`trust: community` — an established but community-run, self-listing directory; verify any community's real activity, ownership, and membership inside Discord before relying on directory metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discord-me |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
