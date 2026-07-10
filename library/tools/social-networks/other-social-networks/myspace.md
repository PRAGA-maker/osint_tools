---
id: myspace
name: Myspace
description: Use when you have a `name` or `username` (often music/2000s-era) and want an old Myspace profile — returns `social-profile`, photos and social connections from active and legacy accounts.
url: https://myspace.com/
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Recovering legacy 2000s-era social presence — old Myspace profiles can carry real names, photos, hometowns, friends, and music tastes long predating a subject's current footprint.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to browse and search; a free account gives fuller access but public profiles are viewable without one.
opsec: passive
opsecNote: Browsing public Myspace profiles is passive and not shown to the profile owner. If you log in to see more, use a sock-puppet account. Note Myspace's 2019 server migration destroyed much pre-2016 uploaded media.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A genuine, still-operating platform, now a shadow of its peak. Surviving profiles are authentic but data is patchy after the 2019 media loss; treat gaps as loss, not absence.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MySpace
- myspace.com
tags:
- social-networks
- legacy
- historical
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Myspace

> The 2000s social giant, still online — a time capsule of old profiles that can hand you a subject's real name, hometown, teenage photos, and friend network from before they curated their modern presence.

## When to use
You have a `name` or `username` for someone who was online in the mid-2000s, or a music/scene connection, and current platforms are thin or too polished. Myspace profiles from that era are often unguarded — real names, schools, hometowns, photos, top-friends lists — making it a strong source for historical identity, early associates, and locating clues in a missing-person or genealogy-adjacent case. Especially useful for musicians/bands, who kept Myspace pages long after others left.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://myspace.com/ and use its people/search feature for the `name`, `username`, or artist/band name.
2. Also try the `myspace.com/<username>` direct URL if you have a candidate handle.
3. Open a matching profile: read bio, location, photos (`image`), music, and connections/top friends (`associate`s).
4. For destroyed/altered content, check the Wayback Machine for archived versions of the profile URL.
5. Pivot: an old username → cross-platform enumeration (people reuse handles for decades); hometown/school → localized records; friends → `associate` mapping.

## Inputs → Outputs
- **In:** `name`, `username`, or artist/band name
- **Out:** `social-profile` (Myspace profile), `image` (photos), plus location, connections, music tastes
- **Empty/negative result looks like:** no profile, or a profile stripped of pre-2016 media (the 2019 migration deleted ~12 years of uploaded content). "Found but empty of old photos" usually means data loss, not that the account was inactive — check the Wayback Machine.

## Gotchas & OpSec
- **2019 data loss:** roughly all music/photos uploaded 2003–2015 were destroyed; surviving text/metadata may still help. Use web archives to recover lost pages.
- Search is weak; direct-URL guessing and Google `site:myspace.com` X-ray often work better.
- OpSec: **passive** — public browsing; log in only with a puppet.

## Overlaps ("do both")
- Pairs with the `[[wayback-machine-2]]`/Internet Archive for recovering deleted profiles, and with username enumerators for reused handles.
- Google `site:myspace.com "<name>"` complements the native search.

## Trust & verifiability
`trust: unverified` — authentic platform, but heavily degraded by data loss; corroborate old-profile claims (name, location) against archives and other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | myspace |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
