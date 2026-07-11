---
id: disboard
name: Disboard
description: Use when you have a topic, community `name`, or keyword and want to find public Discord servers around it — returns server listings with invite links, tags, and member/activity metadata (`social-profile` leads).
url: https://disboard.org/
category: messaging
path:
- messaging
- discord
bestFor: Discovering public Discord servers by keyword, tag, or category and getting their invite links.
input: Keyword, category, or tag searches
output: Indexed public Discord server listings with invite links and tags
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public Discord-server directory. No account needed to search and browse; joining a server needs a Discord account.
opsec: passive
opsecNote: Searching Disboard is passive — you browse a directory, not the target. The moment you *join* a listed server via its invite, that becomes active: the server (and its members) can see your account. Join from a sock-puppet Discord identity only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-running third-party Discord server listing. Listings are self-submitted by server owners, so descriptions/tags are promotional and unverified; the invite links themselves are real.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- discord-com
- disboard-alternatives
aliases:
- disboard.org
- Discord server list
tags:
- discord
- server-discovery
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Disboard

> The biggest public Discord server directory — search by topic, tag, or community name to find servers and their invite links, then pivot into the ones your subject frequents.

## When to use
You're mapping a subject's community footprint and want to find the public Discord servers tied to a topic, fandom, locality, or community `name` they're associated with. Disboard indexes hundreds of thousands of self-listed servers with keywords and tags; it's a discovery layer that turns "they're into X / from town Y" into concrete servers you can then observe (from a sock puppet) for the person's `username` and activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://disboard.org/.
2. Search by keyword, community `name`, or browse by tag/category (and language/region).
3. Review the listings: each shows the server name, description, tags, member count, and a "Join" invite link.
4. Shortlist servers plausibly linked to your subject; join the relevant ones from a **sock-puppet** Discord account to look for the target's handle.
5. Pivot: a found server + the subject's `username` feeds live `[[discord-com]]` investigation and leak archives; regional/interest servers corroborate `geolocation` and interests.

## Inputs → Outputs
- **In:** keyword / community `name` / tag (and, once inside, a target `username` to look for)
- **Out:** server listings → invite links and metadata (`social-profile` context: which communities exist around a topic)
- **Empty/negative result looks like:** few or no listings for a keyword — the community may not advertise on Disboard (many private/invite-only servers never list), so absence here doesn't mean the community doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none to search; joining requires a Discord login and is where exposure begins.
- OpSec: **passive** while browsing the directory; **active** once you join a server. Always join from a compartmentalised sock-puppet account, never your real Discord.
- Listings are owner-submitted marketing — member counts and descriptions can be inflated; verify inside the server.

## Overlaps ("do both")
- Pairs with `[[discord-com]]` (the platform itself) — Disboard *finds* candidate servers; Discord is where you observe the subject in them. Also complements Discord-leak archives when investigating a handle's history.

## Trust & verifiability
`trust: community` — a legitimate, widely-used directory, but its entries are self-submitted and promotional. The invite links are genuine; treat the descriptive metadata as unverified and confirm anything important by observing the server directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disboard |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
