---
id: archive-md
name: Archive.today (archive.md)
description: Use when you have a `domain`/URL and want a frozen, tamper-proof snapshot of a page — returns a permanent archived capture with a citable `document-id`.
url: https://archive.md/
category: archives-cache
path:
- archives-cache
bestFor: Capturing an on-demand permanent snapshot of a specific web page (incl. JS-heavy/social pages) and retrieving existing snapshots.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, no account. archive.md is one of several interchangeable domains for Archive.today (also archive.ph, archive.today, archive.is).
opsec: passive
opsecNote: The archive fetches the page from ITS servers, so the target site sees Archive.today, not you — a low-footprint way to preserve evidence. Note that submitting a URL makes the capture public; don't archive a private link you don't want exposed.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, widely-cited independent web archive; captures are immutable snapshots suitable as evidence.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- archive.today
- archive.ph
- archive.is
- archive.md
tags:
- Archives
- web-archive
- evidence-preservation
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Archive.today (archive.md)

> An on-demand web archiver: paste a URL and it stores a permanent, immutable snapshot — including the rendered page — so evidence survives deletion, edits, or the account going private.

## When to use
You've found a page that matters to a case — a social post, a profile, a listing, a news article, a forum thread — and you need to preserve it *now*, before it's edited or removed. Archive.today captures a fixed snapshot (screenshot + saved HTML) at a citable URL. Unlike the Wayback Machine, it handles many JavaScript-heavy and social pages and lets you force a fresh capture on demand. Also search it for existing snapshots of a URL to see a page's past states.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://archive.md/ (or a sibling domain — archive.ph/.is/.today — if one is blocked on your network).
2. To preserve: paste the target URL into "My url is alive..." and submit; solve a CAPTCHA if shown. You get a permanent snapshot URL (`document-id`).
3. To retrieve: paste the URL into the "I want to search the archive" box to list existing captures and dates.
4. Save the resulting archive URL and capture date as your citation.
5. Pivot: archive volatile pages the moment you find them; use the immutable link in reports and cross-reference with the Wayback Machine for a fuller history.

## Inputs → Outputs
- **In:** `domain`/URL of a live page
- **Out:** a permanent snapshot (screenshot + HTML) at a citable `document-id` URL, with capture date
- **Empty/negative result looks like:** "no results" when searching (the page was never archived), or a capture that failed to render fully (some paywalled/anti-bot pages archive incompletely). Re-submit or capture manually.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA often gates new captures.
- OpSec: **passive** — the archive fetches the page, masking you; but every capture is **public**, so don't archive sensitive private URLs.
- Access can be flaky by network/DNS — the multiple domains exist precisely so you can switch if one is blocked.

## Overlaps ("do both")
- Pairs with the Internet Archive Wayback Machine — Wayback has deeper historical breadth; Archive.today captures on demand and handles dynamic/social pages Wayback misses. Do both for important evidence.

## Trust & verifiability
`trust: trusted` — a durable, independent archive producing immutable snapshots; the capture is self-verifying (screenshot + stored source) and citable by its permanent URL and date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-md |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
