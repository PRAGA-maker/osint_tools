---
id: pastebin-cz
name: Pastebin.cz
description: Use when you have a `username`, `email`, or keyword and want public pastes — returns snippet/text dumps that may leak credentials, contacts, or handles.
url: https://www.pastebin.cz/en/
category: communities-forums
path:
- communities-forums
bestFor: Sweeping a Czech-run paste host for leaked code, text, credentials, or handles.
selectorsIn:
- username
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free to read and post; no account required to view public pastes.
opsec: passive
opsecNote: Reading public pastes is passive. As with any paste host, content may include live credentials/PII — do not re-post or exfiltrate, and use a clean browser. No login is needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent paste host with English UI and ~100 syntax languages; content is anonymous, user-submitted, and unmoderated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- pastebin.cz
tags:
- pastebins
- paste-site
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Pastebin.cz

> A Czech-run, English-friendly paste host — one more site to sweep when hunting leaked snippets, credentials, and handles tied to a subject.

## When to use
You are running paste-site reconnaissance and want to check whether a `username`, `email`, project name, or distinctive string appears in a text/code dump here. Pastes are a common vector for leaked credentials, config files, contact lists, and reused handles, so a hit can surface an `email`, a secondary account, or infrastructure detail. Use it alongside other paste hosts — each indexes different content.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.pastebin.cz/en/ for the English interface.
2. Because internal discovery is limited, run a scoped web search: `site:pastebin.cz "<username>"` (or an email/keyword).
3. Open matching public pastes and read for credentials, contacts, reused handles, and technical references.
4. Note paste expiry (from minutes to a month) and capture anything relevant immediately.
5. Pivot: a leaked `email` feeds breach/email-OSINT; a reused `username` feeds a cross-site enumerator; infrastructure strings feed domain/IP lookups.

## Inputs → Outputs
- **In:** `username` / `email` / keyword
- **Out:** public pastes that may contain `email`, reused handles (`social-profile`), and technical leads
- **Empty/negative result looks like:** no indexed pastes match — expected, since pastes expire and search engines index only a slice. Absence is weak evidence; check other paste hosts too.

## Gotchas & OpSec
- Pastes expire, so an indexed copy may already be gone — snapshot fast.
- Discovery leans on external search engines; the site itself offers little browse/search, so coverage is partial.
- Content is anonymous and may contain live secrets; handle ethically and never redistribute.

## Overlaps ("do both")
- Pairs with `[[snippet-host]]` and other paste/breach tools — each host holds different content, so sweep several; a handle absent here may sit on another.

## Trust & verifiability
`trust: community` — a legitimate but anonymous, unmoderated paste host; anything found is user-submitted and must be corroborated and handled with care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastebin-cz |
| category | communities-forums |
| selectorsIn → selectorsOut | username → email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
