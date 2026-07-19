---
id: replayweb
name: ReplayWeb.page
description: Use when you have a WARC/WACZ web-archive file and want to browse it as a live site — returns an interactive replay of the captured pages, in-browser and offline.
url: https://github.com/webrecorder/replayweb.page
category: archives-cache
path:
- archives-cache
bestFor: Opening and browsing WARC/WACZ web-archive captures locally, with no server, to review preserved evidence.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (Webrecorder); use the hosted app or self-host — no account.
opsec: passive
opsecNote: It replays your local archive file entirely in the browser — the WACZ/WARC is loaded client-side and not uploaded, so reviewing a capture leaks nothing about the archive's contents or the subject. Fully passive and offline-capable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built by Webrecorder, the leading open-source web-archiving project; a standard, reliable tool for WARC/WACZ replay.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- har2warc
aliases:
- replayweb.page
- ReplayWeb
tags:
- Archives
- Tools for working with WARC (WebARChive) files
- web-archiving
- evidence
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# ReplayWeb.page

> Webrecorder's in-browser player for web archives — drop in a WARC or WACZ file and browse the captured site interactively, entirely client-side and offline.

## When to use
You have a web-archive file (WARC or WACZ) — a capture you made, evidence handed to you, or a downloaded archive — and need to *view* it as it was when captured: clickable pages, media, dynamic content. Instead of parsing raw WARC, ReplayWeb.page replays it like a live site. Essential for reviewing preserved social-media/profile captures, verifying evidence, and revisiting a page as it existed at capture time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the hosted app at https://replayweb.page (or self-host / use the ArchiveWeb.page desktop app; source is on GitHub).
2. Load your `.warc`/`.warc.gz`/`.wacz` file — it stays local in the browser, nothing is uploaded.
3. Browse the captured pages: navigate links, view media, and use the capture's URL/timestamp list to jump to specific snapshots.
4. For sharing, WACZ files can be embedded in a page with the ReplayWeb.page web component.
5. Pivot: content/media inside the replay → the normal analysis (reverse-image, EXIF, links); capture timestamps → timeline evidence.

## Inputs → Outputs
- **In:** a WARC or WACZ web-archive file (no live selector)
- **Out:** an interactive, offline replay of the archived pages and media
- **Empty/negative result looks like:** the archive loads but pages are broken/incomplete — the original capture missed resources (JS/media not archived), a capture-quality issue, not a replay bug; try the raw WARC index to see what was actually captured.

## Gotchas & OpSec
- Replay fidelity is bounded by capture quality — if the crawler didn't grab a resource, ReplayWeb.page can't show it.
- Large archives can be slow in-browser; the desktop app handles big files better.
- OpSec: passive and local — the file isn't uploaded, so it's safe for sensitive/evidentiary captures.

## Overlaps ("do both")
- Pairs with `[[har2warc]]` (convert a browser HAR into WARC to replay) and capture tools (ArchiveWeb.page, wget/warc, Conifer) — those create the archive, ReplayWeb.page reviews it.

## Trust & verifiability
`trust: trusted` — the reference open-source replay tool from Webrecorder; it faithfully renders whatever the archive contains, so trust rests on the capture's provenance, which you control.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | replayweb |
| category | archives-cache |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
