---
id: otzberg-net-find-your-instagram-user-id
name: Otzberg.net | Find your Instagram User-ID
description: Use when you have an Instagram `username` and want its stable numeric user ID — returns the account's permanent device-id/social-profile identifier.
url: https://www.otzberg.net/iguserid
category: social-networks
path:
- social-networks
bestFor: Resolving an Instagram handle to the immutable numeric user ID that survives username changes.
selectorsIn:
- username
selectorsOut:
- social-profile
- device-id
status: live
pricing: free
costNote: Free single-purpose utility; no account or payment.
opsec: passive
opsecNote: You submit only the public handle to a small third-party site; the target is not notified and no login is involved. The lookup itself queries Instagram's public endpoint server-side, so your own IP does not touch Instagram. Otzberg can log the handles you resolve — nothing sensitive, but be aware.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing single-purpose tool by developer Claus Wolf; does one narrow thing (handle → numeric ID) reliably, but depends on Instagram's public API and can break without notice.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- dumpor-io
aliases:
- Instagram User ID Finder
- iguserid
tags:
- instagram
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Otzberg.net | Find your Instagram User-ID

> A narrow utility that converts an Instagram `username` into the account's permanent numeric user ID.

## When to use
You have an Instagram `username` and want the account's **numeric user ID** — the identifier that stays constant even when the person renames their handle or goes private. Anchor your investigation to the numeric ID so you can re-find the account after a handle change, feed API/scraper tools that require an ID, and confirm two handles are (or aren't) the same underlying account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.otzberg.net/iguserid.
2. Enter the target's Instagram `username` (no `@`) and submit.
3. Read back the numeric user ID.
4. Pivot: record the ID as the durable anchor; feed it to viewers/scrapers that key on user ID, and use it later to check whether a re-appeared handle points at the same account.

## Inputs → Outputs
- **In:** `username`
- **Out:** numeric Instagram user ID (`device-id`-style stable identifier for the `social-profile`)
- **Empty/negative result looks like:** an error or no ID returned — usually the username doesn't exist, was just changed, or Instagram's endpoint is temporarily blocking; retry or try an alternate ID finder.

## Gotchas & OpSec
- Depends on Instagram's public API; if Instagram tightens access the tool may fail — keep a backup ID finder handy.
- The tool resolves handle→ID; going the other way (ID→current handle) needs a different lookup.
- OpSec: **passive**; only a public handle leaves your side.

## Overlaps ("do both")
- Pair with `[[dumpor-io]]` — get the stable numeric ID here, then use a viewer like Dumpor to pull the actual posts, stories and follower connections behind that account.

## Trust & verifiability
`trust: community` — a reputable, single-purpose community tool. The numeric ID it returns comes straight from Instagram's own endpoint, so it's authoritative when it works; failures are availability issues, not bad data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | otzberg-net-find-your-instagram-user-id |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
