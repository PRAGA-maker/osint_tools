---
id: web-botim-me
name: web.botim.me (BOTIM)
description: Use when you have a `phone` number likely used in the UAE/Gulf and want to check whether it's on BOTIM and pull the profile photo/name — a popular Gulf VoIP/messaging app, returning social-profile presence.
url: https://web.botim.me/#/
category: messaging
path:
- messaging
bestFor: Confirming a phone number's presence on BOTIM (widely used in the UAE/Gulf) and capturing its profile photo and display name.
selectorsIn:
- phone
selectorsOut:
- social-profile
- image
- name
status: degraded
pricing: free
costNote: Free app/service. The web endpoint now centers on BOTIM Meet (video meetings/login); the contact-registration check is done in the mobile app, which is the practical OSINT surface.
opsec: active
opsecNote: Active — adding a target number to your contacts to check BOTIM presence is a query against the platform, and depending on settings the target may see a contact/"joined" signal. Use a dedicated sock account and burner number; do not initiate calls or messages.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: BOTIM is a genuine, widely used Gulf-region messaging/VoIP app. The number-check technique mirrors WhatsApp-style contact syncing; profile visibility depends on the target's privacy settings.
missingPersonsRelevance: high
coverage:
- ae
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- BOTIM
- botim.me
tags:
- messengerapps
- Messenger Apps
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# web.botim.me (BOTIM)

> BOTIM — a VoIP/messaging app hugely popular in the UAE and wider Gulf — used as a number-presence oracle: is this phone number on BOTIM, and what profile photo/name does it show?

## When to use
Your subject is tied to the UAE or Gulf region (where WhatsApp/Skype voice calling has been restricted and BOTIM is a dominant alternative) and you have a `phone` number. Checking BOTIM tells you whether the number is active on that app and, subject to the owner's privacy settings, exposes a profile photo, display name, and sometimes a last-seen/status — strong corroboration of an active number and a face/name lead. This is often the *right* messenger to check for Gulf numbers, where mainstream apps under-perform.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install BOTIM on a **sock** device/account with a burner number (the web endpoint at web.botim.me is now meeting-focused; the contact check is an app function).
2. Save the target `phone` number to the sock device's contacts.
3. Open BOTIM's contacts/new-chat view and see whether the number appears as a BOTIM user.
4. Read the output: if present, capture the profile `image`, display `name`, and any status (`social-profile`). If absent, the number isn't on BOTIM (or is hidden).
5. Pivot: the profile photo feeds reverse-image/face tools; the display name feeds name searches; presence corroborates the number is live and Gulf-linked.

## Inputs → Outputs
- **In:** `phone` (likely UAE/Gulf number)
- **Out:** `social-profile` (BOTIM presence/status), `image` (profile photo), `name` (display name)
- **Empty/negative result looks like:** the number doesn't surface as a BOTIM user — either it's not registered or the owner restricts discovery. Not proof the number is inactive elsewhere.

## Gotchas & OpSec
- Profile photo/name visibility depends on the target's privacy settings — many show nothing to non-contacts.
- Human-in-the-loop: requires a real app install, a sock account, and a burner number.
- OpSec: **active** — contact-syncing a number is a platform query; a "X joined" or contact signal can reach the target. Use a burner; never call or message.

## Overlaps ("do both")
- Pairs with WhatsApp/Telegram number checks — for Gulf numbers BOTIM often shows a profile where mainstream apps show nothing. Run BOTIM alongside them rather than instead of.

## Trust & verifiability
`trust: community` — BOTIM is a legitimate, widely used app; the presence signal is genuine, but what you can see is gated by the target's privacy settings, so treat a blank profile as "hidden," not "absent."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-botim-me |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile, image, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
