---
id: uk-web-archive
name: UK Web Archive
description: Use when you have a UK `domain`, site title, `name`, or keyword and want historical captures of UK web content — returns domain, metadata-exif.
url: https://www.webarchive.org.uk/ukwa/
category: archives-cache
path:
- archives-cache
- web
bestFor: Finding preserved snapshots of UK websites (including deleted/changed pages) archived under legal deposit by the British Library.
selectorsIn:
- domain
- name
selectorsOut:
- domain
- metadata-exif
status: degraded
pricing: free
costNote: Free to search and view archived pages. Some material is only viewable on-site at legal-deposit libraries, but much is openly accessible online.
opsec: passive
opsecNote: Passive read of an archive — the original site owner is not notified you viewed a capture. No login. Since the archive stores a copy, it may preserve content the live site has since removed; that is the point, but note the capture is dated.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the British Library and UK legal-deposit libraries; captures are authentic, timestamped preservation copies.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UK Web Archive
- UKWA
- webarchive.org.uk
- British Library web archive
tags:
- archives
- web-archive
- uk
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# UK Web Archive

> The British Library's legal-deposit archive of the UK web: recover deleted or changed pages from `.uk` sites and organisations by URL, title, or keyword.

## When to use
You have a UK-connected `domain`, organisation, site title, or a person's `name` that appeared on a now-changed or deleted UK web page, and you want a preserved snapshot. Because UKWA archives under UK legal deposit, it captures British sites (clubs, small businesses, blogs, org pages, event listings) that the Internet Archive may have missed, letting you recover an old bio, contact detail, staff list, or removed statement tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.webarchive.org.uk/ukwa/ and use the search: enter a URL to find its captures, or a title/keyword/name to search across archived content.
2. Open a result to view the dated snapshot(s); step through capture dates to see how a page changed over time.
3. Extract what the live site no longer shows — old addresses, phone numbers, names, affiliations, images — and note the capture date as the "as-of" timestamp (`metadata-exif`).
4. Pivot: recovered `domain`s/contact details feed domain- and people-OSINT; compare against the Internet Archive Wayback Machine for gaps in either archive.

## Inputs → Outputs
- **In:** UK `domain`/URL, site title, organisation, or `name`
- **Out:** archived page `domain`/snapshots and capture `metadata-exif` (dates, historical page content)
- **Empty/negative result looks like:** no captures — the site was outside UKWA's scope (non-UK), never crawled, or blocked; or the service is temporarily unavailable. Cross-check the Wayback Machine before concluding nothing was archived.

## Gotchas & OpSec
- Human-in-the-loop: none online; a subset of legal-deposit content is restricted to library reading rooms.
- OpSec: **passive** — no notification.
- Availability has been **degraded** since the 2023 British Library cyberattack; full-text search and some captures may be intermittently offline. Retry, and fall back to the Wayback Machine.
- Coverage is UK-focused — this is a complement to, not a replacement for, the global Internet Archive.

## Overlaps ("do both")
- Do both with the Internet Archive Wayback Machine — UKWA has deeper `.uk` legal-deposit coverage; the Wayback Machine is broader globally. Each catches captures the other lacks.

## Trust & verifiability
`trust: trusted` — an official British Library legal-deposit archive; snapshots are authentic, dated preservation copies you can cite by capture date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-web-archive |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, name → domain, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
