---
id: wayback-machine
name: Wayback Machine
description: Use when you have a `domain`/URL or `social-profile` and want to see what a page said in the past — returns archived `social-profile` snapshots and deleted/changed content over time.
url: https://web.archive.org/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted, edited, or vanished web pages and profiles by viewing their historical snapshots.
selectorsIn:
- domain
- social-profile
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free, no account (donation-funded Internet Archive). Saving a page also free. No paywall.
opsec: passive
opsecNote: Reading archived snapshots does not touch the target's live site — the request goes to the Internet Archive, so the target is not alerted. Fully passive. Note that if you "Save Page Now" a live URL, that fetch DOES hit the live site and creates a public, permanent archive record — do that deliberately, not by reflex.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive, a long-established nonprofit. Snapshots are authentic captures with timestamps; the standard, court-cited source for web history.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- archive-org
- internet-archive
- web-archive-org
- web-archive-org-2
- wayback-machine-2
- internet-archive-open-source-videos
- internet-archive-videos
- parler-archives
- snitch-list
- the-twitter-stream-grab
- tv-closed-caption-search
aliases:
- web.archive.org
- Internet Archive Wayback Machine
- archive.org web
tags:
- web-history-and-website-capture
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Wayback Machine

> The Internet Archive's web-history tool — view timestamped snapshots of any URL to recover pages, profiles, and content that have since been deleted or edited.

## When to use
Something you need is gone from the live web: a deleted social profile, a scrubbed bio, an old company page, a removed classified ad, a taken-down blog. Or you need to prove a page *used to* say something. Feed the Wayback Machine a `domain`/URL (or a profile URL) and read historical captures — often the single highest-yield move in OSINT when a subject has cleaned up their footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://web.archive.org/ and paste the exact URL (page, profile, or site). Use the specific profile/page URL, not just the homepage, for the richest history.
2. Pick a capture from the calendar/timeline; compare captures across dates to see what changed, when, and what was removed.
3. For bulk/automated work, query the CDX API (`http://web.archive.org/cdx/search/cdx?url=example.com/*`) to list every archived URL under a domain — great for enumerating deleted subpages and profiles.
4. If a live page is disappearing, use "Save Page Now" to capture it *before* it's gone (this touches the live site — see OpSec).
5. Pivot: an archived profile yields an old `username`/`name`/bio to feed people- and username-search; a CDX URL list reveals hidden/removed pages.

## Inputs → Outputs
- **In:** `domain`/URL or `social-profile` URL
- **Out:** archived `social-profile`/page snapshots, historical `name`/bio/content, change history
- **Empty/negative result looks like:** "Hrm. Wayback Machine has not archived that URL" — the page was never captured. Try URL variants (with/without `www`, trailing slash, old paths), the CDX API wildcard, and other archives (archive.today) before concluding nothing exists.

## Gotchas & OpSec
- Not everything is archived, and captures can be partial (missing images/JS) — absence of a snapshot is not proof a page never existed.
- "Save Page Now" fetches the LIVE URL and publishes a permanent public record — use deliberately; it can tip off a target and is itself discoverable.
- Robots/removal requests and JS-heavy pages can leave gaps; cross-check with archive.today which captures differently.

## Overlaps ("do both")
- Pairs with `[[web-archive-org]]` / archive.today — different archives capture different snapshots, so a page missing in one may exist in the other; always check both when history matters.

## Trust & verifiability
`trust: trusted` — a long-established nonprofit archive whose timestamped captures are widely relied upon (including in legal contexts); the snapshots are authentic, with the only caveat being coverage gaps, not fabrication.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-machine |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, social-profile → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
