---
id: egrul-bot
name: egrul_bot (Telegram — Russian company registry)
description: Use when you have a Russian `employer-org`, INN/OGRN, or a director's `name` and want official EGRUL company data via Telegram — returns company status, address, directors, and founders.
url: https://t.me/egrul_bot
category: messaging
path:
- messaging
bestFor: Querying Russia's EGRUL legal-entity registry (companies, directors, founders) from within Telegram.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: free
costNote: Free Telegram bot; a Telegram account is required to use it. Some such bots gate extended reports behind limits or paid tiers.
opsec: active
opsecNote: You must query it from a Telegram account, which ties the search to that identity, and the bot operator sees your queries. Use a sock-puppet Telegram account. The company/directors are not notified.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Telegram front-end over Russian EGRUL/EGRIP data. The underlying registry data is official, but the bot is an unofficial intermediary — corroborate against the FNS source where it matters.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: false
aliases:
- egrul bot
- EGRUL Telegram bot
tags:
- telegram
- company-registry
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# egrul_bot (Telegram — Russian company registry)

> A Telegram bot front-end to Russia's EGRUL legal-entity register — type a company name, INN/OGRN, or director and get official-style company data back in chat.

## When to use
You have a Russian company (`employer-org`), an INN/OGRN number, or a person you suspect is a Russian company director/founder, and you want the registry record — status, registered address, directors, and founders — without navigating the FNS site directly. Useful when an investigation touches Russian corporate structures and you need to connect a `name` to companies and co-founders (`associate`s).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/egrul_bot from a **sock-puppet** Telegram account and start the bot.
2. Send a company name, INN, or OGRN (or a director's `name` where supported).
3. Read the reply: legal entity name, status (active/liquidated), registered `address`, director(s), and founders/participants.
4. For anything decisive, confirm against the official FNS EGRUL source — the bot is an unofficial intermediary.
5. Pivot: directors/founders become `associate` leads; shared addresses/founders reveal linked companies; a person's directorships map their Russian business footprint.

## Inputs → Outputs
- **In:** `employer-org` (name), INN/OGRN, or director `name`
- **Out:** company status, registered `address`, director/founder `name`s (`associate`s), registration details
- **Empty/negative result looks like:** no record / bot error — wrong INN, transliteration mismatch (Cyrillic vs Latin), a dissolved entity, or a rate/format limit. Absence isn't proof; retry via the official source.

## Gotchas & OpSec
- Unofficial intermediary: the bot reflects EGRUL data but isn't the registrar — verify critical facts at FNS.
- Transliteration: Russian names/companies transliterate many ways; prefer INN/OGRN for precision.
- OpSec: **active** via the required Telegram account — the operator sees your queries; use a throwaway account.

## Overlaps ("do both")
- Pairs with OpenCorporates and other registry tools plus the official FNS EGRUL — the bot is a fast Telegram lookup; the official source and aggregators confirm and cross-link across jurisdictions.

## Trust & verifiability
`trust: community` — an unofficial Telegram front-end over official EGRUL data; treat its output as an accurate-but-unverified reflection and confirm at the registrar for anything that matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | egrul-bot |
| category | messaging |
| selectorsIn → selectorsOut | employer-org, name → address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
