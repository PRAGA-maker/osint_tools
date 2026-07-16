---
id: pimeyes
name: PimEyes
description: Use when you have a `face`/`image` of a subject and want to find other web pages showing that same face — returns matching photos and the URLs they appear on across the open web.
url: https://telegram.me/pimeyesbot
category: messaging
path:
- messaging
bestFor: Facial-recognition reverse search of a face photo to locate other appearances of that person online.
selectorsIn:
- face
- image
selectorsOut:
- image
- social-profile
- face
status: live
pricing: freemium
costNote: On the official pimeyes.com, a free search shows blurred/limited matches; seeing the source URLs and setting alerts requires a paid plan (Open Plus / PROtect / an OSINT institutional tier). The Telegram bot at this URL is an UNOFFICIAL third-party front — do not pay it.
opsec: active
opsecNote: Semi-active — you upload the subject's face to a third-party engine that stores and indexes queries. Use only a photo you're entitled to search, from a sock-puppet account, and never upload your own face. Treat any Telegram "pimeyes" bot as untrusted; prefer the official web app.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: PimEyes itself is a well-known, effective facial-recognition search (widely covered by BBC and used in OSINT). This entry's URL, however, is a Telegram bot — an unofficial front of unknown provenance; verify against the official pimeyes.com.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- PimEyes face search
- pimeyes.com
tags:
- telegram
- face-recognition
- reverse-image
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- avtogram-bot
- datxpert
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- leak-osint
- oksearch
- searchforchats
- spyggbot
- unamer
---

# PimEyes

> A facial-recognition search engine that finds where a given face appears across the open web — far more powerful than plain reverse-image search because it matches the person, not the picture. (Note: the URL here is an unofficial Telegram bot; the real tool is pimeyes.com.)

## When to use
You have a clear `face`/`image` of a subject and want to find other places that face appears online — different photos, different sites, different contexts. In missing-person work this is a top-tier lead generator: one photo can surface a personal blog, a news image, a dating/forum avatar, or an event photo that plain reverse-image (which needs the *same* image) would miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Prefer the official app at https://pimeyes.com/en (the Telegram bot at the listed URL is an unverified third party — avoid entering payment there).
2. Create/sign in to a dedicated sock-puppet account.
3. Upload a clear, front-facing crop of the subject's `face` and run the search.
4. Read results: a grid of matching faces. The free tier blurs/limits them; a paid plan reveals the source URLs you actually need.
5. Confirm each match is the same person (PimEyes returns look-alikes too), then pivot: open source pages for names, handles, locations; feed found profiles into username/social tooling.

## Inputs → Outputs
- **In:** `face`/`image` (a single face crop)
- **Out:** matching face `image`s and their source URLs (`social-profile`/web pages) — paid to unblur sources
- **Empty/negative result looks like:** no confident matches, or only low-similarity look-alikes — meaning the face isn't indexed on the open web PimEyes covers (it excludes most social-media and video platforms). Not proof the person has no online photos.

## Gotchas & OpSec
- Coverage excludes major social networks and video sites — a blank result doesn't clear those; check them separately.
- Free tier is a teaser: matches are blurred and sources locked behind Open Plus/PROtect. Budget for a plan if you need the URLs.
- It returns look-alikes; facial similarity is not identity — always corroborate.
- Ethics/legality vary by jurisdiction; only search faces you're authorised to. Uploading a face is an active, logged act.
- The Telegram bot in the URL is unofficial — treat as untrusted; use the official site.

## Overlaps ("do both")
- Pairs with `[[face-recognition]]` and other face engines — run more than one, as each indexes a different slice of the web and misses different sources.
- Feed a good face crop from `[[imageyoutube-com]]` (channel avatar) or another extractor into PimEyes.

## Trust & verifiability
`trust: community` — the PimEyes engine is real and highly capable, but (a) it returns probabilistic look-alikes that must be confirmed, and (b) this entry points at an unofficial Telegram bot. Use the official pimeyes.com, verify every match against a second selector, and never treat a face hit as identification on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pimeyes |
| category | messaging |
| selectorsIn → selectorsOut | face, image → image, social-profile, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial) |
