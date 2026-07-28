---
id: chattoday
name: ChatToday
description: Use when you have a `username`/`name` and want a person's messaging-app handles — returns self-listed Kik/Snapchat/Telegram/Discord `social-profile`s and location.
url: https://chattoday.com
category: messaging
path:
- messaging
bestFor: Finding a person's cross-app messaging handles (Kik, Snapchat, Telegram, Discord) from a public profile directory.
selectorsIn:
- username
- name
- geolocation
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to browse and search; posting your own profile requires a free account.
opsec: passive
opsecNote: Passive browsing of a public directory — you read self-posted profiles and never contact the subject. Profiles are user-submitted and often tied to people seeking chat/dating contacts, so handle the data (and any minors' presence) with care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small user-generated chat-directory site; profiles are self-submitted and unverified, with no authority behind the identity claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ChatToday.com
tags:
- chat
- messaging
- username-directory
source: osintambition-social
lastVerified: '2026-07-28'
enrichment: full
---

# ChatToday

> A public directory where users post their messaging handles (Kik, Snapchat, Skype, Telegram, Discord) to find chat partners — searchable by handle, interest, or nearby location.

## When to use
You have a `username` (or a `name`/location) and want to find the same person's handles on messaging apps. Because ChatToday profiles deliberately list *multiple* platform usernames in one place, a single match can bridge a Kik handle to a Snapchat, Telegram, or Discord one — a useful pivot when a subject uses chat/dating apps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://chattoday.com in a puppet browser.
2. Search by `username`, keyword/interest, or use the "near me" / location feature for a `geolocation` angle.
3. Open a matching profile; read the listed messaging handles, stated interests, age/location, and any linked social pages.
4. Pivot: take each listed handle and verify it on its native platform, and run it through username-enumeration tooling to expand the identity graph.

## Inputs → Outputs
- **In:** `username`, `name`, or `geolocation`
- **Out:** self-listed messaging `social-profile`s / `username`s across apps, plus stated location and interests
- **Empty/negative result looks like:** no matching profile — most people never post here, so absence means nothing; a match is only a *claim* until verified on the native app.

## Gotchas & OpSec
- Everything is self-submitted and unverified — a listed handle may be aspirational, stale, or impersonation; always confirm on the real platform.
- The site skews toward casual/dating chat; be mindful of privacy, consent, and the possibility of minors.
- Small directory with sparse coverage — treat a hit as a lead, not proof of identity.

## Overlaps ("do both")
- Pairs with username-enumeration tools — ChatToday supplies candidate handles across apps, and those tools test each handle's presence and links elsewhere.

## Trust & verifiability
`trust: unverified` — a user-generated directory with no identity verification; useful only as a lead source to be corroborated on each named platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chattoday |
| category | messaging |
| selectorsIn → selectorsOut | username, name, geolocation → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
