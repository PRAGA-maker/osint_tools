---
id: chrome-extension-archive-search-engine
name: Chrome Extension Archive Search Engine
description: Use when you have a Chrome extension name, id, or developer and want to find archived/indexed extension pages — returns `domain`, `social-profile` (developer) links.
url: https://cse.google.com/cse/publicurl?cx=000501358716561852263:h-5uyshsclq
category: search-engines
path:
- search-engines
bestFor: Locating archived or indexed Chrome Web Store extension listings and developer details for an extension of interest.
selectorsIn:
- username
- domain
selectorsOut:
- domain
- social-profile
status: degraded
pricing: free
costNote: Free Google Programmable Search Engine; no account needed.
opsec: passive
opsecNote: This is a scoped Google search; queries go to Google like any search. Passive to the extension developer, but assume Google logs the query — use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-configured Google Custom/Programmable Search Engine — coverage is whatever sites the (anonymous) creator scoped it to, and it can silently rot over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- mindmap-search-engine
aliases: []
tags:
- google-cse
- browser-extensions
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Chrome Extension Archive Search Engine

> A community-built Google Programmable Search Engine scoped toward Chrome extension listings/archives — a niche shortcut, not an authoritative store index.

## When to use
You are investigating a specific Chrome extension — by name, extension id, or developer handle — and want to find its Web Store listing, archived copies, or write-ups without wading through unscoped Google. Useful when analyzing a suspicious/removed extension or tying an extension back to a developer identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (it loads as a Google Programmable Search box).
2. Enter the extension name, 32-character extension id, or developer name/`username`.
3. Read the scoped results — Web Store pages, archive.org captures, review/analysis sites.
4. Pivot: a developer name or contact from a listing feeds `social-profile`/`email` OSINT; an extension id feeds Web Store / permissions analysis.

## Inputs → Outputs
- **In:** extension name / id / developer `username`
- **Out:** `domain` (listing/archive URLs), `social-profile` (developer) links
- **Empty/negative result looks like:** no hits, which for a scoped CSE often means the target site fell outside its configured scope — try a plain `site:chromewebstore.google.com` search as a fallback rather than concluding the extension never existed.

## Gotchas & OpSec
- **Degraded/opaque coverage:** a CSE only searches sites its creator configured; that scope is invisible to you and may be stale. Never treat an empty result as authoritative.
- No login, passive; standard Google query hygiene applies.
- The Chrome Web Store moved to `chromewebstore.google.com` — older CSE scopes may miss the new host.

## Overlaps ("do both")
- Pairs with `[[mindmap-search-engine]]` and a manual `site:` search — CSEs are hit-or-miss, so always cross-check with an unscoped engine.

## Trust & verifiability
`trust: community` — an anonymous, community-configured search engine of unknown, unauditable scope; corroborate every hit against the first-party Web Store or an archive capture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chrome-extension-archive-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | username, domain → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
