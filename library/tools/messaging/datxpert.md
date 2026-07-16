---
id: datxpert
name: datXpert
description: Use when you have an email, username, or domain and want to check whether it appears in leaked ULP (URL:login:password) / stealer-log databases — returns password and credential-exposure hits.
url: https://telegram.me/datxpertbot
category: messaging
path:
- messaging
bestFor: Checking an identifier against aggregated ULP / stealer-log credential dumps via a Telegram bot.
selectorsIn:
- email
- username
- domain
selectorsOut:
- password
- email
status: degraded
pricing: freemium
costNote: Telegram bot with a small number of free lookups; deeper/bulk results are gated behind paid credits. Availability of these bots is volatile.
opsec: active
opsecNote: Interacting means starting the bot from a Telegram account and sending the target's identifier to an unknown third party that trades in stolen credentials — assume everything you submit is logged and possibly resold. Use a burner Telegram account on a research device, never a personal one, and never submit your own or a client's live credentials.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous "probiv"-style Telegram bot searching public/private ULP dumps; provenance and freshness of its data are unverifiable and results may be false, stale, or seeded. Treat any hit as a lead requiring independent confirmation.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- datXpert bot
- datxpertbot
tags:
- telegram
- breach-data
- stealer-logs
- credential-leak
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- avtogram-bot
- discord-sensor
- getchatlist
- getsendgifts
- instabot
- leak-osint
- oksearch
- pimeyes
- searchforchats
- spyggbot
- unamer
---

# datXpert

> A Telegram "probiv" bot that searches leaked ULP (URL:login:password) and stealer-log databases for an identifier's credential exposure.

## When to use
You have an `email`, `username`, or `domain` for a subject and want to know if it surfaces in credential-leak / infostealer-log collections — which can confirm an account is real, reveal associated services (the URL half of a ULP triple shows which sites a person used), or corroborate an alias. In a missing-persons context, a stealer-log hit can point to accounts and services a subject actively used. Treat outputs strictly as investigative leads, not proof.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a **burner** Telegram account on a research device, open https://telegram.me/datxpertbot and press Start.
2. Send the identifier you want checked (email / username / domain) following the bot's prompt syntax.
3. Read the response: matched entries typically show a service/URL, a login, and (partially or fully) a password from a leak.
4. Free lookups are limited; the bot will prompt for paid credits for more — stop at the free tier unless there is clear justification.
5. Pivot: a revealed associated service/URL feeds account-existence and profile-enrichment tools; a recurring username feeds username-search tools.

## Inputs → Outputs
- **In:** `email`, `username`, or `domain`
- **Out:** `password` / credential-exposure records, associated service URLs, sometimes a linked `email`
- **Empty/negative result looks like:** "no data found" / no rows — meaning the identifier isn't in the bot's indexed dumps, NOT that the person has never been breached. Absence proves nothing.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account to talk to the bot (account-login).
- OpSec: **active and sensitive** — you are handing a target selector to an anonymous operator dealing in stolen data; it is logged and may be resold. Burner identity only.
- Legal/ethical: handling breached credentials carries legal and ethical constraints. Do not use recovered passwords to access any account; use hits only to inform the investigation.
- Data quality is unverifiable — false positives, recycled combolists, and stale entries are common.

## Overlaps ("do both")
- Sits alongside other breach/leak bots such as `[[leak-osint]]` — cross-check any hit across more than one source before trusting it, since each indexes different dumps.

## Trust & verifiability
`trust: unverified` — an anonymous grey-market Telegram bot with no accountability for accuracy or data origin. Corroborate every result through independent, lawful means.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | datxpert |
| category | messaging |
| selectorsIn → selectorsOut | email, username, domain → password, email |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
