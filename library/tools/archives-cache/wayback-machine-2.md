---
id: wayback-machine-2
name: Wayback Machine
description: Use when you have a `domain`, `social-profile` or `username` URL and want to see historical snapshots — including deleted or changed pages — returns archived page content, prior profile states, and timestamps.
url: https://archive.org/web/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted social posts, profiles, or pages tied to a subject.
selectorsIn:
- domain
- social-profile
- username
selectorsOut:
- social-profile
- name
- metadata-exif
status: live
pricing: free
costNote: Free public service of the Internet Archive; no account needed to browse. A free account is only needed to submit "Save Page Now" captures.
opsec: passive
opsecNote: Passive and covert toward the subject — you view an archived copy held by the Internet Archive, so the subject's live site is never touched and gets no visitor/log entry. Note that submitting a "Save Page Now" capture DOES fetch the live URL from Archive's servers (not yours), which can leave a hit in the target's logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive, a long-standing nonprofit; snapshots are authentic captures with reliable timestamps, widely accepted as evidence of what a page said at a point in time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Internet Archive
- web.archive.org
tags:
- archive
- cache
- deleted-content
source: tracelabs-repos
lastVerified: '2026-07-10'
enrichment: full
---

# Wayback Machine

> The Internet Archive's Wayback Machine — a time machine for the web that lets you read deleted or altered pages, profiles and posts exactly as they appeared on a given date.

## When to use
You have a `domain`, a `social-profile`, or a `username`-based URL and the current version is gone, changed, or scrubbed. This is the go-to for recovering a deleted tweet/post, a since-edited bio, an old "about" page with a phone/address, or a defunct personal site — content a subject has removed but that was captured before deletion. Also invaluable for establishing *when* something changed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://archive.org/web/ and paste the exact URL (profile, page, or domain).
2. Use the calendar/timeline to pick snapshots; blue dots mark captures. Compare multiple dates to see what changed.
3. Read the archived page as it appeared then — pull `name`s, contact detail, linked accounts, images, and any `metadata-exif` on archived files.
4. For a whole site, browse the URL prefix (`/web/*/example.com/*`) to list every archived path.
5. Pivot: dead outbound links in an old page, a former username, or an old address each become new leads. Use the API (`http://archive.org/wayback/available?url=`) to script snapshot lookups.

## Inputs → Outputs
- **In:** `domain` / `social-profile` / `username` URL
- **Out:** archived page content, prior `social-profile`/bio states, `name`s, linked handles, `metadata-exif` on archived assets, capture timestamps
- **Empty/negative result looks like:** "Hrm. Wayback Machine has not archived that URL" — the page was never captured. Absence of a snapshot is not evidence the page never existed; try URL variants, the domain root, or Google-cache/archive.today as alternates.

## Gotchas & OpSec
- Not everything is archived, and JS-heavy pages (many modern social feeds) often capture poorly or blank — verify the snapshot actually rendered the content.
- Robots.txt and takedown requests can retroactively hide captures; a gap may mean "removed," not "never captured."
- Browsing is fully passive; **submitting** a Save Page Now capture makes Archive fetch the live target and can leave a footprint in the subject's logs — avoid on-demand captures when you need to stay covert.
- Timestamps are UTC; note them precisely when using a snapshot as evidence.

## Overlaps ("do both")
- Pairs with `[[sowdust-fb-search]]` and platform-specific tools — those find live content; Wayback recovers what was deleted.
- Complementary to metasearch (`[[webcrawler-com]]`): search finds the URL, Wayback recovers its history. Cross-check with archive.today for pages Wayback missed.

## Trust & verifiability
`trust: trusted` — the Internet Archive is an established nonprofit and its captures carry authentic, citable timestamps. The main caveat is coverage completeness, not authenticity: a snapshot faithfully shows what was fetched, but not every page or every change was ever captured.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-machine-2 |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, social-profile, username → social-profile, name, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
