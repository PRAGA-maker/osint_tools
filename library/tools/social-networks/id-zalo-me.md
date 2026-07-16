---
id: id-zalo-me
name: id.zalo.me
description: Use when you have a Vietnamese `phone` number and want to confirm it maps to a Zalo account — returns the linked `social-profile`, display `name`, and avatar `image`.
url: https://id.zalo.me/account?continue=https%3A%2F%2Fchat.zalo.me%2F
category: social-networks
path:
- social-networks
bestFor: Confirming a (usually Vietnamese) phone number belongs to a Zalo user and pulling the display name/avatar.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Zalo and its account/lookup features are free; a Zalo account (and the mobile app for QR login) is required.
opsec: active
opsecNote: id.zalo.me itself is only the login gateway. The actual phone→account lookup happens inside Zalo (add-by-phone / find-friend), which is ACTIVE — adding or viewing a target can surface you to them and may send a contact/friend signal. Use a dedicated sock-puppet Zalo account and burner device/number, never your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Zalo (VNG Corporation) endpoint; the account-existence and profile data come from the platform itself, not a scraper.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- checkwa
- telegram-phone-number-checker
- zalo-me
aliases:
- Zalo account
- Zalo login
- chat.zalo.me
tags:
- gsocialmedia
- General Social Media Sites
- vietnam
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# id.zalo.me

> The login gateway to Zalo — Vietnam's dominant messaging app — used as a bridge to Zalo's in-app phone→account lookup, which confirms a number belongs to a real user and returns their name and avatar.

## When to use
Your subject is Vietnamese or Vietnam-linked and you have a `phone` number (or a Zalo `username`). Zalo has ~75M+ users and is the default messenger in Vietnam, so an account often exists where WhatsApp/Telegram would not. Use it to confirm the number is live on Zalo and to grab the display `name` and avatar `image` for corroboration and cross-referencing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Understand that `id.zalo.me` itself is just the sign-in page — it does no lookup on its own. Log in by scanning its QR code with the Zalo mobile app (on your **sock-puppet** account/device).
2. Once into Zalo Web (chat.zalo.me) or the app, use **Add friend / Find friend by phone number** and enter the target `phone`.
3. If an account exists, Zalo shows the display `name` and avatar `image`; if not, it reports no user found.
4. Do NOT send a friend request or message — stop at the profile preview to stay as passive as the platform allows.
5. Pivot: the display name and avatar feed reverse-image search and name-based people-search; cross-check the same number on `[[checkwa]]` (WhatsApp) and `[[telegram-phone-number-checker]]`.

## Inputs → Outputs
- **In:** `phone` (Vietnamese numbers most productive) or a Zalo `username`
- **Out:** `social-profile` existence, display `name`, avatar `image`
- **Empty/negative result looks like:** "no user found" for the number — the person may simply not use Zalo, or have restricted phone-based discovery in privacy settings.

## Gotchas & OpSec
- Human-in-the-loop: requires a Zalo **account login** (QR scan from the app) before any lookup is possible.
- OpSec: **active** — in-app lookup can generate a contact/friend signal and you may appear in "people you may know". Always use a burner account, burner number, and separate device; never your real identity.
- Privacy settings let users hide themselves from phone-number discovery, so a negative is not conclusive.
- The interface is Vietnamese-first; expect to navigate localized labels.

## Overlaps ("do both")
- Pairs with `[[checkwa]]` and `[[telegram-phone-number-checker]]` — run the same `phone` across WhatsApp, Telegram, and Zalo, since a Vietnamese subject is far likelier to be on Zalo.

## Trust & verifiability
`trust: trusted` — Zalo is a first-party platform (VNG), so existence and profile data are authoritative. The caveat is operational, not data-quality: reaching the lookup requires logging in, which is why this is gated and active rather than a clean passive oracle.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | id-zalo-me |
| category | social-networks |
| selectorsIn → selectorsOut | phone, username → social-profile, name, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
