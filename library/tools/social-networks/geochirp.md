---
id: geochirp
name: GeoChirp
description: Use when you have a `geolocation` or keyword and want to find tweets/Twitter users near a place on a map — returns `social-profile` and `geolocation` matches (functionality now impaired by X API limits).
url: http://www.geochirp.com
category: social-networks
path:
- social-networks
bestFor: Map-based geographic Twitter/X search — finding tweets and users around a location on a Google Map.
selectorsIn:
- geolocation
- username
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free to use, but now requires a logged-in Twitter/X account and is constrained by X's API restrictions.
opsec: active
opsecNote: It now requires you to authenticate with a Twitter/X account, so any use is tied to that account and visible to X — always use a dedicated sock-puppet account, never your own, and expect limited or no results due to API throttling.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A 2009-era Twitter/Google Maps mashup (CueBlocks); the site still loads but its usefulness has been undercut by X's post-2023 API lockdown — verify it returns results before relying on it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Geochirp
- geochirp.com
tags:
- twitter
- geosocial
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# GeoChirp

> A veteran Twitter-on-a-map mashup for finding tweets and users near a location — still online, but hobbled by X's API restrictions, so treat results as best-effort.

## When to use
You have a `geolocation` (or a keyword/topic) and want to see Twitter/X activity around that point on a map — for example, users tweeting from near a last-known location. Historically handy for geosocial discovery; today its value is limited because X has locked down the API these mashups depend on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.geochirp.com in a browser signed into a **sock-puppet** Twitter/X account (login is now required).
2. Set the map location/radius and/or enter a search term.
3. Run the search to plot matching tweets/users on the Google Map.
4. Read the output: pinned tweets and the associated accounts (`social-profile`) with their approximate `geolocation`.
5. Pivot: take surfaced handles into username lookups and native X search; corroborate any location, since geotags are sparse and often imprecise.

## Inputs → Outputs
- **In:** `geolocation` and/or keyword (optionally a `username`)
- **Out:** `social-profile` (matching accounts/tweets), `geolocation` (approximate tweet locations)
- **Empty/negative result looks like:** no pins returned — increasingly the norm given X API limits and the scarcity of geotagged tweets; absence is not evidence of absence.

## Gotchas & OpSec
- **Status: degraded** — the site loads but X's API lockdown since 2023 means it frequently returns few or no results; confirm it works before depending on it.
- Requires a Twitter/X login now; only a tiny fraction of tweets carry precise geotags, so coverage is thin.
- OpSec: **active** — usage is tied to the authenticated account; use a throwaway, never a personal one.

## Overlaps ("do both")
- Complements native X advanced search (`geocode:` operator) and other geosocial tools — those are more reliable today; use GeoChirp only as a supplementary map view.

## Trust & verifiability
`trust: unverified` — an old third-party mashup with no guarantees of current accuracy or completeness; whatever it returns should be confirmed on X directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geochirp |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation, username → social-profile, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
