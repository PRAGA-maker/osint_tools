---
id: wayback-machine-chrome-extension
name: Wayback Machine (Chrome Extension)
description: Use when you hit a dead/changed page (a `domain` or URL) and want its archived version fast — returns the Internet Archive's saved snapshots for the page you're viewing, in one click.
url: https://chromewebstore.google.com/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak
category: archives-cache
path:
- archives-cache
- web
bestFor: One-click access to Internet Archive snapshots (and one-click saving) of the page you're currently on.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free official extension from the Internet Archive; no account needed to view or save snapshots.
opsec: passive
opsecNote: Fetching an archived snapshot hits the Internet Archive, not the target's live server, so the site owner isn't alerted. Note that clicking "Save Page Now" DOES fetch the live URL through the Archive and creates a public, permanent snapshot — use it deliberately, not on sensitive/private URLs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published by the Internet Archive, the operator of the Wayback Machine; snapshots are authentic captures with recorded timestamps.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wayback-machine
- archive-today
- google-cache
aliases:
- Wayback Machine extension
- Internet Archive Chrome extension
tags:
- archive
- cache
- wayback
- browser-extension
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Wayback Machine (Chrome Extension)

> The Internet Archive's official browser extension: on any page, jump to its archived snapshots — or save the current page — without leaving the tab.

## When to use
You land on a `domain`/URL that is dead (404, parked, taken down) or has changed since it was cited, and you want the historical version immediately. The extension surfaces the Wayback Machine's snapshots for whatever page you're viewing and offers "oldest / newest / overview," so you can recover deleted profiles, edited pages, and removed evidence in one click — and preserve a live page you fear will vanish.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store and pin it.
2. On a dead or suspicious page, click the extension and choose **Oldest**, **Newest**, or **All versions** to view archived snapshots with their capture timestamps.
3. Use **Save Page Now** to create a permanent public snapshot of a live page you want to preserve as evidence (note: this fetches the live URL).
4. Compare snapshots across dates to see what changed and when (edited bios, removed content).
5. Pivot: an archived page may expose old `domain`s, contact details, or profile text that the live site scrubbed — feed those into further lookups.

## Inputs → Outputs
- **In:** `domain`/URL (the page you're on)
- **Out:** archived snapshots of that `domain`/URL with timestamps (recovered historical content)
- **Empty/negative result looks like:** "This page has not been archived" — the Wayback Machine never captured that URL; try `[[archive-today]]` or Save-Page-Now going forward. Absence of a snapshot isn't proof the page never existed.

## Gotchas & OpSec
- Not every page is archived, and snapshots can be incomplete (missing images/JS) or blocked by later robots.txt changes — check multiple dates.
- **Save Page Now** creates a *public, permanent* record and fetches the live target — don't use it on private/sensitive URLs you don't want preserved or the owner to potentially notice.
- OpSec: **passive** for viewing snapshots (served by the Archive, not the target).

## Overlaps ("do both")
- Pairs with `[[archive-today]]` (captures pages the Wayback Machine misses and freezes exact renders) and the full `[[wayback-machine]]` site — check both archives, since coverage of any given URL differs.

## Trust & verifiability
`trust: trusted` — it's the Internet Archive's own extension; snapshots are authentic, timestamped captures you can also verify directly on web.archive.org.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-machine-chrome-extension |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
