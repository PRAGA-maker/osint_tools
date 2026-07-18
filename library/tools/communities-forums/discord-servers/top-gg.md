---
id: top-gg
name: Top.gg
description: Use when you have a `username` or community/bot name and want to discover public Discord servers and bots — returns server/bot listings with owners, member counts, and invite links.
url: https://top.gg/
category: communities-forums
path:
- communities-forums
- discord-servers
bestFor: Discovering public Discord servers and bots by name/topic, with member counts and invites — an entry point into communities a subject frequents.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to browse and search; it also offers a public API. Paid options exist only for owners promoting their own listings.
opsec: passive
opsecNote: Browsing Top.gg's public listings queries Top.gg, not any target. Note that following a server invite and joining the Discord IS active (you appear in the member list) — enumerate on Top.gg first and join only from a sock-puppet Discord account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The largest public Discord server/bot directory; listings are self-submitted by owners, so vote counts and descriptions are promotional and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- discord-me
aliases:
- Top.gg
- Discord Bot List
tags:
- discord
- community-directory
- arf-seed
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Top.gg

> The biggest public directory of Discord servers and bots — search by name or topic to find communities, their owners, member counts, and invite links.

## When to use
You want to map the Discord communities around a subject, a topic they care about, or a bot/brand they run. Top.gg turns a `username`, community name, or interest into a set of discoverable public servers with invite links and metadata — a starting point for finding where a person is active before you (carefully) join to observe. Also useful to identify a bot's developer/owner or a community's staff, which can pivot to usernames and profiles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://top.gg/ and use the search (servers or bots) or browse by tag/category.
2. Enter a community name, topic, or `username`/brand associated with your subject.
3. Read each listing: description, tags, member count, the server's invite link, and (for bots) the developer/owner.
4. Note owners/staff usernames and linked social accounts shown in descriptions.
5. Do NOT join casually — plan the join from a sock-puppet Discord account (see OpSec) if you need to observe inside.
6. Pivot: an owner's `username` → username enumeration and profile search; a server → its public members/staff for further leads.

## Inputs → Outputs
- **In:** `username`, community/bot `name`, or topic
- **Out:** server/bot listings, owner/developer `social-profile`s and `username`s, invite links, member counts
- **Empty/negative result looks like:** no matching listings — the community isn't listed on Top.gg (many servers aren't); absence here doesn't mean the community doesn't exist.

## Gotchas & OpSec
- Only lists servers whose owners opted in — a large fraction of Discord is invisible here.
- Listing text and vote counts are owner-supplied marketing; treat descriptions and popularity as unverified.
- Passive while browsing, but **joining** a server via an invite makes you visible in its member list — always join from a sock-puppet, never your real account.

## Overlaps ("do both")
- Pairs with `[[discord-me]]` — a second, overlapping Discord directory; run both since each indexes servers the other misses.

## Trust & verifiability
`trust: community` — a large, well-known directory, but every listing is self-submitted and promotional, so verify community details and ownership inside Discord itself before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | top-gg |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
