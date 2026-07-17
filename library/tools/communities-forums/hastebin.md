---
id: hastebin
name: hastebin
description: Use when you have a hastebin link (or a paste key) surfaced in a breach, chat, or search result and want to read the shared text before it expires — returns raw pasted `document-id` content.
url: https://www.toptal.com/developers/hastebin/
category: communities-forums
path:
- communities-forums
bestFor: Reading or capturing plaintext shared via a hastebin paste link found during an investigation.
selectorsIn:
- username
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to read and post; no account required. Hosted by Toptal after adopting the original open-source haste-server project.
opsec: passive
opsecNote: Reading a paste by its URL is passive and anonymous. If you POST a paste, note that content is public to anyone with the key and effectively permanent within its retention — never paste target data or your own notes here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known open-source pastebin (haste-server) hosted by Toptal; the platform is legitimate, but paste *content* is user-generated and unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- justpaste
- rentry
- controlc-pastebin
- dpaste
aliases:
- hastebin.com
- toptal hastebin
- haste-server
tags:
- pastebins
- paste-sites
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# hastebin

> A minimalist open-source pastebin (haste-server, hosted by Toptal): retrieve the plaintext behind a short paste key found in your investigation.

## When to use
A hastebin link or bare paste key has turned up — in a breach dump, a chat log, a forum post, a phishing kit, or a search hit — and you need to read what was shared before it rotates out. Pastes are commonly used to drop credential lists, config files, code, contact details, or manifestos, so the content behind a hastebin key can be direct evidence or a strong pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the paste URL directly, e.g. `https://www.toptal.com/developers/hastebin/<key>`.
2. Read the raw text. Append `/raw/<key>` (or click "Just Text") to get the unformatted body for copying/archiving.
3. Capture it immediately — screenshot plus save the raw text — because pastes can be short-lived and are not indexed for later re-finding.
4. Pivot: extract emails, usernames, IPs, wallet addresses, or phone numbers from the body and feed them to the relevant selector tools; note any timestamps/handles for attribution.

## Inputs → Outputs
- **In:** a hastebin paste key / URL (often carried alongside a `username` or handle that shared it)
- **Out:** `document-id` — the raw pasted text and whatever selectors it contains
- **Empty/negative result looks like:** "Document not found" or a 404 — the paste expired or was deleted; try a web cache/archive of the key, since the content itself is gone.

## Gotchas & OpSec
- Ephemerality: hastebin pastes can disappear; archive on first sight rather than bookmarking.
- Content is unverified user text — a paste claiming to be a subject's data may be fabricated or misattributed; corroborate before relying on it.
- OpSec: reading is passive/anonymous. Do NOT paste your own investigation notes or a target's data here — anyone with the key can read it and it is not truly private.

## Overlaps ("do both")
- Runs in the same family as `[[justpaste]]`, `[[rentry]]`, `[[controlc-pastebin]]`, and `[[dpaste]]` — when a lead references "a paste," check the paste-site ecosystem, since actors reuse whichever host is convenient.

## Trust & verifiability
`trust: community` — the platform itself is a reputable open-source project on Toptal's infrastructure, but treat every paste's *content* as unverified until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hastebin |
| category | communities-forums |
| selectorsIn → selectorsOut | username → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
