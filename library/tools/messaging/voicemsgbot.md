---
id: voicemsgbot
name: '@VoiceMsgBot'
description: Use when you have a Telegram voice message and want it transcribed to searchable text — returns the spoken content as text you can quote, translate and search.
url: https://t.me/VoiceMsgBot
category: messaging
path:
- messaging
bestFor: Converting collected Telegram voice notes into text for searching, quoting, and translation.
selectorsIn:
- metadata-exif
selectorsOut:
- name
- geolocation
- associate
status: degraded
pricing: freemium
costNote: Free bot for basic transcription; may impose rate limits or premium tiers, and Telegram bots can disappear without notice.
opsec: active
opsecNote: You must forward the audio to a third-party bot inside Telegram, using a real Telegram account — that account (not anonymous) is exposed to the bot operator, and the audio content leaves your control. Use a dedicated sock-puppet Telegram account and never forward sensitive/evidential audio you can't risk exposing.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party Telegram bot of unknown operator; transcription accuracy and data handling are unverified, so treat both the transcript and the operator's discretion with caution.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- VoiceMsgBot
- Telegram voice-to-text bot
tags:
- Messengers
- Telegram
- transcription
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# @VoiceMsgBot

> A Telegram bot that transcribes voice messages to text — turning un-searchable audio notes into quotable, translatable content.

## When to use
You have Telegram voice notes (from a subject's public channel/group or lawfully collected material) and need them as text to search, quote in a report, or run through translation. Audio is otherwise opaque to text-based OSINT; transcription unlocks names, places, and references spoken aloud. Use it when the evidentiary value of the audio's content outweighs the exposure of routing it through a third-party bot.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a dedicated sock-puppet Telegram account, open https://t.me/VoiceMsgBot and start the bot.
2. Forward or send the voice message to the bot.
3. Receive the text transcription in the chat.
4. Read the transcript for spoken names (`name`), places (`geolocation`), and mentioned people (`associate`).
5. Pivot: transcribed leads feed people-search/geolocation; run non-English transcripts through a translator.

## Inputs → Outputs
- **In:** a Telegram voice message (audio `metadata-exif`/content)
- **Out:** text transcription → spoken `name`, `geolocation`, `associate` references
- **Empty/negative result looks like:** garbled or empty output — expect this with poor audio, heavy accents, background noise, or unsupported languages; verify by ear before trusting a transcript.

## Gotchas & OpSec
- Active exposure: you must use a real Telegram account and hand the audio to an unknown operator — always use a sock puppet and never submit sensitive audio you can't risk leaking.
- Accuracy varies: automated transcription errs on names/proper nouns — treat every transcribed name as a lead to verify, not a fact.
- Ephemerality: Telegram bots vanish or change behavior without notice (status: degraded).
- OpSec: active/human-in-the-loop (Telegram login required).

## Overlaps ("do both")
- Pairs with translation tools and general audio-transcription utilities — this handles the Telegram-native flow; a standalone transcriber is the fallback if the bot is down or the audio is too sensitive to forward.

## Trust & verifiability
`trust: unverified` — an anonymous third-party bot; both its transcription accuracy and its handling of your audio are unverified, so confirm the transcript and minimise what you send.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | voicemsgbot |
| category | messaging |
| selectorsIn → selectorsOut | metadata-exif → name, geolocation, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
