---
id: context
name: Context (ctxt.io)
description: Use when you have a `username` or keyword and want to find pastes/leaked text shared on ctxt.io — returns email, username and password.
url: https://ctxt.io/
category: communities-forums
path:
- communities-forums
bestFor: A rich-text pastebin whose public pastes can hold leaked credentials, contact lists and dumped text worth searching.
selectorsIn:
- username
- email
selectorsOut:
- email
- username
- password
status: live
pricing: free
costNote: Free; no account needed to create or view a paste.
opsec: passive
opsecNote: Viewing a paste is passive, but note ctxt.io lets a poster IP-restrict access and set expiry — a paste can log/limit who opens it. Search via an engine cache rather than hitting the live paste where possible, and never post investigation material to it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A general-purpose paste host with no first-party search; treat any content as unverified user-supplied text.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ctxt.io
- ctxt paste
tags:
- pastebins
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Context (ctxt.io)

> A rich-text pastebin — one more paste site to sweep for a subject's leaked credentials, contact dumps and shared snippets.

## When to use
You are hunting for a subject's data in the paste ecosystem: leaked credential lists, exported contacts, config files, or chat logs that get dumped to paste sites. ctxt.io is one such host. Search it (indirectly) for a `username`, `email`, real name, or breach keyword; a hit can expose `email`/`password` pairs, phone numbers, or `associate` handles. It has no native search box, so you reach its content through search-engine indexing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Run a scoped engine query for the host: `site:ctxt.io "targetuser"` (or the email/keyword) on Google/Bing and cached copies.
2. Open matching pastes (prefer the search-engine cache first, since live pastes can be IP-restricted or expired).
3. Read the paste for credentials, contact fields, or named associates tied to the subject.
4. Pivot: any `email`/`username` → account-existence and breach lookups; a `password` → credential-reuse checks (in authorized contexts only); named handles → `associate` mapping.

## Inputs → Outputs
- **In:** `username`, `email`, real name, or breach keyword
- **Out:** `email`, `username`, `password` (whatever the paste contains); often phone/associate leads
- **Empty/negative result looks like:** no indexed pastes match, or the paste has expired/is IP-locked — meaning nothing is publicly retrievable here; check other paste hosts and paste-aggregators.

## Gotchas & OpSec
- No first-party search — you depend entirely on what engines have indexed, and many pastes are short-lived (5-minute to 30-day expiry) or IP-restricted, so coverage is patchy and time-sensitive.
- Handle any credentials strictly within your authorization; do not test passwords without a lawful basis.
- OpSec: reading is passive, but a poster-set IP restriction can log your visit — go through cache when you can, and use a sock-puppet egress.

## Overlaps ("do both")
- Run alongside dedicated paste-aggregators/monitors (e.g. PSBDMP-style tools) and breach-search services — this covers one host, while aggregators sweep many and breach DBs give structured credential context.

## Trust & verifiability
`trust: community` — a neutral paste host; content is unverified user-supplied text that may be fabricated, stale, or planted. Corroborate any lead against an independent source before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | context |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → email, username, password |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
