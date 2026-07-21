---
id: paste-sh
name: paste.sh
description: Use when you have a `password`-protected or link-shared snippet and want to read or create an end-to-end-encrypted paste — returns text content, but is NOT indexable/searchable so it yields no discovery leads.
url: https://paste.sh/
category: communities-forums
path:
- communities-forums
bestFor: Reading a specific encrypted paste.sh link a subject shared, or creating one yourself for secure snippet handoff.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source (bash + JS) pastebin; no account or payment required.
opsec: passive
opsecNote: Retrieving a paste.sh URL a subject already published is passive. The encryption key lives in the URL fragment (after #), so the server never sees plaintext — but anyone with the full link can read it. Do not create pastes containing case data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source, single-author project (Dave Coombs); reputable in the security community, but a niche self-hosted-style service, not a data source.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- paste.sh encrypted pastebin
tags:
- pastebins
- encrypted
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# paste.sh

> A zero-knowledge, end-to-end-encrypted pastebin — useful only when you already hold a specific link, because there is nothing to search.

## When to use
You have a **specific paste.sh URL** (e.g. a subject posted one, or it turned up in a chat/forum export) and need to read its contents, or you need to hand a snippet to a colleague/source without it being server-readable. This is **not** a discovery tool: unlike Pastebin, paste.sh content is encrypted client-side and never indexed, so you cannot search it for a target's leaked data.

## How to use it (`bestInteractionPattern`: web-manual)
1. To **read**: open the full paste.sh URL exactly as given — the part after the `#` is the decryption key, so a truncated link will not decrypt. Add `raw` behaviour via the on-page control if you need the plain text.
2. If the paste was password-protected, enter the password when prompted.
3. To **create**: click "new", paste text, and share the generated link (which embeds the key in its fragment).
4. Pivot: content read from a paste (usernames, emails, phone numbers) feeds the usual selector lookups; the paste itself leads nowhere further.

## Inputs → Outputs
- **In:** a full `domain`/URL (a paste.sh link, key fragment intact)
- **Out:** the decrypted text of that one paste
- **Empty/negative result looks like:** "paste not found / expired" or garbled output — the link expired, or the `#key` fragment was stripped in transit.

## Gotchas & OpSec
- **No search, no index, no discovery** — its whole design goal is to be un-findable, which makes it near-useless for *hunting* a target's data; value only appears once you already hold a link.
- The decryption key is in the URL fragment; treat any paste.sh link as a full credential and handle it like a secret.
- Pastes can be set to expire; a dead link is not evidence the content never existed.

## Overlaps ("do both")
- Contrast with indexed pastebins and paste-scrapers — those you *search*; paste.sh you can only *open*. When chasing leaked data, use the searchable ones, not this.

## Trust & verifiability
`trust: community` — a well-regarded open-source project, but a plumbing utility rather than an intelligence source; nothing to verify beyond "did the link decrypt".

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paste-sh |
| category | communities-forums |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
