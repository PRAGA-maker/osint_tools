---
id: web-page-saver
name: Web Page Saver (Magnet Forensics)
description: Use when you have a list of web URLs and need forensic-grade, offline, court-ready captures — a free Windows tool producing scrolling snapshots in a navigable HTML report.
url: https://www.magnetforensics.com/resources/web-page-saver/
category: evidence-capture
path:
- evidence-capture
- web-browsing
bestFor: Preserving web pages as timestamped scrolling snapshots for evidence/citation, viewable offline, from a batch of URLs.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free tool from Magnet Forensics; Windows only (registration/download may be requested).
opsec: active
opsecNote: Capturing a page means your machine actually visits each URL, so the target site's logs see your IP/user-agent at capture time — that is an active footprint on the source. Capture from a sock-puppet/VPN'd machine for sensitive targets. Once saved, the report is offline and passive to store/share.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Published by Magnet Forensics, a mainstream digital-forensics vendor; widely used for defensible web-evidence capture (exports to SQLite for AXIOM).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- send-to-internet-archive-chrome-google-com
aliases:
- Magnet Web Page Saver
- WPS
tags:
- evidence-capture
- forensics
- web-archiving
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Web Page Saver (Magnet Forensics)

> A free forensic tool that turns a list of URLs into timestamped, scrolling, offline-viewable snapshots — for evidence you may need to show in court.

## When to use
You've found web content about a subject (a social post, listing, forum thread, article) and need to preserve it defensibly before it changes or disappears — with a capture that looks like the real page, is timestamped, and can be viewed offline in a courtroom or report. Feed it one or many URLs and get a clean HTML report.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download and install Web Page Saver on Windows (7+) from Magnet Forensics.
2. Add URLs manually or import a list from a text/CSV file. Optionally set agency logo/title for the report.
3. Run the capture: it loads each page and saves a full scrolling snapshot.
4. Output: a navigable HTML report of all captured pages (optionally an SQLite DB compatible with Magnet AXIOM). Store/share it offline.

## Inputs → Outputs
- **In:** one or more web page URLs (`domain`s/pages)
- **Out:** a timestamped, offline HTML evidence report (a preserved `document-id`/artifact per page)
- **Empty/negative result looks like:** a page that fails to load (login-walled, geo-blocked, or removed) is captured empty/errored — note it and try an archive/cache instead.

## Gotchas & OpSec
- Windows-only desktop app; needs internet at capture time.
- **Active at capture:** the source site sees your visit — use protected infrastructure for sensitive targets.
- Login-walled content won't capture unless you're authenticated in the session; dynamic pages may render imperfectly.
- Human-in-the-loop: none beyond running the app.

## Overlaps ("do both")
- Do both with `[[send-to-internet-archive-chrome-google-com]]` / the Wayback Machine — WPS gives you a local, court-formatted copy; a public archive gives an independent third-party timestamp. Both together make preservation defensible.

## Trust & verifiability
`trust: trusted` — reputable forensics vendor; captures are designed to be defensible, but always record capture time/method and pair with an independent public archive for corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-page-saver |
| category | evidence-capture |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | no |
