---
id: chatbottle-telegram-bots
name: ChatBottle Telegram Bots
description: Use when you want to find a Telegram bot for a task (OSINT lookups, search, monitoring) — a searchable directory of Telegram bots with categories and descriptions.
url: https://chatbottle.co/bots/telegram
category: messaging
path:
- messaging
bestFor: Discovering Telegram bots — including OSINT/lookup bots — by keyword and category.
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free bot directory; browsing and searching require no account.
opsec: passive
opsecNote: Browsing the directory does not touch any subject. Note that actually running an OSINT Telegram bot later is a different, often active step — the bot operator sees your queries and your Telegram identity; use a sock-puppet Telegram account for that, not this directory.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party aggregator of publicly listed Telegram bots; listings are user/self-submitted, so treat any bot's claimed function as unverified until you test it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- chatbottle
- ChatBottle
tags:
- telegram
- bots
- directory
source: osintambition-social
lastVerified: '2026-07-29'
enrichment: full
---

# ChatBottle Telegram Bots

> A searchable directory of Telegram bots — a jumping-off point for finding the many lookup/OSINT bots that live only inside Telegram.

## When to use
You know Telegram hosts bots that resolve phone numbers, search leaked data, geolocate, or monitor channels, but you don't know which one to use. Search this directory by keyword to discover candidate bots, then evaluate and run the promising ones from a sock-puppet Telegram account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Telegram section of the directory.
2. Search a keyword or browse categories (search, tools, utilities) for a bot matching your task.
3. Read the bot's listing/description and open its Telegram link.
4. In a **sock-puppet** Telegram account, start the bot and test it on benign input first.
5. Pivot: a working bot becomes your actual lookup tool; the directory itself just gets you there.

## Inputs → Outputs
- **In:** `name`/keyword of a capability you want
- **Out:** matching Telegram bot listings (name, description, link → `social-profile`/bot handle)
- **Empty/negative result looks like:** no relevant listings, or listings for bots that are dead/renamed — Telegram bots churn fast, so a directory entry is a lead, not a guarantee the bot still works.

## Gotchas & OpSec
- Listings are self-submitted and often stale; verify each bot still exists and does what it claims.
- Directory browsing is passive, but *using* an OSINT bot is active and exposes your Telegram identity to the bot's operator — always use a burner account.
- Many "OSINT" Telegram bots trade in leaked/illegal data; weigh legality and provenance before relying on results.

## Overlaps ("do both")
- Pairs with Telegram-native search/monitoring tools — this finds the bot; those help you work the channels and messages once you're in.

## Trust & verifiability
`trust: community` — an unofficial aggregator of self-listed bots; nothing here is vetted, so treat discovered bots as untrusted until you test them yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chatbottle-telegram-bots |
| category | messaging |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
