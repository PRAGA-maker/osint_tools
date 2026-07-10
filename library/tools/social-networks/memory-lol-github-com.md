---
id: memory-lol-github-com
name: memory.lol (github.com)
description: Use when you have a Twitter/X `username` or numeric account ID and want its historical screen-name changes — returns prior `username`s and account identity continuity.
url: https://github.com/travisbrown/memory.lol/
category: social-networks
path:
- social-networks
bestFor: Looking up the past screen-name history of a Twitter/X account to defeat username changes and confirm account identity over time.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free service and open-source. Unauthenticated access is limited to name changes observed in the last ~60 days; logging in with GitHub/Google unlocks more, and full multi-year histories are reserved for vetted researchers/journalists.
opsec: passive
opsecNote: You query memory.lol's archived dataset (built from the Internet Archive Twitter Stream Grab and Wayback Machine), not the target's live account, so nothing touches the subject. Optional GitHub/Google login ties queries to that identity — use a research account if you authenticate.
humanInLoop: false
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: trusted
trustNote: Maintained by researcher Travis Brown; data derived from Internet Archive sources, widely cited in the OSINT community as reliable for Twitter username history.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- memory.lol
- Twitter username history
tags:
- xtwitter
- X / Twitter Related Sites
- username-history
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# memory.lol (github.com)

> Travis Brown's archive of Twitter/X screen-name history — map a current handle or account ID back to every username it has used since 2011.

## When to use
You have a Twitter/X `username` (or the account's numeric ID) and need to know what handles that same account used before — essential when a subject renames their account to shed history, or when you must prove that two differently-named accounts are actually the same underlying ID. Also lets you catch a suspect who took over an abandoned handle.

## How to use it (`bestInteractionPattern`: api)
1. Query the web app at https://memory.lol/app/ or hit the JSON API directly: `https://memory.lol/tw/<username>` (also supports lookup by numeric account ID).
2. Read the JSON: it returns the account's numeric ID and a list of screen names with the date ranges each was observed.
3. For fuller history, log in via GitHub/Google (research account); unauthenticated results are capped to recent (~60-day) observations for most accounts.
4. Pivot: feed each historical `username` into cross-platform username search (`[[whatsmyname-python]]`, `[[spy]]`) and archive/search tools to recover deleted content posted under old handles.

## Inputs → Outputs
- **In:** `username` (or numeric Twitter/X account ID)
- **Out:** prior `username`s with observed date ranges, the stable numeric account ID, and thus `social-profile` continuity
- **Empty/negative result looks like:** an empty/`{}` JSON or "no data" — the account has no archived name changes in the dataset (common for newer or low-profile accounts), not proof the account never renamed.

## Gotchas & OpSec
- Coverage is best from 2011 onward (when the Internet Archive stream grab began); older or very new accounts may be sparse.
- Public access is deliberately throttled to recent observations; full histories require vetted access.
- Passive; only optional login is attributable.

## Overlaps ("do both")
- Pairs with `[[wayback-machine-2]]` and Twitter bio-history tools (e.g. lolarchiver) — memory.lol gives the handle timeline, the archive tools recover the content posted under each handle.

## Trust & verifiability
`trust: trusted` — maintained by a known researcher and sourced from the Internet Archive; the historical mappings are well-regarded and reproducible via the open JSON API.
