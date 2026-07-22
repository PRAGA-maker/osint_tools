---
id: archive-page-chrome-google-com
name: Archive Page (Chrome extension)
description: Use when you have a `domain`/URL you are viewing and want to preserve a permanent snapshot before it changes — sends the current page to Archive.today and returns the archived `document-id`/URL.
url: https://chromewebstore.google.com/detail/archive-page/gcaimhkfmliahedmeklebabdgagipbia
category: archives-cache
path:
- archives-cache
bestFor: One-click preservation of the page you're viewing to Archive.today, straight from the Chrome toolbar.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free Chrome extension (developer John Navas); Archive.today itself is free.
opsec: active
opsecNote: Submitting a page pushes its URL to Archive.today, which fetches the page from ITS servers and creates a PUBLIC, permanent snapshot. Do not archive URLs that would tip off a subject or that contain session/auth tokens. Archiving a private/soft-target profile URL can leave a public trace of your interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: ~80k users, 4.2★; a thin community-built convenience wrapper around Archive.today's public submission endpoint.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- archive-today
tags:
- archive
- Archive & Cached Related Sites
- browser-extension
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Archive Page (Chrome extension)

> A toolbar button that snapshots the page you're on to Archive.today — capture evidence before it's edited or deleted.

## When to use
You are viewing a page (a `domain`/URL — a social profile, listing, forum post, news item) that is relevant to a case and could be edited or removed. Click once to freeze a citable, timestamped copy on Archive.today. In a missing-persons context this preserves volatile evidence (a suspect's post, a for-sale listing, a since-deleted profile) so it survives deletion and can be referenced later.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Archive Page" from the Chrome Web Store (the URL above).
2. Navigate to the page you want to preserve.
3. Click the toolbar button (or its keyboard shortcut / right-click context menu). The extension sends the current tab's URL to Archive.today.
4. A new tab opens with the resulting Archive.today snapshot and its permanent `document-id`/URL.
5. Record that archive URL as your citation, and pivot: compare against the Wayback Machine for earlier states.

## Inputs → Outputs
- **In:** `domain`/URL (the page currently open)
- **Out:** `document-id` — a permanent Archive.today snapshot URL of that page
- **Empty/negative result looks like:** Archive.today can reject/soft-fail on pages behind logins, aggressive bot-blocking, or heavy JavaScript; you'll get an error or a blank/partial capture rather than a clean snapshot.

## Gotchas & OpSec
- OpSec: **active** — Archive.today fetches the target from its own servers and publishes a PUBLIC snapshot. Anyone browsing Archive.today can later see that URL was archived. Never archive a URL whose preservation would alert the subject, and strip session tokens from URLs first.
- It archives only the exact URL/tab you're on — it does not crawl a whole site.
- Captures reflect the page at submission time; it is not retroactive. For past states, use the Wayback Machine.

## Overlaps ("do both")
- Pairs with `[[archive-today]]` (this is a front-end to it) and the Wayback Machine — do both, because Archive.today and web.archive.org capture different pages and different moments.

## Trust & verifiability
`trust: community` — a small third-party convenience wrapper, but the resulting snapshot lives on Archive.today, a widely-cited archive; the evidentiary value comes from Archive.today, not the extension.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-page-chrome-google-com |
| category | archives-cache |
