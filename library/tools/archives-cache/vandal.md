---
id: vandal
name: Vandal
description: Use when you have a `domain`/URL and want to browse its Wayback Machine history efficiently — a browser extension that overlays archive.org captures (calendar/graph views) on the page you're viewing.
url: https://chromewebstore.google.com/detail/vandal/knoccgahmcfhngbjhdbcodajdioedgdo
category: archives-cache
path:
- archives-cache
bestFor: Fast, in-tab navigation of a page's Wayback Machine captures without leaving the current site.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (AGPLv3); no account required.
opsec: passive
opsecNote: It queries the Internet Archive's Wayback API for the URL you're on, not the live target site — so it does not touch the subject's infrastructure. As with any extension, install it in a research-only browser profile; the archive lookups are attributable to your IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Open-source extension by Vignesh Anand, not affiliated with the Internet Archive; it is a UI wrapper over the public Wayback Machine API.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Vandal Wayback extension
- Vandal archive navigator
tags:
- Archives
- wayback-machine
- browser-extension
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Vandal

> A browser extension that turns the Wayback Machine into an in-tab time-travel UI — jump between a page's historical captures via calendar and graph views without leaving the site.

## When to use
You are looking at a `domain`/URL (a subject's old site, a deleted profile page, a company page that recently changed) and you want to see how it looked over time and pull deleted content — but the archive.org interface is clunky to page through. Vandal overlays the Wayback captures for the current URL so you can scrub through history quickly, which speeds up archive work on any investigation involving changed or removed web pages.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Vandal" from the Chrome Web Store into a research-only browser profile.
2. Navigate to the page whose history you want (or paste the URL). Open the Vandal panel.
3. Use the calendar view to pick a date, or the graph/timeline view to see capture density, then step forward/backward through snapshots in the same tab.
4. Pivot: capture the archived content (screenshots, text, old links/handles/emails) into your case notes; a deleted page often preserves selectors — an old `email`, `username`, or address — that the live site no longer shows.

## Inputs → Outputs
- **In:** `domain`/URL to inspect
- **Out:** historical `domain` snapshots (archived versions of the page and their content)
- **Empty/negative result looks like:** no captures for the URL — the Internet Archive never crawled that page, so there is nothing to show. Absence is a coverage gap, not proof the page never existed.

## Gotchas & OpSec
- It only surfaces what the Wayback Machine actually archived; pages behind logins, robots.txt exclusions, or simply never-crawled won't appear.
- It is a convenience layer over archive.org — if the Wayback Machine is down or rate-limiting, Vandal shows nothing.
- OpSec: passive. Lookups hit the Internet Archive, not the target; nothing reaches the subject.

## Overlaps ("do both")
- Complements direct use of the Wayback Machine and other archive tools (e.g. cachedview, archive.today) — Vandal makes archive.org faster to browse, while archive.today catches pages the Wayback Machine missed. Check both when a page is gone.

## Trust & verifiability
`trust: community` — an open-source third-party extension, but its data is the Internet Archive's genuine captures, which are high-integrity primary evidence. Trust flows from archive.org; Vandal is just the viewer.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vandal |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
