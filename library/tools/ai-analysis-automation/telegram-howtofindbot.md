---
id: telegram-howtofindbot
name: Telegram HowToFindBot
description: Use when you have a `username` or `email` and want a per-platform checklist of where and how to look for it — returns curated OSINT method links (social-profile leads), not the data itself.
url: https://t.me/HowToFindBot
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Getting a fast, platform-by-platform "how would I find this?" playbook inside Telegram.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Telegram bot; requires a Telegram account to message it.
opsec: passive
opsecNote: Passive to the subject — you query a bot, not the target's accounts. But you are handing your selectors to a third-party Telegram bot operator; use a sock-puppet Telegram account and assume queries are logged.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Front-end for the open-source HowToFind-bot/osint-tools catalogue on GitHub; community-maintained, and it returns method/link guidance rather than raw personal data.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- HowToFind bot
- HowToFind-bot
tags:
- Tools collections/toolkits
- telegram-bot
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Telegram HowToFindBot

> A Telegram bot that turns a selector into a research plan: pick a platform and it lists the OSINT tools and techniques for finding an account there.

## When to use
You have a `username` or `email` and want a quick, structured reminder of *where to look* — which resources exist for Facebook, Instagram, LinkedIn, GitHub, Gmail, Telegram, TikTok, Twitter/X and dozens more. It is a signpost/checklist tool: it does not resolve the selector itself, it tells you which tools to run next.

## How to use it (`bestInteractionPattern`: web-manual, via Telegram)
1. Open https://t.me/HowToFindBot in Telegram (sock-puppet account recommended) and press Start.
2. Choose a target platform from the bot's menu (or send the platform name).
3. The bot returns the catalogue of methods/links for finding and enumerating accounts on that platform.
4. Pivot: run the suggested tools against your `username`/`email`; the bot itself produces no `social-profile` hits, only the route to them. The same catalogue is browsable at github.com/HowToFind-bot/osint-tools.

## Inputs → Outputs
- **In:** `username` or `email` (conceptually — you supply these to the tools it recommends)
- **Out:** curated links/methods toward `social-profile` discovery
- **Empty/negative result looks like:** a platform with no listed methods simply has no curated entry yet — not evidence the account doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in Telegram account (`account-login`).
- It is a meta-tool: expect guidance and links, not finished intelligence. Budget time to actually run the recommended tools.
- Third-party bot: don't feed it live-case sensitive selectors you wouldn't want logged.

## Overlaps ("do both")
- Complements automated username-enumeration tools (Sherlock/Maigret-class): HowToFindBot tells you *what to try*, the enumerators *do the trying* at scale.

## Trust & verifiability
`trust: community` — it fronts a public, open-source OSINT catalogue on GitHub; treat its links as leads to verify, and confirm the catalogue is current since directory bots drift as tools die.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-howtofindbot |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
