---
id: odnoklassniki
name: Odnoklassniki
description: Use when you have a `name`, `username` or `phone` for a Russian/CIS subject and want their social profile, photos and connections — returns profile, photos, groups and friends.
url: https://ok.ru/
category: social-networks
path:
- social-networks
- other-social-networks
bestFor: Finding and profiling Russian- and CIS-region subjects on a major regional social network.
selectorsIn:
- name
- username
- phone
selectorsOut:
- social-profile
- image
- associate
- geolocation
status: live
pricing: free
costNote: Free to search and view public profiles. A (sock-puppet) account unlocks more search and full profile/photo viewing; some features nudge toward the mobile app.
opsec: active
opsecNote: Queries hit OK.ru's (VK-owned, Russia-based) servers directly and are subject to Russian data jurisdiction. Logged-in profile views can trigger a "guest"/visitor notification to the account owner. Always use a sock-puppet account and a clean/VPN browser; assume the platform logs and may attribute your activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: OK.ru is a genuine, major social network (owned by VK), so profile data is first-party and authoritative — but it sits under Russian jurisdiction, so treat the operating environment, not the data authenticity, as the risk.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- vk-com
- yandex-people-search
aliases:
- OK.ru
- Odnoklassniki
- Одноклассники
tags:
- russia
- cis
- social-network
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Odnoklassniki

> One of the two dominant Russian-language social networks (VK-owned) — the go-to for locating and profiling older/CIS-region subjects who aren't on Western platforms.

## When to use
You have a `name` (Cyrillic or transliterated), a `username`, or sometimes a `phone`, and your subject is Russian-speaking or from a CIS country. Odnoklassniki ("Classmates") skews to an older demographic and to reconnecting with school/military/work cohorts, so it often carries people who have little Western-platform footprint. Good for photos, family/friend links, group memberships and hometown/school details that anchor a geolocation.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet OK.ru account in a clean/VPN browser, use the search (people) with the `name` — try both Cyrillic and transliterated spellings.
2. Filter by city, age, school/university or workplace to disambiguate common names.
3. Open candidate profiles; read photos, "friends," groups, gifts, and any city/school/employer fields.
4. Note that a logged-in visit may notify the owner you viewed them — pace yourself and avoid interacting.
5. Pivot: friends/family feed `associate` mapping; a school/hometown feeds `geolocation`; the same photo feeds reverse-image/face tools; cross-check the person on `[[vk-com]]`.

## Inputs → Outputs
- **In:** `name`, `username`, or `phone`
- **Out:** `social-profile`, `image` (profile/album photos), `associate` (friends/family), `geolocation` (city, school, workplace)
- **Empty/negative result looks like:** no candidate matching your disambiguators, or heavily privacy-restricted profiles showing only a name and avatar — common, since users can lock down profiles. Absence here doesn't rule out a VK presence.

## Gotchas & OpSec
- **Active and jurisdictionally sensitive:** OK.ru is Russia-based; assume logging and possible attribution. Use a sock-puppet and VPN, and don't log in with anything tied to your identity.
- Visitor notifications: logged-in profile views can appear in the owner's "guests" list — a real leak.
- Cyrillic vs transliteration matters; search both, and account for patronymics and maiden names.

## Overlaps ("do both")
- Pairs with `[[vk-com]]` (the larger VK network — many people have both, and one fills gaps in the other) and `[[yandex-people-search]]` (index that surfaces OK.ru profiles from a name/phone). Do both: OK.ru skews older, VK skews younger.

## Trust & verifiability
`trust: trusted` — a first-party major social network, so profile content is authentic. The caution is operational (Russian jurisdiction, visitor logging), not about data reliability; still verify identity via photos and cross-network matches.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | odnoklassniki |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, phone → social-profile, image, associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
