---
id: vk-city4me-com
name: Vk.city4me.com
description: Use when you have a VK `social-profile`/`username` and want their activity patterns — returns online/offline timelines and profile-change history (`metadata-exif`-style behavioral data).
url: http://vk.city4me.com/
category: social-networks
path:
- social-networks
bestFor: Logging a VKontakte user's online/offline times, avatar/wall changes and friend/group activity over time.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
- associate
status: live
pricing: freemium
costNote: Basic monitoring is free; extended/continuous tracking uses a paid "bonus" system (~100 RUB/month per tracked user). A VK login is required to use most features.
opsec: active
opsecNote: The service requires authorizing with a VK account and tracks a target on your behalf — do this ONLY with a dedicated sock-puppet VK account, never your real one, since the tool (and VK) sees your login. It is a monitoring/"stalking" tool; use within legal/ethical bounds.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Russian VK-monitoring service; effective for behavioral timelines but a third party you must trust with a VK login — use a throwaway account.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- city4me
- vk.city4me.com
tags:
- Social Media
- VK
- activity-tracking
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Vk.city4me.com

> A VKontakte activity tracker: point it at a VK user and it logs when they're online/offline and records profile changes over time — turning a static VK profile into a behavioral timeline.

## When to use
Your subject has a VK (`social-profile`/`username`) and you want *patterns*, not just a snapshot: their online/offline schedule (which reveals timezone and daily routine), when they change avatars or post to their wall, and shifts in friends/groups. This is powerful for establishing a person's likely timezone/location, confirming an account is actively used, and spotting behavioral changes — all valuable in a missing-persons or activity-verification context on the Russian-speaking web.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create/prepare a **sock-puppet** VK account (never your real one).
2. Go to http://vk.city4me.com/ and authorize with that VK account.
3. Add the target by VK ID/username; the service begins logging online/offline times and profile changes.
4. Let data accumulate, then read the timeline: online sessions (→ timezone/routine), avatar/wall/friend changes, group activity.
5. Pivot: use the inferred timezone to narrow location; take newly-added `associate`s (friends/groups) into further VK/person lookups. Extended history needs the paid bonus.

## Inputs → Outputs
- **In:** `social-profile`/`username` (a VK account)
- **Out:** `metadata-exif`-style behavioral data (online/offline timeline, change history) and `associate` friend/group activity
- **Empty/negative result looks like:** little data — the account is private/inactive, VK is hiding "last seen," or you've only just started tracking (the tool builds history going forward, so early results are thin).

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — a VK account is mandatory; use a throwaway, as your login is exposed to the service and to VK.
- OpSec: **active** — this is surveillance tooling; stay within legal/ethical limits and never use a personal account.
- "Last seen" can be hidden by the user in VK privacy settings, blanking the online timeline.

## Overlaps ("do both")
- Pairs with general VK-profile analysis tools — those enumerate the profile's static content, while city4me adds the time dimension (when they're active, what changed).

## Trust & verifiability
`trust: community` — an effective but unofficial third-party tracker; corroborate inferred timezone/routine with other signals, and treat behavioral inferences as probabilistic, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vk-city4me-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → metadata-exif, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
