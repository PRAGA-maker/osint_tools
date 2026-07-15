---
id: getchatlist
name: getChatList (GetChatListBot)
description: Use when you have a Telegram `username` or user ID and want to map which groups/channels that account belongs to — returns the list of Telegram communities the account is in, exposing associates and interests.
url: https://telegram.me/getchatlistbot
category: messaging
path:
- messaging
bestFor: Discovering which Telegram groups/channels a given username or user ID is a member of, to map a subject's communities and associates.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free Telegram bot; you only need a Telegram account to message it.
opsec: active
opsecNote: You send the subject's username/ID to a third-party bot backed by an unofficial scraped index; the operator can log your queries and your Telegram account. Query from a sock-puppet Telegram account, not one linked to you. This does not notify the target, but you are trusting an opaque operator with the identifiers you search.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known Telegram OSINT bot with a large scraped catalogue (hundreds of thousands of channels, tens of millions of users); coverage is partial and historical, so absence of a group is not proof of non-membership.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- GetChatListBot
- getchatlistbot
tags:
- telegram
- group-membership
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# getChatList (GetChatListBot)

> A Telegram OSINT bot that reverses a username/ID into the groups and channels it belongs to — turning one handle into a map of a subject's communities and the people around them.

## When to use
You have a Telegram `username` or numeric user ID and want to know which groups/channels that account participates in. Membership reveals a subject's interests, ideology, local communities, and — crucially — `associate` leads (co-members you can then investigate). It works against a pre-scraped index of channels/users, so it can surface communities you'd never find by browsing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telegram.me/getchatlistbot in Telegram (web/desktop/mobile) using a dedicated sock-puppet account.
2. Start the bot and send the target Telegram `username` (or numeric user ID; resolve a username to an ID first if the bot requires it).
3. Read the returned list of groups/channels the account is indexed as belonging to.
4. Corroborate: the index is partial and historical — a listed group is a strong lead, but confirm current membership by checking the group directly where feasible; an empty result is not proof the account joined nothing.
5. Pivot: notable groups feed community/channel analysis; co-members feed `associate` investigation; the confirmed username feeds cross-platform username search.

## Inputs → Outputs
- **In:** Telegram `username` or user ID (`social-profile`)
- **Out:** list of groups/channels (`social-profile`), co-member `associate` leads
- **Empty/negative result looks like:** the bot returns no groups — meaning the account isn't in its scraped index for any public group, NOT that the person has no Telegram activity (private/unindexed groups won't show).

## Gotchas & OpSec
- Human-in-the-loop: requires a Telegram account to message the bot; use a sock puppet.
- Coverage: the index is a snapshot of public/scraped groups — partial and dated. Treat hits as leads and misses as inconclusive.
- OpSec: **active** — you disclose the subject's identifier to an opaque third-party operator who can log it. Never use your real Telegram account.

## Overlaps ("do both")
- Pairs with other Telegram OSINT bots and channel-search tools (and `[[opendatauabot]]` for region-specific data) — coverage of the scraped indexes differs, so a group missed by one bot may appear in another.

## Trust & verifiability
`trust: community` — a widely-cited Telegram OSINT bot, but it relies on an unofficial scraped catalogue with partial, historical coverage, so verify membership at the source and don't treat an empty result as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | getchatlist |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
