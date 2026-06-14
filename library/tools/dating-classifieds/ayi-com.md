---
id: ayi-com
name: AYI.com
description: Use when checking whether a subject keeps a casual/location-based dating profile by `username` or `geolocation` — a legacy "Are You Interested" style dating site.
url: https://www.ayichat.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking for a location-based casual-dating profile by handle or area
selectorsIn:
- username
- geolocation
- image
selectorsOut:
- social-profile
- username
- physical-description
status: degraded
pricing: freemium
costNote: Free signup; messaging/advanced search typically paywalled. Original AYI ("Are You Interested?") brand has changed hands; current site may differ.
opsec: active
opsecNote: Requires an account to view profiles; activity is logged. Use a sock-puppet account only.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: AYI/"Are You Interested" is a legacy dating brand; the linked ayichat.com domain and its current operator are not independently verified.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Are You Interested
tags:
- dating
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# AYI.com

> A legacy "Are You Interested?" style location-based dating site — a possible place to find a subject's casual-dating profile, though the brand/domain has shifted over time.

## When to use
Use it when you have a `username` or approximate `geolocation` and want to check for a casual-dating profile. Like other dating sites, a match can confirm a reused handle, a profile photo (`physical-description`), and a city/area. Treat coverage as thin — its OSINT yield is lower than mainstream apps.

## How to use it (`bestInteractionPattern`: web-manual)
1. Confirm the live site behind the URL first; the AYI brand has changed operators, so verify you are on the intended platform.
2. Register a sock-puppet account and log in.
3. Search by location/age and look for matching photos or handles; corroborate against known selectors.
4. Pivot: a confirmed handle or photo goes to username-enumeration and reverse-image search.

## Inputs → Outputs
- **In:** `username`, `geolocation`, `image`
- **Out:** `social-profile`, reused `username`, `physical-description`
- **Empty/negative result looks like:** no match, redirected/parked domain, or a rebranded site — if the platform no longer resembles a dating service, treat as down.

## Gotchas & OpSec
- Human-in-the-loop: account login; messaging/full search paywalled.
- OpSec: active — use an isolated puppet account; never contact the subject.

## Overlaps ("do both")
- Pairs with `[[badoo]]` and reverse-image search, which cover the same casual-dating niche with far larger user bases.

## Trust & verifiability
`trust: unverified` — the AYI brand is real but the current domain/operator and whether the platform still functions are unconfirmed; verify the live site before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ayi-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, geolocation, image → social-profile, username, physical-description |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
