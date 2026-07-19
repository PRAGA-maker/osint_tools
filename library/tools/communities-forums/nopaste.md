---
id: nopaste
name: NoPaste
description: Use when you have found a `nopaste.boris.sh` link in a subject's history and want to read its contents — decodes the paste that is embedded entirely in the URL.
url: https://nopaste.boris.sh/
category: communities-forums
path:
- communities-forums
bestFor: Decoding a self-contained NoPaste link found elsewhere; NOT a searchable leak index (no server storage, no search).
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Fully free and open-source; no account, no server-side storage.
opsec: passive
opsecNote: Because the paste content lives entirely inside the URL and nothing is stored server-side, opening a link reveals the content only to you locally. Still open unknown links in a sandbox/sock-puppet browser in case the decoded content is malicious.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source client-side pastebin by a known developer (boris.sh); the mechanism (data compressed into the fragment) is verifiable from the public source and stores nothing centrally.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- nopaste.boris.sh
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# NoPaste

> A server-less pastebin that packs the entire paste into the shareable URL — so for OSINT it is a link *decoder*, not a searchable source: you can only read a NoPaste you already have the link to.

## When to use
You have come across a `nopaste.boris.sh/...` link (in a subject's messages, a forum post, a bio, or a breach dump) and need to read what it contains. NoPaste stores nothing on its server and is explicitly hidden from search engines, so — unlike Pastebin — you cannot search it for a target's leaked data. Its only investigative use is decoding a specific link you have already found, rather than proactive discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the full `nopaste.boris.sh/...` URL you found (the payload is in the part after `#`; do not truncate it).
2. Open it in a sandboxed/sock-puppet browser — the client decompresses the fragment and renders the text locally.
3. Read the content; copy it out for your records because there is no server copy to return to if the link is lost.
4. If you instead want to *find* a subject's pastes, this tool cannot help — use an indexed pastebin/search instead.
5. Pivot: content decoded here (usernames, emails, keys) feeds the relevant selector tools.

## Inputs → Outputs
- **In:** `document-id` (a complete NoPaste share URL you already possess)
- **Out:** the decoded text of that paste (`document-id` content)
- **Empty/negative result looks like:** a truncated/altered fragment fails to decode, or the page is blank — the link was incomplete or corrupted, not that content was deleted (there is no server-side copy to delete).

## Gotchas & OpSec
- Human-in-the-loop: none, but treat unknown decoded content as potentially hostile.
- OpSec: **passive** — nothing is sent to a server on open. The flip side is there is no index to search, so it is useless for proactive discovery.
- The whole payload must be preserved exactly; URL shorteners or copy/paste that drops the fragment will break decoding.

## Overlaps ("do both")
- Pairs with indexed pastebins/leak search when your goal is discovery — those can be searched for a target, which NoPaste fundamentally cannot.

## Trust & verifiability
`trust: community` — open-source and self-verifiable; the client-side-only design means the content you decode is exactly what the sharer encoded, with no server intermediary.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nopaste |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
