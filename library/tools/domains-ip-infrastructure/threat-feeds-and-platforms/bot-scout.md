---
id: bot-scout
name: Bot Scout
description: Use when you have an `email`, `ip-address`, or `username` and want to check it against a database of known bots/spammers — returns a bot/not-bot verdict with sighting details.
url: https://botscout.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Checking whether an email/IP/username is a known bot or spammer account.
selectorsIn:
- email
- ip-address
- username
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: Free lookups (~1,500/day without a key; a free API key raises this). No payment for basic use.
opsec: passive
opsecNote: You query BotScout's own database of reported bot signatures, not the person — passive, no signal to the subject. Sending a target's email/IP to a third party is a minor data-sharing consideration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: Long-running community anti-bot database (10M+ signatures); a hit means "reported as a bot", which is a signal, not proof of automation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- BotScout
tags:
- domains-ip-infrastructure
- anti-bot
- reputation
- spam
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Bot Scout

> A reputation database of known bots and spammers — check an email, IP, or username against 10M+ reported signatures to judge whether an account is automated/abusive.

## When to use
You have an `email`, `ip-address`, or `username` tied to a registration, message, or profile and want a quick signal on whether it's a known bot/spammer. Useful for triaging whether an account contacting your subject (or a persona in your investigation) is likely automated, and for cross-checking IPs seen in abuse.

## How to use it (`bestInteractionPattern`: api)
1. Use the web lookup at https://botscout.com/ or the API (`/test/` endpoint) with the `email`, `ip-address`, or `username`.
2. Optionally get a free API key to raise the daily lookup limit.
3. Read the response: whether the identifier matches a known bot, and associated sightings (count, last-seen `ip-address`, country).
4. Pivot: a flagged `ip-address` feeds geolocation/reputation checks; a flagged email/username suggests the account is disposable/automated rather than a real person.

## Inputs → Outputs
- **In:** `email`, `ip-address`, or `username`
- **Out:** bot/not-bot verdict + sighting metadata (count, last `ip-address`, country)
- **Empty/negative result looks like:** no match — the identifier isn't in BotScout's database, which is not proof it's human (many bots are unreported); corroborate.

## Gotchas & OpSec
- A hit means "reported", based on crowd/honeypot data — treat as a strong hint, not a definitive "this is a bot".
- Absence of a hit is weak evidence of legitimacy — the DB is not exhaustive.
- Free daily limits apply; grab a key for volume.

## Overlaps ("do both")
- Pairs with IP-reputation/abuse tools (`[[malwareurl]]`, abuseipdb-style) — BotScout focuses on registration/spam bots; those cover broader malicious-IP reputation. Cross-check for a fuller picture.

## Trust & verifiability
`trust: community` — a long-standing community-fed reputation list; useful as a signal, but every verdict is a crowd-sourced report to weigh, not confirm blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bot-scout |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | email, ip-address, username → ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | passive |
| human-in-loop | no |
