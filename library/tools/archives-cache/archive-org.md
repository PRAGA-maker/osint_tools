---
id: archive-org
name: archive.org
description: Use when you have a `domain` or URL and want to retrieve historical snapshots of a page as it looked in the past — returns archived captures (document-id) you can read even after the live page changed or vanished.
url: https://www.archive.org/
category: archives-cache
path:
- archives-cache
bestFor: Retrieving deleted, edited, or historical versions of a web page via the Wayback Machine.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, non-profit service; no account needed to browse captures. A free account only adds the ability to trigger new "Save Page Now" captures.
opsec: passive
opsecNote: You query the Internet Archive, not the target's server, so the subject sees nothing. The Archive logs your IP and does not notify the site owner. Safe to run without a sock puppet, though a VPN is prudent for large-scale scraping.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive, a long-standing non-profit; captures are timestamped and reproducible, and the same data is available via a documented public API.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- wayback-archive-it-org
- archive-vn
- internet-archive
- internet-archive-open-source-videos
- internet-archive-videos
- parler-archives
- snitch-list
- the-twitter-stream-grab
- tv-closed-caption-search
- wayback-machine
- wayback-machine-2
- web-archive-org
- web-archive-org-2
aliases:
- Wayback Machine
- web.archive.org
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# archive.org

> The Internet Archive's Wayback Machine — the first place to look when a page has been deleted, edited, or scrubbed, because it keeps timestamped snapshots of the public web.

## When to use
You have a `domain`, profile URL, or specific page and the current version is gone, altered, or sanitized — a taken-down social profile, an edited "about" page, a deleted job listing, a removed obituary. The Wayback Machine lets you read the page as it existed on a given date, which is invaluable for recovering a subject's earlier self-description, old contact details, or content the person later tried to erase.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://web.archive.org/ and paste the full URL (or `domain`) into the search box.
2. Pick a year on the calendar and a highlighted day (a colored dot means a capture exists) to open that snapshot.
3. Read the archived page. Compare captures across dates to see what changed — a name, an email, a phone number, a photo that was later removed.
4. For programmatic use, query the CDX API: `http://web.archive.org/cdx/search/cdx?url=example.com*&output=json` lists every capture of a URL and its subpaths.
5. Pivot: recovered emails/usernames/handles feed email or username tools; a recovered image feeds reverse-image search.

## Inputs → Outputs
- **In:** `domain` or full page URL
- **Out:** timestamped archived snapshots (`document-id`) of the page across its history
- **Empty/negative result looks like:** "Hrm. The Wayback Machine has not archived that URL" — the page was never captured. Try a broader URL (root domain with `*`) via the CDX API, or check [[archive-vn]], which captures on demand and often has pages the Wayback missed.

## Gotchas & OpSec
- Not everything is archived; capture frequency depends on the site's popularity and whether anyone requested a save. Robots.txt exclusions historically blocked some captures.
- Dynamic/JS-heavy pages and content behind logins are often captured incompletely — the shell renders but data panels are blank.
- OpSec: **passive**. The subject is not touched; only the Archive sees your request.

## Overlaps ("do both")
- Pairs with [[archive-vn]] because archive.today captures on demand and snapshots JS-rendered pages the Wayback Machine skips.
- Pairs with [[wayback-archive-it-org]], which surfaces curated institutional crawls (governments, universities, libraries) not always in the main Wayback index.

## Trust & verifiability
`trust: trusted` — run by the non-profit Internet Archive; every capture carries a verifiable timestamp and permanent URL, and the underlying data is reachable through a stable public API.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
