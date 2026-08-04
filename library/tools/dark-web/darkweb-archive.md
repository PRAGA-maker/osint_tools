---
id: darkweb-archive
name: Darkweb archive
description: Use when you have a `.onion` `domain` and want a preserved snapshot of the site's files — returns a downloadable ZIP of its HTML, CSS, JavaScript and assets.
url: https://darkweb-archive.activetk.jp/
category: dark-web
path:
- dark-web
bestFor: Snapshotting a Tor (.onion) site's files so you can preserve and analyse them offline.
selectorsIn:
- domain
selectorsOut:
- domain
- metadata-exif
status: live
pricing: free
costNote: Free web service; no account or payment required.
opsec: active
opsecNote: The service fetches the target .onion site on your behalf, so the archive request touches that hidden service. Do not submit URLs that would tip off an investigation subject that their site is being crawled; where stealth matters, archive via your own Tor client instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent free tool by ActiveTK (Japan); open-source (C#) with an onion mirror, but a single-maintainer project with no institutional backing — verify captures rather than trusting them blindly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- activetk
- ghunt-online-version
aliases:
- darkweb archive
- activetk darkweb archive
tags:
- Search engines
- Darknet/deepweb search tools
- tor
- archiving
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Darkweb archive

> A one-click archiver for Tor hidden services: give it a `.onion` URL, get back a ZIP of the whole page's files for offline preservation.

## When to use
You have located a `.onion` site (a marketplace listing, forum thread, paste, or profile page) that is relevant to an investigation and want to preserve it before it disappears — dark-web pages are notoriously ephemeral. This tool downloads the page's HTML, CSS, JavaScript and other assets so you have a fixed evidentiary copy and can inspect the source (metadata, embedded links, contact handles) offline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://darkweb-archive.activetk.jp/ (clearnet; an onion mirror also exists for Tor-only use).
2. Paste the target `.onion` URL into the input field.
3. Submit and wait for the service to fetch the hidden service and package its files.
4. Download the resulting ZIP; unpack it and read the raw HTML/JS for `metadata-exif`, embedded onion/clearnet links, usernames, PGP keys or contact addresses to pivot on.
5. Pivot: extracted handles/emails feed username and email tools; embedded links feed further dark-web crawling.

## Inputs → Outputs
- **In:** a `.onion` `domain`/URL
- **Out:** a downloadable ZIP archive of the site's files; inside it, source `metadata-exif`, links, and contact selectors
- **Empty/negative result looks like:** an error or empty archive if the hidden service is offline, gated behind a login/CAPTCHA, or blocking crawlers — a snapshot is only as good as what the site served at fetch time.

## Gotchas & OpSec
- Only captures what the server returns to an anonymous fetch; login-walled or CAPTCHA-gated content won't be archived.
- Active: the fetch reaches the target hidden service. For sensitive targets, prefer archiving through your own controlled Tor client so timing/behaviour is yours to manage.
- Single-maintainer tool — keep your own hash of the ZIP if the capture needs to stand as evidence.

## Overlaps ("do both")
- Pairs with `[[activetk]]` — same author's toolset; use the archive to freeze a page and the broader ActiveTK utilities to inspect it, since one preserves and the other analyses.

## Trust & verifiability
`trust: community` — an open-source hobbyist tool with no institutional backing; useful and free, but treat captures as your own evidence to verify (hash them) rather than as an authoritative archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | darkweb-archive |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
