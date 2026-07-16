---
id: toutatis
name: Toutatis
description: Use when you have an Instagram `username` and want to pull the account's hidden contact data — returns obfuscated email/phone, the numeric user ID and linked profile details.
url: https://github.com/megadose/toutatis
category: social-networks
path:
- social-networks
bestFor: Extracting an Instagram account's partially-hidden email/phone, user ID and profile metadata from just the handle.
selectorsIn:
- username
selectorsOut:
- email
- phone
- name
- social-profile
status: live
pricing: free
costNote: Free, open-source (GPL) Python tool; no payment. It does require a valid Instagram session cookie, which means a (free) Instagram account.
opsec: active
opsecNote: Toutatis authenticates with an Instagram sessionid cookie, so every query is made AS that logged-in account — use a dedicated sock-puppet Instagram account on a burner, never a real or investigator account. Heavy use can get the puppet flagged or banned.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A well-known, widely-used tool by researcher megadose (Palenath); open-source and auditable, but it depends on Instagram's private endpoints, which change and can break it.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- megadose toutatis
tags:
- instagram
- account-enumeration
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- holehe
- onion-search
- palenath
---

# Toutatis

> A CLI tool that squeezes an Instagram handle for the obfuscated email/phone and numeric ID Instagram exposes to logged-in clients — a fast way to pivot from a username to contact leads.

## When to use
You have an Instagram `username` (or a known Instagram profile) and want more than the public bio: Instagram's app-facing endpoints leak a partially-masked recovery `email`/`phone`, the account's numeric `user ID`, and other profile metadata. Reach for Toutatis to convert a handle into contact-shaped leads and a stable user ID that survives username changes.

## How to use it (`bestInteractionPattern`: cli)
1. `pip3 install toutatis` (or clone https://github.com/megadose/toutatis).
2. Obtain an Instagram `sessionid` cookie from a **sock-puppet** Instagram account (log in via browser, copy the cookie).
3. Run `toutatis -u target_username -s YOUR_SESSIONID` (or `-i <userid>`).
4. Read the output: obfuscated email (e.g. `j****@g****.com`), obfuscated phone (e.g. `+1 *** *** **89`), the numeric user ID, and profile flags.
5. Pivot: the masked email/phone hints feed `[[account-live-com]]`-style existence checks and phone-OSINT; the numeric ID anchors the account across username changes; run the same account through `[[palenath]]`/Holehe.

## Inputs → Outputs
- **In:** `username` (Instagram handle) or numeric user ID
- **Out:** obfuscated `email`, obfuscated `phone`, numeric user ID, display `name`, `social-profile` metadata
- **Empty/negative result looks like:** an error/empty result if the account is private, deleted, or the sessionid is invalid/expired; masked fields may be blank if the account has no linked recovery email/phone.

## Gotchas & OpSec
- Human-in-the-loop: requires a live Instagram sessionid — treat the sock-puppet cookie as disposable; rotate if flagged.
- Masks are partial: the revealed characters are leads, not the full address/number — never present them as confirmed.
- Fragility: Instagram changes endpoints often; check the repo's recent commits/issues before trusting a clean run.
- OpSec: **active** — queries run as your logged-in puppet account.

## Overlaps ("do both")
- Pairs with `[[palenath]]`/Holehe — Toutatis extracts the masked email; Holehe/Ignorant then map where that email/phone is registered.
- Pairs with `[[account-live-com]]` — turn a masked recovery hint into a confirmed provider account.

## Trust & verifiability
`trust: community` — open-source and battle-tested in the OSINT community, but reliant on Instagram's private endpoints; a broken/empty run may mean the tool is stale rather than the account absent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toutatis |
