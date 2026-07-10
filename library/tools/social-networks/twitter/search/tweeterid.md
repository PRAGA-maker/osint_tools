---
id: tweeterid
name: TweeterID
description: Use when you have an X/Twitter `username` (or numeric ID) and want the stable numeric account ID, which survives handle changes — returns the mapped social-profile ID.
url: https://tweeterid.com/
category: social-networks
path:
- social-networks
- twitter
- search
bestFor: Converting an X/Twitter handle to its permanent numeric ID (and back).
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web converter; no account.
opsec: passive
opsecNote: Resolves public account metadata through a third-party page; the target is not notified. Nothing sensitive is disclosed beyond the handle you look up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small third-party utility; the numeric ID it returns is verifiable against X itself, so the risk is low even though the operator is unaudited.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- x-com
- wayback-machine
aliases:
- tweeterid.com
tags:
- twitter
- account-id
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# TweeterID

> A one-field converter between an X/Twitter @handle and its permanent numeric account ID — the ID that stays constant even when the person renames the account.

## When to use
You have an X/Twitter `username` and want its numeric ID because you need an identifier that survives handle changes. If a subject renames or a handle gets recycled, the numeric ID is what lets you keep tracking the *same* account across archives, third-party datasets, and deleted-tweet tools. Also works in reverse: given a numeric ID from a dataset, recover the current handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tweeterid.com/.
2. Paste the @handle (to get the numeric ID) or the numeric ID (to get the current handle) and submit.
3. Read the mapped pair.
4. Pivot: use the numeric ID in archive/deleted-tweet tools and datasets; a handle recovered from an ID feeds profile review and username enumeration.

## Inputs → Outputs
- **In:** `username` (@handle) or numeric `social-profile` ID
- **Out:** the corresponding `social-profile` (numeric ID ↔ handle)
- **Empty/negative result looks like:** "not found" means the account is suspended, deleted, or never existed — a recycled handle will resolve to whoever holds it now, so confirm the ID matches your subject's known ID.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; no alert to the target.
- Handle recycling: a handle you knew may now belong to a different person — anchor on the numeric ID, not the name.

## Overlaps ("do both")
- Pairs with `[[x-com]]` — verify the resolved handle/ID against the live X profile.
- Pairs with `[[wayback-machine]]` — with the stable ID/handle, pull archived snapshots of the account over time.

## Trust & verifiability
`trust: unverified` — an unaudited third-party utility, but its single output (the numeric ID) is independently checkable against X, so it is low-risk in practice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweeterid |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
