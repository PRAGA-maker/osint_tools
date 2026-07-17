---
id: arquivo-pt
name: Arquivo.pt
description: Use when you have a `domain`/URL or a `name` and want historical snapshots of Portuguese-web pages back to 1996 — returns archived page versions and deleted content.
url: https://arquivo.pt/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted or changed Portuguese web pages, and full-text searching the historical .pt web.
selectorsIn:
- domain
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free national research infrastructure operated by FCT|FCCN (Portugal); no account or payment. Offers a public API in addition to the web UI.
opsec: passive
opsecNote: You query the archive, never the live site or its owner, so retrieving a snapshot leaves no footprint on the target — an ideal way to view a page without alerting whoever runs it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A government-backed national web archive (FCCN) with a stable, citable preservation mandate; snapshots are faithful captures, comparable to the Internet Archive for the Portuguese-language web.
missingPersonsRelevance: medium
coverage:
- pt
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- archive-org
- archive-today
- archive-it
aliases:
- Arquivo.pt
- Portuguese Web Archive
- arquivo.pt
tags:
- Archives
- web-archive
- wayback
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Arquivo.pt

> Portugal's national web archive — a Wayback-style time machine for the Portuguese-language web since 1996, with full-text search over archived pages.

## When to use
Your subject has a footprint on the Portuguese-language web — a `.pt` `domain`, a profile on a Lusophone site, a name mentioned in Portuguese/Brazilian pages — and the live page is deleted, changed, or scrubbed. Arquivo.pt often holds snapshots the Internet Archive missed, and its full-text search lets you hunt a `name`, handle, or phrase across historical captures, surfacing deleted bios, removed posts, and old contact details.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://arquivo.pt/ and choose page search (full-text over archived content) or paste a specific URL to see its capture timeline.
2. For a URL, use the timeline sliders to pick a snapshot date and open that version; for a `name`/phrase, run the full-text search and filter by date range.
3. Try the image search for archived pictures tied to the query.
4. Capture what you find (screenshot + note the permalink/date) since you now have a citable archived record.
5. Pivot: recovered emails, handles, and addresses feed the relevant selector tools; compare snapshots over time to build a change timeline.

## Inputs → Outputs
- **In:** `domain`/URL or `name`/phrase (best for Portuguese-language content)
- **Out:** archived page versions, deleted `social-profile`/bio content, `name` mentions, and historical contact details
- **Empty/negative result looks like:** no captures for the URL/term — the page was never crawled, is too recent/obscure, or isn't Lusophone-web; fall back to `[[archive-org]]` / `[[archive-today]]`.

## Gotchas & OpSec
- Regional focus: strongest for the Portuguese/Lusophone web; not a general global archive — pair with the Internet Archive.
- Crawl gaps: like any archive, coverage is patchy; absence of a snapshot is not proof a page never existed.
- OpSec: fully passive — viewing a snapshot never touches the live site, so it's the safe way to inspect a page covertly.

## Overlaps ("do both")
- Run the same URL/term through `[[archive-org]]`, `[[archive-today]]`, and `[[archive-it]]` — different archives crawl different pages at different times, and Arquivo.pt uniquely deep-covers the Portuguese web, so the union recovers the most.

## Trust & verifiability
`trust: trusted` — a government-funded national archive with a preservation mandate and citable permalinks; snapshots are authentic captures you can cite as evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | arquivo-pt |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
