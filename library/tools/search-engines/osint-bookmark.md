---
id: osint-bookmark
name: osint-bookmark
description: Use when you want a ready-made browser bookmark set of OSINT tools organised by task — returns an importable catalog spanning people, `domain`, DNS, and social research.
url: https://github.com/neospl0it/osint-bookmark
category: search-engines
path:
- search-engines
bestFor: Importing a categorised OSINT tool collection straight into your browser's bookmarks bar.
selectorsIn:
- domain
- name
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source on GitHub; download the HTML bookmark file, no account.
opsec: passive
opsecNote: The repo itself is just a bookmark file — reading/importing it touches nothing. OpSec depends on the individual tools you then open from it; vet each before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated bookmark set by GitHub user neospl0it (~220 stars); it's a link collection, so link rot and unvetted third-party tools are the main caveats.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- neospl0it osint-bookmark
- OSINT bookmarks
tags:
- bookmarks
- catalog
- tool-directory
source: gh-topic-osint-resources
lastVerified: '2026-07-28'
enrichment: full
---

# osint-bookmark

> A curated, importable browser-bookmark file of OSINT tools, sorted by task — company research, scanning, DNS/WHOIS, people, social media, image/video, geo, email/phone.

## When to use
You want a broad, organised starting point rather than a single lookup: import `osint.html` into Chrome/Firefox/Edge/Safari and you get a bookmarks folder tree of investigation tools grouped by category. Reach for it when scoping a new case and you want the relevant tool families one click away. It's a directory, not a data source — its own MP relevance is low, but the people/social/email sections point at tools that do the work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/neospl0it/osint-bookmark.
2. Download `osint.html` (Raw → Save As).
3. In your browser's bookmark manager, choose **Import bookmarks from HTML** and select the file.
4. Browse the imported folder tree (Company Research, Scanning, DNS & Whois, People Search, Social Media, Image/Video, Geo, Email & Phone).
5. Pivot: open the category matching your current selector — e.g. a `domain` lead → DNS/Whois tools; a `name` lead → People Search tools.

## Inputs → Outputs
- **In:** `domain` or `name` (the kind of lead you're routing to a tool)
- **Out:** an importable `domain`-organised catalog of tool links — the value is navigation, not a query result
- **Empty/negative result looks like:** dead links — as a static bookmark set, some entries will have rotted since last update; check the repo's commit date for freshness.

## Gotchas & OpSec
- Importing is passive; OpSec risk comes entirely from whichever linked tools you then use — vet each individually.
- Static collection: expect some link rot and a corporate/infra tilt (it leans toward company and DNS research).
- Not a substitute for this library's per-tool guidance; use it to discover, not to judge a tool's trust/opsec.

## Overlaps ("do both")
- A convenience index that overlaps every category here; treat it as a discovery layer and rely on the individual tool skills for how/OpSec.

## Trust & verifiability
`trust: community` — a single maintainer's curated list; the file is inspectable and popular (~220 stars), but the tools it links are third-party and unvetted, so verify each before acting on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-bookmark |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
