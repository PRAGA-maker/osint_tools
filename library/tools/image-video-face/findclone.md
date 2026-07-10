---
id: findclone
name: FindClone
description: Use when you have a face `image` and want to match it against VKontakte (Russian social network) profile photos — returns candidate social-profile matches.
url: https://findclone.ru/
category: image-video-face
path:
- image-video-face
bestFor: Facial-recognition search of a photo against millions of VK (Russian social media) profile images to identify a person's Russian-internet presence.
selectorsIn:
- face
- image
selectorsOut:
- social-profile
- name
status: degraded
pricing: freemium
costNote: Requires registration with a phone number and, since 2022 sanctions, payment from a Russian/Belarusian bank (historically ~$5/month for a search bundle). A small number of free trial searches may be granted on signup; sustained use is paid and payment is the main access barrier for non-Russian users.
opsec: active
opsecNote: You upload the target's face to a Russian commercial facial-recognition service and register a phone number with it — that phone/account and the query are retained by a Russian operator. Treat this as active and jurisdiction-sensitive: use a burner number, never upload photos you can't risk exposing, and consider the legal/ethical weight of feeding a face into this service.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known, effective Russian face-search service widely used by investigators (e.g. Bellingcat); operated by an opaque Russian commercial entity, so trust its results as leads, not its data handling.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: true
aliases:
- FindClone
- findclone.ru
tags:
- face-recognition
- vkontakte
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# FindClone

> A Russian facial-recognition engine that matches an uploaded face against VKontakte profile photos — the go-to for identifying someone's Russian-internet (VK) presence from a picture.

## When to use
You have a `face`/`image` of a person and suspect a Russian or former-Soviet-space connection, and you want to find their VK profile(s). FindClone compares your photo against a huge index of VK profile images and returns visually similar faces with links to the profiles — turning an anonymous photo into a named `social-profile`. It is one of the few effective consumer face-search tools for the Russian internet, valuable when Western reverse-image tools come up empty on an Eastern-European subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://findclone.ru/ with a phone number (use a burner); complete SMS verification.
2. Arrange access — free trial searches are limited, and sustained use requires payment, which since 2022 sanctions generally means a Russian/Belarusian card.
3. Upload a clear, front-facing photo of the target's face.
4. Review the ranked candidate matches, each linking to a VK profile; open promising profiles to confirm via other photos, name, city and connections.
5. Pivot: a confirmed VK profile feeds VK-native OSINT (friends, posts, groups); the real `name` and city feed people-search.

## Inputs → Outputs
- **In:** `face`/`image` (clear, frontal works best)
- **Out:** `social-profile` (candidate VK profiles), `name` (from matched profiles)
- **Empty/negative result looks like:** no visually similar faces, or only false matches — expected if the subject has no VK photo, uses obscured/low-quality images, or isn't in the index; a miss is not proof of absence.

## Gotchas & OpSec
- **Access is the hard part:** sanctions make payment difficult for non-Russian users; the tool works, but getting a paid account is the barrier — reflected in `status: degraded`.
- **Jurisdiction/ethics:** you are handing a face and a phone number to a Russian commercial operator; weigh legal, ethical and personal-OpSec risk. Use a burner and don't upload sensitive photos.
- Matches are similarity-ranked, not identity-proven — always confirm on the profile.

## Overlaps ("do both")
- Pairs with `[[search4faces]]`-style VK/OK face tools and Western reverse-image engines (Yandex especially) — run several face engines, since each indexes different photo sets and one often finds what the others miss.

## Trust & verifiability
`trust: community` — an effective, investigator-trusted engine for VK face search, but operated opaquely; treat every match as a lead to verify against the actual profile and other selectors.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findclone |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → social-profile, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
