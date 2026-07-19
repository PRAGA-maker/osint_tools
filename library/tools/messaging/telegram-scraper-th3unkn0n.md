---
id: telegram-scraper-th3unkn0n
name: TeleGram-Scraper (th3unkn0n)
description: Use when you have a Telegram group you can join and want its member list — returns members' usernames, user IDs and (where exposed) phone numbers, plus scraped media, as CSV.
url: https://github.com/th3unkn0n/TeleGram-Scraper
category: messaging
path:
- messaging
bestFor: Bulk-exporting the member list (usernames/IDs/phones) and media of a Telegram group you have access to.
selectorsIn:
- username
- social-profile
selectorsOut:
- username
- phone
- device-id
- social-profile
status: live
pricing: free
costNote: Free open-source Python tool; you supply your own Telegram API credentials (free from my.telegram.org).
opsec: active
opsecNote: You must run it from a real Telegram account that has joined the target group — that account is visible to admins and is what does the scraping, so use a dedicated sock-puppet account and number, never your own. Mass-scraping can trip Telegram anti-abuse and get the account limited/banned. Members whose privacy hides their phone won't expose it; don't assume a number is retrievable.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source OSINT script (th3unkn0n/TeleGram-Scraper); community-maintained Python wrapping the official Telegram (Telethon) API, so data comes from Telegram itself.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- osi-ig
aliases:
- Telegram Scraper
- th3unkn0n TeleGram-Scraper
tags:
- telegram
- scraping
- python
source: osintambition-social
lastVerified: '2026-07-19'
enrichment: full
---

# TeleGram-Scraper (th3unkn0n)

> A Python CLI that exports a Telegram group's membership — usernames, IDs and any visible phone numbers — and can scrape its media, turning a group you've joined into a structured contact list.

## When to use
Your subject is active in a Telegram group/channel (a community, a marketplace, an interest group) and you want the full picture of who else is there and how to pivot on them. It dumps the member roster to CSV — usernames, numeric user IDs, and phone numbers for members who haven't hidden them — and can pull posted media. Useful for mapping a subject's community, finding their alternate accounts, and extracting a phone number that ties a Telegram handle to a real identity.

## How to use it (`bestInteractionPattern`: cli)
1. Create Telegram API credentials (api_id/api_hash) at my.telegram.org and clone the repo; `pip install -r requirements.txt`.
2. Run `python3 setup.py` and authenticate with a **dedicated sock-puppet** Telegram account (its own SIM/number) that has already **joined** the target group.
3. Use the scrape command to export the member list to `members.csv` (username, user ID, name, phone-if-visible); use the media/message options to pull posted files.
4. Pivot: a `phone` → reverse-phone OSINT tying the handle to an identity; a `username` → cross-platform username search; a numeric user ID (`device-id`-style stable identifier) → track the same person across handle changes.

## Inputs → Outputs
- **In:** a Telegram group your account has joined (target `username`/group)
- **Out:** CSV of members → `username`, numeric user ID, `phone` (only where the member allows it), plus scraped media
- **Empty/negative result looks like:** an empty/short list or auth error — you haven't joined the group, the group hides members, credentials are wrong, or Telegram rate-limited the account; phone columns are blank when members' privacy hides their number.

## Gotchas & OpSec
- Human-in-the-loop: needs your own API key and an authenticated (sock-puppet) account that has joined the group.
- OpSec: **active** — the scraping account is a real member visible to admins; heavy scraping risks Telegram limiting/banning it. Isolate it from your identity (separate number, device/session).
- Most members' phone numbers are hidden by privacy settings; usernames/IDs are the reliable output, phones are opportunistic.

## Overlaps ("do both")
- Pairs with Telegram-search/channel-analytics tools and `[[osi-ig]]`-style social scrapers — this gives the raw roster, the analytics tools map activity and the cross-platform tools resolve each handle to a person.

## Trust & verifiability
`trust: community` — a widely-used open-source script over Telegram's official API; the data is Telegram's own, so it's reliable, but review the code before running and treat scraped phones as leads to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-scraper-th3unkn0n |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → username, phone, device-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
