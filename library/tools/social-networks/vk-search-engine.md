---
id: vk-search-engine
name: VK Search Engine
description: Use when you have a `name`/`username` and want to search VKontakte (VK) profiles and content via a pre-scoped Google Custom Search Engine — returns social-profile, name.
url: https://cse.google.com/cse?cx=f5e7cd4c6e33954ec
category: social-networks
path:
- social-networks
bestFor: Finding VK (VKontakte) profiles and posts for a name/handle via a VK-scoped Google CSE.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free browser widget; a Google Custom Search Engine scoped to vk.com. No account for the widget.
opsec: passive
opsecNote: Queries hit Google (not VK directly), so it's passive and the target isn't notified. Opening the VK profiles it surfaces does touch VK — use a sock-puppet browser and stay logged out of VK. Note VK is Russian-operated; treat all interaction accordingly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Google runs the engine, but the vk.com scope is defined by an unknown third party's `cx` config and Google's index of VK is partial and can lag — coverage is unverifiable and drifts.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- VK Google CSE
- VKontakte search
tags:
- vk
- vkontakte
- google-cse
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# VK Search Engine

> A Google Custom Search Engine scoped to VKontakte (vk.com) — search VK for a name or handle without VK's own (login-gated, patchy) search getting in the way.

## When to use
You have a `name` or `username` and want VK profiles/posts for the subject — useful when the target has a Russian/CIS or Eastern-European connection, since VK is dominant there. A VK-scoped CSE lets you Google-search VK's indexed content without logging into VK, which is handy because VK's native search is limited to logged-in users.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL (https://cse.google.com/cse?cx=f5e7cd4c6e33954ec) in a sock-puppet browser.
2. Enter the subject `name` (quoted, try transliterations/Cyrillic) or `username`.
3. Review results — Google hits restricted to vk.com: profiles, wall posts, communities.
4. Open promising profiles for confirmation (bio, photos, friends), staying logged out of VK.
5. Pivot: a confirmed VK `social-profile` feeds VK-specific tools and username enumeration; friends/photos feed relationship and image OSINT.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (VK profiles/communities), `name`
- **Empty/negative result looks like:** no results or off-target hits — often because Google's VK index is partial or the CSE config drifted, not proof the person isn't on VK; try native VK search (logged-in) or transliterated spellings.

## Gotchas & OpSec
- Only searches Google's index of vk.com, which is incomplete — much VK content isn't indexed; a miss here is not conclusive.
- Try Cyrillic and transliterated name variants; VK is Russian-language-heavy.
- OpSec: the CSE query is passive; opening VK profiles touches a Russian-operated platform — use a throwaway session.

## Overlaps ("do both")
- Pairs with native VK search and VK-specific OSINT tools, and with [[google-custom-search-2]] for cross-platform breadth — run the scoped CSE and native VK, then reconcile.

## Trust & verifiability
`trust: community` — Google's engine over an opaque third-party VK scope; results are real VK pages, but coverage is partial and unverifiable, so absence proves nothing.
