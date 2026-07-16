---
id: line-me
name: line.me
description: Use when you have a `phone` number or LINE ID (`username`) for a subject likely in Japan/Taiwan/Thailand and want to confirm a LINE account and its display profile — returns a `social-profile` (display name, photo, status).
url: https://line.me/en/
category: messaging
path:
- messaging
bestFor: Confirming a LINE account and reading its public display profile from a phone number or LINE ID, especially in East/Southeast Asia.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The LINE app is free; you need a LINE account (which itself requires a phone number to register) to search or add contacts.
opsec: active
opsecNote: Adding a subject by phone/ID, or enabling "add by phone number," can surface you to them or push a contact notification — and LINE may show mutual-contact hints. Operate only from a dedicated sock-puppet account on a separate device/number; never from a personal LINE. Stop at viewing the public display profile; do not message the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: Official LINE service. The display name/photo are user-set and often not a real identity, so treat the profile as a lead requiring corroboration.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- LINE
- line messenger
tags:
- messengerapps
- Messenger Apps
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- line
- line-play
---

# line.me

> The official LINE messenger — dominant in Japan, Taiwan, and Thailand — used in OSINT to confirm an account and read its display profile from a phone number or LINE ID.

## When to use
Your subject is likely in Japan, Taiwan, Thailand, or the broader East/Southeast Asian region and you have a `phone` number or a LINE ID (`username`). LINE is the primary messenger there, so confirming they have an account — and capturing the display name, photo, and status message — corroborates the number/handle and yields an avatar for reverse-image work.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install LINE and set up a dedicated sock-puppet account on a separate device and phone number (registration requires a number).
2. To check a `phone`: add it as a contact / use "add by phone number" (requires the target to permit phone-number adds). To check a LINE ID: use "Add by ID / QR" and search the `username`.
3. If an account exists, view the public display profile: display name, profile photo, status message, cover image.
4. Capture the avatar and name; do **not** send a message or otherwise contact the subject.
5. Pivot: profile photo → reverse-image (`[[yandex-images]]`, `[[pimeyes]]`); display name/ID → username OSINT across platforms.

## Inputs → Outputs
- **In:** `phone` or LINE ID (`username`)
- **Out:** `social-profile` — display name, profile/cover photo, status message
- **Empty/negative result looks like:** "no account found," or a number that can't be added because the owner disabled phone-number adds — the latter does NOT prove there's no account, only that discovery is off. Display fields may be blank or generic.

## Gotchas & OpSec
- Registration requires a phone number and the app; there is no clean web-search path. Plan the sock-puppet and separate number in advance.
- Adding-by-phone can notify the target and expose your sock account — the biggest operational risk here.
- Display name/photo are freely set and frequently non-identifying; corroborate before attributing.

## Overlaps ("do both")
- Pairs with `[[whatsapp]]`/`[[telegram]]` profile checks and phone-OSINT — different messengers reveal different avatars/names for the same number, so check each; a photo from one feeds reverse-image against the others.

## Trust & verifiability
`trust: trusted` — the account-existence and display data come straight from the official LINE platform; the *content* of the display profile is user-set and must be corroborated for identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | line-me |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
