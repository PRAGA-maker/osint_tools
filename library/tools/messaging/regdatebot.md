---
id: regdatebot
name: RegDateBot (Telegram)
description: Use when you have a Telegram `username` or account and want to estimate when it was created — returns an approximate account registration date to age-check and disambiguate accounts.
url: https://t.me/regdate_clone_bot
category: messaging
path:
- messaging
bestFor: Estimating the creation/registration date of a Telegram account to judge whether it is old/established or freshly made.
selectorsIn:
- username
- social-profile
selectorsOut: []
status: live
pricing: free
costNote: Free Telegram bot; you only need a Telegram account to message it.
opsec: active
opsecNote: You send the target's Telegram ID/username to an unknown third-party bot operator, who sees both your account and the query. Use a sock-puppet Telegram account, and note that forwarding a message from the target to a bot can, in some setups, be observable — prefer looking up by numeric ID.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party "clone" bot of unknown operator; the registration date is an ESTIMATE derived from the sequential Telegram user ID, not an official timestamp, and the operator could log or mishandle queries.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- regdate_clone_bot
- Telegram registration date bot
tags:
- telegram
- account-age
- messaging
source: awesome-osint
lastVerified: '2026-07-13'
enrichment: full
---

# RegDateBot (Telegram)

> A Telegram bot that estimates when an account was created, from its numeric user ID — a fast age-check that helps tell an established account from a throwaway.

## When to use
You are investigating a Telegram account (you have its `username` or a `social-profile`/forwarded message) and want to know roughly how old it is. A creation-date estimate helps you judge credibility (a "long-standing" persona on a 2-week-old account is a red flag), corroborate that an account predates events it claims to, or disambiguate two similar handles.

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sock-puppet Telegram account, open the bot at https://t.me/regdate_clone_bot and start it.
2. Provide the target's Telegram numeric user ID, or forward a message from the account (a message forward can reveal the underlying ID the bot uses).
3. Read the returned approximate registration date.
4. Cross-check with another age bot (e.g. Creation Date bot) since these are all estimates.
5. Pivot: an account-age estimate contextualises other Telegram-OSINT findings (username history, groups) rather than yielding identity directly.

## Inputs → Outputs
- **In:** Telegram `username` / numeric ID / forwarded message (`social-profile`)
- **Out:** an approximate account creation/registration date (an account-age estimate, not a fixed identity selector)
- **Empty/negative result looks like:** the bot can't resolve the ID, returns a vague/wide range, or is offline — clone bots come and go; try an alternative regdate/creation-date bot before concluding anything.

## Gotchas & OpSec
- The date is an **estimate** interpolated from Telegram's roughly sequential user IDs — treat it as approximate, never exact.
- Human-in-the-loop: requires a Telegram account to message the bot; use a research account, never your own.
- OpSec: **active** — you hand the target's ID to an unknown operator. Assume queries are logged; prefer ID lookup over forwarding a message when discretion matters.

## Overlaps ("do both")
- Pairs with other Telegram-OSINT bots (username-history, ID resolvers) — do both: registration date plus username history and group membership together build the account's provenance.

## Trust & verifiability
`trust: unverified` — an anonymous third-party clone bot producing estimates; corroborate the date with a second bot and never treat it as an official timestamp.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regdatebot |
