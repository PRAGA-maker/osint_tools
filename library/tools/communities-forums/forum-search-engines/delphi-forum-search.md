---
id: delphi-forum-search
name: Delphi Forums
description: Use when you have a username or a niche topic and want decades of community forum posts to mine — returns social-profile, associate and text leads from one of the web's oldest surviving forum hosts.
url: https://www.delphiforums.com/
category: communities-forums
path:
- communities-forums
- forum-search-engines
bestFor: Mining a long-running forum host for a username's post history or historical niche-community discussions.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to browse public forums and member profiles and to register; some communities gate deeper content behind membership. Core reading is free.
opsec: passive
opsecNote: Browsing public forums and profiles is passive and does not notify members. Joining a private community to read it is active and may be visible to moderators — use a sock-puppet account and only where justified.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Delphi Forums is a genuine, decades-old forum host with hundreds of millions of posts; content is authentic user-generated discussion, though as with any forum, self-reported details are unverified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- delphiforums.com
- Delphi Forums
tags:
- forum-search
- legacy-community
- online-communities-blogs
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# Delphi Forums

> One of the internet's oldest surviving forum hosts (hundreds of millions of posts across decades). Two OSINT angles: pull a member's long-running post history from a `username`, or mine a niche community for historical discussion.

## When to use
Your subject may have a Delphi Forums account, or your case touches a niche community (hobby, health, local, fandom) that has lived on Delphi for years. Because the archive spans decades, it can surface a `username`'s old posts, a real name or location disclosed years ago, the communities they frequented (`associate` network), and historical threads that predate modern social media. It is especially useful for older subjects and long-tail communities that mainstream searches miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.delphiforums.com/ and browse by category or use the site search for a `username`, `name`, or topic keyword.
2. Also try a scoped web search: `site:delphiforums.com "<username or term>"` to catch indexed threads.
3. Open member profiles and threads: note the member's posting history, the forums they belong to, join dates, and any self-disclosed details.
4. For a private/members-only community that's relevant, join with a sock-puppet account only if justified — reading it may be visible to moderators.
5. Pivot: the username, named associates, and disclosed details feed username-enumeration and people-search tooling; old posts also feed timeline reconstruction.

## Inputs → Outputs
- **In:** `username`, `name`, or a topic keyword.
- **Out:** `social-profile` (member profile + post history), `associate` (co-members/thread partners), post `text` with possibly-disclosed identity/location details.
- **Empty/negative result looks like:** no matching member or threads — the handle isn't on Delphi, or relevant forums are private and unindexed. Absence isn't proof; old content may only survive in web archives.

## Gotchas & OpSec
- Human-in-the-loop: reading public content needs no login, but private communities require **account-login** (use a sock puppet) and moderators may see joins.
- OpSec: **passive** for public browsing; joining/posting is active and attributable — stay read-only where possible.
- It's a decades-old forum: expect dead links, moved threads, and content best recovered via the Wayback Machine when the live page is gone.

## Overlaps ("do both")
- Pairs with the Wayback Machine and username-enumeration tools — archives recover deleted Delphi threads, and enumeration tools confirm whether the same handle appears on other platforms.

## Trust & verifiability
`trust: community` — a real, long-standing forum host; posts are authentic user discussion, but self-reported identity/location details are unverified. Corroborate any lead before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | delphi-forum-search |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
