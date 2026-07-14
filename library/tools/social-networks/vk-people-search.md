---
id: vk-people-search
name: VK People Search
description: Use when you have a `name` (plus city/school/employer) for a Russian/CIS subject and want their VKontakte profile — returns profiles filterable by location, age, school and workplace.
url: https://vk.com/people
category: social-networks
path:
- social-networks
bestFor: Finding and filtering VKontakte profiles by name, city, age, school and workplace.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- image
- associate
- geolocation
status: live
pricing: free
costNote: Free. Basic profile viewing works logged-out, but the powerful people-search filters (city, age, school, workplace) require a logged-in VK account.
opsec: active
opsecNote: Queries hit VK's (Russia-based) servers and, once logged in, are tied to your account under Russian data jurisdiction. Logged-in profile visits do not notify the owner on VK by default, but assume the platform logs your activity. Always use a sock-puppet account and a clean/VPN browser.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: VK is the largest Russian-language social network; profile data is first-party and authoritative. The risk is operational (Russian jurisdiction, login requirement), not data authenticity.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- odnoklassniki
- yandex-people-search
aliases:
- VKontakte people search
- vk.com/people
tags:
- vkontakte
- russia
- cis
- social-network
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# VK People Search

> VKontakte's native people search — the single most productive way to locate and profile Russian- and CIS-region subjects, with rich filters for city, age, school and workplace.

## When to use
You have a `name` (Cyrillic or transliterated) or `username` for someone Russian-speaking or from a CIS country. VK is the dominant regional network (younger/broader than Odnoklassniki), and its people search lets you filter by city, birth year, school, university and employer — powerful for disambiguating common names and for finding someone via their known school/workplace. High-value for photos, friend/family networks, groups, and location signals.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet VK account in a clean/VPN browser (the filters need a login).
2. Go to https://vk.com/people (or the People search) and enter the `name`; try Cyrillic and transliterated spellings.
3. Apply filters — city, age/birth year, school, university, workplace, relationship — to narrow common names.
4. Open candidate profiles: photos (`image`), friends (`associate`), groups, and city/school/employer fields (`geolocation`).
5. Pivot: friends feed network mapping; a photo feeds reverse-image/face tools; school/city feeds geolocation; cross-check on `[[odnoklassniki]]`.

## Inputs → Outputs
- **In:** `name` or `username` (plus optional city/school/employer filters)
- **Out:** `social-profile`, `image` (profile/album photos), `associate` (friends/family), `geolocation` (city, school, workplace)
- **Empty/negative result looks like:** no candidate matching your filters, or profiles locked to friends-only (name + avatar only). VK privacy controls are common; absence doesn't rule out a presence under a different spelling or on Odnoklassniki.

## Gotchas & OpSec
- **Active and jurisdictionally sensitive:** VK is Russia-based; use a sock-puppet account and VPN, never anything tied to your identity.
- The strong filters require login — logged-out search is far weaker.
- Cyrillic vs transliteration, plus maiden names and patronymics, change results — search variants.

## Overlaps ("do both")
- Pairs with `[[odnoklassniki]]` (the other major RU network — many people have both, skewing older) and `[[yandex-people-search]]` (surfaces VK profiles from a name/phone via Yandex's index). Do both: coverage differs by demographic.

## Trust & verifiability
`trust: trusted` — first-party data from the largest RU social network, so profile content is authentic. Caution is operational (login, Russian jurisdiction); still verify identity via photos and cross-network matches.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk-people-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, image, associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
