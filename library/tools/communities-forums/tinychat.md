---
id: tinychat
name: Tinychat
description: Use when you have a `username` and want to check for a presence on Tinychat's video-chat platform — a long-running live video-chat community.
url: http://tinychat.com
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a handle maps to a Tinychat account/room on a veteran live video-chat service.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free random one-on-one video chat; premium features (location/gender filtering) are paid, but not needed for a presence check.
opsec: passive
opsecNote: Checking for a profile/handle is passive. Entering a live room or matching with users is active and can expose your camera/presence — never join a room to observe a target without a locked-down sock-puppet setup (no real camera, mic, name, or account).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An established consumer video-chat service; there is no vetted public directory, so any presence found is user-generated and self-reported.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TinyChat
- tinychat.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- video-chat
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Tinychat

> A long-running live video-chat community — useful mainly to check whether a `username` corresponds to an account/room, since the platform itself is real-time and largely ephemeral.

## When to use
You have a `username` you are tracing across platforms and want to see whether it maps to a Tinychat identity, or you have intelligence that a subject frequents a named Tinychat room. Tinychat is a live, mostly ephemeral medium (random one-on-one matching plus rooms), so its OSINT value is limited to confirming a handle/presence rather than pulling stored history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tinychat.com and try the handle as a profile/room path, or search a search engine with `site:tinychat.com "<username>"`.
2. If a profile/room exists, note the handle, any linked identity, and room name — these corroborate a persona and may reuse elsewhere.
3. Do NOT enter a live room to observe a subject unless you are in a fully sandboxed sock-puppet session (no real camera/mic/name); live rooms expose your presence to other participants.
4. Pivot: a confirmed handle feeds cross-platform username enumeration; a linked identity is a corroboration lead.

## Inputs → Outputs
- **In:** `username` (handle or room name)
- **Out:** `social-profile` (Tinychat account/room, any linked identity)
- **Empty/negative result looks like:** no profile/room and no indexed hits — the handle isn't on Tinychat, which is common; the current product is random-match-oriented with little persistent public profile surface.

## Gotchas & OpSec
- The platform is now oriented around anonymous random video chat, so persistent, searchable public profiles are thin — expect confirmation-of-presence at best, not a content archive.
- OpSec: **live rooms are active exposure.** Watching a target in a room means being a visible participant; treat any real-time interaction as active and sandbox accordingly.

## Overlaps ("do both")
- Run the same `username` through a cross-platform username enumerator and other community handle searches — Tinychat only tells you if the handle lives here; the graph of where else it appears comes from the broader sweep.

## Trust & verifiability
`trust: unverified` — a real, established service, but there is no authoritative public directory and any identity is self-asserted. Confirm a match by content/linked accounts, not the handle alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinychat |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
