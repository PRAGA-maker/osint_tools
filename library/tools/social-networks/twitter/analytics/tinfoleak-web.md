---
id: tinfoleak-web
name: Tinfoleak (Web)
description: Use when you have a Twitter/X `username` and want an automated intelligence dossier on the account — returns profile details, activity patterns, devices/apps, hashtags, mentions, and any geolocated posts.
url: https://tinfoleak.com/
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Automated Twitter/X profile and timeline intelligence — activity times, apps/devices, top hashtags/mentions, geolocated tweets.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- device-id
status: degraded
pricing: freemium
costNote: The hosted web version requires (free) registration/login; the underlying tool is open-source and self-hostable. Depth is constrained by current X API access.
opsec: active
opsecNote: Queries run through Tinfoleak's third-party infrastructure (web version) or your own credentials (self-hosted), and pulling a timeline is an API-level interaction that can be logged. Use a sock-puppet account/keys; don't tie it to your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, well-documented open-source Twitter OSINT tool (by Vicente Aguilera Díaz), bundled in Kali/BlackArch. Reputable, but its output completeness has degraded with X's API restrictions.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- tinfoleak
- tinfoleak.com
tags:
- twitter
- analytics
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Tinfoleak (Web)

> A veteran Twitter/X intelligence tool that turns a username into a structured dossier — when someone posts, from what apps/devices, their top hashtags and contacts, and any tweets with location data.

## When to use
You have a Twitter/X `username` and want more than raw tweets: behavioural patterns (active hours/days), the apps/devices used to post (a `device-id`-style fingerprint), frequent hashtags and mentions (their network), and geolocated posts that place the person. Strong for building a subject's routine and location footprint from their timeline in a missing-person or identity workup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://tinfoleak.com/ and register/log in (free), or self-host the open-source version with your own X API credentials.
2. Enter the target `username` (the tool also supports coordinates/keywords in some modes).
3. Run the analysis and read the dossier: profile info, activity timeline, source apps/devices, top hashtags/mentions, media, and any geotagged tweets.
4. Because X's API changes limit what's retrievable, treat sparse output as an access limit, not proof of inactivity.
5. Pivot: geotagged posts feed `[[mapillary-2]]`/mapping; frequent mentions feed `associate`/network mapping; device/app info corroborates identity.

## Inputs → Outputs
- **In:** Twitter/X `username` (+ optional coordinates/keywords)
- **Out:** profile + activity dossier, source `device-id`/apps, top hashtags/mentions, geolocated posts (`geolocation`), media
- **Empty/negative result looks like:** thin or empty output, or errors on auth — increasingly common post-API lockdown; verify against native `[[twitter-search]]` before concluding the account is inactive.

## Gotchas & OpSec
- Degraded by API changes: geolocation and full-history features depend on X access that is now restricted; expect gaps.
- Login/keys required: the web version needs an account; self-hosting needs API keys — use sock-puppet credentials.
- OpSec: **active** — timeline pulls are API interactions that can be logged; isolate your identity.

## Overlaps ("do both")
- Pairs with `[[twitter-search]]` — native search finds specific posts, Tinfoleak aggregates the account into behavioural/geo intelligence; run both and cross-check.

## Trust & verifiability
`trust: community` — a reputable, long-standing open-source OSINT tool; its methods are sound, but output completeness now depends on constrained X API access, so verify key findings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinfoleak-web |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, device-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
