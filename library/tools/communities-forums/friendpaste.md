---
id: friendpaste
name: Friendpaste
description: Use when you have a `username`, `email`, or leak keyword and want to find text/code dumps posted publicly — returns pasted `password`, `email` and other leaked content.
url: https://friendpaste.com/
category: communities-forums
path:
- communities-forums
bestFor: Hunting leaked credentials, dumps and shared snippets that actors post to this Pastebin-style service.
selectorsIn:
- username
- email
selectorsOut:
- password
- email
- username
status: live
pricing: free
costNote: Free, no account required to create or read a paste.
opsec: passive
opsecNote: Reading pastes and Google-dorking the domain is passive. There is no site-wide search, so you rely on external search engines — which is invisible to whoever posted the paste. Do not post the target's data yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An open, anonymous paste host with no moderation guarantee; pasted content is unauthenticated and may be fabricated, stale or planted.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- friendpaste pastebin
tags:
- pastebins
- credential-leaks
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Friendpaste

> A minimalist, anonymous Pastebin clone — worth checking because actors dump credentials, contact lists and code here where mainstream pastebins have removed them.

## When to use
You have an `email`, `username`, breach handle or other distinctive keyword and want to see whether it appears in a public paste on this host. Because there is no login and no site-wide search box, treat Friendpaste as a *dork target*: you search it via Google/Bing rather than on-site. Useful when triaging whether a subject's credentials or data have been shared publicly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Dork the domain in a search engine: `site:friendpaste.com "<email>"`, `site:friendpaste.com "<username>"`, or a leaked password/phrase.
2. Open any matching paste directly (URLs look like `friendpaste.com/<id>`); pastes are plain text and load without an account.
3. Read the dump for linked selectors — credential pairs, contact lists, related handles, source code with embedded secrets.
4. Pivot: a recovered `password` feeds credential-reuse checks; a co-listed `email`/`username` feeds cross-platform enumeration; note the paste date for recency.

## Inputs → Outputs
- **In:** `username`, `email`, or any leak keyword
- **Out:** `password`, `email`, `username` and free-text dump content found inside pastes
- **Empty/negative result looks like:** no indexed pastes for the term — either nothing was posted here, or the paste exists but was never crawled (individual paste IDs are unguessable, so uncrawled pastes are effectively invisible).

## Gotchas & OpSec
- No native search: you are entirely dependent on search-engine coverage, which misses fresh or unlinked pastes.
- Anonymous and unmoderated: content can be planted, edited or fake — verify any credential out-of-band, never by logging into a target's account.
- Passive only — reading pastes does not notify the poster; keep it that way.

## Overlaps ("do both")
- Run alongside other paste-site dorks (Pastebin, Ghostbin-style hosts) and breach-lookup services — each host is crawled differently, so a handle absent on one may surface on another.

## Trust & verifiability
`trust: community` — an open anonymous paste service. The platform is real and reachable; the *content* is unauthenticated and must be corroborated before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | friendpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → password, email, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
