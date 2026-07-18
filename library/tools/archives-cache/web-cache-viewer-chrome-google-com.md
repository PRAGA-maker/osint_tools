---
id: web-cache-viewer-chrome-google-com
name: Web Cache Viewer (Chrome extension)
description: Use when you have a `domain`/URL and want an archived copy of a page — right-click to open its Wayback Machine or Google Cache version, returning historical page content.
url: https://chromewebstore.google.com/detail/web-cache-viewer/pbkloffickinnlnmefmjmjbacohecpbd
category: archives-cache
path:
- archives-cache
bestFor: One right-click jump from any live URL to its Wayback/Google-cached snapshot.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free Chrome extension; no account, just a browser install.
opsec: passive
opsecNote: Requesting an archived copy hits the Wayback Machine / cache host, not the target's server, so the site owner is not alerted. Use in a sock-puppet browser profile to keep it separate from your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Third-party Chrome extension (~60k users, updated 2025); it merely links out to the Wayback Machine and Google Cache, which are the authoritative archive sources.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- wayback-archive
- wayback-machine
aliases:
- Web Cache Viewer
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Web Cache Viewer (Chrome extension)

> A right-click shortcut from any page to its archived version on the Wayback Machine or Google Cache — no copy-pasting URLs into archive sites.

## When to use
You are on a live page (or have a URL) that has changed, been edited, or is 404/paywalled, and you want to see what it said earlier — a deleted profile, an edited listing, a removed post. This extension adds a context-menu entry that jumps straight to the archived snapshot, saving the step of manually pasting the URL into web.archive.org.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Web Cache Viewer" from the Chrome Web Store in a sock-puppet browser profile.
2. Navigate to the page (or right-click a link) whose `domain`/URL you want archived.
3. Right-click → choose the Web Cache Viewer entry → pick **Wayback Machine** or **Google Cache**; it opens the archived copy (a snapshot / `document-id`).
4. Pivot: an archived snapshot may show contact details, older bios, or images since deleted — feed those back into the appropriate selector-specific tool.

## Inputs → Outputs
- **In:** `domain` / page URL (the page you are on or a link)
- **Out:** an archived snapshot of the page (`document-id`) from Wayback or Google Cache
- **Empty/negative result looks like:** the archive says "page not in the Wayback Machine" / no snapshots — the URL was never crawled; try the domain root or a different archive.

## Gotchas & OpSec
- Human-in-the-loop: none beyond the one-time install; requires a Chromium-based browser.
- OpSec: passive — the request goes to the archive host, not the target server.
- Google Cache has been largely deprecated by Google; the Wayback path is the reliable one, so prefer it when the extension offers a choice.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` / `[[wayback-archive]]` — this extension is just a fast launcher into those archives; use the full Wayback site directly when you need the calendar of all snapshots over time, not just the latest.

## Trust & verifiability
`trust: community` — it is a third-party convenience wrapper; the trustworthy data comes from the Internet Archive it links to, so verify anything critical on the Wayback site itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-cache-viewer-chrome-google-com |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
