---
id: defuse
name: Defuse Pastebin
description: Use when you have found a `defuse.ca` pastebin link in a subject's trail and want to read it — decrypts a client-side-encrypted paste you already hold the link for.
url: https://defuse.ca/pastebin.htm
category: communities-forums
path:
- communities-forums
bestFor: Decrypting a specific defuse.ca paste link you already possess; NOT a searchable index (robots-blocked, link-only access).
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to use; no account required.
opsec: passive
opsecNote: Defuse's pastebin encrypts text in the browser before it is sent over TLS, and blocks search-engine indexing via robots.txt, so pastes are link-only. Opening a link decrypts locally, but the operator could in principle serve modified code — open unknown links in a sandbox, and never paste a target's data here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Defuse Security (Taylor Hornby), a reputable security site with a long-lived, high-traffic pastebin. Client-side encryption is auditable, but you must trust the server operator not to tamper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- big-number-calculator
- html-sanitizer-tool
- text-and-file-hash-calculator
- x86-and-x64-intel-assembler
aliases:
- defuse.ca pastebin
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Defuse Pastebin

> Defuse Security's long-running encrypted pastebin — for OSINT it is a *decoder*, not a source: content is client-side-encrypted and blocked from search engines, so you can only read a paste you already have the link to.

## When to use
You have found a `defuse.ca/pastebin...` link (in a message, a forum thread, a bio, or a dump) and need to read what it holds. The site encrypts before storage and uses robots.txt to keep pastes out of search indexes, so you cannot search it for a subject's leaked data. Its only investigative value is opening a specific link you already possess — not proactive discovery.

## How to use it (`bestInteractionPattern`: web-manual)
1. Take the complete paste URL you found (preserve any key/fragment) and open it in a sandboxed/sock-puppet browser.
2. The page decrypts and renders the text locally.
3. Read and snapshot the content immediately in case the paste later expires or is removed.
4. If you instead want to *find* a subject's pastes, this tool cannot help — use an indexed pastebin/leak search.
5. Pivot: any selectors inside (emails, passwords, handles, keys) feed the relevant breach-check and username tools.

## Inputs → Outputs
- **In:** `document-id` (a complete defuse.ca paste link you already hold)
- **Out:** the decrypted paste text (`document-id` content)
- **Empty/negative result looks like:** a not-found/expired page or a failed decryption from an incomplete link — the paste is gone or the URL is truncated, not evidence about the subject.

## Gotchas & OpSec
- Human-in-the-loop: none, but treat unknown decoded content as potentially hostile.
- OpSec: **passive** on view; encryption is client-side. The flip side is the robots.txt/no-index design means there is nothing to search for discovery.
- Trust caveat: as the site itself warns, you must trust the operator not to intercept or alter the encryption code.

## Overlaps ("do both")
- Behaves like [[verybin]] and [[nopaste]] (link-only, non-searchable); pair with indexed pastebins/leak search when the goal is to *find* a subject's data.

## Trust & verifiability
`trust: community` — a reputable security operator with an auditable client-side design; the plaintext you decrypt matches what the sharer posted, subject to trusting the server not to tamper.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | defuse |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
