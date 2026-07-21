---
id: ricks-apps-com
name: SiteSucker (ricks-apps.com)
description: Use when you have a `domain`/URL and want a full local, offline copy of the site before it changes or disappears — returns a browsable mirror of pages, images, PDFs and files preserved as evidence.
url: https://ricks-apps.com/osx/sitesucker/index.html
category: archives-cache
path:
- archives-cache
bestFor: Mirroring a target website to disk (macOS/iOS) to preserve evidence before it's edited or taken down.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free version on the Mac App Store handles standard site downloads; SiteSucker Pro (paid) adds embedded-video download and Tor access. The free tier is fully usable for basic mirroring.
opsec: active
opsecNote: Downloading a site fetches every page from the target's server — that is direct, logged contact from your IP. Use a VPN/sock-puppet network; the Pro version's Tor support helps. A crawl can be noisy, so throttle it for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: A long-established, actively maintained macOS/iOS app (Rick Cranisky) distributed via the Mac App Store; the download it produces is a faithful copy you control and can verify.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SiteSucker
- SiteSucker Pro
tags:
- archive
- Archive & Cached Related Sites
- website-mirror
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- sitesucker
---

# SiteSucker (ricks-apps.com)

> A macOS/iOS website downloader — grab a full offline mirror of a target site (pages, images, PDFs) while you still can, and hold it as evidence you control.

## When to use
You've found a website, profile, forum, or listing that matters to the case and you fear it will be **edited or deleted** — a subject's personal site, a scam page, a for-sale listing. SiteSucker copies the whole site (or a scoped subtree) to your disk, preserving the directory structure, so you have a timestamped, browsable snapshot independent of the live server or third-party archives.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install SiteSucker from the Mac App Store (free) — or SiteSucker Pro for embedded-video/Tor features — from https://ricks-apps.com/osx/sitesucker/index.html.
2. Paste the target `domain`/URL, set crawl limits (depth, same-host only, file types) to avoid pulling the whole internet.
3. Start the download; it mirrors HTML, images, PDFs and other files locally, rewriting links so the copy browses offline.
4. Note the capture time and keep the folder read-only for chain-of-custody.
5. Pivot: PDFs/images in the mirror feed metadata/EXIF extraction; page text yields names, emails, and phone numbers for further lookups.

## Inputs → Outputs
- **In:** a `domain`/URL (with crawl scope)
- **Out:** a local, browsable site mirror — pages plus downloaded documents/files (`document-id`-style preserved artifacts)
- **Empty/negative result looks like:** a near-empty download — the site is JS-rendered (SiteSucker sees limited dynamic content), blocked the crawler, or requires login; consider a headless-browser capture instead.

## Gotchas & OpSec
- **Active and noisy**: a crawl hammers the target from your IP and appears in their logs — VPN/Tor and throttle for sensitive work.
- Heavily JavaScript-driven sites (SPAs) mirror poorly; it's best for classic server-rendered pages and file trees.
- Respect scope limits or you'll pull gigabytes; set same-host and depth caps first.

## Overlaps ("do both")
- Pairs with the Wayback Machine and other cache tools — SiteSucker gives you a *self-held* copy you control, archives give an independent third-party timestamp; capture both for a contested site.

## Trust & verifiability
`trust: trusted` — a reputable, long-maintained App Store application; because you hold the raw downloaded files, the evidence is directly inspectable and hash-verifiable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ricks-apps-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
