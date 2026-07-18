---
id: archivebox
name: ArchiveBox
description: Use when you need to preserve web pages, profiles, or posts before they change or vanish — self-hosted, it captures HTML/PDF/WARC/screenshots and any metadata-exif inside saved media.
url: https://archivebox.io
category: archives-cache
path:
- archives-cache
bestFor: Self-hosted, court-defensible archiving of URLs (social posts, listings, articles) into multiple durable formats you fully control.
selectorsIn:
- domain
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: MIT-licensed and free/open-source; you supply your own hardware/hosting. No account or subscription.
opsec: active
opsecNote: ArchiveBox fetches each target URL directly from your infrastructure, so the capture hits the site from your IP and can appear in the site's logs. Run it behind a VPN/proxy or a dedicated egress IP when archiving a target who might notice repeated fetches.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: trusted
trustNote: Mature, widely used open-source project (nonprofit-supported, source on GitHub); you can audit exactly what it does.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- archivebox.io
- ArchiveBox self-hosted
tags:
- archives-cache
- web-archiving
- self-hosted
- evidence-preservation
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# ArchiveBox

> An open-source, self-hosted web archiver: point it at any URL and it saves rendered HTML, a screenshot, a PDF, a WARC, extracted article text, and downloaded media — all on infrastructure you control.

## When to use
You have found a page that matters to a case — a social `social-profile`, a classified listing on a `domain`, a forum post — and you need a fixed, timestamped copy before it is edited or deleted. Unlike a public cache, ArchiveBox gives you a private, complete capture (including downloaded images whose `metadata-exif` you can then examine) that won't disappear and that you can present as evidence.

## How to use it (`bestInteractionPattern`: docker)
1. Install via Docker Compose (recommended): `docker compose run archivebox init --setup`, then `docker compose up`. (Pip, Brew, and .deb installs also exist.)
2. Add URLs: `docker compose run archivebox add 'https://example.com/target-page'`, or feed a list of URLs / a browser-history / bookmarks export for bulk capture.
3. ArchiveBox creates a snapshot folder per URL containing `index.html`, `screenshot.png`, `output.pdf`, `warc/`, `media/`, extracted text, favicon, and response headers.
4. Review through the built-in web UI (`docker compose up`, then browse the admin), and inspect saved media for embedded `metadata-exif`. Pivot: EXIF in a downloaded image can yield `geolocation` or `device-id`; the frozen copy backs up any later claim about the page's content.

## Inputs → Outputs
- **In:** `domain` / URL or a `social-profile` URL to capture
- **Out:** a durable multi-format snapshot; `metadata-exif` recoverable from saved media (and a fixed record of the page's text/appearance)
- **Empty/negative result looks like:** a snapshot that captured only a login wall, a CAPTCHA page, or a JS-blocked shell — the URL was gated, so the archive holds no real content.

## Gotchas & OpSec
- Human-in-the-loop: none for open pages, but content behind a login won't archive unless you supply cookies/session config — and doing so ties the capture to that account.
- OpSec: **active** — captures originate from your server's IP and can show in the target site's logs; route egress through a VPN/proxy for sensitive targets and avoid hammering a small site.
- Chain of custody: keep the original snapshot folder and its hashes untouched if you may need to demonstrate integrity later.

## Overlaps ("do both")
- Complements public caches/`web.archive.org`-style tools — a public archive is quick and third-party-attested, while ArchiveBox gives you a private, complete, self-controlled copy including media the public cache skips.

## Trust & verifiability
`trust: trusted` — it is a mature open-source project whose code you can audit; because you run it yourself, you know exactly what was fetched and when.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archivebox |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, social-profile → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | docker |
| opsec | active |
| human-in-loop | no |
