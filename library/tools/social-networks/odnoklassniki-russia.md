---
id: odnoklassniki-russia
name: Odnoklassniki (Russia)
url: http://ok.ru
category: social-networks
path:
- social-networks
description: Use when you have a `name` or `username` of a Russian/CIS subject and want their social profile — returns a `social-profile` with photos, connections and life details.
bestFor: Finding a Russian/CIS person's social presence — especially older users and reconnected classmates/family — on one of Russia's largest networks.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
- name
status: live
pricing: free
costNote: Free to use; much profile detail (and search) is gated behind a free account, and viewing others is easier when signed in.
opsec: active
opsecNote: Logged-out visibility is limited, so real use usually means signing in — which is active, ties activity to an account, and OK.ru (VK-group, Russian jurisdiction) logs it; profile visitors can sometimes be seen by the owner. Use a burner account, never your real one, and assume Russian data-law exposure.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: A genuine, major Russian social network (part of the VK group); the platform is authentic, though individual accounts may be fake/impersonators and content is subject to heavy Russian moderation/surveillance.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OK.ru
- Odnoklassniki
- Одноклассники
tags:
- major-social-networks
- russian-social
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Odnoklassniki (Russia)

> OK.ru — one of Russia's largest social networks ("Classmates"), strong for older Russian/CIS users and family/classmate reconnection, a key place to look when a subject has a Russian footprint.

## When to use
You have a `name` or `username` for someone in Russia or the CIS (or a diaspora member) and want their social presence. Odnoklassniki skews older and family-oriented and is built around reconnecting classmates and relatives, so it often surfaces family links, hometowns, schools and photos that Western networks miss. Essential for Russian/CIS traces alongside VK.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in with a **burner** OK.ru account (logged-out access is heavily limited).
2. Search the `name` (Cyrillic and transliterated) or handle; filter by city, age, school where offered.
3. Open the profile: photos, city/hometown, school/graduation year, friends and family links.
4. Note schools/graduation years — the network's classmate structure is a strong `associate` source.
5. Pivot: friends/family feed `associate` mapping; photos feed reverse-image/face search; a reused handle feeds cross-platform enumeration and VK.

## Inputs → Outputs
- **In:** `name` (Cyrillic/transliterated) or `username`
- **Out:** `social-profile` (photos, city, school), `associate` (friends/family/classmates), real `name`
- **Empty/negative result looks like:** no match or lookalikes — try Cyrillic spelling, maiden names, and city filters before concluding. Absence may just mean the subject uses VK or a different name variant.

## Gotchas & OpSec
- Search names in Cyrillic and transliteration; common names need city/school/age to disambiguate.
- Impersonation and fake accounts exist; corroborate via cross-links and photos.
- OpSec: **active** — you generally must sign in; use a burner, expect the visit to be logged, and be aware of Russian data-law/surveillance exposure.

## Overlaps ("do both")
- Pairs with VK and `[[username-search-tool]]` — OK.ru and VK cover overlapping but different Russian/CIS populations (OK skews older/family); check both plus handle reuse.

## Trust & verifiability
`trust: trusted` — a genuine major platform, so profiles are real accounts; treat individual account *contents* as self-published and potentially impersonated, and factor in heavy moderation of what's visible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | odnoklassniki-russia |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
