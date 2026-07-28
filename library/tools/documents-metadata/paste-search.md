---
id: paste-search
name: Paste Search (psbdmp.ws)
description: Use when you have an `email`, `username`, `domain`, or keyword and want to find it in dumped Pastebin/paste-site content (often leaked creds/data) — returns email, password, associate leads.
url: https://psbdmp.ws/
category: documents-metadata
path:
- documents-metadata
bestFor: Searching archived pastes (Pastebin & similar) for a selector that appears in leaks or dumps.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- password
- associate
status: live
pricing: freemium
costNote: Free web search of the paste archive; an API is available (paid/keyed) for automated queries.
opsec: passive
opsecNote: You query psbdmp's archive of already-public pastes, not any live account — passive and target-invisible. Pastes may contain real credentials and sensitive PII of many people; handle results lawfully, never authenticate with found passwords, and don't redistribute dumps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running paste-dump archive/search. Coverage is a best-effort scrape of paste sites; a hit is a lead (the same string can be anyone's), and content is unverified and often stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- have-i-been-pwned
- intelligence-x
- dehashed
tags:
- pastebin
- leaks
- breach-search
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Paste Search (psbdmp.ws)

> A searchable archive of dumped pastes (Pastebin and similar) — the place to check whether a subject's email/username/domain has turned up in a leak, credential dump, or doxx.

## When to use
You have an `email`, `username`, `domain`, or other distinctive string and want to know if it appears in publicly dumped pastes — often where breached credentials, config leaks, and doxxes are posted before removal. A strong pivot toward exposed passwords, associated accounts, and the context of a leak.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://psbdmp.ws/.
2. Search the selector (email, username, domain, or keyword).
3. Open matching paste entries; note the paste ID/date and what surrounds your selector (other emails, passwords, handles).
4. Correlate co-occurring data as `associate`/context leads — but treat found `password`s as evidence of exposure, never as login material.
5. Pivot: an exposed email → `[[have-i-been-pwned]]` to scope the breach; co-listed selectors → their own searches; a leak's context → the source incident.

## Inputs → Outputs
- **In:** `email`, `username`, `domain`, or keyword
- **Out:** matching pastes revealing associated `email`s, `password`s (exposure evidence), and `associate` leads
- **Empty/negative result looks like:** no pastes match — meaning the selector isn't in this archive (pastes are often deleted quickly, and coverage is partial), not that it was never leaked. Check other breach sources.

## Gotchas & OpSec
- **Handle sensitively:** results may contain real credentials/PII for many people. Do not authenticate with found passwords (illegal), and don't redistribute dumps.
- Coverage is partial and time-limited — pastes get removed; absence is weak evidence.
- A string match is a lead, not identity proof; corroborate.

## Overlaps ("do both")
- Pairs with `[[have-i-been-pwned]]` (breach confirmation), `[[dehashed]]` and `[[intelligence-x]]` (deeper leak/darkweb search) — coverage differs, so run several.

## Trust & verifiability
`trust: community` — an unofficial archive of unverified user-posted content. Useful for exposure signals and leads; independently verify anything you act on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paste-search |
| category | documents-metadata |
| selectorsIn → selectorsOut | email, username, domain → email, password, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
