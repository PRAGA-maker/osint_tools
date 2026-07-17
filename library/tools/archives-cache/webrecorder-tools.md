---
id: webrecorder-tools
name: Webrecorder Tools
description: Use when you need to capture a live web page (dynamic, logged-in, or soon-to-vanish) as a high-fidelity archive — returns a self-contained WARC/WACZ you can replay and cite as evidence.
url: https://webrecorder.net/tools
category: archives-cache
path:
- archives-cache
bestFor: Making your own court-grade, interactive web archives (including JS-heavy and authenticated pages) that public archives miss, then replaying them offline.
selectorsIn:
- domain
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: The core tools (ArchiveWeb.page, ReplayWeb.page) are free and open-source. Browsertrix (hosted crawling service) has paid tiers, but the browser-extension/desktop capture and the replay tools are free.
opsec: active
opsecNote: Capturing a page means YOU load the target site in your browser, so the site sees your visit (IP/User-Agent/any logged-in session). Capture from a sock-puppet browser/VPN if the target could notice. Archiving a logged-in page records whatever your session shows — mind what credentials/PII you bake into the WARC.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Webrecorder is the reference open-source project behind the WARC/WACZ web-archiving ecosystem, widely used by libraries and journalists; the formats are open and independently replayable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- conifer
- archive-today
aliases:
- Webrecorder
- ArchiveWeb.page
- ReplayWeb.page
tags:
- archives
- warc
- web-archiving
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Webrecorder Tools

> The open-source web-archiving suite — capture even dynamic/logged-in pages as a self-contained WARC/WACZ with ArchiveWeb.page, then replay them anywhere with ReplayWeb.page.

## When to use
You need to **preserve evidence** before it disappears or is edited: a social profile, a marketplace listing, a page you expect to be deleted. Public archives (Wayback, archive.today) often fail on JavaScript-heavy or login-gated content — Webrecorder captures exactly what your browser sees, interactively, and produces a portable archive you can timestamp, hash, and replay offline. Essential for defensible preservation in an investigation.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install **ArchiveWeb.page** (Chrome extension or desktop app) from https://webrecorder.net/tools.
2. Start a recording session and browse the target page(s) as you normally would — scroll, expand, log in if needed; it captures everything loaded.
3. Stop and export the archive as a **WACZ/WARC** file. Note the capture time and hash the file for chain-of-custody.
4. Replay any time with **ReplayWeb.page** (drag the WACZ in) — fully offline, no live site needed.
5. Pivot: the archived page's content → the selectors within it (usernames, images, addresses); the WARC's embedded `metadata-exif`/headers → provenance detail.

## Inputs → Outputs
- **In:** a live URL / `domain` you browse during capture
- **Out:** a self-contained WARC/WACZ archive (replayable), including page assets, timestamps, and HTTP metadata (`metadata-exif`-style provenance)
- **Empty/negative result looks like:** an archive that replays blank/partial — capture missed lazy-loaded content (scroll/interact more during recording) or the site blocked resources. Re-capture, interacting fully.

## Gotchas & OpSec
- **Active capture:** you load the target live, so the site logs your visit — use a sock-puppet browser/VPN for sensitive targets.
- Archiving a logged-in view bakes your session/PII into the file; scrub or isolate before sharing.
- Fidelity depends on interacting during capture — anything you don't load isn't archived.

## Overlaps ("do both")
- Pairs with `[[archive-today]]` — archive.today makes a quick public, citable snapshot; Webrecorder makes a private, high-fidelity, interactive one you control. Do both: public snapshot for a shareable link, WACZ for the evidentiary record.

## Trust & verifiability
`trust: trusted` — the reference open-source archiving project; WARC/WACZ are open standards replayable by independent tools, so your archive is verifiable and not locked to a vendor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webrecorder-tools |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
