---
id: psnprofiles
name: PSNProfiles
description: Use when you have a PlayStation Network `username` and want a public gaming profile — returns trophy/games activity, country, avatar `image`, and an activity timeline for pattern-of-life.
url: https://psnprofiles.com/
category: social-networks
path:
- social-networks
bestFor: Looking up a PSN gamertag's public trophy/activity profile — games, country, avatar, and daily activity timing.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- image
- metadata-exif
status: live
pricing: free
costNote: Free to search and view public PSN profiles; no account required (an optional account only adds tracking features).
opsec: passive
opsecNote: PSNProfiles scrapes public PSN trophy data; viewing a profile here does not touch the target's PSN account or notify them. Standard sock-puppet browsing is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running third-party PSN trophy tracker; data mirrors public PlayStation profiles but depends on the user having public trophies and on PSNProfiles' scraping being current.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- namechk-2
aliases:
- PSN Profiles
- psnprofiles.com
tags:
- bellingcat-toolkit
- other-platforms
- gaming
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# PSNProfiles

> A public trophy tracker for PlayStation Network — resolve a PSN `username` into a profile showing games, country, avatar, and a dated activity timeline usable for pattern-of-life.

## When to use
You have a PlayStation Network gamertag (`username`) — or want to test whether a known handle is used on PSN — and want to confirm it, see the account's country/avatar, and read its trophy-earning activity over time. The dated trophy timeline is a genuine pattern-of-life signal (active hours → timezone; game choices → interests), which is valuable for corroborating identity and behaviour in a missing-persons or identity investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://psnprofiles.com and search the PSN `username`.
2. Open the matching profile: note the avatar `image`, declared country, games list, and trophy timeline.
3. Read the activity dates/times — clustering reveals active hours (timezone/routine).
4. Cross-reference the same handle on other platforms to link identities.
5. Pivot: the avatar feeds reverse-image search; the confirmed handle feeds `[[whatsmyname-web]]`/`[[namechk-2]]`; country + activity pattern corroborates other findings.

## Inputs → Outputs
- **In:** PSN `username` (or a candidate `name`/handle to test)
- **Out:** `social-profile` (games, country), avatar `image`, and `metadata-exif`-style activity timestamps/timeline
- **Empty/negative result looks like:** no profile, or a found account with private/hidden trophies showing little data — PSN privacy settings suppress trophy visibility, so absence of activity isn't proof of inactivity.

## Gotchas & OpSec
- Only public PSN profiles with visible trophies appear; users can hide trophies, blanking the timeline.
- Data is scraped and can lag; a stale profile may under-represent recent activity.
- The declared country is user-set and can be inaccurate.
- OpSec: passive — no contact with the target's PSN account; use a sock puppet for browsing hygiene.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` and `[[namechk-2]]` — confirm the same gamertag across platforms; PSNProfiles adds the PlayStation-specific activity depth those breadth-checkers lack.

## Trust & verifiability
`trust: community` — a reputable, long-standing trophy tracker mirroring public PSN data. The profile facts are as reliable as the user's public PSN settings; verify identity by corroborating the handle/avatar elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | psnprofiles |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
