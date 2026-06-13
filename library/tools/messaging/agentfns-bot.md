---
id: agentfns-bot
name: AgentFNS_Bot
description: Use when you have a Russian company INN/OGRN (or counterparty name) and need instant official business-registry details via Telegram.
url: https://t.me/AgentFNS_bot
category: messaging
path:
- messaging
bestFor: Free Telegram bot for instant verification of Russian business counterparties using official (FNS/registry) data.
selectorsIn:
- employer-org
- document-id
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Advertised as a free counterparty-check bot ("Бесплатный бот ... Только официальные данные").
opsec: passive
opsecNote: Queries Russian official business registries (FNS), not the subject. Use within a Telegram account you control; consider a sock-puppet account since the bot logs your queries.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Russian-language Telegram bot pulling FNS/registry data; community OSINT tool, accuracy depends on the underlying official sources it mirrors.
missingPersonsRelevance: low
coverage: [ru]
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- AgentFNS
tags:
- telegram
- russia
- corporate-records
source: awesome-osint
lastVerified: '2026-06-13'
enrichment: full
---

# AgentFNS_Bot

> Telegram counterparty-check bot: enter a Russian company's INN/OGRN or name and get official registry details for free.

## When to use
You have an `employer-org` link or a Russian tax/registry ID (`document-id` — INN/OGRN) for a person of interest or their associate, and you want the official company record: legal name, registered `address`, director/founder `associate` links. Mostly relevant when a missing person is tied to a Russian business or sole proprietorship.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/AgentFNS_bot in Telegram and press Start.
2. Send the company INN/OGRN (or, where supported, the company/person name).
3. Read the returned official registry card: legal name, status, address, officers.
4. Pivot: take director/founder names (`associate`) into a people-search, or the `address` into mapping/registry tools.

## Inputs → Outputs
- **In:** `employer-org` / `document-id` (INN/OGRN) / `name`
- **Out:** `employer-org` (legal entity), `address`, `associate` (officers/founders)
- **Empty/negative result looks like:** "not found" or no matching entity — the ID is wrong, the entity is dissolved, or it isn't in the Russian registry.

## Gotchas & OpSec
- Russian-language interface; expect Cyrillic inputs/outputs.
- Human-in-the-loop: requires a logged-in Telegram account to interact with the bot.
- OpSec: passive toward the subject, but the bot operator sees your queries — use a sock-puppet Telegram account.

## Trust & verifiability
`trust: community` — a third-party bot mirroring official FNS/registry data. Verify anything material against the primary Russian registry (e.g. egrul.nalog.ru) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | agentfns-bot |
| category | messaging |
| selectorsIn → selectorsOut | employer-org, document-id, name → employer-org, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (Telegram login) |
