---
id: osint-discord-resources-github-com
name: OSINT Discord resources (github.com)
description: Use when you have a Discord `username`, user ID or server invite and want the method to pivot on it — returns a curated toolset for Discord user/server/ID lookups.
url: https://github.com/Dutchosintguy/OSINT-Discord-resources
category: messaging
path:
- messaging
bestFor: A curated jump-off list of Discord OSINT tools and techniques for searching users, servers and IDs.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free public GitHub repository; it's a reference list, and most linked tools are also free (some third-party lookup sites may gate features).
opsec: passive
opsecNote: Reading the repo is passive. The techniques it points to vary — server-search engines are passive, but joining a server or messaging a user to confirm identity is active and exposes your account. Use a sock-puppet Discord account for any live pivoting, and note Discord user IDs are stable pivots that leak account-creation timestamps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained resource list (Dutchosintguy). It's a directory of third-party tools, so its value depends on those tools staying alive — expect some link rot and verify each still works.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- disboard
- discord-lookup
aliases:
- OSINT-Discord-resources
- Dutchosintguy Discord OSINT
tags:
- discord
- Discord Related Sites
- resource-list
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# OSINT Discord resources (github.com)

> A curated GitHub directory of Discord OSINT tools and techniques — the map for pivoting on a Discord username, user ID, or server invite.

## When to use
You have a Discord lead — a `username`, a numeric user ID, or a server invite — and need the *right* tool and method to pivot on it: find which servers a handle appears in, resolve a user ID, decode a Discord snowflake ID into an account-creation timestamp, or discover public servers by topic. Rather than a single lookup, this repo consolidates the current Discord OSINT toolset (server-search engines, user-lookup sites, ID guides, the Discord search-filter syntax). Reach for it to orient before you pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo and skim the sections: server search (Disboard, Discord.me, etc.), user lookup, ID extraction, and the "attack surface" reference PDF.
2. Pick the tool matching your lead — e.g. a server-search engine for a `username`, or a snowflake→timestamp converter for a user ID.
3. Follow the technique (get a user's ID via developer mode; use Discord's native search filters in a server you're in).
4. Verify each linked tool still works — resource lists rot over time.
5. Pivot: a resolved user ID (`metadata-exif`-style creation timestamp) and cross-server presence feed identity correlation; a matching handle feeds username enumeration elsewhere.

## Inputs → Outputs
- **In:** Discord `username`, user ID, or server invite (`social-profile`)
- **Out:** routes to `social-profile` (servers/accounts), `metadata-exif` (snowflake creation timestamps, IDs)
- **Empty/negative result looks like:** the repo can't itself return a "no match" — but the tools it points to will. A dead link in the list means that tool is gone; move to the next.

## Gotchas & OpSec
- It's a directory, not a lookup — the intelligence comes from the tools it links, some of which will be stale.
- Passive to read, but *joining* a server or DMing a user to confirm identity is active and exposes your (sock-puppet) account — never use a personal Discord.
- Discord user IDs (snowflakes) are durable pivots and encode account-creation time — useful and stable.

## Overlaps ("do both")
- Points you to `[[disboard]]` (public server discovery) and `[[discord-lookup]]` (ID/user resolution) among others — use the repo to choose, then run those tools directly.

## Trust & verifiability
`trust: community` — a maintained but community-run list of third-party tools. Reliable as a starting map; verify each linked tool independently, since their availability and accuracy vary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-discord-resources-github-com |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
