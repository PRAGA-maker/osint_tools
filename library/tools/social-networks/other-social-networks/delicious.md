---
id: delicious
name: Delicious
description: Use when you have a `username` and want that person's public social-bookmarking profile and saved links to infer interests and other handles — but the service is defunct, so this returns nothing live.
url: https://del.icio.us/
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Historically, mining a person's public bookmark collection (saved URLs + tags) to profile interests and surface linked accounts.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: down
pricing: free
costNote: Was free; the service has shut down, so there is nothing to pay for or query.
opsec: passive
opsecNote: Moot while offline. Historically, viewing a public bookmark profile was passive and did not notify the owner. Archived copies (Wayback) are equally passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Once a mainstream social-bookmarking service, now defunct; the del.icio.us domain no longer serves a working product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- del.icio.us
- Delicious bookmarking
tags:
- social-bookmarking
- other-social-networks
- defunct
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Delicious

> A once-mainstream social-bookmarking site — a person's saved links and tags were a rich interest/handle map — but it is defunct and no longer serves a working product.

## When to use
Do not reach for the live site: del.icio.us is down. It matters only for historical/archived accounts. If your subject was active online in roughly 2005–2015 and you have a `username`, an archived Delicious profile can still reveal what they bookmarked and how they tagged it — a strong interest and reused-handle signal — but you must go through web archives, not the dead domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. The live site (https://del.icio.us/) no longer functions as a bookmarking service — do not expect a working profile lookup.
2. To recover historical data, query the Wayback Machine for `del.icio.us/<username>` (and the later `delicious.com/<username>`) to view archived snapshots of that user's public bookmarks and tags.
3. Read the archived collection for interests, projects, and — crucially — other URLs/handles they linked to, which pivot to live accounts.
4. Pivot: reused `username` feeds cross-platform username search; bookmarked domains/handles feed direct account checks.

## Inputs → Outputs
- **In:** `username` (against an archive, not the live site)
- **Out:** (historical) `social-profile`, saved links/tags, other `username`s referenced
- **Empty/negative result looks like:** the live domain returns nothing usable; an archive query with no snapshots means that user either never had a public Delicious or it was never crawled — not proof of anything.

## Gotchas & OpSec
- Human-in-the-loop: none — but also no live function; everything is archive-only.
- OpSec: passive. Archived viewing does not touch the subject.
- Data is frozen in time: anything found reflects the person years ago, not now. Use it for handle/interest pivots, not current status.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]`-style archive tools generally, since recovering any Delicious data now depends entirely on web archives rather than the dead service.

## Trust & verifiability
`trust: unverified` — the service is defunct; only archived snapshots remain, and those are historical, so treat anything recovered as a dated lead rather than current fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | delicious |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
