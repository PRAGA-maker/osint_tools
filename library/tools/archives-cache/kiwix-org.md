---
id: kiwix-org
name: kiwix.org
description: Use when you need offline, censorship-proof access to a whole website/wiki (a `domain`) — returns a locally-served snapshot whose articles you can cite as `document-id`.
url: https://www.kiwix.org/en/
category: archives-cache
path:
- archives-cache
bestFor: Reading and searching entire websites/wikis (Wikipedia, Stack Exchange, wikis, forums) offline from downloaded ZIM snapshots — useful when the live source is blocked, down, or altered.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free and open source; funded by donations, no ads, no personal-data collection. ZIM content packages are free downloads.
opsec: passive
opsecNote: Once a ZIM is downloaded, all reading/searching is local — no network calls, so nothing about your query reaches the origin site or anyone else. Downloading the ZIM itself is the only networked (and passive) step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Nonprofit (Kiwix) with 20+ years of operation, open-source code, 10M+ users; ZIM snapshots are faithful captures of their source sites at capture time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Kiwix
- kiwix reader
- ZIM
tags:
- archive
- Archive & Cached Related Sites
- offline
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# kiwix.org

> The "internet that works offline" — a free reader that serves entire websites (Wikipedia, wikis, Stack Exchange, forums) from downloaded ZIM snapshots, immune to takedowns, blocks and edits.

## When to use
You need a whole reference site — most often Wikipedia, but also Stack Exchange, Wikivoyage, wikis and forum captures — available offline and frozen at a point in time. Valuable when the live `domain` is censored/blocked in a region, has gone down, or when you want a snapshot that later edits or deletions cannot alter (an archival copy you can cite by article, `document-id`).

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install a Kiwix reader (Kiwix Desktop for Windows/macOS/Linux, or the mobile app) from https://www.kiwix.org/en/ .
2. Open the in-app content catalog and download the ZIM package for the site/topic you need (e.g. a full or "no-pictures" Wikipedia, a Stack Exchange, a specific wiki).
3. Open the ZIM in the reader; browse and full-text-search the entire site locally.
4. Read the output: individual articles/pages (`document-id`) exactly as captured, with no live connection to the origin.
5. Pivot: cite the offline article as a stable snapshot; for larger deployments, serve a ZIM to others via Kiwix Server/Hotspot.

## Inputs → Outputs
- **In:** `domain` (a site available as a ZIM package)
- **Out:** `document-id` (offline articles/pages from that captured site)
- **Empty/negative result looks like:** the site you want has no ZIM in the catalog — Kiwix can only serve content someone has already packaged; it is not a live archiver of arbitrary URLs.

## Gotchas & OpSec
- Snapshot, not live: a ZIM reflects the source as of its capture date; newer content/edits are absent until a fresh ZIM is released.
- It serves pre-packaged collections, not on-demand captures of any URL — for arbitrary page archiving use a web-archive tool instead.
- ZIM files are large (a full Wikipedia is tens of GB); mind disk space.
- OpSec: reading is entirely offline and passive.

## Overlaps ("do both")
- Complements live web-archive/cache tools: those capture a single arbitrary URL on demand, while Kiwix gives you an entire site offline and frozen for censorship-proof reference.

## Trust & verifiability
`trust: trusted` — an established open-source nonprofit; ZIM snapshots are faithful, verifiable captures of well-known sources, though always as-of their capture date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kiwix-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | no |
