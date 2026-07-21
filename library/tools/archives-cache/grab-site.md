---
id: grab-site
name: grab-site
description: Use when you have a `domain` or `social-profile` URL and want to capture a full, court-quality WARC archive of it before it changes or disappears — returns a self-contained WARC archive (evidence preservation, no selector output).
url: https://github.com/ArchiveTeam/grab-site
category: archives-cache
path:
- archives-cache
bestFor: Recursively crawling and preserving a target website or profile to WARC with a live dashboard and adjustable ignore rules.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source (ArchiveTeam). Costs are only your own bandwidth and disk.
opsec: active
opsecNote: This is ACTIVE — a recursive crawl hits the target's server directly and appears in their logs (source IP, User-Agent, request volume). Crawl from a sock-puppet VPS/IP, throttle with --delay and --concurrency, and prefer a one-shot capture (--1) if you only need a single page. Never point it at a login-gated area you accessed with the subject's credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by ArchiveTeam (the group behind large-scale web preservation); widely used, open-source, produces standard WARC readable in any WARC viewer.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- grab-site
- ArchiveTeam grab-site
tags:
- Archives
- Tools for working with WARC (WebARChive) files
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# grab-site

> ArchiveTeam's recursive website crawler — the tool for making a defensible, complete WARC snapshot of a target's site or profile before it can be edited or deleted.

## When to use
You have a `domain`, blog, or public `social-profile` URL that matters to a case and you need to *preserve* it — pages, images, requisites, structure — as evidence, in a standard WARC you can revisit, hash, and re-render later. Reach for it when a subject's site might change or be taken down and a single screenshot isn't enough.

## How to use it (`bestInteractionPattern`: cli)
1. Install per OS (Ubuntu/Debian/macOS-brew/WSL): set up a Python 3.8 venv and `pip install grab-site` (see the repo README for the exact supported steps).
2. Start the dashboard: `gs-server`, then open the local dashboard URL to watch progress.
3. Launch a crawl: `grab-site 'https://target.example'`. Add:
   - `--1` capture only that URL + page requisites (no recursion) — smallest footprint,
   - `--igsets=IGSET1,IGSET2` apply ignore sets, `--concurrency=N`, `--delay=N` to throttle politely,
4. Output is a timestamped WARC directory; verify by re-rendering it in a WARC viewer (e.g. an offline replay tool).
5. Pivot: read the captured pages for `associate`, `employer-org`, contact details, or `metadata-exif` in downloaded images; keep the WARC as the immutable record.

## Inputs → Outputs
- **In:** `domain` / URL to preserve
- **Out:** a WARC archive (preservation artifact); the *contents* are what you then mine for selectors
- **Empty/negative result looks like:** the crawl stalls, 403s, or captures a login wall / JS-only shell — meaning the site blocks crawlers or renders client-side; try `--1`, adjust ignore sets, or switch to a hosted archiver.

## Gotchas & OpSec
- **Active**: recursive crawling is loud in the target's logs and can trip rate-limits or bot defenses — throttle, and use a disposable IP.
- Large sites produce large WARCs quickly; watch disk (a hard constraint in ephemeral environments).
- Heavily JavaScript-driven sites archive poorly (WARC captures HTTP responses, not a rendered DOM).
- Do not crawl authenticated/private areas of a subject's account.

## Overlaps ("do both")
- Pairs with hosted one-click archivers like `[[archive-today]]` and `[[archive-org]]` — those give a quick public snapshot with less setup, while grab-site gives you a complete, self-hosted, offline WARC you control. Capture with both so a public snapshot exists *and* you hold the raw evidence.

## Trust & verifiability
`trust: community` — open-source, maintained by ArchiveTeam; output is standard WARC, independently verifiable in any WARC replay tool, and hashable for chain-of-custody.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grab-site |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
