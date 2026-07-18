---
id: line
name: LINE
description: Use when you have a LINE ID (`username`) or `phone` and want to confirm a LINE account and view its public profile — returns display name, avatar, and status message.
url: https://line.me/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Confirming a LINE account exists and viewing its public profile via ID search or add-by-phone, especially in Japan/Taiwan/Thailand.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free app; you need your own (ideally sock-puppet) LINE account to search.
opsec: active
opsecNote: Searching a LINE ID or adding by phone touches the target's account graph — if you send a friend request or your number is in their contacts, LINE may surface you to them ("added you"/friend suggestion). Use a dedicated sock-puppet account with no real contacts, and stop at viewing the public profile; do not send requests or messages.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: trusted
trustNote: LINE is the first-party messaging platform; a profile you retrieve is the genuine account's public data, not a third-party scrape.
missingPersonsRelevance: high
coverage:
- global
- jp
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
aliases:
- LINE Messenger
- line.me
tags:
- messaging
- instant-messaging
- account-existence
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
relatedTools:
- line-me
- line-play
---

# LINE

> The dominant messenger across Japan, Taiwan, and Thailand — usable as an account-existence and public-profile oracle when you have a LINE ID or a phone number.

## When to use
You have a candidate LINE ID (`username`) or a `phone` number and need to know whether it maps to a real LINE account and what that account's public profile shows. In East/Southeast Asian cases LINE is often a person's primary account, so confirming the account and capturing its display `name`, avatar `image`, and status message can corroborate identity and yield a photo to run through face/reverse-image search.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Sign in to a **sock-puppet** LINE account on a dedicated device/emulator with no real contacts.
2. To check an ID: use **Add friends → Search** and enter the LINE ID (`username`). To check a number: add it to the sock-puppet's address book, then use **Add friends → by phone** (only works if the target has enabled "allow add by phone").
3. If a profile card appears, the account **exists** — read the display `name`, profile/cover `image`, and status message.
4. STOP at the public card. Do not tap "Add" / send a request or message — that notifies the target.
5. Pivot: the profile `image` feeds face/reverse-image tools; the display `name` and status message feed name/username searches.

## Inputs → Outputs
- **In:** LINE ID (`username`) or `phone`
- **Out:** account-exists confirmation, display `name`, avatar `image`, status message (`social-profile`)
- **Empty/negative result looks like:** "no results" for an ID, or no card for a number — meaning no discoverable account, which is NOT proof of absence: LINE IDs are optional and users can disable ID search and add-by-phone entirely.

## Gotchas & OpSec
- Human-in-the-loop: you **must** be logged into a LINE account to search — use a sock puppet, never a personal one.
- OpSec: this is **active**. Add-by-phone requires the number in your contacts and can trigger a friend suggestion in both directions; a friend request notifies the target. Keep to the passive profile-view only.
- Many users disable "allow others to add by ID/phone", so negatives are common and weak.

## Overlaps ("do both")
- Pairs with other messenger account-existence checks (e.g. a phone across WhatsApp/Telegram): run the same `phone` across platforms since a person's primary app varies by region. Any avatar found here feeds a reverse-image/face tool.

## Trust & verifiability
`trust: trusted` — LINE is the first-party platform, so a returned profile is the account's genuine public data. The caveat is discoverability, not authenticity: absence of a result reflects the target's privacy settings, not a data-quality problem.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | line |
