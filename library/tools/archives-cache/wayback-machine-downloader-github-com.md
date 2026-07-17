---
id: wayback-machine-downloader-github-com
name: Wayback Machine Downloader
description: Use when you have a `domain` and want to bulk-download its entire archived history from the Internet Archive — returns the reconstructed site (every captured file) for offline review.
url: https://github.com/hartator/wayback-machine-downloader
category: archives-cache
path:
- archives-cache
bestFor: Bulk-downloading and reconstructing a whole website's Wayback Machine history to a local folder for offline analysis.
selectorsIn:
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: free
costNote: Free and open source (MIT). No account or payment; you only need Ruby installed.
opsec: passive
opsecNote: All requests hit web.archive.org, never the target's live site, so the subject is not notified. Your IP is visible to the Internet Archive; use a VPN/sock IP if you want to keep the pull unattributable, and throttle concurrency to avoid being rate-limited.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source Ruby gem (~6k GitHub stars, MIT-licensed) by hartator; widely used in the OSINT/archival community.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- wayback_machine_downloader
- hartator wayback downloader
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Wayback Machine Downloader

> A Ruby CLI that rips an entire site out of the Wayback Machine and rebuilds its directory tree locally — for when the live site is gone but its history matters.

## When to use
You have a `domain` (a defunct personal site, a deleted business page, a scrubbed blog tied to a subject) and you need more than a single archived snapshot — you want the whole captured history on disk so you can grep it, diff versions over time, and recover pages the live web no longer serves. Ideal when a target has taken content down but the Internet Archive still holds it.

## How to use it (`bestInteractionPattern`: cli)
1. Install Ruby (1.9.2+), then: `gem install wayback_machine_downloader`.
2. Run against the target domain/URL: `wayback_machine_downloader http://example.com`.
3. Scope the pull with flags as needed:
   - `--from 20150101 --to 20181231` to bound a date range,
   - `--only "/blog"` / `--exclude` to filter by URL pattern,
   - `--concurrency N` to speed it up (keep it modest to stay polite),
   - `--list` to emit a JSON index of captured files without downloading.
4. Read the output: files land in `./websites/<domain>/`, mirroring the original structure with generated `index.html` files. Open them offline, search the text, and compare captures across dates.

## Inputs → Outputs
- **In:** `domain` (or a specific URL/path prefix)
- **Out:** a local reconstructed copy of the archived site — HTML, assets, and a browsable directory tree (each archived file = a recoverable `document-id`)
- **Empty/negative result looks like:** "no matching files" / an empty `websites/` folder — the domain was never archived, or your date/pattern filters excluded everything. Loosen filters and retry.

## Gotchas & OpSec
- Purely passive against the subject: everything comes from web.archive.org. The target learns nothing.
- Large sites can be many thousands of snapshots — use date/path filters and reasonable concurrency, or you will pull far more than you need and risk temporary rate-limiting by the Archive.
- Captures are as-archived: dynamic pages, forms, and JS-loaded content may be incomplete. Absence of a page in the dump ≠ it never existed live.

## Overlaps ("do both")
- Pairs with the Wayback Machine web UI / other archive-cache tools — use the web UI to eyeball whether captures exist and pick a date range, then this tool to bulk-download that range for offline analysis.

## Trust & verifiability
`trust: community` — it's a well-established MIT-licensed open-source project; you can read the source. The *data* is the Internet Archive's, which is authoritative, so trust rides on the Archive, not the downloader.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-machine-downloader-github-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
