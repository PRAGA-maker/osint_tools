---
id: google-com-75
name: Google site-search — Odnoklassniki (ok.ru)
description: Use when you have a `username` or `name` and want to find a subject's Odnoklassniki (OK.ru) profile without an account — returns a `social-profile`.
url: https://www.google.com/search?q=site:ok.ru&ie=utf-8&oe=utf-8&gws_rd=cr&ei=5gelVs6GM8KZUfHyq7gI
category: social-networks
path:
- social-networks
bestFor: Dorking Odnoklassniki (major Russian/CIS social network) via Google's site: operator to surface profiles.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Google `site:` dork; no OK.ru or Google account required for indexed public pages. OK.ru gates much content behind login.
opsec: passive
opsecNote: The query hits Google, not OK.ru, so the subject is not alerted. OK.ru pushes hard login walls — do not register an attributable account; use a sock puppet for deeper viewing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A search-engine technique over OK.ru's public pages, not a product; coverage depends on Google's index and OK.ru's login-gating.
missingPersonsRelevance: high
coverage:
- ru
- global
aliases:
- Odnoklassniki site search
- site:ok.ru
- OK.ru dork
tags:
- russiansocialmedia
- Russian Social Media Sites
- google-dork
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Google site-search — Odnoklassniki (ok.ru)

> A Google `site:ok.ru` dork for Odnoklassniki — a major Russian/CIS social network skewing older — to find profiles from the outside without hitting its login wall.

## When to use
You have a `username` or `name` with a Russian/CIS lead. Odnoklassniki ("Classmates") is heavily used across the former Soviet region, especially by older demographics, and complements VK. Dorking it via Google surfaces public profiles without an OK.ru account — useful because OK.ru walls most content behind login.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the URL, or in Google, scope and add your selector:
   - `site:ok.ru "First Last"` / `site:ok.ru <username>`
   - add a city or birth year to disambiguate; try Cyrillic spelling too.
2. Read results: OK.ru profile URLs, display `name`, city, and snippet content.
3. Open a public profile logged-out to review what's visible.
4. Pivot: an OK.ru handle feeds username checks and reverse-image on the avatar; the same person often also has a VK profile.

## Inputs → Outputs
- **In:** `username` or `name` (+ city/year to disambiguate)
- **Out:** OK.ru `social-profile`, display `name`, city context
- **Empty/negative result looks like:** no `site:ok.ru` hits — the person may be login-gated, use Cyrillic naming, or not be on OK.ru. Search Cyrillic forms and cross-check VK.

## Gotchas & OpSec
- Transliteration matters — search both Latin and Cyrillic name forms.
- OK.ru's login wall is aggressive; logged-out you may only see indexed snippets.
- OpSec: passive against the target. Use a sock-puppet account, never a real one, for deeper access.

## Overlaps ("do both")
- Pairs with `[[google-com-74]]` (vk.com) — a subject present on one Russian network is often on the other. Also pairs with reverse-image search on the profile photo to confirm identity across both.

## Trust & verifiability
`trust: community` — a technique reflecting Google's index of OK.ru, not authoritative. Confirm a match by photo, city, and cross-network overlap.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-75 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
