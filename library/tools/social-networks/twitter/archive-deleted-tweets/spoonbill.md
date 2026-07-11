---
id: spoonbill
name: Spoonbill
description: Use when you have Twitter/X `username`s you want to monitor and want to catch profile edits (bio, name, location, URL changes) — returns change alerts revealing prior `social-profile` states and `name`/location shifts.
url: https://spoonbill.io/
category: social-networks
path:
- social-networks
- twitter
- archive-deleted-tweets
bestFor: Detecting and logging changes to the accounts you follow (bio, display name, location, link) on Twitter/X.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: degraded
pricing: freemium
costNote: Free to use with a connected account; functionality depends on Twitter/X API access, which has been heavily restricted since 2023.
opsec: passive
opsecNote: Monitoring is indirect — you observe changes to accounts you already follow, without engaging the target. However, Spoonbill connects to your Twitter/X account via OAuth, so use a sock-puppet X account, not a personal one, and review the permissions you grant.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A real, established profile-change tracker, but its coverage was undermined by X's API pricing changes; results may be partial or delayed. It requires OAuth access to your account.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- spoonbill.io
tags:
- twitter
- profile-monitoring
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# Spoonbill

> A Twitter/X profile-change tracker — it watches the accounts you follow and flags when someone edits their bio, display name, location, or link.

## When to use
You are monitoring one or more Twitter/X subjects and want to catch the small, revealing edits people make: a changed display `name`, a bio rewrite, a new/removed location, a swapped link. Those changes can signal a life event, a new job/location, an attempt to scrub identity, or a slip that briefly exposes real info — all valuable for an ongoing watch on a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://spoonbill.io/ and connect a **sock-puppet** Twitter/X account via OAuth.
2. Spoonbill tracks changes across the accounts that sock account follows — so follow your targets from it.
3. Review the change feed: each entry shows the old vs. new value (bio, `name`, location, URL) with a timestamp.
4. Record notable edits (a briefly-shown real name/location, a job change) before they're reverted.
5. Pivot: a changed location feeds geo-context; an exposed name/link feeds identity work; a scrub attempt is itself a signal.

## Inputs → Outputs
- **In:** Twitter/X `username`s (via the accounts your connected sock account follows)
- **Out:** profile-change alerts — prior/updated `social-profile` fields, `name`/location/bio/link shifts, with timestamps
- **Empty/negative result looks like:** no changes logged, or gaps in tracking — increasingly likely given X's API restrictions, which can throttle or break change detection. A quiet feed may mean "no edits" OR "not currently able to track."

## Gotchas & OpSec
- API-dependent and degraded: X's 2023+ API pricing has hampered many such trackers; expect partial coverage and delays.
- Requires OAuth to a Twitter/X account — use a sock puppet and scrutinise permissions.
- Only tracks accounts within your follow graph; you must follow a target to watch it.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` and tweet-archiving tools — Spoonbill catches *profile-field* edits going forward, while archives recover deleted *tweets* and past page states.

## Trust & verifiability
`trust: unverified` — a genuine tool whose reliability is now constrained by X's platform changes; corroborate any critical change against an archive or a direct check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spoonbill |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
