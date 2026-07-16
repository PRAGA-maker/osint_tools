---
id: botim-me
name: BOTIM
description: Use when you have a `phone` number (often Gulf/Middle-East) and want to check whether it has a BOTIM messaging account and see any public profile name/photo — returns social-profile, name and image.
url: https://botim.me/
category: messaging
path:
- messaging
bestFor: Checking whether a phone number is registered on the BOTIM VoIP/messaging app (popular in the UAE/Gulf).
selectorsIn:
- phone
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: The BOTIM app is free to install and use for basic messaging; some premium calling features are paid, but the account-existence check needs only the free app.
opsec: active
opsecNote: To check a number you add it as a contact in the BOTIM app on a device logged into an account — the app then shows whether that number has BOTIM. Adding a contact / any interaction can be visible to the other party and ties the check to the account you use. Use a dedicated sock-puppet account and burner device/SIM, and do not initiate a call or message.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: community
trustNote: BOTIM is a mainstream commercial messaging app (widely used where WhatsApp/Skype calling is restricted); the existence/profile signal is as reliable as the user's own privacy settings allow.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- Botim
- botim.me
tags:
- messengerapps
- Messenger Apps
- voip
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- web-botim-me
---

# BOTIM

> A mainstream VoIP/messaging app (big in the UAE and wider Gulf) — used as a presence oracle: does this phone number have a BOTIM account, and what does its public profile show?

## When to use
You have a `phone` number, especially one in the UAE/Gulf region where BOTIM is a default calling app (WhatsApp/Skype voice being restricted there), and you want to confirm the number is active and tied to a person. Registering the number as a contact reveals whether it has BOTIM and, subject to the owner's privacy settings, a display `name` and profile `image` — corroborating that the line is real, in use, and possibly attaching a face/name.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install BOTIM on a burner device and register a **sock-puppet** account (registration/login required).
2. Add the target `phone` number to the device's contacts and let BOTIM sync contacts.
3. Check whether the number surfaces as a BOTIM user; if so, view the available public profile — display name and photo.
4. STOP at the existence/profile check — do **not** call or message the number.
5. Pivot: a profile photo feeds reverse-image/face; a display name feeds people-search; presence on BOTIM (a regional app) is itself a geographic/identity clue.

## Inputs → Outputs
- **In:** `phone`
- **Out:** BOTIM account exists (`social-profile`), display `name`, profile `image` (privacy-permitting)
- **Empty/negative result looks like:** the number doesn't appear as a BOTIM user — they may not use BOTIM (common outside the Gulf) or have strict privacy; not proof the number is inactive.

## Gotchas & OpSec
- **Active:** the check is done from a real logged-in app account; adding a contact and any interaction can expose your sock-puppet to the target — use a burner account/device and never call or text.
- Profile name/photo visibility depends entirely on the owner's privacy settings.
- Strongest signal in the UAE/Gulf; elsewhere adoption is low, so a null result is weak evidence.

## Overlaps ("do both")
- Pairs with WhatsApp/Telegram/Signal presence checks and `[[freecarrierlookup]]` — run the same number across several messaging apps; each app the number is on adds a profile photo/name and narrows region and platform habits.

## Trust & verifiability
`trust: community` — a legitimate mainstream app. The presence signal is reliable; the amount of profile detail depends on privacy settings, and adoption is regional, so weigh a negative result by geography.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | botim-me |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
