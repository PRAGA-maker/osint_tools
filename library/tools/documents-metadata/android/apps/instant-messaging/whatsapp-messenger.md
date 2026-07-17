---
id: whatsapp-messenger
name: WhatsApp Messenger
description: Use when you have a `phone` number and want to confirm it has an active WhatsApp account and pull its public profile — returns `image` (photo), `physical-description`, and status text.
url: https://www.whatsapp.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Confirming a phone number is a live WhatsApp account and capturing its public profile photo, About text, and (sometimes) online/last-seen signals.
selectorsIn:
- phone
selectorsOut:
- image
- physical-description
- social-profile
status: live
pricing: free
costNote: Free app; you need your own WhatsApp account (a burner SIM/number is standard tradecraft).
opsec: active
opsecNote: To view a number's profile you save it as a contact — that itself is silent, but do NOT message, call, or add the number to a group, which would alert the owner. Repeated viewing or a persona that gets reported risks a ban. Use a dedicated sock-puppet number/device, never your personal WhatsApp.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: First-party Meta/WhatsApp app; the existence and public-profile signals come straight from the platform (authoritative), though privacy settings gate what's visible.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- WhatsApp
- WhatsApp number check
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# WhatsApp Messenger

> The WhatsApp app itself, used as an account-existence and profile oracle: does this phone number have WhatsApp, and what does its public profile show?

## When to use
You have a `phone` number and want to (a) confirm it is a real, active line with WhatsApp registered — strong evidence the number is current and in use — and (b) capture its public profile: photo (`image` → a face for reverse-image/face search), About/status text, and business-account details. High value early in a trace when all you have is a number.

## How to use it (`bestInteractionPattern`: mobile-app)
1. On a sock-puppet device with a burner WhatsApp account, save the target `phone` number as a new contact.
2. Open WhatsApp → refresh contacts → open the contact / start (but do NOT send) a chat to view the profile.
3. Record the profile photo, About text, and whether it's a Business account (business profiles expose address, category, website).
4. Do not message, call, or add to a group. Screenshot the photo before it changes.
5. Pivot: run the profile photo through reverse-image/face tools; About text and business fields feed further searches.

## Inputs → Outputs
- **In:** `phone`
- **Out:** account-exists signal, `image` (profile photo), `physical-description`/face for the photo, `social-profile` (About text, business profile fields).
- **Empty/negative result looks like:** contact shows no WhatsApp / can't invite → number isn't on WhatsApp (or blocked you). A registered account with privacy set to "nobody" shows no photo/About — existence confirmed but profile hidden. Absence of a photo is a privacy setting, not proof of no account.

## Gotchas & OpSec
- Human-in-the-loop: requires your own logged-in (burner) account and a real device/emulator.
- Privacy settings control visibility — many users hide photo/last-seen; you may confirm existence yet see nothing else.
- OpSec: this is **active**. Viewing is quiet, but any message/call/group-add alerts the owner; bulk-adding numbers or a reported persona gets banned. Isolate from your identity entirely.

## Overlaps ("do both")
- Pairs with phone-intelligence lookups and reverse-image/face tools — WhatsApp confirms the line is live and yields a face; those tools resolve the number's owner and match the photo elsewhere.

## Trust & verifiability
`trust: trusted` — signals come directly from Meta's platform, so existence and profile data are authoritative; just remember privacy settings limit what you can see.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsapp-messenger |
| category | documents-metadata |
| selectorsIn → selectorsOut | phone → image, physical-description, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
