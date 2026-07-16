---
id: xboxgamertag
name: XboxGamertag
description: Use when you have an Xbox `username` (gamertag) and want the public gaming profile behind it — returns games played, achievements, activity and game clips as a `social-profile`.
url: https://xboxgamertag.com/
category: social-networks
path:
- social-networks
bestFor: Resolving an Xbox gamertag into its public profile — games played, gamerscore, recent activity and shared game clips.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to search and view public gamertag profiles; no account required.
opsec: passive
opsecNote: You look up a public gamer profile without contacting the person; passive. Do NOT sign in with or friend the target from a real Xbox/Microsoft account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party front-end over public Xbox Live profile data; it surfaces only what the account has made public, so accuracy tracks the platform.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- xboxgamertag.com
- Xbox Gamertag search
tags:
- bellingcat-toolkit
- other-platforms
- gaming
source: bellingcat-toolkit
lastVerified: '2026-07-16'
enrichment: full
---

# XboxGamertag

> A public lookup for Xbox gamertags — turn a gaming handle into its Xbox Live profile, showing what the person plays and when they've been active.

## When to use
You have an Xbox `username` (gamertag), or a handle a subject reuses across platforms that might be their gamertag, and you want the public gaming footprint behind it: games played, gamerscore/achievements, recent activity, and any shared game clips/screenshots. Gaming profiles often reveal active hours, interests, and linked friends useful in a people search — especially for younger subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://xboxgamertag.com/ .
2. Search the gamertag (`username`).
3. Open the matching profile.
4. Read the output: the public Xbox profile (`social-profile`) — games list, gamerscore, achievements, recent activity timestamps, and shared clips/screenshots.
5. Pivot: use activity timestamps to infer active hours/time zone; run the same handle through username-enumeration for other platforms; note game titles as interest leads.

## Inputs → Outputs
- **In:** `username` (Xbox gamertag)
- **Out:** `social-profile` (Xbox Live profile: games, achievements, activity, clips)
- **Empty/negative result looks like:** no profile found (gamertag doesn't exist or was changed), or a profile with private settings showing little beyond the name.

## Gotchas & OpSec
- Shows only what the account has left public; privacy-locked profiles reveal almost nothing.
- Gamertags can be changed/recycled — confirm you have the right person before drawing conclusions.
- OpSec: passive lookup; never friend/message the target from a real account to see more.

## Overlaps ("do both")
- Complements username-enumeration tools and other gaming-profile lookups (Steam, PSN): this covers Xbox; run the handle across the others to build a cross-platform gaming footprint.

## Trust & verifiability
`trust: community` — a third-party viewer of public Xbox Live data. It reflects the platform's own public profile info; treat activity/clip data as authentic-but-public, and confirm identity before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xboxgamertag |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
