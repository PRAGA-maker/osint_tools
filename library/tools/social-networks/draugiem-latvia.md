---
id: draugiem-latvia
name: Draugiem (Latvia)
description: Use when you have a `name` or `username` of a Latvian subject and want their social profile — returns a Draugiem.lv profile (photos, friends, activity) on Latvia's main homegrown social network.
url: https://www.draugiem.lv
category: social-networks
path:
- social-networks
bestFor: Finding and profiling Latvian subjects on Draugiem.lv, the dominant local social network.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
- image
status: live
pricing: free
costNote: Free to use; searching profiles requires a (free) registered account.
opsec: active
opsecNote: Viewing profiles requires logging in, and Draugiem — like many social networks — can show profile owners who viewed them or surface you in "people you may know." Use a dedicated sock-puppet account with a plausible Latvian persona, never a personal one. Registration ties activity to that account, so keep it clean and separate.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Draugiem.lv is a long-established (since 2004), operational Latvian social network run by SIA Draugiem. Profiles are user-generated, so content is authentic but self-curated and possibly aliased.
missingPersonsRelevance: high
coverage:
- lv
auth: account
api: false
localInstall: false
registration: true
aliases:
- Draugiem.lv
- Draugiem
tags:
- major-social-networks
- latvia
- regional-social-network
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Draugiem (Latvia)

> Latvia's dominant homegrown social network (since 2004) — the first place to look for a Latvian subject's social footprint, friends and photos.

## When to use
You have a `name` or `username` for a subject with a Latvian connection and the mainstream networks (Facebook/Instagram) are thin. Draugiem.lv has deep penetration in Latvia, so a subject who's sparse elsewhere may have an active profile here — with photos, friends (`associate`s), groups and activity that anchor identity, relationships and locality.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a sock-puppet Draugiem account (registration is required to search/view).
2. Log in from a clean browser/persona and search by `name` or `username`.
3. Open matching profiles; note photos, friend list, groups, hometown/locality and activity.
4. Corroborate identity via photos and mutual connections before relying on a match.
5. Pivot: friends are `associate` leads; profile photos feed reverse-image/face tools; a Draugiem `username` can be searched across other platforms.

## Inputs → Outputs
- **In:** `name` or `username` (Latvian subject)
- **Out:** Draugiem `social-profile`, friends/`associate`s, `image`s, locality/activity
- **Empty/negative result looks like:** no profile — the subject isn't on Draugiem, uses a different name/handle, or has a locked profile. Latvian-diaspora subjects may be on Facebook instead; absence here isn't conclusive.

## Gotchas & OpSec
- **Login required** and the platform is Latvian-language — use a plausible sock-puppet and translation.
- Viewing can expose you to the profile owner (view lists / suggestions) — never use a personal account.
- Common Latvian names need photo/mutual-friend corroboration to disambiguate.

## Overlaps ("do both")
- Pairs with Facebook/Instagram search and username enumerators — Draugiem covers Latvian subjects the global networks miss, while those cover diaspora and cross-platform handles.

## Trust & verifiability
`trust: community` — an established, operational regional network; profiles are authentic user content but self-curated, so verify identity via images and connections.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | draugiem-latvia |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
