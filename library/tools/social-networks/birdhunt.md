---
id: birdhunt
name: BirdHunt
description: Use when you have a `geolocation` (place of interest) and want X/Twitter posts sent from near it — returns geographically-filtered posts and their authors as social-profile leads.
url: https://birdhunt.co/
category: social-networks
path:
- social-networks
bestFor: Finding tweets by location — surfacing X posts and accounts active near a chosen point.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: live
pricing: freemium
costNote: Part of the HuntIntel platform; a basic location search is usable, deeper features and higher limits are account/paid-gated. Confirm current limits on the site.
opsec: passive
opsecNote: You query a third-party search of public X posts; no target is notified. BirdHunt/HuntIntel logs your searches and may require an account — use an investigative login. Post geotags are coarse and often profile-set, so a returned location is a lead, not a device fix.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial OSINT search tool (HuntIntel). Depends on X data access, which limits completeness and can change without notice.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- xplore-x-vercel-app
- twitter-advanced-search
aliases:
- BirdHunt
- birdhunt.huntintel.io
tags:
- twitter
- x
- geosocial
- geolocation
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# BirdHunt

> A "find tweets by location" search (HuntIntel): pick a place, see X posts and accounts active nearby.

## When to use
You have a `geolocation` — a last-seen area, an incident site, a landmark from a photo — and want to know what X users posted from there. Good for event/scene monitoring and for discovering local accounts to pivot on when you have no handle yet. Complements handle-first tools by working from place → people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://birdhunt.co/ (redirects to `birdhunt.huntintel.io`); sign in with an investigative account if prompted.
2. Set the location of interest (and radius/time window where offered).
3. Review returned posts and authors mapped to the area.
4. Pivot: open a promising author on `[[xcancel-nitter-mirror]]` to read their full timeline; broaden with keyword+date search via `[[twitter-advanced-search]]`. Corroborate any location before treating it as fact.

## Inputs → Outputs
- **In:** `geolocation` (point/area, optional radius + time)
- **Out:** `social-profile` (X posts and their authors), coarse `geolocation` per post
- **Empty/negative result looks like:** no results for the area/time — few geotagged posts exist there, or X data access is limited; widen the window before concluding nothing happened.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** likely required; deeper features are paid.
- OpSec: **passive** toward targets; your searches are logged by a commercial operator — use an investigative account.
- Geotag precision is weak and often self-declared — never treat a shown location as a confirmed device position.

## Overlaps ("do both")
- Pairs with `[[xplore-x-vercel-app]]` (free map-based X geo-explorer) — run both, since each surfaces posts the other misses — and with `[[twitter-advanced-search]]` for keyword-driven follow-up.

## Trust & verifiability
`trust: community` — a commercial tool riding on X's constrained data. Treat location hits as leads and confirm independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | birdhunt |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
