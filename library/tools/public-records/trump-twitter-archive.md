---
id: trump-twitter-archive
name: Trump Twitter Archive
description: Use when you need the complete, searchable record of Donald Trump's tweets (including deleted ones) — returns dated social-profile posts you can filter and export for research.
url: https://www.thetrumparchive.com/
category: public-records
path:
- public-records
bestFor: Searching and exporting the full historical archive of Donald Trump's tweets, including deleted posts.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search, filter, and browse; the raw dataset is downloadable. No account required.
opsec: passive
opsecNote: You browse a static third-party archive; nothing is sent to the subject and no live account is queried — fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known independent archive widely used by journalists and researchers; corroborate individual tweets against other archives for citation-grade certainty.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- The Trump Archive
- thetrumparchive.com
tags:
- twitter-archive
- public-records
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Trump Twitter Archive

> A complete, searchable archive of Donald Trump's tweets — including deleted ones — that you can filter by date/keyword and export.

## When to use
You need the historical Twitter record of one specific public figure (Donald Trump) — for timeline reconstruction, quote verification, or checking whether a since-deleted tweet existed. It's a narrow, single-subject archive: valuable when that person is relevant, useless for anyone else. As a template it illustrates the broader pattern of preserved-deleted-tweet archives.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.thetrumparchive.com/.
2. Search by keyword or filter by date range, device, retweet/flagged status, and deletion status.
3. Open a result for the full tweet text, timestamp, and metadata; deleted tweets are marked.
4. Export/download the dataset for offline analysis (e.g. building a timeline).
5. Pivot: a dated `social-profile` post → cross-reference with news archives or the Wayback Machine for corroboration.

## Inputs → Outputs
- **In:** a keyword/date range for this one subject (`name`: Donald Trump).
- **Out:** matching tweets as dated `social-profile` posts (text, timestamp, deleted flag), exportable in bulk.
- **Empty/negative result looks like:** no tweets matching your filter — the archive is comprehensive for its window, so a blank result usually means the term/date genuinely has no matching post.

## Gotchas & OpSec
- Single-subject only — it archives one account, not Twitter/X generally.
- It's a third-party archive; for citation-grade proof of a specific (especially deleted) tweet, corroborate with another archive (Wayback, ProPublica's older tools).
- Coverage ends when the archive stopped ingesting; check the latest date before assuming completeness.

## Overlaps ("do both")
- Pairs with the Wayback Machine and news archives: this gives the clean, filterable tweet dataset, those independently corroborate that a given post existed at a given time.

## Trust & verifiability
`trust: community` — an independent but widely-cited archive; treat it as authoritative-in-practice while confirming individual deleted tweets against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trump-twitter-archive |
