---
id: steam-osint-tool
name: Steam OSINT Tool
description: Use when you have a Steam profile `url`/`username` and want hidden connections — returns inferred "closed" friends and the user's public comments.
url: https://github.com/matiash26/Steam-OSINT-TOOL
category: social-networks
path:
- social-networks
bestFor: Enumerating a Steam user's likely private friends and pulling their public profile comments for association and identity leads.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- username
status: live
pricing: free
costNote: Free and open source (GitHub). Runs locally; may require a free Steam Web API key for some lookups.
opsec: passive
opsecNote: It reads public Steam data (and infers friends via public signals); the target is not notified. Passive. If you supply a Steam API key, keep it to a sock-puppet account, and run from a persona/VPN'd environment.
humanInLoop: false
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A community-built GitHub tool; inferred "closed friends" are heuristic, not confirmed — treat them as leads. Vet the code before running, as with any third-party script.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- steam-osint
aliases:
- Steam-OSINT-TOOL
tags:
- Social Media
- Steam
source: cyb-detective
lastVerified: '2026-07-16'
enrichment: full
---

# Steam OSINT Tool

> A CLI tool that mines a Steam profile — inferring "closed" (private) friends from public signals and pulling the user's public comments, turning a gaming handle into association and identity leads.

## When to use
Your subject has a Steam profile (found via a `username`, a linked handle, or a gaming community) and you want to map their social graph and self-disclosures. Gamers often reuse identities and chat openly; this tool surfaces likely friends (even when the friends list is private) and the comments they've left publicly — both rich sources of associates and personal detail.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`github.com/matiash26/Steam-OSINT-TOOL`) and follow its README to install dependencies; obtain a free Steam Web API key if required.
2. Run the tool against the target's Steam profile `url`/ID.
3. Review the output: inferred private ("closed") friends and the user's public comments.
4. Treat inferred friends as heuristic leads — confirm a connection with corroborating evidence before asserting it.
5. Pivot: friend accounts (`associate`s) become new subjects; comment text may reveal a real name, other platforms, or a location.

## Inputs → Outputs
- **In:** Steam profile `url` / `username`
- **Out:** inferred `associate`s (likely private friends) and public comments exposing further `username`s/leads
- **Empty/negative result looks like:** few/no results — the profile is locked down, has little public activity, or the API key/rate limits blocked enumeration; a fully private profile yields little.

## Gotchas & OpSec
- "Closed friends" are *inferred* from public signals — probabilistic, not proof; verify before relying on a link.
- Needs a Steam API key for some functionality (rate-limited).
- Vet the third-party code before running it locally.
- OpSec: passive to the target; use a sock-puppet API key and persona environment.

## Overlaps ("do both")
- Pairs with `[[steam-osint]]` and general username-search — this maps the Steam social graph; username tools resolve the same handle across other platforms.

## Trust & verifiability
`trust: community` — an open-source community tool; public comments are authentic, but inferred friendships are heuristic and must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steam-osint-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → associate, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
