---
id: osint-steam
name: OSINT-Steam
description: Use when you have a Steam `username`/SteamID and want the account's social graph and clues — returns close friends, a probable `geolocation`, and behaviour signals.
url: https://steam-reveal.vercel.app/en
category: social-networks
path:
- social-networks
bestFor: Analysing a Steam profile for its closest connections and an estimated location from public data.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- geolocation
- social-profile
status: live
pricing: free
costNote: Free web app; no login required to run a lookup.
opsec: passive
opsecNote: It reads public Steam profile/friends data via Steam's API through the app — it does not friend, message, or notify the target. The steam-reveal server sees which profile you query; use a clean session for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-built web app (formerly osint-steam, now steam-reveal.vercel.app); its "probable location" and "cheater probability" are inferences/estimates, not verified facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- followgraph-for-mastodon
- gitvio
- section-16-deadline-calculator
- xplore-x-vercel-app
- youtube-lookup
aliases:
- SteamReveal
- steam-reveal.vercel.app
- osint-steam.vercel.app
tags:
- steam
- gaming-osint
- social-graph
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# OSINT-Steam

> A Steam profile analyser (now branded SteamReveal): feed it a SteamID and it estimates the account's closest friends, a probable location, and behavioural flags from public data.

## When to use
You have a subject's Steam `username`, vanity URL, or SteamID64 — a common lead for gaming-active subjects — and want to expand it into a social graph and location estimate. It ranks a profile's *closest* connections (not just the full friend list), which helps identify real-world associates, and infers a probable location and cheater likelihood from activity patterns. Useful when a Steam handle is your main thread on a younger or gaming-focused person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://steam-reveal.vercel.app/en.
2. Enter the subject's SteamID64, custom profile URL (`steamcommunity.com/id/name`), or profile URL — no login needed.
3. Run the analysis and read: ranked "best friends"/connections, an estimated location, and any suspicious-behaviour score.
4. Treat the location and cheater estimates as **inferences** to corroborate, not facts.
5. Pivot: a close-friend `associate` account feeds further Steam/username OSINT; the reused `username` feeds cross-platform handle search; a location estimate narrows geo work.

## Inputs → Outputs
- **In:** `username`/vanity URL or SteamID64 (`social-profile`)
- **Out:** ranked `associate`s (close friends), a probable `geolocation`, linked `social-profile`, behaviour signals
- **Empty/negative result looks like:** a private profile (friends/details hidden) returns little or nothing — Steam privacy settings gate most of what the tool can read.

## Gotchas & OpSec
- Human-in-the-loop: none; single-form web tool.
- If the target's Steam profile is set to private/friends-only, results are thin — the tool can only work with public data.
- The "probable location" and "cheater probability" are algorithmic estimates; never present them as confirmed.
- OpSec: passive — no friend request or message is sent, and the target isn't notified.

## Overlaps ("do both")
- Complements cross-platform username tools — this specialises in the Steam social graph and location inference; generic handle-checkers spread the same `username` across other platforms.

## Trust & verifiability
`trust: community` — a community web app reading genuine public Steam data; the raw profile/friends info is real, but its derived location/behaviour scores are estimates that must be independently corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-steam |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → associate, geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
