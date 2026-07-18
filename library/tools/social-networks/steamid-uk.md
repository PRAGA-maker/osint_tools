---
id: steamid-uk
name: SteamID.uk
description: Use when you have a Steam `username`/ID and want name history and friend-link timelines — returns username, social-profile and associate.
url: http://steamid.uk/
category: social-networks
path:
- social-networks
bestFor: Resolving Steam IDs, viewing a player's previous display names, and seeing when accounts friended each other.
selectorsIn:
- username
- social-profile
selectorsOut:
- username
- social-profile
- associate
status: live
pricing: freemium
costNote: Free tier resolves IDs, shows previous names and friend-link dates. Bulk search-by-former-name and account screenshots are paid.
opsec: passive
opsecNote: Lookups query Steam's public data via the site, not the target — the player is not notified. Sign in with Steam only from a sock-puppet account if you use features that require it; avoid tying queries to your real Steam identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-known community Steam-OSINT utility (in the Bellingcat toolkit); data derives from Steam's public APIs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- steamid.uk
- SteamID UK
tags:
- gaming
- steam
- username
source: bellingcat-toolkit
lastVerified: '2026-07-18'
enrichment: full
---

# SteamID.uk

> Turn a Steam handle into an identity trail — every previous display name the account used and the dated moment it friended other players.

## When to use
The subject games on Steam and you have a `username`, profile URL, or Steam ID. SteamID.uk resolves the various ID formats and — most valuably — lists the account's **previous display names** (catching a handle they've since abandoned but reused elsewhere) and the **dates friendships were formed**, which builds a rough social timeline and surfaces close `associate`s. Reused handles are strong cross-platform pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://steamid.uk/ and enter the Steam profile URL, vanity name, or any Steam ID format.
2. Read the resolved IDs (SteamID64, etc.), the **previous-names** list, and the account's friend list with friend-since dates.
3. Note old handles (search them across other platforms) and early/long-standing friends (likely real associates).
4. For scale, use its API; bulk search-by-former-name and screenshots are paid extras.
5. Pivot: previous `username`s → cross-platform username search; friends → `associate` mapping and their own profiles; SteamID64 → other Steam-OSINT tools and game/ban history.

## Inputs → Outputs
- **In:** `username` / Steam profile URL / Steam ID
- **Out:** `username` (current + previous names), `social-profile` (resolved Steam profile), `associate` (friends with friend-since dates)
- **Empty/negative result looks like:** private profile or no data — a locked-down Steam account limits visibility; some fields need the account to be public or the paid tier.

## Gotchas & OpSec
- A private Steam profile hides friends/history — expect gaps for locked-down accounts.
- Steam identities are pseudonymous; treat handle reuse and friend links as leads to corroborate, not proof of real-world identity.
- OpSec: passive; if a feature asks you to sign in with Steam, use a sock-puppet, never your real account.

## Overlaps ("do both")
- Pairs with cross-platform username tools (Sherlock/WhatsMyName-style) and other Steam-OSINT sites — SteamID.uk is strongest for name history and friend timelines; the others confirm the same handle's spread and add game/ban data.

## Trust & verifiability
`trust: community` — a respected community tool sourcing Steam's public API; resolved IDs and name history are reliable, while real-world attribution from a pseudonymous handle still needs independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steamid-uk |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → username, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
