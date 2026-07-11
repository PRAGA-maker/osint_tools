---
id: douban
name: Douban
description: Use when you have a `name`/`username` of a likely Chinese subject and want their books/film/music and interest-group activity — returns a `social-profile` and interest footprint.
url: https://www.douban.com
category: social-networks
path:
- social-networks
bestFor: Profiling a Chinese-speaking subject via their reviews, ratings, and interest groups on China's culture-focused social network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse much public content; a Chinese-mobile-verified account is generally needed to search fully, view some content, and interact.
opsec: active
opsecNote: Registration typically requires a Chinese phone number, and a logged-in account operating from an unusual location/IP draws scrutiny on Chinese platforms. Prefer read-only access to public profiles; if you must register, use a dedicated, well-warmed sock-puppet and appropriate infrastructure — never an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Major, legitimate Chinese social network; profile content is user-generated, and pseudonymity is common, so attribution to a real identity requires corroboration.
missingPersonsRelevance: high
coverage:
- cn
auth: account
api: false
localInstall: false
registration: true
aliases:
- 豆瓣
- douban.com
tags:
- toddington
- curated-directory
- social-media
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Douban

> China's long-running culture-and-community network (books, film, music, interest groups) — a place to profile a Chinese-speaking subject's tastes, reviews, and social circles.

## When to use
Your subject is Chinese or Chinese-speaking and you have a `name` or `username` and want depth beyond a basic profile: what they read/watch/listen to, the interest groups (小组) they join, and the people they interact with there. Douban skews to educated, urban, culturally-engaged users, so a hit often yields a rich interest and social footprint distinct from Weibo/WeChat.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.douban.com (Chinese; use translation).
2. Search the `username`/`name`, or pivot from a known Douban ID/URL.
3. Open the profile: read their book/film/music lists and reviews, joined groups, status updates, and followers/following.
4. Corroborate identity via consistent handle, avatar, writing style, and cross-links to other platforms.
5. Pivot: reused usernames feed `[[sherlock]]`/`[[maigret]]`; named groups and reviewers feed further Douban and Weibo searches; avatars feed reverse-image.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` with interests (books/film/music), groups, activity, and social connections
- **Empty/negative result looks like:** no profile, or a locked/sparse one — many users are pseudonymous and privacy-tighten their accounts, so a thin result is common and not conclusive. Full search often needs a logged-in, phone-verified account.

## Gotchas & OpSec
- Registration wall (Chinese phone verification) blocks casual full access; plan infrastructure before attempting an account.
- Pseudonymity is the norm — a matching handle is a lead, not proof; corroborate.
- Chinese-language platform; machine translation is imperfect for slang and group names.

## Overlaps ("do both")
- Pairs with `[[weibo-com]]` and WeChat-focused tools — Douban reveals cultural/interest identity while Weibo reveals public broadcasting and news activity; the same person often reuses a handle across them.

## Trust & verifiability
`trust: community` — a legitimate major platform, but content is self-published and pseudonymous; attribution to a real-world identity must be corroborated with other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | douban |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
