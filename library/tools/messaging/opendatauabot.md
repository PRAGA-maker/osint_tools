---
id: opendatauabot
name: OpenDataUABot (Opendatabot)
description: Use when you have a Ukrainian person's `name`, `phone`, vehicle `vehicle-plate` or company and want state open-data — returns registry hits on companies, property, vehicles, courts, debts and wanted/sanction status via a Telegram bot.
url: https://t.me/OpenDataUABot
category: messaging
path:
- messaging
bestFor: One-stop querying of Ukrainian open-state data (companies, people, vehicles, real estate, courts, debts, wanted lists) through a Telegram bot.
selectorsIn:
- name
- phone
- vehicle-plate
- employer-org
selectorsOut:
- employer-org
- address
- vehicle-plate
- associate
- document-id
status: live
pricing: freemium
costNote: The Opendatabot Telegram bot offers free basic checks; deeper reports, monitoring and some registries require a paid subscription. Budget for paid tiers if you need full extracts.
opsec: active
opsecNote: You send the subject's identifiers to a volunteer-run, non-government bot that may log your queries, geolocation and phone number. Query from a sock-puppet Telegram account, never share your own sensitive data with it, and assume everything you type is retained by a third party.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Opendatabot is a well-known Ukrainian open-data aggregator, but the Telegram bot is operated by a private/volunteer team, not the state; data is sourced from official registries yet delivered by a third party with no data-protection guarantees.
missingPersonsRelevance: high
coverage:
- ua
auth: account
api: false
localInstall: false
registration: true
aliases:
- Opendatabot
- OpenDataUA
- OpenDataUABot
tags:
- telegram
- ukraine
- open-data
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# OpenDataUABot (Opendatabot)

> A Telegram front-end to Ukrainian state open data: one query fans out across company, property, vehicle, court, debt and wanted-list registries — powerful in Ukraine-linked cases, but a third-party bot to treat carefully.

## When to use
You have a Ukrainian subject's `name`, `phone`, a `vehicle-plate`, or a company `employer-org` and want a fast sweep of official Ukrainian registries: company ownership, real estate, vehicles, court decisions, debts/enforcement, and whether a person is wanted or under exit/entry bans. Especially useful for missing-person and due-diligence work with a Ukrainian nexus, where these registries are the authoritative public sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/OpenDataUABot in Telegram (web, desktop, or mobile) using a dedicated sock-puppet account — do not use a Telegram account tied to you.
2. Start the bot and choose the query type (person, company, vehicle, court, etc.).
3. Enter the identifier (`name`, tax/`document-id`, company code, or `vehicle-plate`).
4. Read the returned registry hits: company roles/`employer-org`, registered `address`es, vehicle records, court cases, debts, and status flags. Free tier gives basics; deeper extracts/monitoring need a paid subscription.
5. Corroborate against the underlying official registry where possible, and pivot: company codes feed the state company registry; addresses feed mapping; court case numbers feed the court register.

## Inputs → Outputs
- **In:** `name`, `phone`, `document-id` (tax number), `vehicle-plate`, or company code
- **Out:** `employer-org` roles, `address`, `vehicle-plate` records, court/debt records, `associate`/related entities, wanted/ban status
- **Empty/negative result looks like:** no registry hit for the identifier — meaning nothing in the Ukrainian open registries matches, not that the person doesn't exist; also verify you queried the right registry/format.

## Gotchas & OpSec
- Human-in-the-loop: you interact through Telegram chat, and full data requires a paid subscription (payment-wall-partial) plus a Telegram account.
- OpSec: **active** — you hand the subject's identifiers to a non-government bot that may log queries, geolocation and your phone. Use a sock-puppet Telegram account and never submit your own sensitive documents.
- Third-party delivery: data originates in official registries but is relayed by a private operator — corroborate high-stakes findings against the source registry.

## Overlaps ("do both")
- Pairs with the official Ukrainian company/court registries and other Ukraine OSINT bots — this bot is fast and cross-registry, but confirm critical hits directly in the authoritative state source.

## Trust & verifiability
`trust: community` — Opendatabot is a reputable, widely-used Ukrainian open-data service, but it is a private third-party aggregator, so treat its output as a strong lead to verify against the underlying government registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | opendatauabot |
| category | messaging |
| selectorsIn → selectorsOut | name, phone, vehicle-plate, employer-org → employer-org, address, vehicle-plate, associate, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (payment-wall-partial, account-login) |
