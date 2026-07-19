---
id: telegram-group-joiner
name: Telegram Group Joiner
description: Use when you have a list of Telegram group/channel links and want a research account joined to all of them at once — a batch-join helper; enables monitoring, returns access to those `social-profile`s.
url: https://bellingcat.github.io/telegram-group-joiner/
category: messaging
path:
- messaging
bestFor: Bulk-joining many public/private Telegram groups and channels with one research account so you can monitor them for a topic or person.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (MIT), browser-based; runs client-side. No paid tier.
opsec: active
opsecNote: This is ACTIVE — you log a real Telegram account in and it joins groups, which is visible to admins and other members and can expose your account. Use a dedicated, non-personal research account with a burner number and a VPN, never your own; Telegram may rate-limit or block accounts that mass-join. You need your own api_id/api_hash from my.telegram.org.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Bellingcat as part of their public Online Investigation Toolkit; open-source and client-side (uses tdlib, no server-side data retention).
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: false
relatedTools:
- bellingcat-name-variant-search
- bellingcat-tiktok-date-extract
aliases:
- Bellingcat Telegram Group Joiner
tags:
- bellingcat-toolkit
- telegram
- monitoring
source: bellingcat-toolkit
lastVerified: '2026-07-19'
enrichment: full
---

# Telegram Group Joiner

> Bellingcat's browser tool that logs in one Telegram account and batch-joins a list of groups/channels — set up monitoring of many communities in one pass.

## When to use
You have (or are building) a list of Telegram groups/channels relevant to a topic, region, or person and want a single research account inside all of them so you can then read and monitor. It automates the tedious one-by-one joining; the actual reading/searching happens afterwards in Telegram.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create Telegram developer credentials (`api_id`/`api_hash`) at my.telegram.org, using a dedicated research account.
2. Open https://bellingcat.github.io/telegram-group-joiner/ in a modern desktop browser (Chrome/Firefox/Edge).
3. Log in with the research account (phone + code, possibly a 2FA password / email verification).
4. Paste the group/channel links (public `t.me/...` and private invite links). You can also preload them via `?links=` (semicolon-separated) in the URL.
5. Run it: the account joins each group. Then switch to Telegram to read/search the joined communities.

## Inputs → Outputs
- **In:** a list of Telegram group/channel links (`social-profile`s)
- **Out:** your research account joined to those groups (access to their `social-profile` content for monitoring)
- **Empty/negative result looks like:** "Limit reached" after ~500 groups/channels (Telegram's per-account cap), or a link that fails because it's invalid/expired/banned — swap accounts or prune the list.

## Gotchas & OpSec
- **Active and account-risky:** mass-joining can get an account rate-limited or banned; only ever use a disposable research account (burner number, VPN), never your personal one.
- Client-side (tdlib) so no third-party server sees your session, but Telegram itself and group admins see the joins.
- Human-in-the-loop: full Telegram login (code + possible 2FA).

## Overlaps ("do both")
- Pairs with Telegram search/monitoring tools (e.g. Telegago) — this gets you *into* the groups; those help you search across them once joined.

## Trust & verifiability
`trust: trusted` — a Bellingcat toolkit tool, open-source and client-side; the code is inspectable and the org is reputable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-group-joiner |
| category | messaging |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
