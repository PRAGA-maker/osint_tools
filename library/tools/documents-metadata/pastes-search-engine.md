---
id: pastes-search-engine
name: Pastes Search Engine
description: Use when you have an `email`/`username`/keyword and want to search across paste sites (Pastebin et al.) for leaked/dumped text — returns pastes exposing credentials, `password`, and `social-profile` data.
url: https://cse.google.com/cse?cx=661713d0371832a02
category: documents-metadata
path:
- documents-metadata
bestFor: One-box search across many paste/dump sites for an email, handle, or keyword appearing in leaked text.
selectorsIn:
- email
- username
- name
selectorsOut:
- password
- social-profile
- email
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account.
opsec: passive
opsecNote: The query runs against Google's index, not the paste sites, so it's passive to any target. Use sock-puppet egress; be aware that opening a paste containing real credentials may itself be sensitive — handle any exposed data lawfully and don't act on live credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community Google CSE scoped to paste/dump sites; only covers pastes Google has indexed (many are unlisted/removed), and the site list is opaque and can rot.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pastebin search
- paste dump search
tags:
- pastes
- breach-search
- custom-search-engine
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Pastes Search Engine

> A Google Custom Search Engine scoped to paste sites — search an email, handle, or keyword across Pastebin-style dumps for leaked credentials and exposed data.

## When to use
You have an `email`, `username`, or keyword and want to know whether it appears in publicly pasted text — credential dumps, config leaks, doxes, combolists — that people post to Pastebin and its many clones. Pastes are a classic exposure surface for `password`s, associated emails, and identity fragments that don't show up in normal search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE link and enter the `email`/`username`/keyword; quote exact addresses.
2. Read the results — indexed pastes where the term appears.
3. Open relevant pastes to see the surrounding leaked context (co-leaked emails, passwords, usernames).
4. Pivot: a co-leaked `email`/`username` feeds account-existence and breach tools; an exposed credential is a lead only — never use it to access an account.

## Inputs → Outputs
- **In:** `email` / `username` / keyword
- **Out:** indexed pastes → exposed `password`s, linked `email`s, `social-profile` fragments
- **Empty/negative result looks like:** no results — meaning nothing *indexed*, which is a weak signal: most sensitive pastes are unlisted, quickly deleted, or robots-blocked, so absence here does NOT mean no exposure.

## Gotchas & OpSec
- **Heavy blind spots:** Google indexes only a fraction of pastes, and the worst dumps are removed or unlisted fast. Complement with a dedicated paste/breach-monitor (e.g. an -oh-dear / HIBP-style service), not this alone.
- Opaque, rot-prone CSE scope — a null result is inconclusive.
- Legal/ethical: exposed credentials must be handled lawfully; do not authenticate with found passwords.

## Overlaps ("do both")
- Pairs with dedicated breach/paste-monitoring services and email account-existence checks (`[[account-live-com]]`) — this gives quick indexed breadth; the dedicated tools cover the unindexed dumps and confirm account reality.

## Trust & verifiability
`trust: community` — a convenient community CSE with real blind spots; use for leads and never treat an empty result as proof of no leak.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastes-search-engine |
