---
id: archived-moe
name: archived.moe
description: Use when you have a username/tripcode, keyword, or post ID and want to search deleted/archived 4chan threads across many boards — returns social-profile-adjacent posts, images, and their metadata.
url: https://archived.moe/
category: public-records
path:
- public-records
bestFor: Full-text searching archived (including deleted) 4chan threads and posts across boards.
selectorsIn:
- username
- name
- image
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free public archive; no account needed to search or read.
opsec: passive
opsecNote: You are reading a third-party archive, not 4chan itself, so the original posters aren't notified. Content can be extreme/illegal — view in a sandboxed sock-puppet browser, and never download unknown files to your host.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run FoolFuuka archive of 4chan; coverage varies by board and it preserves posts 4chan itself deletes, but it is not an official or authenticated record.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- archived.moe 4chan archive
tags:
- 4chan-archive
- imageboard
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# archived.moe

> A searchable community archive of 4chan — including threads and posts that 4chan itself has since deleted.

## When to use
You're tracing activity on 4chan and have a `username`/tripcode, a distinctive phrase, an email, or an `image` to look for. Because 4chan purges threads quickly, the live site is useless for anything more than hours old; archived.moe preserves the history and lets you full-text search it across many boards. Useful for attributing posts, recovering deleted content, and pulling posted images (and their `metadata-exif`).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://archived.moe/ in a sandboxed sock-puppet browser.
2. Use the search to query by text, tripcode/name field, post ID, or filter by board/date.
3. Read matching threads/posts; open posted images to inspect them (and check EXIF where present).
4. Note tripcodes and recurring phrasing — these are the closest thing to a persistent identity on an anonymous board.
5. Pivot: a tripcode/username → cross-platform username search; a posted image → reverse image search; embedded contact strings → email/username tooling.

## Inputs → Outputs
- **In:** `username`/tripcode, keyword, post ID, or `image`
- **Out:** archived posts (`social-profile`-adjacent attribution), images and their `metadata-exif`
- **Empty/negative result looks like:** no matches — the board may not be archived here, the thread predates coverage, or the poster left nothing distinctive to search on.

## Gotchas & OpSec
- **Content warning:** 4chan archives contain graphic and illegal material; sandbox your browser and never download unknown files to your host.
- Coverage is board- and era-specific; a miss here doesn't mean the post never existed — try sibling archives.
- Attribution on an anonymous board is weak: only tripcodes/names/emails and stylometric patterns persist, and any of them can be spoofed.

## Overlaps ("do both")
- Cross-check other 4chan archives (e.g. desuarchive, 4plebs) since each covers different boards; pair with reverse-image search for posted media.

## Trust & verifiability
`trust: community` — a community mirror, valuable precisely because it keeps deleted content, but unauthenticated; treat attributions as leads and corroborate with independent evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archived-moe |
| category | public-records |
| selectorsIn → selectorsOut | username, name, image → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
