---
id: mavekite
name: MaveKite
description: Use when you have a TikTok `username` and want the public profile without logging in — returns user ID, bio, follower/like counts, region, and verification.
url: https://mavekite.com/
category: social-networks
path:
- social-networks
bestFor: Resolving a TikTok @handle to its public profile stats and region without a TikTok account.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Single-handle lookups are free with no login; bulk imports, historical tracking, and CSV/PDF export require a paid plan.
opsec: passive
opsecNote: You query MaveKite's servers, not TikTok, so the lookup does not touch the target's account or notify them — a passive way to read a TikTok profile without your own logged-in TikTok session appearing in their viewer signals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party TikTok analytics scraper; reflects public TikTok data and derived estimates (e.g. engagement rate), not official platform figures.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- MaveKite
- mavekite.com
- TikTok profile finder
tags:
- tiktok
- profile-lookup
- social-media
source: osintambition-social
lastVerified: '2026-07-22'
enrichment: full
---

# MaveKite

> A no-login TikTok profile viewer: paste a handle and read the public account — user ID, bio, counts, region, and verification — without exposing your own TikTok session.

## When to use
You have a TikTok `username`/handle (from a bio link, another platform, or a witness) and want to confirm the account exists and read its public details without logging into TikTok yourself (which can register you in the target's viewer/analytics signals). MaveKite resolves the handle to a stable numeric user ID, display name, bio, follower/following/like counts, verification status, and a region signal — useful for confirming identity, dating activity, and extracting a `geolocation` hint and a profile image to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://mavekite.com/ (or its TikTok Profile Finder page) and enter the @handle.
2. Read the returned fields: numeric user ID, display name, bio, follower/following/likes, verification, and region.
3. Note the bio for links/other handles and the region as a coarse `geolocation` lead; save the avatar for reverse-image search.
4. The numeric user ID is durable even if the handle changes — record it.
5. Pivot: bio links and reused handles feed cross-site username tools; the region narrows location; the avatar feeds face/reverse-image search.

## Inputs → Outputs
- **In:** `username` (TikTok @handle)
- **Out:** `social-profile` (user ID, bio, counts, verification) and a region `geolocation` signal
- **Empty/negative result looks like:** "profile not found" / no data — the handle doesn't exist, was renamed, or the account is private/removed. A miss on the handle is not proof the person has no TikTok; try handle variants.

## Gotchas & OpSec
- Figures like engagement rate are third-party estimates; treat follower/like counts as approximate and region as coarse, not a precise location.
- Free tier is single lookups; repeated/bulk queries push you toward the paid plan.
- It reads public data only — private accounts expose little beyond existence.

## Overlaps ("do both")
- Pairs with other TikTok viewers and cross-site username enumerators — MaveKite confirms the TikTok profile and ID; the enumerator finds the same handle elsewhere, and reverse-image search links the avatar to other networks.

## Trust & verifiability
`trust: community` — a third-party scraper of public TikTok data; the raw profile fields mirror TikTok, but derived metrics are estimates, so verify anything critical against the live TikTok profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mavekite |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
