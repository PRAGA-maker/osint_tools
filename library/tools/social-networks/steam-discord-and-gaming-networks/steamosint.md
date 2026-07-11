---
id: steamosint
name: SteamOSINT
description: Use when you have a Steam `username`/profile URL and want the account's games, playtime, and public friends — returns social-profile and associate links.
url: https://github.com/Frontline-Femmes/Steam-OSINT
category: social-networks
path:
- social-networks
- steam-discord-and-gaming-networks
bestFor: Pulling a Steam account's profile, games library, playtime, achievements, and public friend list from a username or profile URL.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free and open source (GitHub). Uses Steam's public Web API; some endpoints need a free Steam Web API key.
opsec: active
opsecNote: Queries Steam's public Web API and community pages. Read-only profile data does not notify the target, but requests are made from your IP/API key and Steam logs them; if you view a profile while logged in, that can register. Use a Steam Web API key tied to a sock-puppet account and run from a VPN.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community open-source project on GitHub; it wraps Steam's official public API, so the underlying data is authoritative, but the tool is unverified/unmaintained-risk.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- steamid-io
- namemc
aliases:
- Steam-OSINT
- Steam OSINT
tags:
- steam
- gaming
- cli
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# SteamOSINT

> An open-source CLI that turns a Steam username or profile URL into a full public-profile dump — games, playtime, achievements, and the public friend graph.

## When to use
You have a Steam `username`, SteamID, or profile URL and want to profile the account's activity and social graph: which games and how many hours (behavioral fingerprint), achievements/last-online (activity timeline), and public friends (`associate` leads). Gaming identities are a strong pivot in younger-subject and missing-persons work because handles and friend clusters often reuse across platforms.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/Frontline-Femmes/Steam-OSINT` and install its Python dependencies.
2. Obtain a free Steam Web API key (steamcommunity.com/dev/apikey) using a sock-puppet Steam account.
3. Configure the key, then run the tool against the target's username / SteamID / profile URL.
4. Read the output: profile details, games library + playtime, achievements, and public friends.
5. Pivot: resolve vanity URLs ↔ SteamID with [[steamid-io]]; run the handle through cross-platform username tools; check public friends as `associate` leads.

## Inputs → Outputs
- **In:** `username` / SteamID / Steam profile URL
- **Out:** `social-profile` (games, playtime, achievements, avatar, last-online), `associate` list (public friends)
- **Empty/negative result looks like:** a private profile returns little or nothing — Steam privacy settings hide games/friends; absence is a privacy setting, not proof of an inactive account.

## Gotchas & OpSec
- Private/friends-only profiles expose almost nothing via the API — expect gaps and don't infer absence.
- Human-in-the-loop: you must supply a Steam Web API key; keep it on a burner account.
- OpSec: **active** in that queries carry your API key/IP; never authenticate with a real Steam account when viewing a target.

## Overlaps ("do both")
- Pairs with [[steamid-io]] (ID/vanity resolution and quick web profile view) and cross-platform username enumerators — SteamOSINT gives depth on one account, those spread the handle outward.

## Trust & verifiability
`trust: community` — an unofficial open-source wrapper over Steam's official public Web API. The data is authoritative (straight from Steam); the tool itself is community-maintained, so verify anything critical directly on the Steam profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steamosint |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
