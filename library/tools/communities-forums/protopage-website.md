---
id: protopage-website
name: Protopage
description: Use when you have a `username`/`name` and want a subject's public start page — returns their curated RSS feeds, bookmarks and notes, exposing interests and linked `social-profile`s.
url: http://www.protopage.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's public Protopage start page to read their bookmarks, feeds and interests.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free personalized start-page service; creating a page needs an account, but public pages are viewable without login.
opsec: passive
opsecNote: Viewing a public Protopage is passive and unauthenticated; the page owner is not notified. Prefer finding pages via a search-engine site: query so you never log in against your own identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party start-page service; content is entirely user-curated and unverified, useful only as a window into what the subject reads/links.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Protopage
- protopage.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Protopage

> A free personalized "start page" / RSS dashboard; when a subject makes theirs public, it becomes a readable map of their bookmarks, feeds and interests.

## When to use
You have a `username` or `name` and are building a picture of a subject's online interests and the sites/profiles they follow. Some users publish their Protopage at a shareable URL (`protopage.com/<name>`) packed with RSS feeds, bookmarks and sticky notes — an interest-graph and a source of outbound links to their other `social-profile`s. It is a supplementary lifestyle/interest source, not a primary identity lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Guess the direct URL `http://www.protopage.com/<username>` from a known handle, or run a search-engine query `site:protopage.com "<name/username>"` to find public pages.
2. Open any public page found and read the widgets: bookmark lists, subscribed RSS feeds, and notes.
3. Note recurring themes (hobbies, employer, region) and any outbound links to the subject's other profiles.
4. Pivot: linked profiles feed `social-profile` enrichment; bookmarked sites/feeds hint at interests, employer or location to corroborate elsewhere.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile`/outbound links, `username`, plus interest/lifestyle context (bookmarks, feeds)
- **Empty/negative result looks like:** no page at the guessed URL and no search hits — most Protopages are private or unshared, so absence is the common case, not a finding.

## Gotchas & OpSec
- Human-in-the-loop: none; do not create an account to browse.
- OpSec: passive — reading a public page does not alert the owner.
- Low hit rate: most users keep pages private, and shared pages are hard to attribute to a specific person without corroboration. Treat any match as a lead, not proof of identity.

## Overlaps ("do both")
- Pairs with username-enumeration tools — Protopage may confirm a handle is in use and reveal linked profiles, but a dedicated username checker covers far more platforms; use both to widen the profile net.

## Trust & verifiability
`trust: community` — a third-party service hosting entirely user-generated content; nothing on a Protopage is verified, so use it for interest/link leads and confirm identity elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | protopage-website |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
