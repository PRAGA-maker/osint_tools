---
id: verybin
name: Verybin
description: Use when you have found a `verybin.com` link in a subject's trail and want to read it — decrypts a client-side-encrypted paste you already have the link (and key) for.
url: https://www.verybin.com/
category: communities-forums
path:
- communities-forums
bestFor: Decrypting a specific Verybin link you already possess; NOT a searchable leak index (zero-knowledge server, not indexed).
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open-source (PrivateBin-based); no account, no server-side plaintext.
opsec: passive
opsecNote: Verybin is zero-knowledge — text is AES-encrypted in the browser and the decryption key lives in the URL fragment, so opening a link decrypts locally and nothing is sent in the clear. Open unknown links in a sandbox in case the decoded content is malicious, and never paste a target's data into it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source PrivateBin instance; the mechanism is publicly auditable, but you must trust the operator not to tamper with the served JavaScript. Pastes can be set to expire or burn-after-reading.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- verybin.com
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Verybin

> An anonymous, end-to-end-encrypted PrivateBin pastebin — for OSINT it is a *decoder*, not a source: you can only read a paste you already have the full link (and embedded key) for.

## When to use
You have come across a `verybin.com/...` link (in a chat, a forum post, a bio, or a dump) and need to read what it holds. Because Verybin encrypts client-side and stores no plaintext or index, you cannot search it for a subject's leaked data — Google and the server itself never see the content. Its only investigative use is opening a specific link you already possess, rather than proactive discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the complete `verybin.com/?...#...` URL you found — the part after `#` is the decryption key; do not truncate it.
2. Open it in a sandboxed/sock-puppet browser; the page decrypts the paste locally.
3. If the paste is password-protected, you will also need the password from your source.
4. Read and snapshot the content immediately — pastes may be set to expire or burn-after-reading and can vanish.
5. Pivot: any selectors inside (emails, passwords, handles) feed breach-check and username tools.

## Inputs → Outputs
- **In:** `document-id` (a complete Verybin link, including the `#` key)
- **Out:** the decrypted paste text (`document-id` content)
- **Empty/negative result looks like:** a "paste does not exist / expired" message, or a decryption failure from a truncated/altered key — meaning the link is gone or incomplete, not that content was hidden server-side (there is none to hide).

## Gotchas & OpSec
- Human-in-the-loop: none, but treat unknown decoded content as potentially hostile.
- OpSec: **passive** — decryption is local; nothing about the paste is sent to the server on view. The trade-off is there is no index to search, so it is useless for discovery.
- Preserve the URL fragment exactly; shorteners or copy/paste that drop the `#key` break decryption permanently.

## Overlaps ("do both")
- Pairs with searchable/indexed pastebins and breach search when your goal is to *find* a subject's leaked data — those can be queried, which Verybin fundamentally cannot; behaves like [[nopaste]] and [[defuse]].

## Trust & verifiability
`trust: community` — open-source and auditable; the zero-knowledge design means the plaintext you decrypt is exactly what the sharer encrypted, provided the operator has not tampered with the client code.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | verybin |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
