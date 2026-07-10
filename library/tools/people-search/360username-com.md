---
id: 360username-com
name: 360username.com
description: Use when you have a `username` and want to see which of 150+ social platforms and domain TLDs it is registered/taken on — returns a per-platform taken/available map with direct profile links.
url: https://360username.com/
category: people-search
path:
- people-search
bestFor: Bulk-checking one handle across 150+ platforms at once to map a subject's account footprint.
selectorsIn:
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Completely free, no account required; account creation is optional and adds nothing needed for lookups.
opsec: passive
opsecNote: Passive from the target's view — the tool probes each platform's public availability endpoint, not the subject. Note the checks originate from 360username's servers (or your browser), so no direct login to any target account occurs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free handle/domain-availability checker aimed at brand/creator naming; results reflect availability endpoints, which can false-negative (rate-limited platforms show 'available' wrongly), so confirm hits by opening the profile.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- 360username
- 360username.com
tags:
- peoplesearch
- People Search Sites
- username-enumeration
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# 360username.com

> A fast, free handle-availability scanner: type one `username` and it checks 150+ social platforms and domain TLDs simultaneously, showing where the name is taken (i.e. an account may exist) versus open.

## When to use
You have a `username` and want a broad first-pass map of where that handle is registered across social media. "Taken" on a platform is a lead that the subject (or someone) holds that account; "available" rules a platform out. It's built for brand/name checking, but the same taken/available signal is exactly what username-enumeration OSINT needs to widen a subject's account footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://360username.com/ in a browser (no login).
2. Enter the exact `username` into the availability checker.
3. Read the per-platform grid: each of the 150+ services (Instagram, TikTok, GitHub, Twitch, YouTube, etc.) shows taken vs available, usually with a direct link.
4. Open every "taken" link and confirm the account actually matches your subject — same avatar, bio, activity — because a common handle may be a different person.
5. Pivot: feed confirmed `social-profile`s into `[[gaddr]]` / `[[username-check]]` for cross-correlation, and reverse-image the avatars.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-platform taken/available map, direct `social-profile` links, domain (`.com/.io/.ai/...`) availability
- **Empty/negative result looks like:** the handle shows "available" nearly everywhere — meaning it's an uncommon/unused string, not that the subject has no online presence under a *different* handle.

## Gotchas & OpSec
- Availability endpoints are noisy: a rate-limited or blocking platform can report "available" when an account actually exists (false negative), and reserved/banned handles can report "taken" with no real account (false positive). Always open the link.
- No login/captcha, so it's frictionless and passive — nothing reaches the target's accounts.
- It checks one exact string; try handle variants (underscores, numbers, name+year) separately.
- It answers "does this handle exist," not "who owns it" — attribution is your job via the linked profiles.

## Overlaps ("do both")
- Pairs with `[[username-check]]`, `[[username-checker]]` and `[[gaddr]]` — run more than one enumerator, as each covers a different platform set and different platforms false-negative on each.
- Feed confirmed profiles onward to image/face tooling to tie handles to a single person.

## Trust & verifiability
`trust: community` — a free naming/availability utility, accurate enough for a first sweep but not authoritative. Treat every "taken" as a lead to verify by opening the profile, and never treat "available" as proof of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 360username-com |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
