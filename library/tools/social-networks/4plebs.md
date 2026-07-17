---
id: 4plebs
name: 4plebs
description: Use when you have a keyword, tripcode or post ID and want to read purged 4chan threads — returns archived `social-profile` posts, `username`/tripcodes and `image` attachments.
url: https://4plebs.org/
category: social-networks
path:
- social-networks
bestFor: Full-text searching and reading 4chan threads (esp. /pol/, /x/, /adv/) long after they are deleted from 4chan.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to search and read; no account. Runs on the open FoolFuuka archive software.
opsec: passive
opsecNote: You read a static archive, not 4chan itself; posters are anonymous and are not notified. Because 4chan content can be extreme, use an isolated browser; do not post to 4chan from any account tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent 4chan archive; content is user-generated and anonymous, so treat posts as unverified claims.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- archive-4plebs-org
aliases:
- 4plebs.org
- FoolFuuka 4chan archive
tags:
- bellingcat-toolkit
- other-platforms
- 4chan-archive
source: bellingcat-toolkit
lastVerified: '2026-07-17'
enrichment: full
---

# 4plebs

> A searchable, permanent archive of several high-traffic 4chan boards — it lets you read and full-text-search threads that 4chan itself has long since purged.

## When to use
4chan deletes threads within hours to days and offers no search. When a lead points to 4chan (a leaked post, a tripcode, a claim referencing "/pol/" or "/x/"), 4plebs is how you actually read it after the fact. Search by keyword, tripcode, poster ID or post number to recover the original thread, its images, and the surrounding conversation — useful for tracing the origin of a rumor, a doxx, or an image, and for pulling the `image` attachments (which may carry metadata) posted anonymously.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://4plebs.org/ and pick a board (it archives a fixed set incl. /pol/, /x/, /adv/, /f/, /hr/, /s4s/, /tg/).
2. Use full-text search, or filter by tripcode, poster ID, subject or post number.
3. Open the thread: read the posts, note tripcodes/IDs (a `username`-like persistent identity) and download attached `image`s for reverse-image/EXIF analysis.
4. Remember posters are anonymous; a shared poster-ID only groups posts within one thread, while a tripcode can persist across threads.
5. Pivot: run recovered images through reverse-image/metadata tools; search distinctive phrases/tripcodes across other 4chan archives.

## Inputs → Outputs
- **In:** keyword, tripcode, poster ID or post number (`username`-like identifiers)
- **Out:** archived `social-profile` posts (text + context), `image` attachments, tripcodes/IDs
- **Empty/negative result looks like:** no matches — the board isn't archived by 4plebs, the thread predates its coverage, or the search terms don't appear. Check a sibling archive before concluding it's gone.

## Gotchas & OpSec
- OpSec: **passive** — reading only; posters are anonymous and unaware. Use an isolated/hardened browser given the content.
- Only a subset of boards is archived; other boards need different archives.
- Everything is anonymous and unverified; tripcodes/IDs group posts but do not prove real-world identity.

## Overlaps ("do both")
- Pairs with `[[archive-4plebs-org]]` and other FoolFuuka 4chan archives — coverage differs per board, so check more than one.

## Trust & verifiability
`trust: community` — a durable independent archive faithfully mirroring 4chan; the *posts* it stores are anonymous user claims, so corroborate any factual assertion elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 4plebs |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
