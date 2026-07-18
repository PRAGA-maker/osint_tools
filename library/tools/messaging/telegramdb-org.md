---
id: telegramdb-org
name: TelegramDB.org
description: Use when you have a Telegram `username`/id and want the groups and channels a user belongs to — returns `social-profile` links, group memberships and `associate` context from public Telegram spaces.
url: https://telegramdb.org/
category: messaging
path:
- messaging
bestFor: Finding which public Telegram groups/channels a username has appeared in, and resolving ids to usernames.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- username
status: live
pricing: freemium
costNote: Free tier via the @tgdb_search_bot Telegram bot (basic resolve/search); advanced queries (e.g. /where membership lookups) on TgDB Search Plus require purchased credits.
opsec: passive
opsecNote: Queries run against TgDB's own crawled index of public Telegram content, not against the target's account, so the user is not notified. You must use a Telegram account to run the bot — use a sock-puppet Telegram number/account, never your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: chrome-mcp
trust: community
trustNote: Third-party crawler of public Telegram groups/channels; listed in Bellingcat's investigation toolkit, but data is scraped and unofficial — treat as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- telegramdb
aliases:
- TgDB
- TelegramDB
- tgdb.org
tags:
- telegram
- messaging
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# TelegramDB.org

> A searchable index of public Telegram groups, channels and their members — resolve a username/id and, crucially, list the groups a user has been seen in.

## When to use
You have a Telegram `username` (or numeric id) tied to a subject and want to expand from a single handle to their community footprint: which public groups and channels they participate in, and who they interact with. The `/where` lookup — listing groups a user has appeared in — is the high-value pivot, turning one handle into a map of interests, affiliations and potential `associate`s.

## How to use it (`bestInteractionPattern`: chrome-mcp)
1. Open Telegram (web or app) in a sock-puppet account and start the free bot **@tgdb_search_bot** (or use the web front-end at tgdb.org).
2. Use `/resolve <id or @username>` to convert between a user/group/channel id and its username and confirm the handle exists.
3. Use `/search <keywords>` to find groups/channels by topic, and `/where <user>` to list the public groups a user has been seen in (advanced/credit-gated on Search Plus).
4. Pivot: group memberships reveal interests, language and affiliations; co-members feed `associate` mapping; a resolved username/id feeds other Telegram-OSINT tools.

## Inputs → Outputs
- **In:** `username` or numeric Telegram id
- **Out:** `social-profile` (resolved Telegram identity + linked groups/channels), group/channel memberships, `associate` (co-members), confirmed `username`
- **Empty/negative result looks like:** "not found" / no groups — the user or space isn't in TgDB's crawl (private or never-indexed), which is common; absence is not proof of non-membership.

## Gotchas & OpSec
- Human-in-the-loop: you must drive a Telegram bot from an account — always a sock puppet, never an attributable number.
- Only PUBLIC groups/channels are indexed; private chats are invisible, and the crawl is partial and time-lagged.
- Advanced membership lookups consume paid credits; the free bot covers resolve/keyword search. Treat everything as leads to corroborate, not confirmed fact.

## Overlaps ("do both")
- Pairs with `[[telegramdb]]` (same provider) and other Telegram username tools — TgDB's group-membership angle complements handle-existence checkers, so run both to both confirm the account and map where it operates.

## Trust & verifiability
`trust: community` — TgDB scrapes public Telegram; it is well-known (featured in Bellingcat's toolkit) but unofficial, so verify memberships by viewing the actual public group where possible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegramdb-org |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile, associate, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | chrome-mcp |
| opsec | passive |
| human-in-loop | yes (account-login) |
