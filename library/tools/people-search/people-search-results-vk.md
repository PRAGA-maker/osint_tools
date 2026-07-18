---
id: people-search-results-vk
name: People search results | VK
description: Use when you have a `name` and want to find matching VKontakte profiles — returns candidate `social-profile`s and `username`s to pivot on.
url: https://vk.com/people
category: people-search
path:
- people-search
bestFor: Name-based people search across VKontakte, the dominant social network in Russia and the post-Soviet space.
selectorsIn:
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to use; a logged-in VK account is needed to run the full people search and apply filters.
opsec: active
opsecNote: Searching requires a logged-in VK account, and VK is a Russian platform that logs account activity. Use a dedicated sock-puppet VK account and a clean IP — never your real account. Viewing profiles does not usually notify the target, but do not send friend requests or messages during recon.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party VKontakte people directory/search — the data is the platform's own, so it is authoritative for what users have posted (though users self-report).
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- vk-people-search
- vk-community-search
- vk-com
- get-user-info
- community-search
- vk
- vk-com-2
aliases:
- VK People
- VKontakte people search
tags:
- russia
- social-networks
- people-search
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# People search results | VK

> VKontakte's native people-search directory — the first stop for locating a person across Russia and the post-Soviet region.

## When to use
You have a `name` (ideally in Cyrillic, or a known transliteration) and the subject has any tie to Russia, Ukraine, Belarus, Central Asia, or the wider Russian-speaking diaspora. VK is the largest social network in that region, so a `name` search here often surfaces profiles that Western platforms miss — feeding photos, city, school/employer, friends, and a `username` to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into a **sock-puppet** VK account and open https://vk.com/people.
2. Enter the `name`; VK's search supports strong filters — city, age, school, university, employer, relationship status — use them to narrow large result sets.
3. Review candidate profiles: profile photo (`face`), stated city (`geolocation`), education/work, and friend list (`associate`s).
4. Capture the profile URL and `username` (the vanity slug, e.g. `vk.com/ivan.petrov`) for cross-platform pivoting.
5. Pivot: a confirmed VK profile feeds VK-specific tools (`[[vk-people-search]]`, `[[get-user-info]]`) and reverse-image / username enumeration.

## Inputs → Outputs
- **In:** `name` (Cyrillic or transliterated), plus optional city/school/employer filters.
- **Out:** candidate `social-profile` URLs and `username`s, with visible city, education, work, and friends.
- **Empty/negative result looks like:** no matching profiles, or only unrelated same-name accounts — expected for names with no VK footprint, or when the profile is private/deactivated.

## Gotchas & OpSec
- Login required: the full people search and filters need a logged-in account — use a burner, never your own.
- Transliteration: names may be registered in Cyrillic; try both the Cyrillic and common Latin spellings.
- Self-reported data: city/employer are user-entered and can be fake or outdated — corroborate.
- OpSec: **active** — VK logs your account's activity; avoid any interaction (friend request/message) that would notify the target.

## Overlaps ("do both")
- Pairs with `[[vk-people-search]]` and `[[get-user-info]]` — this is the manual on-platform directory, while those add scripted enumeration and extraction of profile fields.

## Trust & verifiability
`trust: trusted` — it is VK's own people directory, authoritative for what users have published; the caveat is that profile fields are self-reported, so verify identity across multiple signals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | people-search-results-vk |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
