---
id: waybackpy
name: waybackpy
description: Use when you have a `domain` or URL and want to pull its Wayback Machine capture history programmatically — returns archived snapshot URLs and timestamps.
url: https://github.com/akamhy/waybackpy
category: archives-cache
path:
- archives-cache
bestFor: Scripting Wayback Machine snapshot lookups (oldest/newest/near-date) and bulk CDX queries from Python or the CLI.
selectorsIn:
- domain
selectorsOut:
- domain
- metadata-exif
status: live
pricing: free
costNote: Free open-source package (MIT); talks to the Internet Archive's public Wayback APIs, which are free and need no key.
opsec: passive
opsecNote: All queries hit archive.org, not the target's live server, so the subject is never touched. Your IP is visible to the Internet Archive but not to the person you're investigating. Avoid the Save API on a sensitive URL unless you want a fresh public capture to exist.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source wrapper (~600 stars) by akamhy; it only formats requests to the Internet Archive's own APIs, so the underlying data is authoritative even though the wrapper is community-maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- waybackpack
- wayback-google-analytics
aliases:
- waybackpy CLI
- wayback machine python
tags:
- web-history-and-website-capture
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# waybackpy

> A thin Python/CLI wrapper over the Internet Archive Wayback Machine's Save, CDX, and Availability APIs — for scripting capture-history lookups instead of clicking through the web UI.

## When to use
You have a `domain` or a specific URL (a subject's old blog, a since-deleted profile page, a company site) and want to enumerate every archived capture, grab the oldest/newest snapshot, or find the capture nearest a given date — as a repeatable script rather than manual browsing. Ideal when you need to process many URLs or feed snapshot lists into other tooling.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install waybackpy`.
2. Newest / oldest capture of a URL:
   `waybackpy --url "https://example.com/~person" --newest`
   `waybackpy --url "https://example.com/~person" --oldest`
3. Capture nearest a date (useful for "what did this look like the week they disappeared"):
   `waybackpy --url "https://example.com" --near --year 2021 --month 6`
4. Enumerate all snapshots via the CDX API (in Python):
   ```python
   from waybackpy import WaybackMachineCDXServerAPI
   cdx = WaybackMachineCDXServerAPI("example.com/*", "my-ua")
   for snap in cdx.snapshots():
       print(snap.timestamp, snap.archive_url)
   ```
5. Pivot: feed the returned `archive_url`s into a browser or scraper; the timestamps corroborate when content existed and can anchor a timeline.

## Inputs → Outputs
- **In:** `domain` / URL (wildcards like `example.com/*` supported via CDX)
- **Out:** archived snapshot URLs, capture timestamps, HTTP status/MIME metadata
- **Empty/negative result looks like:** `NoCDXRecordFound` / an empty snapshot iterator — the URL was never archived (not proof the page never existed; try broader wildcards or a parent path).

## Gotchas & OpSec
- No login or API key needed, but the Internet Archive rate-limits heavy CDX queries; back off on 429s.
- The **Save API** (`save()`) creates a *new public capture* of a live URL — do not run it on a sensitive target unless you intend a permanent public record.
- Passive toward the subject: everything routes through archive.org, so the person's own server sees nothing.
- v3 pinned to Python 3.6+; some older tutorials show the deprecated `Url` class — use `WaybackMachineCDXServerAPI` / `WaybackMachineSaveAPI`.

## Overlaps ("do both")
- Pairs with `[[waybackpack]]` — waybackpack downloads the archived files to disk; waybackpy is better for querying the index and picking which captures to pull.
- Pairs with `[[wayback-google-analytics]]` — once you have historical captures, extract Google Analytics/AdSense IDs to link the site to others.

## Trust & verifiability
`trust: community` — the wrapper is third-party, but it only marshals calls to the Internet Archive's first-party APIs, so returned snapshots and timestamps are as authoritative as archive.org itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waybackpy |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
