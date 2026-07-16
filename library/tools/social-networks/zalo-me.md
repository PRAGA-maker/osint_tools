---
id: zalo-me
name: Zalo (zalo.me)
description: Use when you have a Vietnamese `phone` number or `name` and want to check for a Zalo messaging account and its public profile — returns a social profile, display name and profile photo.
url: https://zalo.me/pc
category: social-networks
path:
- social-networks
bestFor: Confirming a Vietnamese phone number maps to a live Zalo account and pulling its display name / avatar.
selectorsIn:
- phone
- name
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free consumer messaging app; you need your own Zalo account to search or view profiles.
opsec: active
opsecNote: Zalo primarily resolves people by phone number, and adding/searching a contact happens from YOUR logged-in account — the target may see a friend request or that someone viewed them. Use a sock-puppet Zalo account on a burner number; do not search from a real investigator account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Operated by VNG Corporation, Vietnam's dominant messaging platform; this is the genuine first-party service, not a scraper.
missingPersonsRelevance: high
coverage:
- vn
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Zalo
- VNG Zalo
tags:
- gsocialmedia
- General Social Media Sites
- vietnam
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- id-zalo-me
---

# Zalo (zalo.me)

> Vietnam's dominant messaging app (VNG) — a phone-number-keyed social graph that is often the single best way to place a subject connected to Vietnam.

## When to use
The subject has a Vietnamese `phone` number (or a Vietnamese `name`) and you want to know whether they use Zalo — which in Vietnam is near-universal, so a hit strongly corroborates the number is active and personal. Zalo resolves an account from a phone number and exposes a public display name and avatar, and sometimes a small public feed. Reach for it when investigating anyone with a `.vn` footprint or a `+84` number.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Zalo (mobile) or open https://zalo.me/pc for the desktop/web client, signed into a **sock-puppet** Zalo account on a burner number.
2. Use "Add friend" / search and enter the target `phone` number (in `+84` international form), or search by `name`.
3. If an account exists, Zalo shows the display `name` and profile `image`; open the profile for any public info.
4. STOP before sending a friend request or message — that alerts the target.
5. Pivot: the display name/photo corroborates identity; the avatar feeds `[[pimeyes]]`-style face search, and the confirmed number feeds other phone-OSINT.

## Inputs → Outputs
- **In:** `phone` (Vietnamese/`+84`) or `name`
- **Out:** `social-profile` (Zalo account), display `name`, profile `image`
- **Empty/negative result looks like:** "no user found" for that number — the number is not on Zalo (unusual in Vietnam, so weakly suggests a non-VN or inactive number), or the account is set to not be discoverable by phone.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in Zalo account; searching is done from your session.
- Discoverability settings: users can hide themselves from phone-number search, so a miss is not proof of absence.
- OpSec: **active** — never send a friend request/message; use a burner-number sock puppet and expect the target could notice profile views in some configurations.

## Overlaps ("do both")
- Pairs with `[[pimeyes]]` — Zalo yields the avatar, PimEyes matches that face elsewhere.
- Pairs with phone-intel tools — cross-check the same `+84` number against Truecaller-style directories to corroborate the name.

## Trust & verifiability
`trust: trusted` — first-party VNG/Zalo service; the account-existence and profile data are authoritative (subject to the user's own privacy settings).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zalo-me |
