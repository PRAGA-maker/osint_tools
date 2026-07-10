---
id: whatsapp-checkleaked
name: WhatsApp CheckLeaked (DP Viewer)
description: Use when you have a `phone` number and want to confirm it's on WhatsApp and view its public profile photo and About — returns social-profile, image and account-type.
url: https://whatsapp.checkleaked.cc/
category: messaging
path:
- messaging
bestFor: Checking whether a phone number has an active WhatsApp account and viewing its public profile picture, About/bio and business status without saving the contact.
selectorsIn:
- phone
selectorsOut:
- social-profile
- image
status: degraded
pricing: freemium
costNote: The basic profile-picture/About viewer is free; a paid API is offered for bulk/developer use. Not a breach-search tool (that's the separate checkleaked.cc).
opsec: passive
opsecNote: The lookup is done server-side by the service, so you don't add the number to your own contacts or message it — you stay off the target's radar. You are, however, submitting the target's number to a third party; use a number you're authorised to check and don't rely on the service storing it responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party WhatsApp profile viewer; effective, but WhatsApp policy changes mean profile-photo retrieval for personal accounts is no longer guaranteed, and it falls back to cached/third-party data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- WhatsApp CheckLeaked
- WhatsApp DP viewer
- whatsapp.checkleaked.cc
tags:
- whatsapp
- phone
- profile-viewer
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# WhatsApp CheckLeaked (DP Viewer)

> A WhatsApp profile viewer — enter a phone number to confirm it's on WhatsApp and pull its public display picture, About/bio and business status, all without saving the contact or opening the app.

## When to use
You have a `phone` number and want to confirm it belongs to an active WhatsApp user and grab identifying detail: the profile photo (`image`) for reverse-image search, the About/bio text, and whether it's a business account. Confirming a number is live on WhatsApp is a useful signal that it's in current use, and the profile photo often links the number to a face and other accounts.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://whatsapp.checkleaked.cc/.
2. Enter the target `phone` in full international format.
3. Read the result: whether the number is on WhatsApp, the profile picture (with history where available), the About text, and business-account detection.
4. Download the profile photo for reverse-image/face search.
5. Pivot: the photo feeds reverse-image and face tools; a confirmed active number feeds other phone-OSINT; the About text may leak a name, business or links.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** `social-profile` (WhatsApp presence + About/business status), `image` (profile picture / history)
- **Empty/negative result looks like:** "not on WhatsApp", or a blank photo — the latter is increasingly common, since WhatsApp restricted profile-photo access for personal accounts and privacy settings can hide the DP; absence of a photo is not proof the number lacks WhatsApp.

## Gotchas & OpSec
- **Degraded photo access:** WhatsApp policy changes mean personal-account photos aren't reliably retrievable; the service leans on cached/third-party data, so results are inconsistent.
- Users can hide their photo/About via privacy settings — a hidden profile still may be on WhatsApp.
- Passive toward the target (no contact saved), but you're handing the number to a third party.

## Overlaps ("do both")
- Pairs with reverse-image/face tools and phone-OSINT like PhoneInfoga — confirm the number on WhatsApp and grab the DP here, then run the photo and number through those to build identity.

## Trust & verifiability
`trust: community` — a useful third-party viewer, but photo retrieval is unreliable post-policy-change; verify a "not on WhatsApp" or a missing photo isn't just a privacy setting, and confirm identity via the image and other sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsapp-checkleaked |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
