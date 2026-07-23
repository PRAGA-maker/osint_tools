---
id: single-file
name: SingleFile
description: Use when you have a `domain`/URL and want a faithful, self-contained snapshot of the page for evidence — returns a single archived HTML file.
url: https://github.com/gildas-lormeau/SingleFile
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Capturing a web page as one self-contained HTML file for offline evidence preservation.
selectorsIn:
- domain
selectorsOut:
- domain
- metadata-exif
status: live
pricing: free
costNote: Free and open source (AGPL-3.0). No account, no server — runs entirely in your browser or via the CLI.
opsec: active
opsecNote: SingleFile fetches the live page from your own browser/host, so the target site's logs see your IP and user-agent like any normal visit. It does not phone home. Use a sock-puppet browser profile or VPN when capturing a subject-controlled site.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Mature, widely used open-source project by Gildas Lormeau; source is public and auditable. The archived file is a WYSIWYG copy of what your browser rendered, not a cryptographically notarised capture.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- SingleFile extension
- gildas-lormeau/SingleFile
- SingleFileZ
tags:
- Domain/IP/Links
- archiving
- evidence-capture
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# SingleFile

> A browser extension (and CLI) that saves a complete web page — HTML, CSS, images, fonts — into one self-contained `.html` file for offline evidence and archiving.

## When to use
You are looking at a page that matters to a case — a social profile, a forum post, a listing, a news article — and you need a durable, self-contained copy before it changes or disappears. Unlike a screenshot, SingleFile preserves the live text, links, and structure in a single file you can reopen, search, and re-verify later.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the SingleFile extension for your browser (Chrome, Firefox — desktop and mobile — Edge, Safari, Brave, Vivaldi, Opera and others) from its store, or grab the CLI from the GitHub repo for scripted/headless capture.
2. Navigate to the target URL and fully render it (scroll to trigger lazy-loaded images, expand comments) — SingleFile saves what is currently in the DOM.
3. Click the SingleFile toolbar icon (or run `single-file <url> <output.html>` from the CLI). It inlines every resource and writes one `.html` file.
4. Store the file with contemporaneous notes: capture date/time, the URL, and your capture IP/identity, so the snapshot is defensible later.
5. Pivot: reopen the archived file offline to extract selectors (usernames, images, `metadata-exif` in embedded media) without re-touching the live site.

## Inputs → Outputs
- **In:** a live URL / `domain` open in your browser
- **Out:** one self-contained `.html` archive of the rendered page (plus any `metadata-exif` inside embedded images preserved as-is)
- **Empty/negative result looks like:** a blank or partial capture — usually because the page was behind a login, blocked scripting, or hadn't finished loading; re-render and retry.

## Gotchas & OpSec
- It captures the *rendered* DOM from **your** session — so it fetches the page live and the site sees your visit. This is not a passive archive; use a clean profile/VPN for sensitive targets.
- Content behind auth is only captured if you're logged in — which ties the capture to that account.
- The file reflects your browser at capture time; it is not a tamper-proof/notarised record. For a neutral third-party timestamp, also archive via a public service.

## Overlaps ("do both")
- Complements a public archiver (e.g. Wayback/archive.today) — SingleFile gives you a rich local copy you control, while a public archive gives an independent, timestamped one. Do both for anything contentious.

## Trust & verifiability
`trust: trusted` — open-source, auditable, and long-maintained. The captured file is a high-fidelity copy of what you saw; its evidentiary weight depends on your capture hygiene (notes, timestamps, clean identity), not on the tool itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | single-file |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
