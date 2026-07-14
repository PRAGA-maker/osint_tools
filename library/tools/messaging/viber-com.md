---
id: viber-com
name: viber.com
description: Use when you have a `phone` number and want to check whether it is registered on Viber — returns the account's public display name and profile photo (a social-profile / image confirmation).
url: https://www.viber.com/
category: messaging
path:
- messaging
bestFor: Confirming a phone number is on Viber and capturing its public display name and avatar.
selectorsIn:
- phone
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free app; you need a Viber account (tied to your own number) to perform contact lookups.
opsec: active
opsecNote: To check a number you add it as a contact in the Viber app running on YOUR account — this can expose your account to the target (e.g. if they later see you, or via mutual-contact features) and, depending on settings, may surface you to them. Use a dedicated sock-puppet Viber account on a burner number, never your personal one. Do NOT message the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Viber is a legitimate, widely-used messaging platform (Rakuten). The account-existence + display-name/photo signal is genuine first-party data, though users can hide their photo/name.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- whatsapp-web
- account-live-com
aliases:
- Viber
tags:
- messengerapps
- Messenger Apps
- account-existence
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# viber.com

> The Viber messenger used as an account-existence oracle: does this phone number have a Viber account, and what public name/photo does it show?

## When to use
You have a `phone` number and want to confirm it belongs to a real, active user and attach a face/name to it. Adding the number as a contact in Viber reveals whether it's registered and, if the user hasn't hidden them, their display `name` and profile `image` — a strong corroboration that a number is live and tied to a specific identity, and a possible photo for reverse-image search.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Viber on a device signed into a **sock-puppet** account (burner number), not your personal account.
2. Save the target `phone` number to the device's contacts.
3. Open Viber → contacts; if the number is on Viber it appears with its display name and, if public, profile photo.
4. STOP at the existence/photo check — do not call or message the target. Pivot: run the profile photo through reverse-image/face search; cross-check the number on other messengers like `[[whatsapp-web]]`.

## Inputs → Outputs
- **In:** `phone`
- **Out:** account-exists boolean, public display `name`, profile `image`/`social-profile`
- **Empty/negative result looks like:** the number doesn't appear as a Viber contact — not registered, or registered under privacy settings that hide it; absence isn't proof the person has no Viber.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you must operate from a Viber account.
- OpSec: **active** — adding a contact can create a footprint; always use a burner account/number and never initiate contact.
- Users can hide name/photo, so a "registered but blank" result is common; treat a hidden profile as still-confirms-existence.

## Overlaps ("do both")
- Pairs with `[[whatsapp-web]]` (same phone→profile check on another platform — run both, since a number may be on one and not the other) and `[[account-live-com]]` (email/phone existence on Microsoft).

## Trust & verifiability
`trust: trusted` — Viber is a legitimate first-party platform, so an existence hit and any shown name/photo are authentic. Corroborate the photo/name independently before attributing identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | viber-com |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile, name, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
