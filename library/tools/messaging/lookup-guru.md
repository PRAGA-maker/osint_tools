---
id: lookup-guru
name: Lookup.guru
description: Use when you have a Discord user ID (`device-id`/snowflake) and want the public profile behind it — returns username, avatar/banner image, account creation date and badges.
url: https://lookup.guru/
category: messaging
path:
- messaging
bestFor: Resolving a Discord snowflake user ID to its public profile (username, avatar, account age, badges).
selectorsIn:
- device-id
- social-profile
selectorsOut:
- username
- social-profile
- image
status: live
pricing: free
costNote: Free and open source; no account. A CAPTCHA gates each lookup.
opsec: passive
opsecNote: The lookup queries only Discord's public profile data for a given ID — it does not contact or notify the target, and returns no private data (no email, IP, phone, tokens or DMs). Passive; still use a clean browser session out of habit.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A free, open-source Discord ID lookup (code on GitHub under LookupGuru); it surfaces only what Discord's public API returns, so results are accurate to Discord but limited to public profile fields.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lookupguru
- lookup.guru
tags:
- discord
- id-lookup
- snowflake
source: osintambition-social
lastVerified: '2026-07-11'
enrichment: full
---

# Lookup.guru

> A free, open-source Discord profile viewer — paste a snowflake user ID and it decodes the account: username, avatar, banner, creation date and badges, straight from Discord's public data.

## When to use
You have a Discord user ID (snowflake) — from a log, a scraped mention, or another tool — and want to put a face and handle to it. Discord snowflakes encode the account creation timestamp, and the public profile gives you a username and avatar to pivot on. Useful when a subject is known only by a numeric Discord ID.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lookup.guru/.
2. Paste the Discord user ID (snowflake) and solve the CAPTCHA.
3. Read the returned public profile: username, avatar and banner images, account creation date (decoded from the snowflake), and any public badges.
4. Pivot: the username feeds cross-platform username enumeration (`[[aliens-eye]]`); the avatar feeds reverse-image/face search; the creation date helps age/authenticity assessment of the account.

## Inputs → Outputs
- **In:** Discord user ID / snowflake (`device-id`), or a profile reference
- **Out:** `username`, `social-profile` (public Discord profile), avatar/banner `image`, account creation date, badges
- **Empty/negative result looks like:** the ID resolves to nothing/an invalid account, or only a bare shell with default avatar — means the account is deleted, the ID is wrong, or the profile is minimal. It never returns private data.

## Gotchas & OpSec
- **Public-only:** it exposes no email, IP, phone, token or DMs — anything claiming otherwise is a scam. Set expectations accordingly.
- You need the numeric ID; it does not search by username (use it after you already have the ID).
- Human-in-the-loop: a CAPTCHA gates each lookup — solve manually.
- OpSec: passive; the target is not contacted or notified.

## Overlaps ("do both")
- Pairs with `[[username-to-id-bot]]`-style resolvers (the Telegram equivalent) conceptually, and with reverse-image search on the avatar to tie the Discord account to a real identity.

## Trust & verifiability
`trust: community` — an open-source tool that faithfully mirrors Discord's public profile API. Results are as accurate as Discord's own public data; it adds nothing beyond what Discord exposes, which is exactly why it's trustworthy for what it does.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lookup-guru |
| category | messaging |
| selectorsIn → selectorsOut | device-id, social-profile → username, social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
