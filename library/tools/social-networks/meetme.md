---
id: meetme
name: MeetMe
description: Use when you have a `name` or `username` and want to check for a profile on the MeetMe social/dating "people nearby" network — returns a social-profile with photos and rough location.
url: https://www.meetme.com
category: social-networks
path:
- social-networks
bestFor: Checking whether a subject has a MeetMe social-discovery/dating profile and pulling their photos, bio and approximate location.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
status: live
pricing: freemium
costNote: Free to join and browse; some discovery/messaging features are gated behind MeetMe+ credits/subscription. An account is effectively required to search users.
opsec: active
opsecNote: MeetMe is an interactive social/dating app — viewing or liking profiles from a logged-in account can notify the other user and expose your identity. Always operate from a sock-puppet account with puppet photos; never use a personal profile.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running mainstream social/dating platform (part of The Meet Group / ParshipMeet), operating since 2005; profiles are self-created and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- meetme
- meetme.com
- myYearbook
tags:
- toddington
- curated-directory
- social-media
- dating
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# MeetMe

> A mainstream "discover people nearby" social/dating network (formerly myYearbook) — a place to check for a subject's dating-app presence, photos and approximate location.

## When to use
You are mapping a person's social/dating footprint and want to cover MeetMe, a large location-based social-discovery app that skews younger and toward casual dating/chat. Start from a `name`, a reused `username`, or a known location, and look for a matching `social-profile` with `image` set and a stated age/city. Useful when other platforms are locked down but the subject maintains a public dating-style profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet MeetMe account (needed to browse/search) at https://www.meetme.com — set the puppet's location near the subject's suspected area, since discovery is location-based.
2. Use profile search / the "Meet" and nearby feeds; filter by age and location to narrow candidates.
3. Match on photos, first name, age, and city against what you already know.
4. Extract the profile handle/URL and photos (`social-profile`, `image`) and any bio details (interests, city, links to other socials).
5. Pivot: photos feed reverse-image search; a linked handle or reused username feeds cross-platform username search.

## Inputs → Outputs
- **In:** `name`, `username`, or an area to browse
- **Out:** `social-profile` (MeetMe profile, bio, stated city/age), `image` (profile photos)
- **Empty/negative result looks like:** no matching profile in the searched area, or many similar-looking profiles you can't distinguish — MeetMe has no strong identity verification, so confirm via photos/other selectors.

## Gotchas & OpSec
- Location-based discovery means you may need to set your puppet's location near the target to surface them; results are noisy.
- **Active platform:** likes/views/messages can notify the other user — stay passive (browse only) and never interact from anything but a puppet.
- Profiles are self-asserted; ages, names and photos may be fake or stale.

## Overlaps ("do both")
- Pairs with reverse-image search and username-enumeration tools — a MeetMe photo or reused handle often unlocks the subject's presence on other dating and social platforms.

## Trust & verifiability
`trust: community` — an established mainstream platform, but individual profiles are unverified user-generated content; corroborate identity with photo analysis and other selectors before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | meetme |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
