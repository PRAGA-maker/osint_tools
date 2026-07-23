---
id: sitesucker
name: SiteSucker
description: Use when you have a website URL (`domain`) and want a complete offline copy for preservation and analysis — downloads the site's pages, images, PDFs and files with structure intact.
url: http://ricks-apps.com/osx/sitesucker/index.html
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Mirroring an entire website locally (pages, images, documents) for offline review and evidence preservation.
selectorsIn:
- domain
selectorsOut:
- image
status: live
pricing: freemium
costNote: Standard SiteSucker is free on the Mac App Store; SiteSucker Pro (embedded-video and Tor support) is paid with a 14-day trial. macOS only.
opsec: active
opsecNote: SiteSucker downloads from YOUR machine/IP, crawling the target site directly — the target's server sees and can log the crawl (many requests from your address). Throttle the download, respect robots where appropriate, and consider Tor (Pro) or a VPN when the crawl should not trace back to you. Only mirror sites you're authorized to archive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: A long-established, widely-used macOS site-downloader (Rick Cranisky); mature and reliable, distributed via the Mac App Store.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- ricks-apps-com
aliases:
- SiteSucker
tags:
- website-mirror
- offline-copy
- macos
- evidence-capture
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# SiteSucker

> A macOS application that downloads an entire website — pages, images, PDFs, files — into a local mirror for offline browsing and preservation.

## When to use
You have a `domain` and want a full offline copy — to preserve a site before it changes or disappears, to analyze its structure and files at leisure, or to extract all its documents/images in one pass. More thorough than a single-page screenshot: it recursively pulls the site's content while keeping the directory layout intact.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install SiteSucker from the Mac App Store (standard is free; Pro adds video/Tor).
2. Enter the starting URL (`domain`).
3. Adjust settings — crawl depth, file types, download throttling, and whether to stay on the same host.
4. Start the download and let it mirror the site locally.
5. Review the local copy offline; pull out images/PDFs for further analysis (metadata, reverse-image search).

## Inputs → Outputs
- **In:** a website URL (`domain`)
- **Out:** a local mirror — HTML pages, `image`s, PDFs and other files with the site's structure preserved
- **Empty/negative result looks like:** little downloaded — the site may block crawlers, require login, or be JavaScript-rendered so the crawler sees little; try a browser-based capture instead.

## Gotchas & OpSec
- **Active crawl from your IP:** the target logs many requests from you — throttle and use Tor (Pro)/VPN when attribution matters.
- macOS only; no Windows/Linux build (use wget/HTTrack there).
- JS-heavy sites mirror poorly — dynamic content may be missing.

## Overlaps ("do both")
- Pairs with full-page capture and image-extraction tools (`[[screenshot-guru]]`, `[[image-extractor]]`) — SiteSucker mirrors the whole site while those grab a rendered page or its images; and with the Wayback Machine for a hosted archive.

## Trust & verifiability
`trust: community` — a mature, widely-used macOS utility distributed via the Mac App Store; the local mirror is directly inspectable, so its output is self-verifying.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sitesucker |
