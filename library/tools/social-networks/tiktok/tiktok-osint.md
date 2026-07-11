---
id: tiktok-osint
name: TikTok-OSINT
description: Use when you have a TikTok `username` and want that account's public metadata in one shot — returns display name, bio, follower/following/like counts, verification, user ID, and profile picture.
url: https://github.com/Omicron166/TikTok-OSINT
category: social-networks
path:
- social-networks
- tiktok
bestFor: Fast automated capture of a TikTok account's public profile metadata and avatar from a username.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free and open-source (self-hosted Python CLI). No API key or account required.
opsec: active
opsecNote: The script requests the target's public TikTok profile from your machine; automated/repeated requests can trip TikTok's rate limits and anti-abuse controls. Run behind a VPN/sock-puppet IP. It does not log in and does not notify the account owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small community script (a fork with a couple dozen commits); unaudited and dependent on TikTok's current page structure, so it can break without notice. Read the code before running.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- TikTok OSINT
- tiktokOSINT
tags:
- tiktok
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# TikTok-OSINT

> A one-command Python scraper that dumps a public TikTok account's profile metadata — name, bio, counts, verification, user ID, and avatar — from just the username.

## When to use
You have a TikTok `username` and want its public profile snapshot fast: display `name`, bio, follower/following/like counts, verification status, numeric user ID, and the profile `image`. Useful for confirming an account belongs to a subject, capturing the current avatar for face search, and recording engagement context as a lead in a missing-person or identity workup.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install:
   ```
   git clone https://github.com/Omicron166/TikTok-OSINT.git
   cd TikTok-OSINT
   pip3 install -r requirements.txt
   ```
2. Run against a username:
   ```
   python3 tiktokOSINT.py --username USERNAMEHERE
   ```
   Add the download-picture flag to save the avatar.
3. Read the output: ~10 fields — profile name, image, follower/following counts, bio, verified flag, fan count, likes, video count, user ID.
4. Save the profile picture for reverse-image/face search.
5. Pivot: the numeric user ID is stable across username changes; the avatar feeds `[[berify]]`/face tools; the bio may leak other handles.

## Inputs → Outputs
- **In:** TikTok `username`
- **Out:** display `name`, `image` (avatar), bio, follower/following/like/video counts, verification, numeric user ID (`social-profile`)
- **Empty/negative result looks like:** errors or empty fields — the account is private/renamed/banned, or TikTok changed its markup and broke the scraper. An empty run is usually tooling/access, not proof the account is gone.

## Gotchas & OpSec
- Fragile: scrapes TikTok's public endpoints, which change often; verify against a known account before trusting a case run.
- Rate limits: automated requests can be throttled/blocked — space them out and use a sock-puppet IP.
- OpSec: **active** (requests originate from your host) but no login and no owner notification.

## Overlaps ("do both")
- Pairs with other TikTok search/lookup tools and with face-search — this grabs the structured metadata + avatar, which those use to find the same person on other platforms.

## Trust & verifiability
`trust: unverified` — a small unaudited community scraper tied to TikTok's mutable page structure; the fields are genuine when it works, so confirm the account identity independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiktok-osint |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
