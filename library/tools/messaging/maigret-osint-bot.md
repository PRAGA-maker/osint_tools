---
id: maigret-osint-bot
name: Maigret OSINT bot
description: Use when you have a `username` and want to check thousands of sites for accounts without installing anything — a Telegram bot wrapper for Maigret that returns `social-profile` hits.
url: https://t.me/osint_maigret_bot
category: messaging
path:
- messaging
bestFor: Running Maigret's 3000+-site username search from a Telegram chat, no local install.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free Telegram bot; requires a Telegram account. Third-party bots like this are often rate-limited, intermittently offline, or unmaintained — verify it responds before relying on it.
opsec: active
opsecNote: You send the target's username to an unknown third party's Telegram bot, which sees your Telegram identity and your query, and runs the searches from its own infrastructure. Assume the operator logs everything. Use a sock-puppet Telegram account; for sensitive work run the open-source Maigret locally instead.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An unofficial Telegram front end to the open-source Maigret tool, run by an unknown operator; the underlying Maigret is trusted, but this hosted bot is not verified and could log or alter results.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- whatsmyname-web
- social-analyzer
aliases:
- Maigret bot
- osint_maigret_bot
tags:
- telegram
- username-check
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Maigret OSINT bot

> A Telegram front end to Maigret — the open-source tool that checks a username against 3000+ sites — for when you want the sweep without installing anything.

## When to use
You have a `username` and want a fast, no-install account sweep across thousands of sites, and you're willing to trade OpSec for convenience. Maigret is one of the strongest username-enumeration tools; this bot runs it for you from a Telegram chat. Prefer the local Maigret CLI for anything sensitive — the bot means handing your query to a stranger.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://t.me/osint_maigret_bot in Telegram (use a **sock-puppet** account).
2. Start the bot and send the target `username`.
3. Wait for it to run Maigret's checks; it returns a list of sites where the handle appears to have an account, sometimes with extracted profile details.
4. If the bot is unresponsive or rate-limited (common for public OSINT bots), fall back to running Maigret locally.
5. Pivot: confirm each reported `social-profile` by opening it; feed confirmed handles into per-platform enrichment.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` hits across many sites, occasionally extracted `name`/bio detail
- **Empty/negative result looks like:** no accounts found, or the bot times out/goes silent — with third-party bots, silence often means downtime, not a clean negative.

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram **account**; the bot may be down, rate-limited, or unmaintained.
- OpSec: **active** and higher-risk — an unknown operator receives your Telegram identity and target query and runs searches from their infra. For sensitive investigations, use the open-source Maigret locally instead of this bot.
- Reported hits are heuristic (as with all username checkers); open and verify each before trusting it.

## Overlaps ("do both")
- Same job as `[[whatsmyname-web]]` and `[[social-analyzer]]` with different site coverage — cross-run and union the results; prefer the self-hosted options when OpSec matters.

## Trust & verifiability
`trust: unverified` — the underlying Maigret is well-regarded, but this hosted Telegram bot is operated by an unknown party and cannot be trusted to be private or to return unaltered results. Treat output as leads and verify independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maigret-osint-bot |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
