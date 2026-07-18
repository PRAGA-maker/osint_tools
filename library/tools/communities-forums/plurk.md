---
id: plurk
name: Plurk
description: Use when you have a `username` or `name` and want to find a Plurk microblogging profile — returns the public `social-profile`, timeline posts, and social connections.
url: https://www.plurk.com/
category: communities-forums
path:
- communities-forums
bestFor: Locating and reading a person's Plurk microblog and social graph, especially for Taiwan/SE-Asia subjects.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to browse public profiles; posting/following needs a free account.
opsec: passive
opsecNote: Viewing public Plurk profiles and timelines is passive and unauthenticated. If you want to see friends-only content you'd need to log in and follow — use a sock-puppet account for that, since following notifies the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Plurk is the genuine first-party platform; public profile content is authentic, not a third-party scrape.
missingPersonsRelevance: medium
coverage:
- global
- tw
auth: none
api: true
localInstall: false
registration: false
aliases:
- plurk.com
tags:
- toddington
- curated-directory
- microblogging
- social-networks
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Plurk

> A microblogging social network (very popular in Taiwan and parts of SE Asia) — a place to find a subject's timeline, handle, and social connections that Western-focused searches miss.

## When to use
You have a `username` or real `name` and are building a subject's social footprint, particularly in Taiwan/Hong Kong/SE-Asian cases where Plurk is a common platform. A found profile yields the person's posts (a "plurk" timeline with a distinctive horizontal layout), profile details, and the friends/fans they interact with — useful for confirming identity, activity timeline, and associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.plurk.com/.
2. Try the handle directly as a profile URL (`plurk.com/USERNAME`) or use the search to look up a `username`/`name`.
3. Open the profile: read the public timeline, bio, join date, and the friends/fans lists (`associate`).
4. To view restricted (private/friends-only) plurks you must log in and be accepted as a follower — use a sock puppet and expect this to notify the target.
5. Pivot: the handle feeds cross-platform username search; friends/fans give `associate` leads; timeline content can leak location, employer, or contact details.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (timeline, bio), `associate` links (friends/fans)
- **Empty/negative result looks like:** no profile at that handle, or a profile set to private (bio visible but plurks hidden) — the latter still confirms the account exists.

## Gotchas & OpSec
- Handle ≠ person: common usernames may belong to someone else; corroborate with bio/photo/associates before attributing.
- Private accounts require following to read; do this only from a sock puppet and note it alerts the owner.
- OpSec: passive for public viewing; active the moment you follow or interact.

## Overlaps ("do both")
- Pairs with a cross-platform username-enumeration tool: run the Plurk handle elsewhere to tie the persona to other accounts, and reverse-image the profile photo.

## Trust & verifiability
`trust: trusted` — first-party platform data. Public profiles are authentic; the only caveat is confirming the handle actually belongs to your subject rather than a namesake.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | plurk |
