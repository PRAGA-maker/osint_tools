---
id: reddit-com-2
name: reddit.com (r/Telegram — find a user's ID)
description: Use when you have a Telegram `username` and want the account's stable numeric user ID — this is a community how-to thread describing the bot-forwarding technique, returning a persistent social-profile identifier.
url: https://www.reddit.com/r/Telegram/comments/1f2p61w/how_to_find_another_users_id/
category: messaging
path:
- messaging
bestFor: Learning how to resolve a Telegram handle to its immutable numeric user ID so you can track an account across username changes.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free — a public Reddit discussion thread. The technique it describes uses free Telegram bots; a Telegram account is needed to actually run it.
opsec: active
opsecNote: Reading the thread is passive, but executing the technique is ACTIVE — resolving an ID by forwarding a target's message to a lookup bot means you are operating inside Telegram from an account. Use a dedicated sock Telegram account; forwarding/interaction can be visible.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A Reddit thread, not a tool — crowd-sourced guidance. The core technique (bots like @userinfobot / @getidsbot returning the numeric ID) is well established, but verify any specific bot before trusting it with data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- here
- r-opendirectories
- reddit
- reddit-askmeanything
- reddit-com
- reddit-darknet
- reddit-deep-web
- reddit-guide-to-opting-out-of-background-check-websites
- reddit-old-reddit-search
- reddit-onions
- reddit-r-translator
aliases:
- Telegram user ID lookup
- how to find another user's Telegram ID
tags:
- telegram
- Telegram
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# reddit.com (r/Telegram — find a user's ID)

> A community how-to thread, not a tool: it explains how to resolve a Telegram username to the account's immutable numeric user ID — the identifier that survives handle and display-name changes.

## When to use
You have a Telegram `username` (which the owner can change at will) and need the account's stable numeric user ID so you can keep tracking it even after they rename. This thread documents the standard technique. Treat this file as a **reference to a method**, and reach for it whenever a Telegram investigation needs a durable identifier rather than a mutable handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the thread at the URL for the current community-recommended approach and which lookup bots people trust.
2. The core method: from a **sock** Telegram account, forward a message from (or referencing) the target to an ID-lookup bot such as `@userinfobot` or `@getidsbot`, or open the target's profile and use a bot/client that exposes the numeric ID.
3. Read the output: a numeric user ID (a long integer). This ID is immutable — record it as the account's canonical key.
4. Pivot: the numeric ID lets you re-find the account after username changes and feeds other Telegram-intel tools that key on user ID rather than handle.

## Inputs → Outputs
- **In:** `username` (or a forwarded message from the target)
- **Out:** `social-profile` — the account's persistent numeric Telegram user ID
- **Empty/negative result looks like:** a bot returns no ID / an error — usually because the account is too locked-down to forward from, the handle is wrong, or the bot is defunct. Try an alternate bot.

## Gotchas & OpSec
- This is a Reddit thread; the specific bots it names can change or go rogue — re-verify a bot's reputation before sending it anything.
- Human-in-the-loop: you must manually run the technique inside Telegram and judge which bot to trust.
- OpSec: executing it is **active** and account-bound — use a dedicated sock Telegram account; forwarding a message can reveal interaction. Never do this from a personal account.

## Overlaps ("do both")
- Complements any Telegram intelligence tool that keys on numeric user ID — this thread teaches you how to obtain that ID in the first place.

## Trust & verifiability
`trust: community` — crowd-sourced Reddit guidance. The underlying technique is sound and widely used, but the trust sits with the individual bot you choose, so confirm the returned ID against a second bot when it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-com-2 |
| category | messaging |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
