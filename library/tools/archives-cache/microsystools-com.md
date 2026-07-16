---
id: microsystools-com
name: A1 Website Download (Microsys)
description: Use when you have a `domain` you need to preserve and want a full offline copy — returns a locally-saved, browsable snapshot of the entire site.
url: https://www.microsystools.com/products/website-download/
category: archives-cache
path:
- archives-cache
bestFor: Downloading an entire website to disk (a1 website copier) for offline analysis and evidence preservation.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free mode caps at 500 pages per site; the paid license ($39) removes crawl limits and adds command-line support. 30-day full trial available.
opsec: active
opsecNote: Crawling a target site fetches many pages rapidly from your IP — that traffic is visible in the site's server logs and can look like scraping. Use a sock-puppet IP/VPN, throttle the crawl, and consider mirroring an archived copy instead of hitting the live site if you want to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Commercial desktop software from Microsys (A1 Website Download); a legitimate, long-standing site-copier akin to HTTrack — download from the official vendor only.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- a1-website-download
aliases:
- A1 Website Download
- Microsys Website Downloader
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# A1 Website Download (Microsys)

> A desktop website copier — pull an entire site to disk with links rewritten to local paths, so you can browse, search, and preserve it offline before it changes or disappears.

## When to use
You've found a website relevant to a case (a subject's personal/business site, a forum, a listing) and want a complete, timestamped local copy for evidence and offline analysis — searching across all pages at once, or guarding against the site being taken down. Reach for it when a single-page save (or web.archive.org) isn't enough and you need the whole tree.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install A1 Website Download from the official Microsys page (Windows/Mac); start the 30-day trial or free mode.
2. Enter the target `domain`/URL as the crawl root.
3. Configure scope (depth, page limit — free mode caps at 500 pages), throttling, and file-type filters.
4. Run the crawl; it saves the site with links corrected to relative local paths for offline browsing.
5. Analyze offline: grep the local copy for names, emails, phone numbers, or hidden pages.
6. Pivot: harvested contact details/subpages feed people- and domain-OSINT; the archived copy is your evidence baseline.

## Inputs → Outputs
- **In:** a `domain`/URL to crawl
- **Out:** a local, browsable `domain` snapshot (all pages/assets on disk)
- **Empty/negative result looks like:** a crawl that returns few/no pages — the site blocks crawlers (robots/anti-bot), requires login, or is a JS-only SPA the copier can't render; try an archived version or a headless-browser approach.

## Gotchas & OpSec
- Active crawling is noisy and can be rate-limited or blocked; throttle and use a persona IP.
- Free mode's 500-page cap truncates large sites; paid lifts it.
- JavaScript-heavy sites may not mirror well with a classic copier.
- Legal: only mirror sites you're authorized to collect within your engagement's rules.

## Overlaps ("do both")
- Pairs with `[[a1-website-download]]` (same product) and the Wayback Machine — mirror the live site for a current copy, and pull Wayback snapshots for historical states the live crawl can't show.

## Trust & verifiability
`trust: community` — reputable commercial site-copier software; the local copy is a faithful mirror you control, but note the capture date and source since sites change.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | microsystools-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
