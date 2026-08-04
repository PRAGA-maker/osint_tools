---
id: archiveready
name: ArchiveReady
description: Use when you have a `domain`/URL and want to know whether (and how well) web archives can capture it — returns an archivability score across accessibility, cohesion, metadata, and standards.
url: http://archiveready.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether a page can be archived correctly before relying on (or forcing) a web-archive capture of it.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Free for personal use; commercial API access and support are paid.
opsec: passive
opsecNote: ArchiveReady fetches the target page from its own servers to analyse it, so the request comes from ArchiveReady, not you — your identity/IP isn't exposed to the target. It IS an active fetch of the page (the site owner could see ArchiveReady's crawler in logs), so it's not zero-touch on the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running (since 2012) academic-origin tool measuring archivability; a heuristic score, not a guarantee that a capture will succeed.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- Archive Ready
- archiveready.com
tags:
- web-archiving
- archivability
- preservation
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# ArchiveReady

> A page-archivability checker: given a URL, it scores how completely a web archive (like the Internet Archive) will be able to capture it.

## When to use
In OSINT you often need to *preserve* a page before it changes or disappears. ArchiveReady tells you, ahead of time, whether a target page will archive cleanly — flagging JavaScript-heavy content, missing metadata, or standards issues that cause captures to break. Reach for it when a page you're documenting is critical evidence and you want to know whether an archive.org snapshot will actually preserve it faithfully, or whether you need a fuller capture method.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://archiveready.com and enter the target URL.
2. It analyses the page's HTML, images, CSS, JavaScript, and sitemap.
3. Read the archivability score across four dimensions: **Accessibility, Cohesion, Metadata, Standards compliance**.
4. Interpret: a low score warns that an archive snapshot may miss content — so use a more robust capture (full-page screenshot, WARC capture, manual save) instead of trusting a simple archive.
5. Pivot: once you know it's archivable, push the page to the Internet Archive / archive.today for a permanent citation.

## Inputs → Outputs
- **In:** `domain`/URL
- **Out:** an archivability score and per-dimension `metadata-exif`-style report on what will/won't capture
- **Empty/negative result looks like:** a very low score or analysis failure — the page is JS-driven or blocks crawlers; treat that as "don't rely on a normal archive snapshot," not as "nothing to preserve."

## Gotchas & OpSec
- It evaluates *archivability*, not content — it won't save the page for you; pair it with an actual archiving service.
- The score is heuristic; a decent score still isn't a guarantee a capture is perfect.
- OpSec: the analysis is an active fetch by ArchiveReady's servers (not you), so your identity is shielded but the target's logs may show the crawler.

## Overlaps ("do both")
- Pairs with archiving services (Internet Archive's Save Page Now, archive.today): ArchiveReady tells you *whether* to trust a snapshot, those *make* the snapshot — check first, then capture, especially for evidence you must cite later.

## Trust & verifiability
`trust: community` — an established, academically-originated tool; its score is a well-reasoned heuristic, so use it to decide your capture strategy rather than as a definitive verdict.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archiveready |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
