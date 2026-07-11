---
id: mothersearchbot
name: MotherSearchBot (Telegram search)
description: Use when you have a `username`, `name` or keyword and want to search across Telegram for channels, groups and messages mentioning it — returns social-profile presence and associate links inside Telegram.
url: https://t.me/MotherSearchBot
category: messaging
path:
- messaging
bestFor: Keyword/name search of Telegram channels, groups and discussions to locate a subject's presence or mentions.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to use in Telegram; some search bots of this class add paid tiers for deeper history, but the core search runs without payment.
opsec: active
opsecNote: You must query the bot from a Telegram account — use a sock-puppet, not your real account. The operator can log your queries. Searching does not notify the subject, but joining or interacting with any channel the search surfaces is visible to that channel's admins.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: chrome-mcp
trust: unverified
trustNote: An anonymously operated Telegram search bot; results are unranked and unvetted, and coverage of Telegram's private/closed spaces is inherently partial. Corroborate any hit by opening the source directly.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- MotherSearch
tags:
- telegram
- search-engine
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# MotherSearchBot (Telegram search)

> A Telegram-native search bot for finding channels, groups and message mentions by keyword or name — a way into Telegram's content that the app's own search covers poorly.

## When to use
You want to find where a subject appears inside Telegram: channels/groups they run or are discussed in, or messages mentioning their `name`/`username`/handle. Useful early when you know a person is active on Telegram but don't yet have their specific account or communities.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. From a **sock-puppet** Telegram account, open https://t.me/MotherSearchBot and `/start` (it prompts for a language).
2. Send your query — a username, name, or keyword.
3. The bot returns matching Telegram channels/groups/discussions.
4. Open results *read-only*; note channels and participants of interest without joining where possible.
5. Pivot: a discovered account feeds `[[username-to-id-bot]]` for a permanent ID; group membership and mentions surface `associate` links; channel content can reveal `geolocation`, activity times and other selectors.

## Inputs → Outputs
- **In:** `username`, `name`, or free-text keyword
- **Out:** matching Telegram channels/groups/messages — i.e. `social-profile` presence and `associate` (co-members, people mentioning the subject)
- **Empty/negative result looks like:** no matches — expected for private/closed communities the bot can't index; absence is not proof the subject is not on Telegram.

## Gotchas & OpSec
- Coverage is partial: bots like this index public/known channels, not private groups — a null result mostly means "not in the indexed set."
- Results are unranked and can be noisy; verify each hit by opening the source in Telegram.
- OpSec: **active** — query from a research account; the operator logs searches, and joining a surfaced channel exposes your sock-puppet to its admins.

## Overlaps ("do both")
- Pairs with `[[username-to-id-bot]]` (resolve the discovered handle to a stable ID) and with `[[telegram-finder-telegram-finder-io]]` (reverse a phone/email into the account) — this bot searches by keyword, those pivot on identifiers.

## Trust & verifiability
`trust: unverified` — an anonymous search bot with opaque, partial indexing. Treat every result as a lead to confirm directly in Telegram, never as authoritative coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mothersearchbot |
| category | messaging |
| selectorsIn → selectorsOut | username, name → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | chrome-mcp |
| opsec | active |
| human-in-loop | yes (account-login) |
