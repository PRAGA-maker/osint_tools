---
id: tagrum
name: Targum
description: Use when you have a foreign-language video (uploaded or a social link) and want to understand what's said — returns an AI-translated, English-subtitled version so you can read the content.
url: https://targum.video/
category: image-video-face
path:
- image-video-face
bestFor: Quickly translating and subtitling a short foreign-language video (TikTok/Twitter/Instagram/Reddit or a file) into English.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: "\"Start translating for free\" tier exists; longer/more videos and premium features require a paid plan. Free tier suits one-off short clips."
opsec: passive
opsecNote: You upload/paste a video to a third-party AI service — the clip leaves your control and is processed on Targum's servers. Passive toward the subject (they aren't notified), but don't submit sensitive/unpublished footage you can't put in a third-party cloud. Use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial AI video-translation startup; output is machine translation, so treat subtitles as a fast gist, not a certified transcript.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- targum.video
- Targum Video
tags:
- Video editing and analyze
- translation
- video
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Targum

> An AI video-translation service — drop in a foreign-language clip and get English subtitles so you can understand what's being said.

## When to use
You have a short foreign-language video relevant to a case — a social-media clip (TikTok, Twitter/X, Instagram, Reddit) or an uploaded file — and you need to know what's spoken without a human translator on hand. Targum auto-translates and subtitles it in minutes, giving you a fast gist to decide whether the clip matters and what to investigate next.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://targum.video/ and sign in (free tier available).
2. Paste the social-media video link, or upload the video file.
3. Wait a few minutes for processing; download/view the subtitled English version.
4. Read the subtitles as a *lead-quality* translation — machine output can mistranslate names, slang, and dialect, so verify anything decisive with a human translator.
5. Pivot: place names, names, or events surfaced in the translation feed geolocation (`[[digitaldigging-org]]`), people-search, or news-archive follow-up.

## Inputs → Outputs
- **In:** a foreign-language video (social link or uploaded file)
- **Out:** an English-subtitled/translated version of the clip
- **Empty/negative result looks like:** failure on very long videos, poor/no audio, heavy background noise, or unsupported languages — a garbled or empty subtitle track means fall back to a manual translator, not that the clip is meaningless.

## Gotchas & OpSec
- Human-in-the-loop: requires an `account-login`; longer clips hit the paid tier.
- **Third-party upload:** the video is processed on Targum's cloud — don't submit sensitive or unpublished evidence you wouldn't hand to an outside service.
- Machine translation errs on names, idioms, and dialect; never quote a subtitle as verbatim testimony without human verification.

## Overlaps ("do both")
- Pairs with a manual transcription/translation and with frame-analysis tools — Targum gives a fast automated gist; a human translator confirms the specifics and a frame/EXIF review handles the visual side.

## Trust & verifiability
`trust: community` — a commercial AI translation tool; output is machine-generated, so it's reliable for triage but must be human-verified before any translated content is relied upon as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tagrum |
| category | image-video-face |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
