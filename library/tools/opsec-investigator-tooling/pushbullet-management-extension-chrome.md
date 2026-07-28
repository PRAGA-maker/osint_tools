---
id: pushbullet-management-extension-chrome
name: Pushbullet Management Extension (Chrome)
description: Use when you need a burner `phone`'s SMS and notifications mirrored to your investigation desktop — returns 2FA codes and app alerts on-screen, no selectors extracted.
url: https://chromewebstore.google.com/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Mirroring a sock-puppet Android phone's SMS and notifications to the desktop so you can receive 2FA/verification codes without touching the burner device.
selectorsIn:
- phone
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier covers device mirroring and SMS; Pushbullet Pro (paid) lifts limits on SMS and file size. A Pushbullet account (Google/Facebook/email) is required to link devices.
opsec: passive
opsecNote: This is investigator-side tooling — it doesn't touch any target. The real OpSec concern is your own: linking a sock-puppet phone routes its SMS/notifications (including 2FA codes) through Pushbullet's cloud and your Google-linked browser profile. Use a dedicated sock-puppet Google account and burner device; never link a real personal phone.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Popular, long-standing extension (~300k users, 4.5★) but a third party that would proxy your SMS/notifications through its servers — trust it only with throwaway accounts and non-sensitive burner devices.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Pushbullet Chrome extension
- Pushbullet
tags:
- sock-puppet-tooling
- device-sync
- sms-mirroring
source: toddington-resources
lastVerified: '2026-07-28'
enrichment: full
---

# Pushbullet Management Extension (Chrome)

> A device-bridge extension that mirrors an Android phone's SMS and notifications onto your desktop browser — handy for pulling 2FA codes off a burner phone without picking it up.

## When to use
You maintain sock-puppet accounts and a burner Android phone, and you want its SMS and app notifications to appear on the investigation workstation — so you can read verification/2FA codes, DMs, and alerts from one screen instead of juggling the physical device. This is pure investigator-workflow/OpSec tooling: it extracts no data about any subject and returns no selectors. Include it for sock-puppet hygiene, not as a lookup.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store link above (works in Chrome/Edge).
2. Sign in to Pushbullet with a dedicated sock-puppet account (Google/email) — this is the account-login gate.
3. Install the Pushbullet Android app on your burner `phone` and sign in with the same account to pair them.
4. Enable SMS sync and notification mirroring in the app; incoming texts and alerts now surface in the browser.
5. Use it to read verification codes and messages for your sock-puppet accounts from the desktop.

## Inputs → Outputs
- **In:** `phone` (your own burner device you pair)
- **Out:** none — it relays SMS/notifications to your screen; it does not produce investigative selectors
- **Empty/negative result looks like:** notifications not appearing — usually the phone isn't paired, notification-mirroring permission is off, or the phone is offline.

## Gotchas & OpSec
- Human-in-the-loop: requires creating/logging into a Pushbullet account and pairing a device.
- Your SMS and notifications transit Pushbullet's cloud — treat the linked account and phone as disposable; never mirror a real personal number.
- Freemium: the free tier caps SMS/file features; heavy use needs Pushbullet Pro.
- Not an OSINT data source — no target is queried and nothing is extracted about others.

## Overlaps ("do both")
- Complements sock-puppet-account setup: pair it with a dedicated burner phone and throwaway Google account as part of your identity-management hygiene rather than as an investigative lookup.

## Trust & verifiability
`trust: unverified` — a widely used, reputable consumer extension, but it proxies your messages through a third party; safe only when confined to disposable accounts and devices, and it yields no investigative output to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pushbullet-management-extension-chrome |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | phone → — |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
