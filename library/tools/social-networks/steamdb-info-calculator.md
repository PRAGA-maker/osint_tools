---
id: steamdb-info-calculator
name: SteamDB Calculator
description: Use when you have a Steam `username`/vanity URL or SteamID and want the public account's games, playtime, and value — returns social-profile detail and activity/interest leads.
url: https://steamdb.info/calculator/
category: social-networks
path:
- social-networks
bestFor: Profiling a public Steam account — owned games, hours played, account value, and profile metadata.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to look up any public Steam profile; no account needed. SteamDB is ad-supported and Cloudflare-protected.
opsec: passive
opsecNote: You query SteamDB's index (which reads Steam's public API), not the user directly, so the target isn't notified. Only public profiles resolve — private accounts return little. Behind Cloudflare you may hit a browser challenge; solve it manually and avoid aggressive automated hits.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: SteamDB is a well-known community Steam database; data comes from Steam's public API, so it's accurate for public accounts but bounded by each profile's privacy settings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- SteamDB calculator
- steamdb.info/calculator
tags:
- steam
- gaming-profile
- social-networks
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# SteamDB Calculator

> Point it at a public Steam account and it lays out the games owned, hours played, and total value — a quick profiler for a gaming subject's Steam presence.

## When to use
You have a Steam `username`/vanity URL, a SteamID, or a Steam `social-profile` link and want to characterize the account: which games they own, how many hours they've sunk into each, when they joined, and the library's monetary value. Useful for confirming an account is active and real, gauging interests/routine, and (via the public profile) spotting linked accounts or friends to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://steamdb.info/calculator/ (clear any Cloudflare challenge).
2. Enter the target's SteamID, vanity URL, or profile URL (`selectorsIn`).
3. Read the breakdown: games owned, playtime per title, total hours, account value, and profile creation info (`selectorsOut`).
4. Pivot: cross-check the vanity name as a `username` on other platforms; open the linked Steam profile for friends/groups (`associate`) and showcased info.

## Inputs → Outputs
- **In:** `username`/vanity URL, SteamID, or `social-profile` (Steam URL)
- **Out:** `social-profile` detail (games, playtime, value, join date) and `associate` leads (friends/groups via the profile)
- **Empty/negative result looks like:** "profile is private" or no data — the account exists but hides its library; you learn it's private, not that it's inactive.

## Gotchas & OpSec
- Human-in-the-loop: Cloudflare browser challenge (`captcha`) may appear; solve manually.
- OpSec: passive — SteamDB reads Steam's public API; the user isn't alerted.
- Only public data shows; playtime/library visibility is per-user privacy-gated, so absence of games ≠ inactive account.

## Overlaps ("do both")
- Pairs with Steam username-enumeration and the misiektoja [[steam-monitor]] (live activity tracking) — the calculator gives a static library/value snapshot, while a monitor watches ongoing play activity.

## Trust & verifiability
`trust: community` — a reputable community Steam database sourced from Steam's official public API; data is accurate for public profiles but strictly limited by each account's privacy settings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | steamdb-info-calculator |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
