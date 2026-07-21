---
id: open-source
name: SteamReveal (OSINT-steam)
description: Use when you have a Steam `username`/ID and want its social graph and probable location — returns close-friend associates and a geographic estimate from public profile data.
url: https://github.com/Berchez/OSINT-steam
category: social-networks
path:
- social-networks
bestFor: Mapping a Steam profile's close friends and estimating location from its public social network.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
- geolocation
status: live
pricing: free
costNote: Free and open source (self-hosted web app); no paid tier.
opsec: passive
opsecNote: Analyzes only public Steam data via the Steam Web API, so the target isn't touched or notified. You supply a Steam API key; run it locally so queries originate from your controlled environment.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: An open-source project (TypeScript/Next.js) on GitHub; results are heuristic inferences from public data, reproducible by inspecting the code.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- SteamReveal
- OSINT-steam
- Berchez/OSINT-steam
tags:
- steam
- social-graph
- gaming-osint
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# SteamReveal (OSINT-steam)

> A self-hosted Steam profile analyzer: given a Steam ID it maps the account's close friends and triangulates a likely location from its public social network.

## When to use
Your subject has a Steam presence and you want to exploit it. SteamReveal takes a Steam URL/custom ID/SteamID64 and, from public profile and friends data, identifies likely "close friends" (via mutual-connection analysis) and estimates geographic location by triangulating the network. Gaming identities often reuse handles and connect to real associates, so this can widen an investigation from one Steam account to a cluster of people and a region.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (https://github.com/Berchez/OSINT-steam) and install dependencies (Node/Next.js 14).
2. Obtain a free Steam Web API key and configure it in the project's environment.
3. Run the app locally and open it in your browser.
4. Enter the target's Steam URL, custom ID, or SteamID64 to run the analysis.
5. Read the outputs: close-friend `associate`s, the social-network map, and the location estimate. Pivot handles to cross-platform username search and the region to other geo signals.

## Inputs → Outputs
- **In:** a Steam `username`/custom ID/SteamID64
- **Out:** ranked close-friend `associate`s and `social-profile`s, plus a probabilistic `geolocation` estimate
- **Empty/negative result looks like:** thin or no output when the profile and its friends list are private — the tool only reads public data, so a locked-down account yields little.

## Gotchas & OpSec
- Location is an **inference** from the network, not GPS — treat it as a lead to corroborate, not a fix.
- Requires a Steam API key and a local run (Node build); budget setup time.
- Private profiles/friends lists defeat it.
- OpSec: passive (public API), but self-host so queries come from your controlled environment.

## Overlaps ("do both")
- Pairs with cross-platform username tools and Steam ID resolvers — SteamReveal adds the social-graph and geo-inference layer on top of raw profile lookups.

## Trust & verifiability
`trust: community` — an open-source project whose inferences you can audit in the code; heuristic, so verify associates and location against independent evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-source |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
