---
id: googledrive-search-engine
name: GoogleDrive Search Engine
description: Use when you have a `name`, keyword, or filename and want to find publicly-shared Google Drive/Docs files indexed by Google — returns exposed `document-id` files and their author `name`s.
url: https://cse.google.com/cse?cx=c64ba311eb8c31896
category: search-engines
path:
- search-engines
bestFor: Surfacing publicly-shared Google Drive documents, sheets, and slides that were meant to be private.
selectorsIn:
- name
selectorsOut:
- document-id
- name
status: degraded
pricing: free
costNote: Free Google Programmable (Custom) Search Engine; no account needed to run a query.
opsec: passive
opsecNote: Queries hit Google's index, not the document owners, so no target is alerted. Google logs your searches — use a sock-puppet Google session/VPN for sensitive work, and note that opening a found file may register a view for the owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine restricting results to Google Drive/Docs domains; coverage depends on that config and Google's index, and can drift over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Drive CSE
tags:
- google-drive
- document-search
- custom-search-engine
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# GoogleDrive Search Engine

> A pre-built Google Custom Search Engine scoped to Google Drive/Docs domains — a shortcut for finding publicly-shared documents that surfaced in Google's index by accident.

## When to use
You want to find Google Drive documents, spreadsheets, or slides that are shared "anyone with the link" (and thus crawlable) mentioning a subject's `name`, email, project, or organisation. People routinely over-share Drive files; this CSE narrows a normal Google search to Drive/Docs results.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=c64ba311eb8c31896.
2. Enter a `name`, email, company, or distinctive keyword/filename.
3. Review the results — they are limited to Google Drive/Docs-hosted files the index has captured.
4. Open a promising file (read-only) and check **File → Document properties / version history** for author `name` and timestamps.
5. Pivot: an author name or embedded email feeds people/email lookups; equivalently, run the same query as a manual Google dork (`site:docs.google.com "target"`) since a CSE can drift.

## Inputs → Outputs
- **In:** `name`, email, keyword, or filename
- **Out:** publicly-shared `document-id` files and their author/owner `name`
- **Empty/negative result looks like:** no results — either nothing is publicly shared, or the CSE's scope/index has drifted; confirm with a manual `site:docs.google.com` dork before concluding nothing exists.

## Gotchas & OpSec
- CSEs are third-party configs and **degrade** — if it returns nothing or errors, replicate the intent with manual Google dorks.
- Only indexed, link-shared files appear; properly-private Drive content is invisible here.
- OpSec: **passive** to the search, but opening a found doc can log a view to the owner — decide before you click.

## Overlaps ("do both")
- Pairs with manual Google dorking and other document-search CSEs; do both, since each CSE and dork surfaces a slightly different slice of the index.

## Trust & verifiability
`trust: community` — an unofficial CSE over Google's index; results are real Google hits, but the scope is defined by an opaque third-party config, so corroborate with a plain Google dork.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | googledrive-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id, name |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
