---
id: cachedview
name: CachedView
description: Use when you have a `domain`/URL and want to view archived snapshots of that page — returns historical captures (via the Wayback Machine) as `document-id`.
url: http://cachedview.com
category: archives-cache
path:
- archives-cache
bestFor: A quick front-end for pulling up cached/archived versions of a specific webpage that has changed or gone offline.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free; no account required.
opsec: passive
opsecNote: You paste a URL and it hands off to public archive services (Wayback Machine). The origin site is not contacted by you, so it does not learn you looked — passive. Use a clean browser for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A thin third-party front-end that redirects to established archives (archive.org); the archived content itself is authoritative, this is just a convenience lookup.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- cached-view
aliases:
- cachedview.com
tags:
- web-history-and-website-capture
- cache
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# CachedView

> A simple "type a URL, get the cached copy" front-end — now backed by the Wayback Machine since Google Cache was discontinued.

## When to use
You have a `domain`/URL for a page that has been edited, deleted, or is currently down, and you want to see an earlier captured version — a removed profile, a scrubbed listing, an old business page. It is a fast entry point to archived snapshots of one specific page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://cachedview.com .
2. Paste the full URL of the page you want to retrieve.
3. Choose the archive source — it now routes to Archive.org / Wayback Machine (Google's cached-pages feature was retired in early 2024).
4. Read the output: the archived snapshot(s) of the page (`document-id`) alongside the option to open the live version for comparison.
5. Pivot: for full capture history and multiple dates, go directly to the Wayback Machine; for on-demand capture of a live page, use archive.today.

## Inputs → Outputs
- **In:** `domain` / full URL
- **Out:** `document-id` (archived snapshot of the page)
- **Empty/negative result looks like:** no snapshot exists for that URL in the Wayback Machine — the page was never crawled; try the domain root or a search-engine cache alternative.

## Gotchas & OpSec
- Google Cache is dead (since early 2024); despite the name, this tool now leans entirely on the Wayback Machine, which you can query directly for more control.
- Only pages that were actually crawled/archived are retrievable — never-crawled pages return nothing.
- OpSec: passive; the origin site does not see your lookup.

## Overlaps ("do both")
- Pairs with `[[cached-view]]` and the Wayback Machine — CachedView is the shortcut, the Wayback Machine gives the full timeline of captures; archive.today complements with on-demand snapshots.

## Trust & verifiability
`trust: community` — a convenience wrapper. Reliability rests on the underlying archive (Archive.org), which is authoritative; verify against the archive directly for anything you cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cachedview |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
