---
id: telegram-channels-scraper-telegraphite
name: TeleGraphite (Telegram channels scraper)
description: Use when you have public Telegram channel `username`s and want their posts, media, and any leaked contacts archived to JSON — returns social-profile posts, phone, and email.
url: https://github.com/hamodywe/telegram-scraper-TeleGraphite
category: messaging
path:
- messaging
bestFor: Batch-archiving posts and media from a list of public Telegram channels, with contact extraction.
selectorsIn:
- username
selectorsOut:
- social-profile
- phone
- email
- image
status: live
pricing: free
costNote: Free, open-source Python tool. Installable via `pip install telegraphite`. Requires your own Telegram API credentials (free from my.telegram.org).
opsec: active
opsecNote: Runs through the Telegram API using YOUR API ID/hash tied to a phone-verified Telegram account, so activity is attributable to that account. Use a dedicated sock-puppet Telegram number, not your personal one. Reading public channels does not notify their admins.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Small open-source project (hamodywe) built on Telethon; inspectable but unaudited.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- telegram-scraper
- telepathy
aliases:
- TeleGraphite
- telegraphite
tags:
- telegram
- channel-scraper
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# TeleGraphite (Telegram channels scraper)

> A CLI Telegram scraper that pulls posts and media from a list of public channels to JSON, deduplicates them, and extracts emails/phone numbers found in the text.

## When to use
You have one or more public Telegram channel handles tied to a subject or investigation and want a searchable local archive of everything they post — text, media, and any contact details (emails, phones) buried in messages. Good for monitoring a channel over time and for mining posts for pivotable selectors.

## How to use it (`bestInteractionPattern`: cli)
1. Create a Telegram API app at https://my.telegram.org/ to get an `api_id` and `api_hash`; put them in a `.env` file.
2. Install: `pip install telegraphite` (or `pip install -e .` from source).
3. List target channels in the channels file.
4. Run `telegraphite once` for a single pull, or `telegraphite continuous --interval 3600` to poll on a schedule. Filter by keyword, media-only, or text-only.
5. Read the JSON output and downloaded media; grep for extracted emails/phones.
6. Pivot: extracted `phone`/`email` feed messaging/email OSINT; channel membership and reposts map the network.

## Inputs → Outputs
- **In:** `username` (public channel handles)
- **Out:** `social-profile` (posts, timestamps), `phone`/`email` (extracted from text), `image` (downloaded media)
- **Empty/negative result looks like:** no posts fetched usually means the channel is private/invite-only or the handle is wrong — the API only reads public channels your account can access.

## Gotchas & OpSec
- Human-in-the-loop: you must register a Telegram API app and authenticate an account first.
- OpSec: **active** — the pull runs under your (sock-puppet) Telegram identity. Never use your real number.
- Only public channels are reachable; private/invite channels need your account to already be a member.

## Overlaps ("do both")
- Pairs with `[[telepathy]]` — Telepathy focuses on chat/user analytics; run both to cover channels and group membership.
- Pairs with `[[telegram-scraper]]` — alternative scraper; useful cross-check when one breaks against Telegram API changes.

## Trust & verifiability
`trust: community` — open source and inspectable, but a small unaudited project; the underlying data is authoritative (direct from Telegram's API), so archived posts are reliable even if the tooling is niche.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-channels-scraper-telegraphite |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile, phone, email, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
