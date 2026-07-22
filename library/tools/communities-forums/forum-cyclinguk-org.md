---
id: forum-cyclinguk-org
name: forum.cyclinguk.org
description: Use when you have a `username` that may belong to a UK cyclist and want their forum footprint — returns the member's `social-profile`, posts and joined-date.
url: https://forum.cyclinguk.org/
category: communities-forums
path:
- communities-forums
bestFor: Checking whether a username posts on the Cycling UK (formerly CTC) community forum and mining their public post history for leads.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read publicly; a free account is only needed to post.
opsec: passive
opsecNote: Reading member profiles and threads is passive and unauthenticated — no notice to the member. Do not register or message with an attributable identity; a profile view while logged out leaves no trace to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine phpBB community forum run by Cycling UK; content is member-generated, so treat individual claims as self-reported.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Cycling UK Forum
- CTC Forum
tags:
- forums
- Forums
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# forum.cyclinguk.org

> The Cycling UK (ex-CTC) members' phpBB forum — a niche community where a cycling-linked subject may post under a reusable handle.

## When to use
You have a `username` (or a real name that might be echoed in a handle) for someone connected to UK cycling — touring, audax, commuting, club racing — and want to know whether they are active on this forum. A hit yields a member profile plus a searchable post history that can leak location clues (routes, home region, meets), gear, and links to other handles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://forum.cyclinguk.org/ (public read; no login).
2. Use the member search / memberlist to look up the `username`, or use the site search + a `site:forum.cyclinguk.org "handle"` Google query.
3. Open the member's profile for join date, post count, website/location fields they chose to reveal, and their last-active date.
4. Read their post history — ride reports and "small ads" threads often reveal geography, times and real-world contact hints.
5. Pivot: a distinctive handle here feeds cross-platform username enumeration; a mentioned club or route narrows `geolocation`.

## Inputs → Outputs
- **In:** `username` (or handle guess)
- **Out:** `social-profile` (join date, post count, self-declared location/website), `username` confirmation, post history
- **Empty/negative result looks like:** "No members found" in the memberlist — the handle is not registered here; try spelling variants before concluding absence.

## Gotchas & OpSec
- Members can hide their profile fields; a thin profile is not proof of inactivity — check post history separately.
- Content is self-reported forum chatter; corroborate any location/identity claim elsewhere.
- OpSec: stay logged out and passive; registering or PM-ing would expose an account to the subject.

## Overlaps ("do both")
- Pairs with username-enumeration tools (to confirm the handle is reused elsewhere) and with general forum-search engines when this site's own search is weak.

## Trust & verifiability
`trust: community` — an authentic, well-established phpBB forum operated by Cycling UK, but the posts are member-generated and should be treated as leads, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forum-cyclinguk-org |
