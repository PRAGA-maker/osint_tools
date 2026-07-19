---
id: cached-view
name: Cached View
description: Use when you have a `domain`/URL that has been removed or changed and want to see an archived copy — returns cached snapshots via the Wayback Machine.
url: https://cachedview.com/
category: archives-cache
path:
- archives-cache
- web
bestFor: One-box front end for pulling an archived copy of a page that has been deleted, edited, or taken offline.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free, ad-supported, no account. Value now depends entirely on the underlying Wayback Machine coverage.
opsec: passive
opsecNote: You query the archive/cache service, not the target's live server, so the site owner does not see your request. The archive provider (Internet Archive) logs the lookup, not the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A thin third-party UI over public archives; it holds no data itself. Trust the underlying Wayback snapshot, not CachedView the wrapper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- cachedview
- wayback-machine
tags:
- archive
- cache
- wayback
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Cached View

> A quick lookup box that fetches an archived copy of a URL — historically Google Cache, now (since Google killed its cache in 2024) a thin front end to the Wayback Machine.

## When to use
A page you need — a deleted profile, an edited business listing, a scrubbed forum post, a removed classified ad — no longer exists or has changed since you last saw it. Paste the URL here to check whether an archived snapshot preserves the old content, so you can recover a phone number, address, username, or photo that the subject removed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cachedview.com/.
2. Paste the full URL of the removed/changed page into the box.
3. Submit and follow the provided link, which now resolves to an Internet Archive (Wayback) snapshot of that URL.
4. On the archive page, use the calendar/timeline to pick a capture date close to when the content was live.
5. Read the snapshot for the details that were later deleted; screenshot or save the page as evidence with its capture timestamp.
6. Pivot: recovered selectors (old `phone`, `address`, `username`, image) feed people-search or social lookups.

## Inputs → Outputs
- **In:** a URL / `domain` path
- **Out:** links to archived snapshots of that URL (Wayback captures)
- **Empty/negative result looks like:** no snapshot found / the archive has never captured this URL — that means no cache exists, not that the page never existed. Try the Wayback Machine directly with URL variants (trailing slash, http vs https, www).

## Gotchas & OpSec
- Since Google discontinued cached pages in early 2024, the Google-cache path is dead; only the Wayback route works, so CachedView adds little over going to web.archive.org yourself.
- No snapshot ≠ page never existed; archives are sparse for low-traffic and login-gated pages. Absence is not evidence.
- OpSec: passive — you hit the archive, not the target's server. Safe against a subject who monitors their own site's logs.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` and `[[cachedview]]` — go straight to the Wayback Machine for full timeline/calendar control and CDX search; use CachedView only as a fast one-box shortcut.

## Trust & verifiability
`trust: community` — CachedView stores nothing itself and is just a redirector; the authoritative artifact is the Internet Archive snapshot it points to, which carries its own capture timestamp you should cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cached-view |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
