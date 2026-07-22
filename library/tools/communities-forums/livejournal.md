---
id: livejournal
name: LiveJournal
description: Use when you have a `username` and want to find an associated blog/journal, its posts, interests and friend network — returns a `social-profile` and `associate` links.
url: https://www.livejournal.com
category: communities-forums
path:
- communities-forums
bestFor: Resolving a username to a LiveJournal blog and mining its posts, profile fields and friends list for links and history.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to read public journals and profiles; paid accounts remove ads and add features but are not needed for OSINT reading.
opsec: passive
opsecNote: Reading public journals is passive. Logging in to view friends-locked posts, or leaving a comment/profile view, can be visible — use a sock-puppet account and avoid any interaction that notifies the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running blogging platform (now Russian-owned, SUP Media); public content is user-authored, so treat claims as self-reported.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LJ
- livejournal.com
tags:
- forums
- blogging
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# LiveJournal

> A veteran blogging/community platform whose usernames, profile "interests," long-form posts and public friends lists remain a rich OSINT trail — especially for people active online in the 2000s–2010s.

## When to use
You have a `username` (or a handle reused from another platform) and want to check for a LiveJournal presence. LJ profiles expose birthdays, location, interests, a bio, and — crucially — a friends/friend-of network and years of dated posts, which can establish a person's history, associates, and writing voice for cross-platform matching.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the direct profile URL: `https://<username>.livejournal.com/profile` (and the journal at `https://<username>.livejournal.com/`).
2. Read the profile fields: bio, location, birthday, interests (each interest links to others who share it), and the mutual-friends lists.
3. Scan dated public posts for events, places, names and links.
4. Note that some posts/entries are friends-locked or private — only public content is visible without being an approved friend.
5. Pivot: reused `username`, linked accounts, and named friends (`associate`) feed username-search and cross-platform tools.

## Inputs → Outputs
- **In:** a `username`
- **Out:** a LiveJournal `social-profile` (bio, location, interests), dated posts, friends/`associate` network
- **Empty/negative result looks like:** the profile URL 404s or shows a deleted/suspended journal — that means no live LJ account for that handle, not that the person never had one (deleted journals may survive in archives).

## Gotchas & OpSec
- Ownership moved to Russia (SUP Media); data-handling and availability differ from its US-era reputation — factor that into evidence handling.
- Much content is friends-locked; public view is partial. Check the Wayback Machine for deleted or since-locked entries.
- OpSec: passive for reading; use a sock puppet and avoid comments/friend requests that would alert the subject.

## Overlaps ("do both")
- Pairs with username-enumeration tools and the Wayback Machine — username searchers tell you the handle exists here, archives recover journal content that has since been locked or deleted.

## Trust & verifiability
`trust: community` — a real platform, but every field and post is self-authored; corroborate names, dates and locations against independent sources before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | livejournal |
