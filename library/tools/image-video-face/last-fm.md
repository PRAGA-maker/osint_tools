---
id: last-fm
name: Last.fm
description: Use when you have a `username` (or suspect a music handle) and want the person's public listening profile — returns social-profile, real name, location, and associates.
url: http://www.last.fm
category: image-video-face
path:
- image-video-face
bestFor: Turning a reused music-scrobbling `username` into a public profile with real name, country, join date, and a friends list.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
- geolocation
- associate
status: live
pricing: free
costNote: Free to view any public profile; a paid Pro tier adds personal stats but is irrelevant to looking up someone else.
opsec: passive
opsecNote: Viewing a public profile at last.fm/user/<handle> is a normal unauthenticated pageview — the target is not notified. Don't log in with a personal account or "friend"/message the target, which would leave a trace.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running music social network (CBS/Viagogo-owned); profile data is self-reported by the user, so names/locations are as reliable as what the person chose to publish.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- last.fm
- lastfm
tags:
- social-networks
- username-pivot
- music
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Last.fm

> A music-scrobbling social network whose public profiles (last.fm/user/<handle>) often expose a real name, country, and friends list behind a reused username.

## When to use
You have a `username` from another platform and want to check whether it maps to a Last.fm profile. Music handles are frequently reused, and Last.fm profiles are public and rich: they can show a self-set real `name`, `geolocation` (country), age, join date, avatar, and a friends/neighbours list (`associate`s) — plus a listening history that hints at language, era, and taste for corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go directly to `https://www.last.fm/user/<username>` (substitute the handle), or use the site search for a name.
2. If the profile loads, read the header for real name, country, age, "scrobbling since" date, and avatar.
3. Open the **Friends** tab for connected accounts (often the same person's real-life circle) and the **Library** for recent listening (timezone/activity-pattern clues).
4. Save the avatar for a reverse-image search, and note friend handles to enumerate elsewhere.
5. Pivot: friend usernames feed cross-platform enumeration; the avatar feeds face/image search; a stated country narrows other lookups.

## Inputs → Outputs
- **In:** `username` (or a `name` to search)
- **Out:** `social-profile` (the Last.fm page), self-reported `name`/`geolocation`, `associate` list (friends)
- **Empty/negative result looks like:** a 404 / "user not found" (handle unused here) or a bare profile with default avatar, no real name, and no friends — the account exists but the owner published nothing pivotable.

## Gotchas & OpSec
- Profile fields are self-reported: a name or country may be fake or a joke — treat as leads, corroborate elsewhere.
- Activity timestamps reflect scrobbling, not necessarily the person being online; use listening times only as weak timezone signal.
- OpSec: passive — an unauthenticated pageview raises no alert. Never friend or message the target from a research context.

## Overlaps ("do both")
- Pairs with cross-platform username enumerators (e.g. via [[osint-combine-tools]]' WhatsMyName) — enumeration tells you the handle exists on Last.fm; this tool reads what the profile actually reveals.

## Trust & verifiability
`trust: community` — a legitimate, long-lived social platform, but profile content is user-authored, so names/locations require independent confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | last-fm |
| category | image-video-face |
| selectorsIn → selectorsOut | username, name → social-profile, name, geolocation, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
