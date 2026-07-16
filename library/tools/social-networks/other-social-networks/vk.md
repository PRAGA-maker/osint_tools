---
id: vk
name: VK
description: Use when you have a `name`/`username` for a Russian or Eastern-European subject and want a rich profile — returns photos, friends, wall posts, groups, and activity from VK.
url: https://vk.com/
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Deep profile investigation of Russian and Eastern-European users — photos, friend graph, wall, groups, and activity.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- associate
status: live
pricing: free
costNote: Free; a VK account (login) is needed to search and to see most profile content. Its API is available but access has tightened.
opsec: active
opsecNote: VK is a Russian platform that logs activity extensively and operates under Russian jurisdiction. Searching/viewing requires a login and can leave footprints (VK shows some profile visitors and suggests you in "people you may know"). Use a warmed sock-puppet account on an isolated device; never your real identity, and don't friend/message the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party platform (one of the largest in the Russian-speaking world); profile data is genuine, though privacy settings and the Russian-language interface limit access.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- vk-community-search
- barkov-net
- qzone
- community-search
- get-user-info
- item
- people-search-results-vk
- vk-com
- vk-com-2
- vk-people-search
aliases:
- VKontakte
- vk.com
tags:
- vk
- russia
- social-media
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# VK

> VKontakte — the dominant social network of the Russian-speaking world: a subject's VK profile is often a goldmine of photos, a full friend graph, wall history, and group memberships.

## When to use
Your subject is Russian, Ukrainian, Belarusian, Central Asian, or otherwise Eastern-European, and you want deep profile intelligence: profile and tagged photos (`image`), the friend list (a strong `associate` graph), wall posts revealing timeline and views, and group memberships showing interests and affiliations. VK often holds far more open data than Western platforms and is frequently the single best source for such subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a **warmed sock-puppet** VK account (search and most content require login).
2. Search by `name` or `username`, or open a known profile URL; VK's search supports filtering by city, school, workplace, age.
3. Explore the profile: photos, friends, wall, groups, and "details" fields.
4. Do not friend/message the target; browse only visible content.
5. Pivot: friends are `associate` leads; photos feed reverse-image/face search; group memberships and city/school filters help find and disambiguate; use `[[vk-community-search]]`/`[[barkov-net]]` for group/audience analysis.

## Inputs → Outputs
- **In:** `name` or `username` (+ city/school/workplace filters)
- **Out:** `social-profile` (wall, groups, details), photos (`image`), friend graph (`associate`)
- **Empty/negative result looks like:** a locked-down profile shows little to a non-friend, or no match for the handle — privacy settings and closed profiles suppress data; absence isn't proof of inactivity.

## Gotchas & OpSec
- Human-in-the-loop: **VK account login required**; the interface is Russian-first.
- OpSec: **active** and jurisdiction-sensitive — VK logs heavily and can surface you to the target. Use an isolated sock-puppet account/device; never your real identity.
- Privacy settings vary; some rich profiles are wide open, others closed.

## Overlaps ("do both")
- Pairs with `[[vk-community-search]]` and `[[barkov-net]]` (VK group/audience tools) and `[[qzone]]` if the subject also spans Chinese platforms — check the friend graph across tools.

## Trust & verifiability
`trust: trusted` — a first-party platform, so visible data is genuine. The limits are access (login, privacy, language) and OpSec risk, not authenticity; corroborate identity via photos and the friend graph.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
