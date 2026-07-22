---
id: zbin
name: ZBin
description: Use when you already hold a ZBin paste link and want to read its contents — returns whatever the poster put in it (possibly email, password, crypto-wallet); it is NOT searchable.
url: https://zbin.dev/
category: communities-forums
path:
- communities-forums
bestFor: Reading a specific encrypted paste you were handed a link to; useful mainly as negative knowledge — you cannot discover pastes here.
selectorsIn: []
selectorsOut:
- email
- password
- crypto-wallet
status: live
pricing: free
costNote: Free, no account required.
opsec: passive
opsecNote: Viewing a paste is passive, but a "burn after reading" paste is destroyed the moment you open it — screenshot/preserve before you navigate away, and open in a puppet browser in case the link is booby-trapped or tracked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A public PrivateBin instance (client-side-encrypted, zero-knowledge); the operator cannot read pastes, and neither can you without the full link + key.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- linkode-alpha
aliases:
- zbin.dev
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# ZBin

> A zero-knowledge PrivateBin paste host — a place a target might *store* leaked text, not a place you can search for it.

## When to use
Only when your investigation has already surfaced a `zbin.dev/...` link (from a chat log, a forum post, a breach dump, a bio) and you need to read what it points to. Do **not** reach for ZBin hoping to search for a target's pastes — it has no index and no browse function by design.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the full paste URL in a sock-puppet browser — the decryption key lives in the part of the link after the `#`, so you need the whole link intact.
2. If prompted, enter the paste password (if the poster set one).
3. Read/extract the contents. Copy out any selectors it leaks (`email`, `password`, `crypto-wallet`, usernames) into your case notes immediately.
4. Pivot on whatever you extract; the paste itself is a dead-end for further ZBin discovery.

## Inputs → Outputs
- **In:** a complete ZBin paste link (a `url`, not a searchable selector).
- **Out:** the paste body — potentially `email`, `password`, `crypto-wallet`, or other leaked text.
- **Empty/negative result looks like:** "Paste does not exist, has expired, or has been deleted" (or a decryption error if the key/password is wrong) — the content is simply gone, and there is nothing else to query.

## Gotchas & OpSec
- **No search / no browse.** Encryption is client-side and zero-knowledge; you can never enumerate what a person has posted here.
- "Burn after reading" pastes self-destruct on first open — preserve evidence before closing the tab.
- A truncated link (missing the `#key`) is unrecoverable.

## Overlaps ("do both")
- Same limitation as `[[linkode-alpha]]` — both are view-only paste hosts; treat any link to either as read-and-extract, never as a discovery surface.

## Trust & verifiability
`trust: community` — a community-run PrivateBin deployment. The encryption is reputable and open-source, but the instance itself is operated by an unknown party, so treat uptime and longevity as unguaranteed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zbin |
| category | communities-forums |
| selectorsIn → selectorsOut | — → email, password, crypto-wallet |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
