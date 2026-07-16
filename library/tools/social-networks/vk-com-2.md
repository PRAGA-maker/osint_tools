---
id: vk-com-2
name: vk.com (People Search)
description: Use when you have a `name` or `username` (especially for a Russian/CIS-linked subject) and want to find their VKontakte profile — returns `social-profile`, `name`, photos, and stated location/education/associates.
url: https://vk.com/search/people?c%5Bname%5D=1
category: social-networks
path:
- social-networks
bestFor: Finding and filtering VKontakte profiles by name, with rich filters (city, age, school, employer) — the primary social network for Russia/CIS.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free to search and view public profiles, but VK increasingly gates full profile/photo access and the people-search filters behind a logged-in account.
opsec: active
opsecNote: Meaningful searching/browsing on VK now generally requires a logged-in account, and VK (a Russian-jurisdiction platform) logs your activity and may record profile visits. Use a sock-puppet VK account created on a burner number over a clean IP; never use a personal or attributable account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: VKontakte is the genuine, dominant social network for Russia and the CIS; profiles are first-party, though user-entered detail is self-reported.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
aliases:
- VKontakte
- VK people search
tags:
- russiansocialmedia
- Russian Social Media Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- community-search
- get-user-info
- item
- people-search-results-vk
- vk
- vk-com
- vk-community-search
- vk-people-search
---

# vk.com (People Search)

> VKontakte's native people search — the essential platform for anyone with Russian/CIS ties, with powerful filters by city, age, school, and employer.

## When to use
You have a `name` or `username` for a subject connected to Russia, Ukraine, or the wider CIS/Russian-speaking diaspora, and want to find their VK profile. VK's people search supports rich filtering (city, age range, relationship status, school, university, employer), making it one of the strongest single tools for locating and disambiguating people in that region.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a sock-puppet VK account (clean IP, burner number).
2. Go to https://vk.com/search/people and enter the `name` (VK matches Cyrillic and transliterated forms — try both).
3. Apply filters: city/country, age, school/university, employer, relationship status — to cut a common name down.
4. Open candidate profiles for photos (`image`), stated location/education/work, friends, and wall posts.
5. Pivot: profile photos → reverse image/face search; listed friends → `associate` mapping; school/employer → further VK filtering or other platforms.

## Inputs → Outputs
- **In:** `name` or `username` (Cyrillic or transliterated) + optional demographic filters
- **Out:** `social-profile` (VK profiles), `name`, `image` (photos), stated city/education/employer, friends/associates
- **Empty/negative result looks like:** no matching profiles — try Cyrillic vs Latin spelling, drop filters, or check the subject simply isn't on VK. Note some profiles are hidden from search or friends-only.

## Gotchas & OpSec
- **Login effectively required** for real searching/viewing — always a sock puppet; VK is Russian-jurisdiction and logs activity/visits.
- Try both Cyrillic and transliterated name spellings; VK is strongest with native-script names.
- Self-reported fields can be false; corroborate.

## Overlaps ("do both")
- Pairs with VK-specific OSINT tools (`[[vk-community-search]]`, socid/ID resolvers) and reverse-image search — native search finds the profile, the specialist tools extract IDs, groups, and hidden connections.

## Trust & verifiability
`trust: trusted` — the authentic first-party VK platform; profiles are real, but user-entered detail is self-reported and should be verified against photos, friends, and posts.
