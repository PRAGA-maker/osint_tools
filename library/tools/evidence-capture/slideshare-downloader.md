---
id: slideshare-downloader
name: Slideshare Downloader
description: Use when you have a SlideShare presentation URL and want to capture it as a PDF for evidence — returns a downloaded, offline copy of the slides.
url: https://github.com/mohan3d/slideshare-go
category: evidence-capture
path:
- evidence-capture
bestFor: Downloading a public SlideShare deck to a local PDF so it is preserved before the uploader can edit or remove it.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free, open-source Go CLI; no account or key. You run it yourself.
opsec: active
opsecNote: The tool fetches the deck (and its slide images) directly from SlideShare's servers, so your IP/user-agent hits SlideShare on download — a normal viewer footprint, not a notification to the uploader. Route through a VPN/proxy if the download volume or target is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A single-developer GitHub project (mohan3d/slideshare-go); the code is inspectable, but it scrapes SlideShare's changing HTML/CDN, so it can break without notice and is not officially supported.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- slideshare-go
tags:
- Downloaders
- evidence-capture
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Slideshare Downloader

> A small Go CLI that pulls a public SlideShare presentation down to a local PDF — capture-before-it-vanishes for slide decks.

## When to use
You've found a SlideShare deck that matters to a case — an org's internal-looking presentation, a conference talk naming people, a pitch deck — and you want an offline, timestamped copy before the uploader edits or deletes it. This grabs the slides and saves them as a PDF you can archive, hash, and cite.

## How to use it (`bestInteractionPattern`: cli)
1. Install from https://github.com/mohan3d/slideshare-go (Go toolchain required; `go install` or build per the README).
2. Run the binary with the SlideShare presentation URL as its argument; choose high quality up front.
3. Wait for it to fetch each slide and assemble the PDF locally.
4. Verify the PDF opens and matches the live deck; record the source URL, capture date, and a file hash for chain-of-custody.
5. Pivot: names/logos/dates on the slides → people/org searches; the uploader's SlideShare profile → cross-platform enumeration.

## Inputs → Outputs
- **In:** a public SlideShare presentation URL
- **Out:** a local PDF copy of the deck (evidence artifact)
- **Empty/negative result looks like:** an error or a broken/partial PDF — SlideShare changed its markup/CDN, the deck is private/removed, or download is throttled; fall back to manual screen-capture or the Wayback Machine.

## Gotchas & OpSec
- Reliability: it scrapes SlideShare, which changes often, so `status: degraded` — test on a known deck first and expect occasional breakage.
- Evidence integrity: hash and note the capture time immediately; a scraped PDF is only as trustworthy as your provenance record.
- OpSec: active — downloading is a direct fetch from SlideShare; proxy it for sensitive targets.

## Overlaps ("do both")
- Pairs with the Wayback Machine and generic web-archiving tools — this makes a clean PDF of the deck specifically, while archives capture the surrounding page and history.

## Trust & verifiability
`trust: unverified` — an unofficial single-dev scraper; the output faithfully mirrors the live deck when it works, but there's no vendor guarantee and it can silently break, so always confirm the PDF against the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | slideshare-downloader |
