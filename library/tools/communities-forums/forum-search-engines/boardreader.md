---
id: boardreader
name: BoardReader
description: Use when you have a `name`, `username`, or phrase and want it found across web forums and message boards — returns matching posts/threads with source links and commenter handles.
url: https://boardreader.com/
category: communities-forums
path:
- communities-forums
- forum-search-engines
bestFor: Full-text searching forums and message boards across the web for a name, handle, or phrase that general search engines bury.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
- name
status: live
pricing: free
costNote: Free web forum search; an API/commercial data feed is offered separately for bulk use.
opsec: passive
opsecNote: You search BoardReader's index, not the forums directly, so no forum user is contacted or notified. Opening a result visits the source forum — do that logged-out to avoid tying the view to an account. Use a clean session for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running dedicated forum search engine. It indexes real public forum posts (verifiable at the source), though coverage is a subset of all forums and some indexes may lag.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- google-groups
- reddit
aliases:
- boardreader.com
tags:
- forums
- message-boards
- search
- discussions
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# BoardReader

> A dedicated search engine for web forums and message boards — the way to surface a name, handle, or phrase buried in discussion threads that Google under-indexes.

## When to use
You want to find where a subject appears in forum discussions — under their `name`, an online `username`, an email, or a distinctive phrase they've used. Forums are a rich, under-searched OSINT source (niche communities, hobby boards, complaint sites, regional forums), and general search engines often bury or omit them. BoardReader searches this discussion layer specifically, returning threads and posts (with the source link and the poster's handle) that place your subject in a community and timeframe.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://boardreader.com/.
2. Enter the search term — a `name`, `username`, quoted phrase, or forum-specific keyword; you can narrow by forum/date where supported.
3. Read the results: matching posts/threads, the forum they're on, the poster's handle, and dates.
4. Click through to the source forum to read the full thread in context and confirm.
5. Pivot: a poster `username`/`social-profile` feeds cross-platform username search; the forum itself and the subject's post history reveal interests, location clues, and associates.

## Inputs → Outputs
- **In:** `name`, `username`, or phrase
- **Out:** forum posts/threads, poster `username`/`social-profile`, `name` mentions, source links
- **Empty/negative result looks like:** few/no hits — the term isn't in BoardReader's indexed forums (coverage is partial), or it only appears on boards it doesn't crawl. Absence isn't proof the person never posted anywhere.

## Gotchas & OpSec
- Coverage is a subset of all forums and can lag; a miss here doesn't rule out forum activity — also try `site:` searches and `[[google-groups]]`.
- Forum handles rarely map 1:1 to real names — treat a matched post as a lead to corroborate.
- OpSec: passive to search; open source threads logged-out so the forum doesn't associate the visit with an account.

## Overlaps ("do both")
- Pairs with `[[google-groups]]` (Usenet/mailing-list discussions) and `[[reddit]]` — each covers a different slice of online discussion, so run the same handle/phrase across all three to widen coverage.

## Trust & verifiability
`trust: community` — a dedicated forum-search index of genuine public posts; every hit is verifiable by opening the source thread. The caveat is coverage completeness, not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | boardreader |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, username, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
