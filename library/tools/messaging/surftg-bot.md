---
id: surftg-bot
name: Surftg_bot
description: Use when you have a `name`, `username`, or keyword and want to find matching Telegram messages/channels via a search bot — returns `social-profile` and message leads.
url: https://t.me/surftg_bot
category: messaging
path:
- messaging
bestFor: Full-text searching public Telegram messages and channels for a name, username, or keyword from inside Telegram.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Free keyword/username searches with result limits; heavier use or full result sets may be credit-gated.
opsec: passive
opsecNote: Searches already-public Telegram content, not the subject's account, so it does not alert them. The bot operator logs your search terms — run from a sock-puppet Telegram account, especially since your queries reveal who/what you are investigating.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous Russian-language Telegram search bot ("Поиск по телеграм"); index coverage and freshness are undocumented, and results are only as complete as its crawl.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- surftg_bot
- Surf TG search
tags:
- telegram
- message-search
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Surftg_bot

> A Telegram-native search bot — hunt a subject's name, username, or a keyword across public channels and messages without leaving the app.

## When to use
You have a subject's `username`, `name`, or a distinctive keyword (phone, handle, nickname) and want to find where it appears in public Telegram channels and group messages. Telegram's own search is weak across channels you haven't joined; a search bot surfaces mentions, channel memberships, and leaked-data posts that pin a person to a community or activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open https://t.me/surftg_bot and press Start.
2. Send the search term — a username, real name, or keyword.
3. Read the returned hits: matching messages/channels with links (`social-profile`), letting you jump to the source post.
4. If results are truncated behind a credit wall, refine the query rather than paying an anonymous operator.
5. Pivot: a channel a subject posts in reveals associates and interests; a username hit feeds cross-platform username search.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** matching Telegram messages/channels (`social-profile` links, `username`s)
- **Empty/negative result looks like:** "nothing found" — the term isn't in the bot's index (it only covers channels it has crawled, so absence is not proof the subject has no Telegram presence).

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account-login; use a sock puppet, since your queries expose your investigative interest to the operator.
- Coverage is partial and undocumented — a single search bot never indexes all of Telegram; run the same term through more than one.
- Russian-language interface; be precise with terms, and beware that some "found" content may itself be scraped/leaked data of dubious legality.

## Overlaps ("do both")
- Pairs with other Telegram search/index bots and with cross-platform username tools — no single Telegram searcher is complete, so triangulate.

## Trust & verifiability
`trust: unverified` — an anonymous Telegram search front-end; treat hits as leads and always open the linked source message to confirm context before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | surftg-bot |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
