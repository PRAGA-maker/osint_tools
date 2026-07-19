---
id: pagecached-com
name: pagecached.com
description: Use when you have a `domain`/URL and want to know which archives hold a cached snapshot — returns links to Wayback, Archive.today, Bing, Yahoo Japan and other caches for that page.
url: https://pagecached.com/
category: archives-cache
path:
- archives-cache
bestFor: One-shot check of whether a specific URL is cached across multiple archive services.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free; no account or payment.
opsec: passive
opsecNote: You submit a URL to pagecached, which then queries several third-party caches — the archives (not the target site) see the lookup. Retrieving an archived snapshot does not touch the target's live server, so it's a safe way to view a page without alerting the site owner. Still, do the lookup from a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small third-party aggregator that dispatches to the real archives; it's a convenience router, and the authoritative content lives on Wayback/Archive.today themselves.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-today
- wayback-machine
aliases:
- PageCached
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# pagecached.com

> A one-box front end that checks several archive/cache services at once to tell you whether a given URL was ever snapshotted.

## When to use
You have a `domain` or a specific URL — a since-deleted profile, a scrubbed listing, an edited page — and want to recover the prior content without hitting the live server. Instead of checking Wayback, Archive.today, Bing and others by hand, pagecached fires the URL at all of them and returns the hits.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pagecached.com/ in a sock-puppet browser.
2. Paste the full target URL into the search box and submit.
3. It reports, per source (Wayback Machine, Archive.today, Bing cache, Yahoo Japan, Arquivo and others), whether a cached copy exists and links to it.
4. Click through to the archive that has a snapshot to read the preserved content.
5. Pivot: a recovered snapshot may hold a `name`, `phone`, `email`, or `image` the live page has since removed; feed those onward.

## Inputs → Outputs
- **In:** `domain` / full URL
- **Out:** links to archived snapshots (each a `document-id`-style preserved copy)
- **Empty/negative result looks like:** every source returns "not cached" — the page was never archived by these services; try the archives' own search or a different URL form (trailing slash, http vs https).

## Gotchas & OpSec
- It's a router: some cache providers it lists (e.g. Google cache) have been discontinued, so a "no result" may reflect a dead upstream, not a truly un-archived page — confirm on [[wayback-machine]] and [[archive-today]] directly.
- Snapshots reflect the page *at capture time*; timestamps matter — note the capture date.
- OpSec: passive and safe against the target; the archives see the lookup, not the subject.

## Overlaps ("do both")
- Pairs with [[wayback-machine]] and [[archive-today]] — pagecached is a fast triage that tells you *where* a copy exists; then go to that archive directly for full history, all captures, and to submit a fresh capture if none exists.

## Trust & verifiability
`trust: community` — an unofficial aggregator; trust the underlying archives it points to, and always verify a hit by opening the snapshot on the source service itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pagecached-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
