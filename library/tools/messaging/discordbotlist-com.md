---
id: discordbotlist-com
name: Discord Bot List — Servers
description: Use when you have a community/topic `name` and want to discover public Discord servers (and OSINT bots) around it — returns `social-profile` links to joinable servers with member counts and descriptions.
url: https://discordbotlist.com/servers
category: messaging
path:
- messaging
bestFor: Discovering public Discord servers by topic/name (and finding listed bots) as an entry point into communities a subject may inhabit.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public directory; browsing and searching require no account (joining a server does).
opsec: passive
opsecNote: Browsing the directory is passive and anonymous. The moment you JOIN a listed server you become visible to its members/admins — do that only from a sock-puppet Discord account, never your own, and expect join logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run listing site (51k+ self-submitted servers); it indexes what owners chose to advertise, so it is a discovery aid, not a complete or authoritative map of Discord.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- pixelatomy-com
- discord-bots
aliases:
- discordbotlist.com
- Discord Bot List servers
tags:
- discord
- Discord Related Sites
- server-discovery
- directory
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Discord Bot List — Servers

> A browsable directory of tens of thousands of public Discord servers (and bots) — a way in when you know the topic or community name but not the invite.

## When to use
You have a community, brand, game, or interest `name` tied to your subject and want to find the public Discord servers around it — a plausible place the person congregates — or you're hunting for OSINT-useful Discord bots. It's a discovery layer: it turns a topic into candidate servers you can then join (carefully) and observe.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://discordbotlist.com/servers.
2. Search or filter by topic, tags, size, popularity, or activity.
3. Read each listing: server name, description, member/online counts, and a join link.
4. Shortlist servers matching the subject's interests/communities.
5. Pivot: join a candidate server from a sock-puppet account to look for the subject's handle; feed found handles into Discord ID/age tools like `[[pixelatomy-com]]`.

## Inputs → Outputs
- **In:** community/topic `name` or keyword/tag
- **Out:** `social-profile` links to public Discord servers, with member counts and descriptions
- **Empty/negative result looks like:** few/irrelevant results — the community isn't listed here (many servers are invite-only or never submitted), so absence tells you little; try other server-discovery lists.

## Gotchas & OpSec
- Only self-submitted, public servers appear — it is far from a complete index of Discord.
- Joining is the risky step: it exposes your account to admins/members and is logged — sock-puppet only.
- It doesn't take a username/phone; it's topic-based discovery, not person lookup.

## Overlaps ("do both")
- Pairs with `[[pixelatomy-com]]` and Discord username/ID tools — this finds the servers; those decode and age-check the accounts you find inside them.

## Trust & verifiability
`trust: community` — a self-submission directory; useful for leads, but treat coverage as partial and unverified.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | discordbotlist-com |
