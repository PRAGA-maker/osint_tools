---
id: taxi-driver-co-uk
name: Taxi Driver Online (taxi-driver.co.uk)
description: Use when you have a `username` in the UK private-hire/taxi trade and want a matching forum profile — returns social-profile, posts, and locality/licensing hints.
url: http://www.taxi-driver.co.uk/phpBB2/
category: communities-forums
path:
- communities-forums
bestFor: Finding whether a subject participates in the UK taxi/private-hire trade community and mining posts for locality, licensing authority, and trade details.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free phpBB forum; reading public threads needs no account, posting requires (free) registration.
opsec: passive
opsecNote: Reading public threads is passive. Registering and posting is active and traceable — avoid unless necessary and never with an attributable identity. The community is regional/trade-focused, so newcomers stand out.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running phpBB community forum for UK taxi/private-hire drivers; user-generated, self-reported content — corroborate any claim.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Taxi Driver Online forum
- taxi-driver.co.uk phpBB
tags:
- forums
- Forums
- uk
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Taxi Driver Online (taxi-driver.co.uk)

> A long-running UK taxi/private-hire trade forum (phpBB) — match a username to a member profile and mine posts for the driver's locality, licensing authority, and trade activity.

## When to use
You have a `username` or handle for someone you believe drives a taxi/private-hire vehicle in the UK, and you want to see if they post here. Member profiles and posts often reveal a home locality or licensing authority (drivers discuss their council's rules), vehicle details, and trade grievances — useful for confirming occupation and narrowing `geolocation`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.taxi-driver.co.uk/phpBB2/ and use the forum search, or scope an engine query: `site:taxi-driver.co.uk "<username>"`.
2. Open matching member profiles and threads (News, General, Vehicles, licensing sections).
3. Read for self-stated location/licensing council, vehicle, join date, and post history.
4. Pivot: a stated council/locality narrows `geolocation` and feeds local licensing-register lookups; a reused `username` feeds cross-platform enumeration.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (member page + posts), locality/licensing `geolocation` hints
- **Empty/negative result looks like:** no member matches, or a profile with no posts — treat as "not active here," not proof the person isn't a driver.

## Gotchas & OpSec
- Self-reported content; corroborate licensing/locality claims against the relevant council's public register.
- UK-only, trade-specific — irrelevant outside that context.
- Human-in-the-loop: posting requires a (free) login; reading generally does not.

## Overlaps ("do both")
- Complements UK council taxi-licensing registers — this surfaces the person and locality, those confirm the licence officially.

## Trust & verifiability
`trust: community` — an established but user-generated forum; good for identity/interest corroboration, not authoritative proof of licensing status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | taxi-driver-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
