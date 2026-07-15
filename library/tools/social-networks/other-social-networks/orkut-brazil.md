---
id: orkut-brazil
name: Orkut (archived)
description: Use when you have a `username`/`name` for a subject active before 2014 and want their old Orkut profile via web archives — returns social-profile, name, associates, and photos from historical snapshots.
url: https://orkut.google.com/
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Recovering pre-2014 Orkut profiles, scraps and friend lists for Brazilian/Indian subjects via the Wayback Machine.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- associate
- image
status: down
pricing: free
costNote: Orkut the live service shut down 30 Sep 2014; there is no cost because you query third-party web archives (Wayback Machine, Archive.today), not Orkut itself.
opsec: passive
opsecNote: You are reading archived snapshots on archive.org, not touching any live Orkut endpoint, so the subject cannot be alerted. Normal Wayback OpSec applies — your archive requests are logged by the Internet Archive under your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Content is whatever the Wayback Machine happened to capture before 2014 — coverage is patchy and snapshots may be partial. Authoritative as an archive, but incomplete by nature.
missingPersonsRelevance: high
coverage:
- br
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- wayback-machine
- archive-today
aliases:
- Orkut
- orkut.google.com
- orkut.com
tags:
- other-social-networks
- archived
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Orkut (archived)

> Google's defunct social network (huge in Brazil and India until 2014) reachable only through web archives — a time capsule of a subject's mid-2000s to early-2010s online life.

## When to use
Your subject was likely active online between roughly 2004 and 2014 and has a Brazilian or Indian connection. Orkut was dominant in those markets, so an archived profile can yield a period `username`, real `name`, friend list (`associate`s), community memberships, and photos that no longer exist anywhere else — invaluable for cold/historical cases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Find the likely Orkut profile URL pattern: old profiles used numeric IDs (`orkut.com/Main#Profile?uid=...`) or, later, `orkut.google.com`.
2. Paste that URL (or `orkut.com/<username>`) into the Wayback Machine (`https://web.archive.org/web/*/orkut.com/*`) and Archive.today.
3. Browse captured snapshots by date; open friend lists and community pages, which often survived even when a profile page didn't.
4. Screenshot/save anything useful immediately — archived pages can be de-listed.
5. Pivot: friend-list names feed associate mapping; a period username feeds cross-platform enumeration.

## Inputs → Outputs
- **In:** `username` or `name` (to reconstruct the old profile URL)
- **Out:** `social-profile` (archived), `name`, `associate` (friends/communities), `image` (photos)
- **Empty/negative result looks like:** "This URL has not been captured" in Wayback — try alternate URL formats (orkut.com vs orkut.google.com, numeric uid) before concluding no capture exists.

## Gotchas & OpSec
- The live site is **gone** — never expect orkut.google.com to load; everything runs through archives.
- Wayback coverage of Orkut is spotty and often missing images/JS; profiles may render partially.
- OpSec: fully passive; the subject cannot see archive access.

## Overlaps ("do both")
- Pairs with the Wayback Machine and Archive.today generally — try both, as their Orkut captures differ.
- Combine with Brazilian people-search sources when a real name/associate emerges from the old friend list.

## Trust & verifiability
`trust: unverified` — the data is genuine archived Orkut content but incomplete and unmaintained; treat gaps as "not captured," not "did not exist."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | orkut-brazil |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name, associate, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
