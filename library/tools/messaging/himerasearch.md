---
id: himerasearch
name: HimeraSearch (Telegram probiv bot)
description: Use when you have a `phone`, `name`, `email` or `vehicle-plate` and want a Russian-market data-broker bot to return aggregated identity, contact and record data — returns address, dob, associate, employer-org and vehicle links. Legally and ethically sensitive.
url: https://t.me/HimeraNeGBL8Pro1dp_Search_bot
category: messaging
path:
- messaging
bestFor: Aggregated "probiv"-style lookups (phone/name/email/plate → identity, contacts, records) focused on Russia/CIS data.
selectorsIn:
- phone
- name
- email
- vehicle-plate
selectorsOut:
- address
- dob
- associate
- employer-org
- vehicle-plate
status: live
pricing: freemium
costNote: Limited free lookups, then paid — the bot is tied to the Unirate24 counterparty-verification/credit system; deep results require payment. Treat as a paid service.
opsec: active
opsecNote: This is a data-broker ("probiv") bot querying aggregated and often breach-sourced databases. It is queried from a Telegram account (use a burner/sock-puppet, never your real account and never your real phone as the account number). Its data provenance is largely illegal/leaked; using it against a person may itself be unlawful depending on jurisdiction. Do not enter targets you are not legally authorised to investigate, and do not treat outputs as clean.
humanInLoop: true
humanInLoopReason:
- legal-gate
- payment-wall-partial
bestInteractionPattern: chrome-mcp
trust: unverified
trustNote: An anonymous Russian-market data-broker bot drawing on breached and grey-market databases; accuracy is inconsistent and the sourcing is not lawful or auditable. Corroborate everything and understand the legal exposure.
missingPersonsRelevance: high
coverage:
- ru
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Himera Search
- Химера
tags:
- telegram
- probiv
- data-broker
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# HimeraSearch (Telegram probiv bot)

> A Russian-market "probiv" data-broker bot: feed it a phone/name/email/plate and it returns aggregated identity and contact data — powerful, but sourced from breached/grey-market databases and legally fraught.

## When to use
You are investigating a subject with a Russia/CIS nexus and need to expand a thin selector (a `phone`, `name`, `email`, or `vehicle-plate`) into identity, contact and record data that Western tools won't cover. Reach for it only when you are legally authorised and understand that this class of tool trades in illegally aggregated data — it is a last-resort, high-caution lead generator, not a citable source.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a **burner** Telegram account (never your real account; the account's phone number itself is exposure), open the bot and `/start`.
2. Send the selector you hold — phone, full name, email, or vehicle plate.
3. The bot returns a limited free preview; fuller records require paid credits (via its Unirate24 linkage).
4. Read outputs skeptically — the data is aggregated from many breaches and is frequently stale, mismatched or fabricated.
5. Pivot: use any hit purely as a lead to confirm against lawful, authoritative sources before recording it.

## Inputs → Outputs
- **In:** `phone`, `name`, `email`, `vehicle-plate`
- **Out:** `address`, `dob`, `associate` (relatives/contacts), `employer-org`, `vehicle-plate`/registration links
- **Empty/negative result looks like:** "not found" — meaningless as evidence of absence; the databases are partial and skewed toward Russia/CIS.

## Gotchas & OpSec
- **Legal gate:** the underlying data is breach/grey-market. In many jurisdictions querying or acting on it is unlawful. Do not use it without clear legal authorisation and never for anything you cannot defend.
- **OpSec: active and high-risk.** You are messaging an anonymous operator that logs queries. Use a burner Telegram account on a burner number; assume the operator retains and may sell your search history.
- Data quality is unreliable — treat every field as an unconfirmed lead, never a fact.

## Overlaps ("do both")
- Overlaps with other Telegram probiv bots (Glaz Boga, Quick OSINT and similar) — they draw on overlapping breach sets, so a hit in one means little until corroborated by a lawful source.

## Trust & verifiability
`trust: unverified` — anonymous operator, unlawful/opaque sourcing, inconsistent accuracy. Nothing it returns is verifiable at the point of output; corroborate independently and weigh the legal risk before using it at all.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | himerasearch |
| category | messaging |
| selectorsIn → selectorsOut | phone, name, email, vehicle-plate → address, dob, associate, employer-org, vehicle-plate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes (legal-gate, payment-wall-partial) |
