---
id: a1-website-download
name: A1 Website Download
description: Use when you have a `domain`/URL and want a complete offline mirror of a site for preservation and analysis — returns document-id, image, metadata-exif.
url: http://www.microsystools.com/products/website-download
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Mirroring an entire website to disk for offline evidence review and archiving.
selectorsIn:
- domain
selectorsOut:
- document-id
- image
- metadata-exif
status: live
pricing: freemium
costNote: Free mode crawls up to 500 pages per site indefinitely; 30-day fully-functional trial; Pro license ~$39 for unlimited crawl depth and command-line support.
opsec: active
opsecNote: Active — the crawler downloads pages directly from the target site, exposing your IP/User-Agent and generating a burst of server-log traffic that's easy to notice. Route through a proxy/VPN and throttle the crawl for any subject-controlled site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: community
trustNote: Long-established commercial utility by Microsys; it is a downloader, so the trust question is the integrity of the target site's content, not the tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- A1 Website Download
- Microsys A1
tags:
- offline-browsing
- archiving
- scraping
source: awesome-osint
lastVerified: '2026-07-29'
relatedTools:
- microsystools-com
enrichment: full
---

# A1 Website Download

> A desktop site-ripper that copies an entire website to disk with links rewritten for offline browsing — a way to snapshot a target site before it changes or disappears.

## When to use
You have a `domain`/URL whose contents you need to **preserve and study offline** — a subject's blog, a forum, a listing site, or any page you fear may be edited or taken down. A1 mirrors the whole site (HTML, images, CSS, JS-referenced assets), converting links to relative paths so the copy browses locally. Use it for evidence capture and for grepping a whole site's text/metadata at once.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install the A1 Website Download desktop app (Windows or macOS) from the Microsys site.
2. Enter the target site's root URL and configure scope (paths to include/exclude, depth, file types).
3. Start the crawl; free mode stops at 500 pages, the trial and Pro license lift that limit.
4. Browse the mirrored copy locally, or point local tooling (grep, an EXIF reader, a metadata parser) at the downloaded files.
5. Pivot: harvested images feed reverse-image search; downloaded documents feed `[[metadata-parser]]`-style extraction; the local corpus lets you search the whole site's text at once.

## Inputs → Outputs
- **In:** `domain`/URL (site root + crawl scope)
- **Out:** an offline copy — page `document-id`s (HTML/PDF/docs), `image` assets, and embedded page `metadata-exif`
- **Empty/negative result looks like:** a near-empty mirror — the site is JavaScript-rendered, login-gated, or blocking crawlers, so only shell pages downloaded.

## Gotchas & OpSec
- **Active and noisy:** a site crawl is many rapid requests from your IP; it stands out in logs. Proxy and rate-limit for subject-controlled targets.
- The free tier's 500-page cap may truncate large sites — note the limit rather than assume you captured everything.
- Client-side-rendered content and login-walled pages won't be captured; timestamp your snapshot for evidentiary integrity.

## Overlaps ("do both")
- Complements a live archiving service (e.g. Wayback/archive.today) — public archives give a timestamped third-party copy, while A1 gives you a full local corpus you can search and process offline.
- See the vendor overview at `[[microsystools-com]]`.

## Trust & verifiability
`trust: community` — a mature commercial tool that faithfully copies whatever the site serves; verify the captured content against the live site and record capture time/settings for any evidentiary use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | a1-website-download |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → document-id, image, metadata-exif |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
