---
id: lotus-vn
name: Lotus.vn
description: Use when you have a `username` or `name` and think the subject uses Lotus, a Vietnamese social network — returns `social-profile`, `name`, posts (app-centric, limited web view).
url: https://lotus.vn/w
category: social-networks
path:
- social-networks
bestFor: Checking for a subject's profile/posts on Lotus, a Vietnamese social network.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free to use, but the platform is app-centric — the web view is limited and registering an account requires the mobile app.
opsec: passive
opsecNote: Viewing whatever is public on the web is passive. Deeper access needs the mobile app and an account, which ties a (sock-puppet) identity to your activity; installing/registering exposes device/phone details, so use a burner setup.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: A real Vietnamese social platform (VIVA), but with limited public web access and unclear reach; profile content is user-supplied.
missingPersonsRelevance: high
coverage:
- vn
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lotus Vietnam
- lotus.vn
tags:
- gsocialmedia
- General Social Media Sites
- vietnam
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Lotus.vn

> A Vietnamese social network (operated by VIVA): a place a Vietnam-based subject may have a profile — but it's app-centric, so public web visibility is limited.

## When to use
You have a `username` or `name` and the subject is Vietnamese or Vietnam-based. Lotus is a domestic social platform, so it can hold a profile and posts that Western platforms don't — worth checking when building a subject's footprint in Vietnam. Temper expectations: full access is through the mobile app, and the browser view exposes comparatively little.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Try the web view at https://lotus.vn/w and search the `username`/`name` for anything publicly readable (feeds, trends, groups).
2. For real access, install the Lotus app (iOS/Android) and register — use a **sock-puppet** identity on a burner device/number.
3. Search for the subject; open any profile for posts, bio, and network.
4. Capture posts/media and note mentioned locations, dates and associates.
5. Pivot: reverse-image any avatar/media, match the handle on other platforms, and correlate with Vietnamese records.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (posts, bio where visible), `name`
- **Empty/negative result looks like:** nothing on the web view, or a login/app wall — the subject isn't on Lotus, uses a different handle, or the content simply isn't web-exposed; app access may be needed to confirm.

## Gotchas & OpSec
- **App-centric** — the web view is limited; meaningful search often requires the app and an account.
- Registering needs a phone/device — use a burner, never personal details.
- Vietnamese-language UI; use name/handle variants and Vietnamese diacritics.
- Platform reach/longevity is uncertain — don't assume broad coverage.

## Overlaps ("do both")
- Pairs with mainstream platforms (Facebook/Zalo are dominant in Vietnam) — check those first; Lotus is a supplementary domestic angle.

## Trust & verifiability
`trust: unverified` — a real but limited-visibility domestic platform; any profile content is user-supplied, so corroborate identity via avatar/handle across sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lotus-vn |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
