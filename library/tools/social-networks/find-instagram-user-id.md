---
id: find-instagram-user-id
name: Find Instagram User ID
description: Use when you have an Instagram `username` and want its stable numeric account ID — returns the numeric Instagram user ID that persists across handle changes.
url: https://codeofaninja.com/tools/find-instagram-user-id/
category: social-networks
path:
- social-networks
bestFor: Resolving an Instagram handle to its permanent numeric ID so you can track the account even if the username changes.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: passive
opsecNote: You submit a public username to a third-party lookup that queries Instagram's public endpoints on your behalf — the subject is not notified. The tool operator sees the handle you queried; use a sock-puppet browser. This is a read-only ID resolution, not a login or scrape of private data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing developer utility (Code of a Ninja) that resolves usernames to Instagram IDs via public data. Reliability depends on Instagram not changing its endpoints; if it breaks, equivalent tools abound.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Instagram User ID finder
- codeofaninja instagram id
tags:
- instagram
- account-id
- pivot
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Find Instagram User ID

> A small utility that converts an Instagram `@handle` into its permanent numeric account ID — the stable key that survives username changes and unlocks ID-based tooling.

## When to use
You have an Instagram `username` and want its numeric ID because (a) you need an identifier that won't change if the subject renames the account, (b) a downstream tool/API takes an ID not a handle, or (c) you want to detect that a "new" account is actually a renamed old one (same ID). A foundational pivot step in Instagram investigations, not an end in itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://codeofaninja.com/tools/find-instagram-user-id/ in a sock-puppet browser.
2. Enter the `username` (without the @) and submit.
3. Read the returned numeric ID.
4. Record it against the account so you can spot future renames (the ID stays constant).
5. Pivot: feed the ID into Instagram OSINT tools/scrapers that key on account ID, or use it to confirm two handles are the same underlying account.

## Inputs → Outputs
- **In:** `username` (Instagram handle)
- **Out:** numeric Instagram account ID (a stable `social-profile` identifier)
- **Empty/negative result looks like:** error or no ID — the handle doesn't exist, was deleted/renamed, or Instagram changed its public endpoint and the tool is temporarily broken. Try a mirror/alternative ID-lookup before concluding the account is gone.

## Gotchas & OpSec
- These tools break whenever Instagram alters its public endpoints — keep a couple of alternatives handy.
- It resolves public account IDs only; it does not bypass privacy or reveal private content.
- The ID is the value: record it early, because a subject renaming to evade you keeps the same ID.

## Overlaps ("do both")
- Pairs with Instagram username enumeration and scraping tools — this supplies the stable ID they consume, and it detects handle-swap evasion that name-based tracking misses.

## Trust & verifiability
`trust: community` — a well-known developer utility using Instagram's public data; the returned ID is authoritative when it works, but availability tracks Instagram's endpoint changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-instagram-user-id |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
