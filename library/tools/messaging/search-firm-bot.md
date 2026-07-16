---
id: search-firm-bot
name: Search_firm_bot
description: Use when you have a Russian `employer-org` name/ID and want registry, bank, and postal-index details via a Telegram bot — returns org records and `address`/`associate`.
url: https://t.me/Search_firm_bot
category: messaging
path:
- messaging
bestFor: Looking up Russian organizations, banks, and postal codes through a Telegram bot ("Поиск организаций").
selectorsIn:
- employer-org
- name
- document-id
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: Free basic organization/bank/postcode lookups; extended reports may be credit-gated inside the bot.
opsec: passive
opsecNote: Queries target companies/registries, not the person directly, so it is comparatively low-touch. Still, the bot operator logs your queries — run it from a sock-puppet Telegram account rather than a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous Russian-language Telegram bot mirroring organization/bank/postal data; underlying sources and freshness are not documented or verified.
missingPersonsRelevance: high
coverage:
- ru
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Search_firm_bot
- Поиск организаций
tags:
- telegram
- russia
- corporate-records
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Search_firm_bot

> A Russian-language Telegram bot for organization, bank, and postal-index lookups — the corporate-records leg of a Russian-subject investigation.

## When to use
You have a Russian `employer-org` (company name or registry ID like INN/OGRN), a bank identifier, or a postal code connected to a subject or their associate, and you want the official-style record: legal address, registration details, and linked officers. Mostly relevant when a missing person or associate is tied to a Russian business, employer, or region you're trying to place.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open https://t.me/Search_firm_bot and press Start.
2. Send the company name / INN / OGRN, a bank identifier, or a postal index.
3. Read the returned card: legal name, registered `address`, status, and any listed officers (`associate`).
4. Pivot: take an officer/director `name` into people-search; take the `address` into mapping and registry tools.

## Inputs → Outputs
- **In:** `employer-org` (name or INN/OGRN `document-id`), bank identifier, or postal code
- **Out:** organization record with registered `address` and officer `associate` links
- **Empty/negative result looks like:** the bot returns "not found" for the identifier, or offers only a paid extended report with no free summary.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account-login; use a sock puppet.
- Data is an unofficial mirror — freshness and accuracy are unverified; confirm against a first-party Russian registry before relying on it.
- This finds companies, not people directly — value comes from bridging an employer to named officers, so pair it with a people-search on any officer name.

## Overlaps ("do both")
- Pairs with `[[agentfns-bot]]`, which pulls official Russian FNS counterparty data — cross-check any company/officer detail across both bots.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram aggregator with no accountable maintainer; treat records as leads and corroborate with an official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-firm-bot |
| category | messaging |
| selectorsIn → selectorsOut | employer-org, name, document-id → employer-org, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
