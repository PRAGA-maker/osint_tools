---
id: tv-closed-caption-search
name: TV News Archive (Closed-Caption Search)
description: Use when you have a `name`, phrase or event and want to find when it was said on US TV news — returns matching broadcast clips with transcripts, dates and channels.
url: https://archive.org/details/tv
category: archives-cache
path:
- archives-cache
- other-media
bestFor: Keyword-searching closed captions of US TV news to find when/where something was broadcast.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free at the Internet Archive; no account needed to search captions and view short clips. A free account helps with borrowing/embedding.
opsec: passive
opsecNote: You search an archive of already-broadcast public TV — nothing about a subject is queried live and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive; clips are the actual recorded broadcasts with their closed captions, so results are primary-source and verifiable by watching the clip.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- archive-org
- internet-archive
- internet-archive-open-source-videos
- internet-archive-videos
- parler-archives
- snitch-list
- the-twitter-stream-grab
- wayback-machine
- wayback-machine-2
- web-archive-org
- web-archive-org-2
aliases:
- Internet Archive TV News
- TV News Archive
tags:
- archive
- tv-news
- captions
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# TV News Archive (Closed-Caption Search)

> The Internet Archive's searchable index of US TV news captions — grep decades of broadcasts for a name or phrase and jump to the exact clip.

## When to use
You want to know whether — and when — a `name`, place, phrase, or event appeared on US television news. Because it searches the closed-caption text of recorded broadcasts, you can pinpoint the moment something was said, capture the on-air context, and get a timestamped, verifiable clip. Useful for building a timeline around a person or incident, corroborating a claim, or finding contemporaneous coverage of a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://archive.org/details/tv.
2. Enter a keyword, `name`, or exact phrase (quote it for precision).
3. Filter by channel/program and date range to narrow the hits.
4. Read the results: matching clips with the caption snippet, broadcast date, channel/program, and a short playable segment.
5. Watch the clip to confirm context; note the date/channel as a citable `document-id`. Pivot: on-air statements → source reporting; a date/channel → wider coverage of the same event.

## Inputs → Outputs
- **In:** `name`, phrase, or keyword (optionally channel/date filters)
- **Out:** matching TV-news clips with caption transcript, date, and channel (`document-id`)
- **Empty/negative result looks like:** no clips — the term wasn't in the captioned coverage the Archive holds, the coverage predates its collection, or captions were inaccurate for that segment. Absence isn't proof it was never televised; try synonyms and check the coverage window.

## Gotchas & OpSec
- Caption text drives search, and captions contain errors/omissions (misspelled names, dropped words) — vary spellings and don't rely on a single query.
- Coverage is largely US national/major networks over the Archive's collection period; local and older broadcasts are patchy.
- Passive — you're searching public archived broadcasts; nothing reaches the subject.

## Overlaps ("do both")
- Do both with the broader Internet Archive (`[[internet-archive]]`, `[[archive-org]]`) and news databases: this tool nails the *spoken TV* record, while text news archives cover print/online reporting the captions won't have.

## Trust & verifiability
`trust: trusted` — an Internet Archive service; each result is the real recorded broadcast with its captions, so you verify a hit simply by watching the clip and reading the on-screen date/channel.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tv-closed-caption-search |
| category | archives-cache |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
