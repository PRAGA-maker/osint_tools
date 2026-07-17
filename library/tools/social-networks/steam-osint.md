---
id: steam-osint
name: Steam-OSINT
description: Use when you have a Steam `username`/profile ID and want mutual-friend mapping and past-nickname/URL history — returns `associate` links and prior `social-profile` identifiers.
url: https://github.com/matiash26/steam-osint
category: social-networks
path:
- social-networks
bestFor: Mapping a Steam account's mutual friends and pulling its history of previous names and profile URLs.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free and open source (Python); run locally. Uses public Steam profile data and typically a (free) Steam Web API key.
opsec: passive
opsecNote: It reads public Steam profile data via the API rather than interacting with the target, so there's no notification to the subject. Provide a Steam Web API key tied to a sock-puppet Steam account, not your real one.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A community Python tool over Steam's public data; results (mutual friends, name history) are only as complete as the profiles' privacy settings allow, so absence often means "private", not "none".
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- steam-osint-tool
aliases:
- Steam-OSINT
- matiash26/steam-osint
tags:
- steam
- gaming
- friend-mapping
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Steam-OSINT

> A Python tool for Steam accounts: map mutual friends between profiles and recover an account's history of past nicknames and profile URLs.

## When to use
Your subject games on Steam and you have a `username`, vanity URL, or SteamID. Steam-OSINT does two useful things: it finds mutual friends between accounts (mapping a social graph and revealing shared connections/`associate` links), and it pulls the account's history of previously used names and URLs — a strong pivot when someone rebranded a handle you're trying to correlate across platforms. Gaming identities are often a person's most candid and long-lived online footprint.

## How to use it (`bestInteractionPattern`: cli)
1. Install: clone `github.com/matiash26/steam-osint` and `pip install` its requirements; obtain a free Steam Web API key (register it to a sock-puppet Steam account).
2. Resolve the target to a SteamID64 (the tool/Steam handles vanity-URL resolution).
3. Run the analysis: pull the friend list, compute mutual friends against other accounts of interest, and fetch the name/URL history.
4. Record prior nicknames and URLs — these are your cross-platform correlation seeds.
5. Pivot: past handles feed username search across other sites; mutual friends feed associate mapping; a linked profile may expose real-name, location, or other games.

## Inputs → Outputs
- **In:** `username` / vanity URL / SteamID
- **Out:** `associate` (friends and mutual-friend links) and `social-profile` (previous nicknames and profile URLs)
- **Empty/negative result looks like:** empty friends/history — the profile's friend list and details are set to private (very common on Steam), so you get nothing; treat as "locked down", not "no connections".

## Gotchas & OpSec
- Privacy settings gate everything: Steam users can hide friends, games, and history — a private profile yields little regardless of the tool.
- API key required: needs a Steam Web API key; register it under a burner Steam account.
- Name-history reliability: recovered nicknames are strong leads but confirm before asserting an identity link.
- OpSec: passive (API reads), but tie the key to a sock puppet.

## Overlaps ("do both")
- Pairs with `[[steam-osint-tool]]` and general username-enumeration tools — recover past Steam handles here, then sweep them across other platforms; cross-reference friends against the subject's accounts elsewhere to confirm the social graph.

## Trust & verifiability
`trust: community` — an open-source tool reading Steam's own public API, so its data is authentic where profiles are public; completeness is bounded by privacy settings, and identity links from shared handles still need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam-osint |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
