---
id: google-com-74
name: Google site-search — VK (vk.com)
description: Use when you have a `username` or `name` and want to find a subject's VKontakte (VK) profile without a VK account — returns a `social-profile`.
url: https://www.google.com/search?q=site%3Avk.com&ie=utf-8&oe=utf-8&client=firefox-b-ab
category: social-networks
path:
- social-networks
bestFor: Dorking VK (Russia's largest social network) via Google's site: operator to surface profiles and posts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Google `site:` dork; no VK or Google account required to read indexed public pages. (VK itself gates some content behind login.)
opsec: passive
opsecNote: The search runs against Google, not VK, so the subject is not alerted. Opening a public VK profile logged-out is passive; VK aggressively pushes login walls — do not register an attributable VK account, use a sock puppet if you must go deeper.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A search-engine technique over VK's public pages, not a product; coverage depends on Google's index of vk.com and VK's login-gating.
missingPersonsRelevance: high
coverage:
- ru
- global
aliases:
- VK site search
- site:vk.com
- vkontakte dork
tags:
- russiansocialmedia
- Russian Social Media Sites
- google-dork
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Google site-search — VK (vk.com)

> A Google `site:vk.com` dork for VKontakte — Russia's dominant social network — to find profiles from the outside without touching VK's login wall.

## When to use
You have a `username` or `name` and a Russian, Ukrainian, or ex-Soviet-region lead, or a handle that reuses across platforms. VK holds enormous personal footprint (photos, friends, locations, groups). Dorking it via Google surfaces public profiles without logging into VK, which is valuable because VK increasingly walls content behind an account.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the URL, or in Google, scope to VK and add your selector:
   - `site:vk.com "First Last"` / `site:vk.com <username>`
   - add a city, school, or birth year to disambiguate.
2. Read results: profile URLs (`vk.com/id123...` or `vk.com/<handle>`), display `name`, city, and snippet content.
3. Open a public profile logged-out to review photos, friends, and wall.
4. Pivot: a VK handle feeds username-reuse checks (people often reuse VK handles), reverse-image on profile photos, and friend-network mapping.

## Inputs → Outputs
- **In:** `username` or `name` (+ city/school/year to disambiguate)
- **Out:** VK `social-profile`, display `name`, city and network context
- **Empty/negative result looks like:** no `site:vk.com` hits — the person may have a login-gated or deleted profile, use Cyrillic name spelling, or not be on VK. Try the name in Cyrillic and VK's own search from a sock puppet.

## Gotchas & OpSec
- Name transliteration matters: search both Latin and Cyrillic forms of the name.
- VK login walls hide much from logged-out users; indexed snippets may be all you get without an account.
- OpSec: passive against the target via Google. Use a sock-puppet VK account, never a real one, for deeper viewing.

## Overlaps ("do both")
- Pairs with `[[google-com-75]]` (ok.ru) and other Russian-network dorks — the same person often appears on both VK and Odnoklassniki. Also pairs with reverse-image search on the VK avatar to confirm identity.

## Trust & verifiability
`trust: community` — a technique reflecting Google's index of VK, not an authoritative source. Confirm a match by photo, city, and network overlap before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-74 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
