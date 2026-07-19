---
id: archive-page-addons-mozilla-org
name: Archive Page (Firefox add-on)
description: Use when you have a `domain`/URL and want to preserve a live page before it changes — saves a permanent archive.today snapshot you can cite later.
url: https://addons.mozilla.org/en-US/firefox/addon/archive-page/
category: archives-cache
path:
- archives-cache
bestFor: One-click preservation of a web page to archive.today so evidence survives deletion or edits.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free open-source Firefox extension; archive.today itself is free.
opsec: active
opsecNote: Archiving is ACTIVE — it makes archive.today fetch the target URL, and the snapshot becomes PUBLIC and permanently indexed at a shareable URL. Do not archive pages you need to keep confidential, and be aware the target's server sees archive.today's fetch (not your IP). Archive from a sock-puppet browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: A well-reviewed open-source add-on (10k+ users, ~4.7★) that simply drives archive.today; the archiving service is a widely-used, reputable preservation tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Archive Page Firefox extension
- archive.today saver
tags:
- archiving
- evidence-preservation
- browser-extension
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Archive Page (Firefox add-on)

> A one-click Firefox button that snapshots the current page to archive.today — the "preserve it before it vanishes" reflex, turned into a toolbar button.

## When to use
You've found a live page that matters to a case — a social post, a profile, a listing, a news item — and you need a permanent, citable copy before the owner edits or deletes it. This add-on sends the current URL (or a right-clicked link) to archive.today and returns a stable snapshot URL you can bookmark and reference.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Archive Page" from addons.mozilla.org into your (sock-puppet) Firefox profile.
2. Navigate to the page you want to preserve.
3. Click the toolbar button (or use the context menu on a specific link) to archive it via archive.today.
4. Save the returned snapshot URL as evidence; pivot by comparing later re-archives to detect changes.

## Inputs → Outputs
- **In:** `domain`/URL (the page to preserve)
- **Out:** a permanent archive.today snapshot URL of that page
- **Empty/negative result looks like:** archive.today fails/blocks (some sites, paywalls, or JS-heavy pages don't snapshot cleanly) — try the Wayback Machine or a manual screenshot/PDF as a fallback.

## Gotchas & OpSec
- Snapshots are PUBLIC and permanent — never archive something you need kept private; you can't easily un-publish it.
- ACTIVE: archive.today (not you) fetches the target, and creating a snapshot is a visible event; archive from a research profile.
- Some sites block archive.today or render poorly — keep a screenshot/PDF backup.

## Overlaps ("do both")
- Pairs with the Wayback Machine and screenshot/PDF tools — archive to BOTH archive.today and web.archive.org, since sites block them differently and redundancy protects the evidence.

## Trust & verifiability
`trust: trusted` — a reputable open-source add-on driving a well-established archiving service; the snapshot is a faithful, independently-hosted copy suitable as evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-page-addons-mozilla-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
