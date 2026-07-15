---
id: telegram-facemath-bot
name: Telegram Facemath bot
description: Use when you have a `face`/`image` and want to find that person in an archive of public-event photos from Kazakhstan — returns matching event photos and where/when they were taken.
url: https://t.me/facematch_bot
category: image-video-face
path:
- image-video-face
bestFor: Face-searching a Kazakhstan public-events photo archive to place a person at an event and get more images of them.
selectorsIn:
- face
- image
selectorsOut:
- image
- geolocation
status: unknown
pricing: freemium
costNote: Telegram bot advertised as freemium — typically a few free matches, then credits/subscription for more results or higher-resolution source images. Verify current gating in-bot.
opsec: active
opsecNote: You upload the target's face to an unknown third-party Telegram bot, disclosing both the image and your Telegram identity to its operator. Assume the operator retains every uploaded face. Never upload from your real account or a face you're not authorized to search; use a burner Telegram account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: chrome-mcp
trust: unverified
trustNote: A regional face-search bot catalogued by the Cyber Detective (cyb-detective) OSINT list; underlying dataset, accuracy and operator are not independently verified.
missingPersonsRelevance: high
coverage:
- kz
auth: account
api: false
localInstall: false
registration: true
aliases:
- facematch_bot
- FaceMatch Kazakhstan
tags:
- Image Search and Identification
- Face recognition and search
- telegram
- kazakhstan
source: cyb-detective
lastVerified: '2026-07-15'
enrichment: full
---

# Telegram Facemath bot

> A Telegram face-recognition bot that searches an archive of public-event photographs from Kazakhstan — upload a face, get back event photos of that person.

## When to use
You have a `face` or `image` of someone with a Kazakhstan connection and want to place them at public events (concerts, sports, conferences, city gatherings) or simply find more photos of them. Regional event-photo face engines like this cover imagery that global tools (PimEyes, etc.) often miss, so it is a strong complementary check for Central-Asian subjects in missing-persons and identification work.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a **burner** Telegram account, open https://t.me/facematch_bot and `/start` it.
2. Send a clear, front-facing photo of the target's face.
3. Read the returned matches: photos from the event archive where the face appears, usually with event/location and date context.
4. Pivot: a matched event gives a `geolocation` and time placing the subject; other faces in the same photo are potential `associate` leads; source images feed further reverse-image/face searches.

## Inputs → Outputs
- **In:** `face` / `image` (a clear face photo)
- **Out:** matching `image`s from the archive, with event `geolocation`/date context
- **Empty/negative result looks like:** "no matches" — expected when the subject never appeared in the (Kazakhstan-focused) event archive, when the photo is low-quality/angled, or when free-tier limits truncate results. A miss is not evidence the person isn't in Kazakhstan.

## Gotchas & OpSec
- **Regional scope:** the index is Kazakhstan public-event photos — don't expect global coverage.
- **Active & privacy-sensitive:** uploading a face to an unknown bot exposes the image and your account; use a burner and mind the legality/ethics of face search in your jurisdiction.
- **Unverified operator & dataset:** treat matches as leads to confirm, not identifications; false positives are inherent to face search.
- Freemium limits cap free results — the first hits may not be the best hits.

## Overlaps ("do both")
- Pairs with global face engines (PimEyes / Search4Faces) and reverse-image tools — those cover worldwide imagery, this covers a regional archive they lack; run both and reconcile.

## Trust & verifiability
`trust: unverified` — a third-party regional bot from a curated OSINT list, with an unknown backend. Corroborate any "match" by inspecting the source photo and cross-checking the identity through an independent channel.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-facemath-bot |
| category | image-video-face |
| selectorsIn → selectorsOut | face, image → image, geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes (account-login) |
