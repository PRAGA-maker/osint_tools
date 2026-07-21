---
id: limetorrents
name: LimeTorrents
description: Use when you have a `username`/uploader handle or a content keyword and want to see torrents linked to it — returns uploader `social-profile` handles and content metadata.
url: https://www.limetorrents.cc
category: search-engines
path:
- search-engines
bestFor: Searching a torrent index by keyword or uploader to trace what content a handle has distributed.
selectorsIn:
- username
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to search and browse; ISP/DNS blocking is common, so the working domain rotates between mirrors.
opsec: passive
opsecNote: Searching the index (reading listings) is passive. Do NOT download torrents during an investigation — connecting to a swarm exposes your IP to every peer and may be illegal; stay on the metadata/listing layer and use a sock-puppet browser (many mirrors serve intrusive ads/malvertising).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running but frequently-blocked torrent index reachable mainly via rotating mirror/proxy domains; listings are user-uploaded and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- limetorrents.cc
- limetorrents mirror
tags:
- toddington
- curated-directory
- specialty-search
- torrents
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# LimeTorrents

> A general torrent index — niche in people-work, but occasionally useful for tracing what content a specific uploader handle has distributed, or corroborating a subject's alias.

## When to use
This is a specialty, low-relevance tool. Reach for it only when a case genuinely touches file-sharing: you have an uploader `username`/handle you want to profile (what did they upload, when, under what description), or you're checking whether a distinctive alias appears as an uploader. The OSINT value is the metadata layer — uploader names, upload dates, and content descriptions — never the download itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Reach a working mirror (the `.cc` domain frequently redirects to a live mirror such as `.fun`/`.lol`) in a sock-puppet browser with strong ad-blocking.
2. Search by keyword or, where supported, browse an uploader's page to enumerate their torrents.
3. Read the listing metadata only: uploader handle, upload date, size, seeders, and the content description — these are the leads.
4. **Stop at the listing.** Do not open the magnet link or download; that joins the swarm and exposes your IP.
5. Pivot: run a distinctive uploader handle through a cross-platform username search to link it to other identities.

## Inputs → Outputs
- **In:** `username`/uploader handle or content keyword
- **Out:** uploader `social-profile` handle, upload timeline, content descriptions/metadata
- **Empty/negative result looks like:** no results (or a dead mirror) — the handle/keyword isn't indexed here, or the current domain is blocked; try another mirror before concluding.

## Gotchas & OpSec
- **Legal/OpSec risk:** downloading is out of scope and hazardous — stay on the metadata layer. Mirrors are heavy with malvertising; use ad-block and a disposable browser.
- Availability is unstable: expect DNS/ISP blocks and rotating domains.
- Genuinely low people-search relevance — use only when file-sharing is directly material to the case.

## Overlaps ("do both")
- Pairs with cross-platform username finders — a distinctive uploader handle found here can be pivoted to accounts on mainstream platforms.

## Trust & verifiability
`trust: unverified` — an unofficial, frequently-mirrored index of user-uploaded content; treat every listing as unverified and the download layer as off-limits.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | limetorrents |
| category | search-engines |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
