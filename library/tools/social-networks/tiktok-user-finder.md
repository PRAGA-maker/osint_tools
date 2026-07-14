---
id: tiktok-user-finder
name: TikTok User Finder
description: Use when you have a TikTok `username` and want that account's metadata — numeric user ID, region, creation date, username-change history and stats — returns social-profile detail beyond the app.
url: https://omar-thing.site/
category: social-networks
path:
- social-networks
bestFor: Pulling a TikTok account's hidden metadata (user ID, region, account age, past username edits) from a handle.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
- device-id
status: degraded
pricing: freemium
costNote: Free web lookup; a developer API for bulk/programmatic access starts around $5.99/month. Was intermittently non-responsive at last check — treat availability as flaky.
opsec: passive
opsecNote: Passive to the target — you query a third-party site, not TikTok as the subject. But you are handing the target's handle to an unknown operator; use a sock browser and assume the query is logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous third-party TikTok metadata tool on an unbranded domain. Output can be genuine (drawn from TikTok's API), but provenance and longevity are uncertain — corroborate key facts against TikTok directly.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- omar-thing.site
- TikTok user info lookup
tags:
- tiktok
- TikTok Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# TikTok User Finder

> A third-party lookup that turns a TikTok handle into the account's hidden metadata — numeric user ID, region, creation date, and username-change history.

## When to use
You have a TikTok `username` and want the metadata TikTok's app doesn't surface: the immutable numeric user ID (survives handle changes), the account's region, its creation date, prior username edits, follower/heart/video counts, and the avatar. That numeric ID and creation date are the durable identifiers for tracking an account and estimating account age — valuable for disambiguation and for re-finding an account after a rename.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://omar-thing.site/ in a sock browser. If it hangs on "Fetching data…", retry later — it's been flaky.
2. Enter the TikTok `username` and click Fetch Data.
3. Read the output: numeric user ID (`device-id`-style stable identifier), profile `region` (`geolocation`, coarse), account creation date, nickname/username change timestamps, and public stats. Avatar and story-view options may be offered.
4. Pivot: the numeric user ID re-identifies the account after handle changes and feeds other TikTok-ID tools; the region narrows geography; creation date and rename history help confirm you have the right person.

## Inputs → Outputs
- **In:** `username` (TikTok handle)
- **Out:** `social-profile` (stats, avatar), `device-id` (numeric TikTok user ID), `geolocation` (account region)
- **Empty/negative result looks like:** dashes/placeholders or "No matching users found" — either the handle is wrong, the account is private, or the tool is down. Don't read a failed fetch as "account doesn't exist."

## Gotchas & OpSec
- Unbranded third-party site with uncertain longevity; it was intermittently unresponsive at last check.
- Region is coarse (account-declared/inferred), not a location — don't overstate it.
- OpSec: passive to the target, but the operator sees your query; use a sock browser and verify decisive facts against TikTok itself.

## Overlaps ("do both")
- Complements TikTok's own profile view and any other TikTok user-ID resolver — this exposes the numeric ID and account age; cross-check the ID with a second tool before relying on it.

## Trust & verifiability
`trust: unverified` — an anonymous tool; its data likely comes from TikTok's API but its provenance and uptime aren't guaranteed. Treat outputs as leads to confirm on-platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tiktok-user-finder |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation, device-id |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
