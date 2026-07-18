---
id: minesight
name: MineSight
description: Use when you have a Minecraft `username` (or UUID) and want to see where that player has been active — returns servers seen, past usernames, and any linked `social-profile`.
url: https://github.com/Gobutsu/MineSight
category: social-networks
path:
- social-networks
bestFor: Pivoting a Minecraft nickname into server history, old nicknames, and self-disclosed social links.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, open-source (AGPL-3.0); install locally via pip/pipx, no account.
opsec: passive
opsecNote: Queries public server-side player data, not the target's own machine or Mojang login. It does not notify the player. Run from a sock-puppet environment as normal hygiene, but this does not touch the subject directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project (~50+ stars) by an independent developer; verify against the current repo, as it relies on third-party server data sources that can change or break.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Gobutsu/MineSight
tags:
- Social Media
- Minecraft
- username
- gaming-osint
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# MineSight

> A Minecraft-focused OSINT CLI: give it a nickname and it surfaces the servers a player has appeared on plus the profile crumbs those servers expose.

## When to use
You have a subject's Minecraft `username` (or their account UUID) — often the same handle they reuse elsewhere — and you want to expand it. Servers frequently publish player data the player never realises is public: last-seen dates, previous nicknames, language, and sometimes self-entered social links. Useful when a gaming handle is your only lead on a younger or gaming-active subject.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pipx install minesight` (or clone the repo and `python setup.py install`).
2. Run by name: `minesight -u <username>` — or by account id: `minesight -i <UUID>`.
3. Read the output: a compiled list of servers where the account was active, plus the public profile fields those servers expose (last seen, old usernames, links).
4. Pivot: an old `username` re-runs across username-search tools; a self-disclosed `social-profile` link jumps you to a real social account.

## Inputs → Outputs
- **In:** `username` (Minecraft nickname) or account UUID
- **Out:** list of servers seen, historical `username` changes, and any linked `social-profile`
- **Empty/negative result looks like:** no servers return data for that nickname — the player may be inactive, on private servers, or the name is wrong; absence is not proof the account doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none once installed; it's a straight CLI query.
- Depends on third-party server/data endpoints — if those rate-limit or go offline, results thin out or the tool errors. Check the repo's issues if it returns nothing.
- OpSec: passive — you query public server records, not the player. No notification is sent, but still run from an isolated environment.
- UUID input is more reliable than a nickname, since nicknames change; resolve the UUID first if you have it.

## Overlaps ("do both")
- Complements general username-enumeration tools: this is the Minecraft-ecosystem specialist that generic name-checkers miss, while they cover mainstream social platforms it doesn't.

## Trust & verifiability
`trust: community` — an independent open-source project; the code is inspectable but it leans on external server data whose accuracy and availability you can't guarantee, so corroborate any lead before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | minesight |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
