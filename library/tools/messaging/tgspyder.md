---
id: tgspyder
name: tgspyder
description: Use when you have a Telegram `username`/channel and want to scrape and analyze its members and messages — returns member `username`s/`social-profile`s and any exposed `phone` numbers.
url: https://github.com/Darksight-Analytics/tgspyder
category: messaging
path:
- messaging
bestFor: Scraping and analyzing Telegram channels/users for social-media-intelligence and threat research.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
- phone
status: live
pricing: free
costNote: Free, open-source CLI on GitHub; you supply your own Telegram account and API credentials.
opsec: active
opsecNote: Active — it authenticates to Telegram with your account/API credentials to read channels and members, so Telegram logs the activity and can ban the account. Use a dedicated burner account and number, never your own, and a clean IP.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool released by Darksight Analytics (a few hundred GitHub stars); functional but community-maintained and unaudited.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: false
localInstall: true
registration: true
relatedTools:
- telepathy
- telegram-scraper
- informer-telegram
aliases:
- Darksight-Analytics/tgspyder
tags:
- telegram
- scraper
source: gh-topic-osint-resources
lastVerified: '2026-07-18'
enrichment: full
---

# tgspyder

> A CLI for scraping and analyzing Telegram channels and users — enumerate members, pull messages, and surface pivotable identifiers.

## When to use
You have a Telegram channel/group or `username` tied to a subject or investigation and want a structured pull of its members and message history for analysis — mapping who participates, what's posted, and any leaked identifiers (occasionally a member's `phone` if their privacy settings expose it). Suited to social-media-intelligence / threat-research workflows over Telegram communities.

## How to use it (`bestInteractionPattern`: cli)
1. Create a **burner** Telegram account and get `api_id`/`api_hash` from https://my.telegram.org.
2. Clone `https://github.com/Darksight-Analytics/tgspyder` and install its requirements (Python).
3. Configure your API credentials/session per the README.
4. Run it against the target channel/user to scrape members and messages; export the results.
5. Analyze the output: member `username`s → cross-platform pivots; any exposed `phone` → phone-OSINT; message content → leads and timeline.

## Inputs → Outputs
- **In:** Telegram channel/group or user `username`.
- **Out:** member `username`s / `social-profile`s, message data, and any `phone` numbers exposed by members' privacy settings.
- **Empty/negative result looks like:** a private channel you can't join, an account rate-limited/banned mid-run, or members who all hide their number (no `phone` output — the norm).

## Gotchas & OpSec
- Credentials required: needs a logged-in Telegram account and API keys — use a disposable one.
- Phone numbers are rare: most users hide their number, so `phone` output is the exception, not the rule.
- Ban risk / ToS: automated scraping can get the account banned and breaches Telegram's terms — ensure authorization.
- Unaudited: community code; review before running on real infrastructure. OpSec: **active** — the read is tied to your account.

## Overlaps ("do both")
- Pairs with `[[telepathy]]` and `[[telegram-scraper]]` (alternative channel exporters) and `[[informer-telegram]]` (continuous multi-channel monitoring) — cross-check exports, since coverage differs by tool as Telegram changes.

## Trust & verifiability
`trust: community` — an unofficial open-source scraper; data comes from Telegram itself, but verify member/message extractions against the live channel and treat the code as unaudited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tgspyder |
| category | messaging |
| selectorsIn → selectorsOut | username → username, social-profile, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes |
