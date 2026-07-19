---
id: paaster
name: paaster
description: Use when you hold a `paaster.io` link (or need to preserve text) and want to read/store an end-to-end-encrypted paste — returns the paste content (`document-id`) only if you have the key in the URL.
url: https://paaster.io/
category: communities-forums
path:
- communities-forums
bestFor: Reading or preserving an end-to-end-encrypted paste whose decryption key is in the shared link.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (self-hostable); no account required to create or view a paste.
opsec: passive
opsecNote: Content is end-to-end encrypted — the decryption key lives in the URL fragment (after #) and never reaches the server, so paaster itself can't read pastes and can't index/search them. You can only open a paste if you were given the full link. Opening one is passive and unlogged to any subject; treat the key-bearing URL as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source E2EE pastebin (github.com/WardPearce/paaster); code is auditable, but any content is user-submitted and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- paaster.io
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# paaster

> An end-to-end-encrypted, open-source pastebin: the server stores only ciphertext, and the decryption key rides in the URL fragment — so a paaster link is all-or-nothing.

## When to use
Two cases. (1) You've obtained a `paaster.io` link (in a chat log, forum post, or breach discussion) and need to read what it holds. (2) You want to preserve your own findings in a paste the host can't read or hand over. Because it's E2EE, paaster is *not* a searchable leak surface — you can't sweep it for a subject's data; you either have the key-link or you have nothing.

## How to use it (`bestInteractionPattern`: web-manual)
1. To read: open the full `paaster.io/#...` link exactly as given, including everything after the `#` — that fragment is the decryption key.
2. The browser decrypts client-side and renders the text; without the complete fragment the content is unrecoverable.
3. To preserve: go to https://paaster.io/, paste your text, and copy the generated key-link somewhere safe.
4. Note there is no directory or search — you cannot browse other people's pastes.
5. Pivot: decrypted content may expose `email`, `username`, credentials, or `crypto-wallet` strings to feed onward.

## Inputs → Outputs
- **In:** a full paaster key-link (`document-id` + embedded key)
- **Out:** the decrypted paste content (`document-id`)
- **Empty/negative result looks like:** a decryption error or blank paste — usually a truncated URL (missing the `#` fragment) or an expired/deleted paste; there is no way to brute-force the missing key.

## Gotchas & OpSec
- The key is in the URL fragment — if you only have the path without the `#...`, the paste is permanently unreadable to you.
- Not indexable: don't expect Google dorks or a search box to find pastes here, unlike a plaintext pastebin.
- OpSec: passive; the operator can't see plaintext, so this is a privacy-respecting place to stash notes — but guard the key-link, since anyone with it can read the paste.

## Overlaps ("do both")
- Contrast with plaintext pastebins like [[tutpaste]] — those are *searchable* leak surfaces you can dork; paaster is encrypted and only reachable with the key. Use plaintext bins for discovery, paaster for handling links you already have or storing sensitive notes.

## Trust & verifiability
`trust: community` — the code is open-source and the crypto model is sound, but paste *content* is unverified user data; corroborate anything you decrypt.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paaster |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
