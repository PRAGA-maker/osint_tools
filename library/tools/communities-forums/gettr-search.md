---
id: gettr-search
name: Gettr Search
description: Use when you have a `username` or `name` and want to find that person's posts/profile on the GETTR social network — returns profiles, posts, and media.
url: https://www.gettr.com/
category: communities-forums
path:
- communities-forums
bestFor: Locating a subject on GETTR and reading their posts, media, and connections.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to browse and search; viewing public profiles/posts needs no account, though some actions prompt a login.
opsec: passive
opsecNote: Searching and reading public profiles is passive and doesn't notify the target. If you log in to see more, use a sock-puppet account — never your real identity — since following/liking is visible. For bulk collection prefer an API client over hammering the site from your IP.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: GETTR is a real, sizable public social network; the platform data is authentic, though (like any social site) profiles can be impersonations or parody.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gogettr
- gettr-com
aliases:
- GETTR
- gettr.com search
tags:
- social-media
- socmint
- search
source: inteltechniques-tools
lastVerified: '2026-07-29'
enrichment: full
---

# Gettr Search

> The search function of the GETTR social network — find a subject's profile, posts, media, and hashtags on a platform that mainstream tools often skip.

## When to use
You have a `username` or `name` and want to know whether the subject is active on GETTR (a Twitter/X-style network popular with certain political communities). Search resolves people, posts, photos, video, and hashtags — useful when a target isn't on mainstream platforms or maintains a parallel presence here. Posts can leak location chatter, associates, images, and timestamps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.gettr.com/ and use the Search icon.
2. Enter a `username` or `name`; filter results by **Top / Latest / People / Visions / Photos / Video**.
3. Open the profile: read posts, media, bio links, and following/followers for `associate` leads.
4. Save images (`image`) for reverse-image/face work and note post timestamps.
5. For bulk/systematic collection, switch to the `[[gogettr]]` API client instead of manual scrolling.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile`, posts, `image` media, hashtags, follower/associate lists
- **Empty/negative result looks like:** no matching people, or only unrelated posts — the subject may not use GETTR, or uses a different handle. Try name variants and cross-check handles from other platforms.

## Gotchas & OpSec
- Human-in-the-loop: some content prompts a **login** — use a sock-puppet account, not your own.
- Handles are not identity — verify a profile is really your subject (photos, cross-linked accounts) before relying on it; impersonation/parody exists.
- OpSec: **passive** to read; interactions (follow/like) are visible, so don't.

## Overlaps ("do both")
- Pairs with `[[gogettr]]` — the manual site is best for eyeballing a specific profile; gogettr (an open-source API client) is for archival/bulk pulls of a user's timeline and followers at scale.

## Trust & verifiability
`trust: community` — a genuine large platform, so the data is real; the caveat is the usual social-media one: confirm account ownership and watch for impersonators.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gettr-search |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
