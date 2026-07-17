---
id: transcriber-bot
name: '@transcriber_bot'
description: Use when you have an audio/voice message or an `image` of text and want it turned into searchable text — a Telegram bot that transcribes voice notes (20+ languages) and OCRs photos.
url: https://t.me/transcriber_bot
category: messaging
path:
- messaging
bestFor: Converting Telegram voice messages to text and extracting text from forwarded photos, in 20+ languages, without leaving the chat.
selectorsIn:
- metadata-exif
selectorsOut:
- name
status: live
pricing: free
costNote: Free to use inside Telegram; requires a Telegram account. No separate signup or payment for core transcription/OCR.
opsec: active
opsecNote: You forward the audio/image to a third-party bot, so its operator receives your content — never send case-sensitive media (a victim's voice note, private evidence) to it. Use a sock-puppet Telegram account and non-identifying media; assume anything sent is retained by the bot operator.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: mobile-app
trust: unverified
trustNote: A third-party Telegram bot of unknown operator; convenient but opaque about data handling, so treat it as a quick utility for non-sensitive media only.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- transcriber_bot
- Transcriber Bot
tags:
- messengers
- telegram
- transcription
- ocr
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# @transcriber_bot

> A Telegram utility bot that converts voice messages to text and pulls text out of photos (OCR) in 20+ languages — handy for making spoken or pictured content searchable.

## When to use
You are working within Telegram and hit media you can't grep: a subject's voice note, a forwarded audio clip, or a screenshot/photo containing text (a sign, a document, a chat capture). Forward it to the bot to get transcribed/OCR'd text you can search, translate, and quote — turning opaque media into a `name`, handle, place, or phrase you can pivot on. Use only on **non-sensitive** media given the third-party disclosure.

## How to use it (`bestInteractionPattern`: mobile-app)
1. In Telegram (ideally a sock-puppet account), open https://t.me/transcriber_bot and start the bot.
2. Forward or send the voice message or photo you want processed.
3. The bot replies with the transcribed/OCR'd text; set the language if auto-detection misreads it.
4. To use it in a group, add the bot — note it typically responds only to non-anonymous admins' commands.
5. Pivot: a transcribed `name`/handle/place → username/social/people tools; OCR'd document text → document-metadata or records lookups.

## Inputs → Outputs
- **In:** an audio/voice message, or an `image` containing text
- **Out:** plain text (transcription / OCR) — often yielding a `name`, handle, or location to pivot on
- **Empty/negative result looks like:** garbled or empty output — poor audio quality, an unsupported language/accent, or low-resolution/handwritten images. Verify against the source media before trusting the text.

## Gotchas & OpSec
- **Active / third-party disclosure:** the bot operator receives whatever you send. Never forward a victim's voice note or private evidence; use only non-sensitive media and a throwaway account.
- Human-in-the-loop: needs a Telegram account (account-login).
- Automated transcription/OCR makes mistakes on accents, noise, and stylised text — treat output as a lead, not a verbatim record.

## Overlaps ("do both")
- Pairs with a local, self-hosted transcription tool (e.g. a Whisper-based bot) — for sensitive media, prefer local transcription that doesn't hand your audio to an unknown operator; use @transcriber_bot only for quick, low-risk clips.

## Trust & verifiability
`trust: unverified` — a convenient but opaque third-party bot with no clear data-handling guarantees. Fine for non-sensitive quick jobs; verify transcriptions against the source and keep confidential media off it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transcriber-bot |
| category | messaging |
| selectorsIn → selectorsOut | metadata-exif → name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | mobile-app |
| opsec | active |
| human-in-loop | yes (account-login) |
