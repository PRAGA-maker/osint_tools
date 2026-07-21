---
id: spacebin
name: Spacebin
description: Use when you have an `email`, `username`, or `name` and want to check a paste host for dumps or mentions — returns pasted text that may expose passwords, emails, and personal data.
url: https://spaceb.in/
category: communities-forums
path:
- communities-forums
bestFor: Checking an open-source paste host for leaked dumps or mentions tied to a selector.
selectorsIn:
- email
- username
- name
selectorsOut:
- password
- email
- phone
status: live
pricing: free
costNote: Free, ad-free, donation-supported open-source pastebin; accounts optional.
opsec: passive
opsecNote: Reading public pastes is passive. It lacks full-text search, so query via Google (`site:spaceb.in "selector"`); never paste your own case data, as content is public.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A generic open-source paste host; anonymous and unmoderated, so any data found is unverified and possibly fabricated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Spacebin
- spaceb.in
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Spacebin

> An open-source, ad-free paste host — another of the pastebins where leaked credentials and personal data land, searchable through a general engine.

## When to use
Paste sites are where dumps and doxes surface. When you have an `email`, `username`, or `name` and are hunting breach data or mentions, sweep paste hosts like Spacebin for text containing the selector. Hits may expose passwords, alternate emails, phone numbers, or contextual chatter — always to be verified, never trusted at face value.

## How to use it (`bestInteractionPattern`: web-manual)
1. Because Spacebin has no robust internal search, use a search engine: `site:spaceb.in "target@email.com"` (repeat for username/name).
2. Open matching pastes and read for the selector and any leaked fields around it.
3. Note the paste's date and any linked handles/pastes.
4. Corroborate sensitive findings (a password, an address) against an independent source before acting.
5. Pivot: leaked secondary `email`/`phone` feeds account-existence and reverse lookups; a handle feeds username search.

## Inputs → Outputs
- **In:** `email`, `username`, or `name`
- **Out:** pasted text possibly containing `password`, secondary `email`, `phone`, and personal context
- **Empty/negative result looks like:** no indexed pastes — expected for most people, and pastes often expire or are never indexed, so absence isn't proof of no exposure.

## Gotchas & OpSec
- Relies on Google indexing; short-lived or removed pastes may be invisible.
- Anonymous/unmoderated — content can be fake, stale, or planted; verify before believing.
- Legal/ethical care with leaked data; do not re-host it.
- OpSec: passive to read; never post investigation data (it becomes public).

## Overlaps ("do both")
- Pairs with `[[nopaste-net]]`, Pastebin dorks, and breach indexes like Have I Been Pwned — each paste host is siloed, so sweep several plus a breach index together.

## Trust & verifiability
`trust: community` — an anonymous open-source paste bin; anything found is unverified user content requiring independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spacebin |
| category | communities-forums |
| selectorsIn → selectorsOut | email, username, name → password, email, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
