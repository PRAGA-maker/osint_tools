---
id: pastebin-bisque
name: Pastebin-Bisque
description: Use when you have a Pastebin `username` and want to bulk-download all of that user's public pastes for offline review — returns their paste `document-id` contents.
url: https://github.com/bbbbbrie/pastebin-bisque
category: dark-web
path:
- dark-web
bestFor: Downloading every public paste from a specific Pastebin user in one command.
selectorsIn:
- username
selectorsOut:
- document-id
status: degraded
pricing: free
costNote: Free and open-source Python CLI. Note Pastebin's scraping/API has become restrictive, which can limit what the tool can pull.
opsec: passive
opsecNote: It fetches public pastes tied to a username; it does not notify the user. Run behind a VPN/sock-puppet so a burst of requests is not tied to you, and preserve downloaded pastes with hashes as evidence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small community script (bbbbbrie); a thin wrapper over Pastebin's public pages/API, so results depend on Pastebin's current access rules — verify it still works before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- pastebin-bisque
tags:
- Search engines
- Darknet/deepweb search tools
- paste-sites
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Pastebin-Bisque

> A small Python CLI that grabs all of a given Pastebin user's public pastes at once — useful for preserving and reviewing everything a handle has posted before it disappears.

## When to use
You have a Pastebin `username` (surfaced from a leak, a forum, or a reused handle) and want a local copy of everything they have publicly posted — dumps, notes, code, contact lists — rather than clicking each paste. Pastes often contain emails, credentials, and other identifiers worth mining offline.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/bbbbbrie/pastebin-bisque and install its Python requirements.
2. Run it against the target Pastebin `username` per the repo README.
3. It downloads that user's public pastes to local files.
4. Grep the saved pastes for emails, phones, usernames, and credentials.
5. Pivot: extracted selectors (`email`, `username`, etc.) feed the relevant per-selector lookups; hash and log the pastes as evidence.

## Inputs → Outputs
- **In:** `username` (a Pastebin user)
- **Out:** downloaded paste `document-id` contents (text files)
- **Empty/negative result looks like:** no pastes retrieved — the user may have none public, or Pastebin's access restrictions blocked the scrape; check manually on pastebin.com before concluding empty.

## Gotchas & OpSec
- **Degraded:** Pastebin has tightened scraping (parts of its API now need a paid PRO account) — the tool may under-collect or fail; verify against the live profile.
- Only public pastes; private/removed ones are invisible.
- OpSec: **passive**; public content, but VPN to avoid tying a request burst to you.

## Overlaps ("do both")
- Pairs with broader paste-site search engines and leak-search tools; this one is specifically per-user bulk retrieval.

## Trust & verifiability
`trust: unverified` — small community script dependent on Pastebin's changing rules; confirm completeness against the user's live paste list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pastebin-bisque |
| category | dark-web |
| selectorsIn → selectorsOut | username → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
