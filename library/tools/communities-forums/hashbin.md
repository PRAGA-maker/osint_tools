---
id: hashbin
name: HashBin
description: Use when you have a `hashb.in` paste link (with its key in the URL fragment) and want to read its contents — returns the decrypted paste text and any selectors inside it.
url: https://hashb.in/
category: communities-forums
path:
- communities-forums
bestFor: Decrypting and reading a hashb.in paste link you found, since the decryption key travels in the URL fragment.
selectorsIn:
- password
selectorsOut: []
status: live
pricing: free
costNote: Free, client-side-encrypted pastebin; no account needed to create or read a paste.
opsec: passive
opsecNote: Because encryption/decryption happen in your browser and the key is in the URL fragment (after #), the server never sees the plaintext — but the fragment can sit in your browser history/logs. Open suspect links in a clean, sandboxed browser and never paste sensitive material into a new bin.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open-source, zero-knowledge pastebin (source on GitHub); trustworthy as a reader of links you already have, but its contents are not indexed or searchable by anyone, including you.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- hashb.in
- HashBin encrypted pastebin
tags:
- pastebins
- encrypted-paste
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# HashBin

> A zero-knowledge pastebin whose contents are client-side encrypted and unsearchable — useless for hunting leaks, but the way to read a hashb.in link a subject shared, because the key rides in the URL.

## When to use
You have found a `hashb.in/...#...` link — in a subject's posts, a chat, a profile, a breach dump — and want to read what it holds. HashBin encrypts paste contents in the browser, and the decryption key is embedded in the URL fragment (the part after `#`), so possessing the full link is enough to reveal the plaintext. This is a paste **reader**, not a discovery tool: you cannot search or browse other people's pastes here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the complete hashb.in URL **including the `#...` fragment** (without the fragment it can't be decrypted).
2. Open it in a clean/sandboxed browser; the page decrypts client-side and shows the paste text.
3. Read the contents for selectors — `email`, `username`, `phone`, credentials, addresses, links.
4. Pivot: feed any recovered selectors into the appropriate lookups; archive the plaintext, since encrypted pastes can vanish.

## Inputs → Outputs
- **In:** a full hashb.in link (the fragment/`password`-key is part of the URL)
- **Out:** the decrypted paste text and whatever selectors it contains
- **Empty/negative result looks like:** a decryption error or blank page — the fragment/key is missing or truncated, or the paste was deleted/expired. There is no way to recover contents without the full link.

## Gotchas & OpSec
- **Not searchable by design** — you cannot use HashBin to find leaks about a subject; it only helps when you already hold a specific link. Don't treat it as a monitorable pastebin.
- The key in the fragment ends up in your browser history and any proxy that logs full URLs — open sensitive links in a throwaway/sandboxed session.
- Never create a bin to store investigation material; treat it as read-only.

## Overlaps ("do both")
- Pair with searchable paste-monitoring tools — those find where a subject's data was pasted, while HashBin only decodes a specific encrypted link once you have it.

## Trust & verifiability
`trust: community` — open-source and transparent about its zero-knowledge model; reliable as a decoder, but by design it offers no search, indexing, or moderation, so its investigative use is narrow.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hashbin |
| category | communities-forums |
| selectorsIn → selectorsOut | password → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
