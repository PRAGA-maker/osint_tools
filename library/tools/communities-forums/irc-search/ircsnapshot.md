---
id: ircsnapshot
name: ircsnapshot
description: Use when you have an IRC server/network and want its structure — returns channels, users, and user↔channel relationships as a graph.
url: https://github.com/bwall/ircsnapshot
category: communities-forums
path:
- communities-forums
- irc-search
bestFor: Snapshotting an IRC server's channels and users and mapping who is in what, exportable as a Gephi graph.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open-source (MIT) Python tool; no cost, run locally.
opsec: active
opsecNote: This CONNECTS to the target IRC server as a client (it joins/queries), so the server and its operators can see your bot's nick, host, and activity — that is ACTIVE. Use SOCKS4 proxy support and a throwaway nick/host; do not use an attributable identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An established open-source recon tool (packaged in Kali); it faithfully reports what the server exposes, but IRC identities (nicks, realnames) are trivially spoofable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- ircsnapshot
- bwall/ircsnapshot
tags:
- irc
- network-mapping
- recon
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# ircsnapshot

> A Python recon tool that connects to an IRC server and snapshots its structure — every channel, every visible user, and the relationships between them — exportable as a graph for analysis.

## When to use
You're investigating activity on an IRC network (still a hub for hacking, warez, and niche communities) and want a structured picture: which channels exist, who's in them, and how users and channels interconnect. Starting from a known `username`/nick or server, ircsnapshot enumerates the visible topology so you can spot the subject's channels and co-present users (`associate` leads).

## How to use it (`bestInteractionPattern`: cli)
1. Clone github.com/bwall/ircsnapshot and run `python ircsnapshot.py` against the target server (set a throwaway nick/user/realname; enable SSL and a SOCKS4 proxy as needed).
2. Let it enumerate channels and users (optionally checking channels).
3. Convert output with the bundled `to.gexf` for Gephi to visualize user↔channel and user↔link relations.
4. Pivot: channels the subject frequents and co-present nicks are `associate`/community leads; reused nicks feed username enumeration across networks and platforms.

## Inputs → Outputs
- **In:** an IRC server/network (and optionally a `username`/nick of interest)
- **Out:** channels, users, and user↔channel `associate` relationships (`social-profile`-level nick data), Gephi graph
- **Empty/negative result looks like:** few channels/users returned — the server may hide listings (private/keyed channels), restrict LIST, or require registration; you only see what the server exposes to a connecting client.

## Gotchas & OpSec
- ACTIVE: you connect as a real IRC client; the server sees you. Proxy and use a throwaway identity.
- IRC nicks/realnames are freely spoofable — treat identities as claims, corroborate via reused handles elsewhere.
- Private/keyed channels won't appear; the snapshot is only the publicly-visible topology.

## Overlaps ("do both")
- Complements username-enumeration and paste/forum tools — ircsnapshot maps the IRC side; those trace a discovered nick onto the wider web.

## Trust & verifiability
`trust: community` — a solid open-source tool that accurately reports server-exposed structure; the caveat is IRC's weak identity model, so verify who a nick really is elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ircsnapshot |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
