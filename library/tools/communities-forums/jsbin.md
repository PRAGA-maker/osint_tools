---
id: jsbin
name: JS Bin
description: Use when you have a `jsbin.com` link or need to inspect/preserve shared front-end code — returns the saved HTML/CSS/JS of a "bin" (a `document-id`) that may leak endpoints, keys or author hints.
url: https://jsbin.com
category: communities-forums
path:
- communities-forums
bestFor: Reading or preserving shared front-end code snippets ("bins") that may expose leads.
selectorsIn:
- document-id
selectorsOut:
- document-id
- domain
status: live
pricing: freemium
costNote: Free to create and view bins; a paid "Pro" tier adds private bins and extras. Public bins are viewable without an account.
opsec: passive
opsecNote: Viewing a public bin is passive and the author isn't notified. There's no global search, so you usually arrive via a shared link or a search-engine dork. Bins can embed live API calls — open untrusted bins' code as text/read-only rather than running them, and use a sandboxed browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known, long-running code playground; the platform is reputable, but bin *content* is arbitrary user code to be treated as unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- jsbin.com
- JSBin
tags:
- pastebins
- code-playground
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# JS Bin

> A live front-end code playground (HTML/CSS/JS) — an occasional OSINT surface where developers paste snippets that leak API endpoints, keys, internal URLs, or authorship clues.

## When to use
Two cases. (1) You have a `jsbin.com` link (from a chat, forum, repo, or breach discussion) and want to read the saved code and what it reveals. (2) You're sweeping code-paste surfaces for a subject's leaked snippets — a distinctive handle, an API key, an internal endpoint, or a domain. JS Bin stores runnable "bins," and their code often embeds telling details (backend URLs, tokens, author comments).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open a known bin URL directly (`jsbin.com/<id>`), appending `/edit` to see the source panels.
2. To discover bins, dork a search engine: `site:jsbin.com "<selector>"` (a domain, key fragment, username, or endpoint).
3. Read the HTML/CSS/JS for embedded API endpoints (`domain`), keys, comments, and author signatures.
4. Preserve anything relevant via [[wayback-machine]] — bins can be edited or deleted.
5. Pivot: a leaked endpoint/`domain` feeds infrastructure OSINT; an author handle feeds username searches; a key may indicate a breach to report responsibly.

## Inputs → Outputs
- **In:** a bin URL or a search-dork `selector` (`document-id`)
- **Out:** the saved code (`document-id`) and any embedded `domain`s/endpoints, keys, or author hints
- **Empty/negative result looks like:** the bin 404s (deleted) or dorks return nothing — most subjects have no JS Bin footprint; absence here says little, so check other paste/code surfaces.

## Gotchas & OpSec
- No native site-wide search — your real index is Google/Bing coverage of `site:jsbin.com`.
- Bins run code; don't execute untrusted bins — inspect the source as text and use a sandbox.
- Handle any exposed credentials responsibly (evidence only; report, don't reuse).
- OpSec: passive; the author isn't alerted to your view.

## Overlaps ("do both")
- Pairs with other paste/code surfaces like [[tutpaste]] and [[paaster]] and general code search (GitHub dorking) — run the same selector across several so a snippet on one host isn't missed.

## Trust & verifiability
`trust: community` — a reputable platform, but each bin is arbitrary user code; verify any endpoint/identity clue against an independent source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jsbin |
| category | communities-forums |
| selectorsIn → selectorsOut | document-id → document-id, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
