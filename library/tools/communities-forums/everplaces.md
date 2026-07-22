---
id: everplaces
name: Everplaces
description: Use when you have a `username` and want a subject's saved/recommended places — returns `geolocation` travel footprint and `social-profile` links.
url: https://everplaces.com
category: communities-forums
path:
- communities-forums
bestFor: Pulling the locations a person has saved, visited or recommended from their travel/places profile.
selectorsIn:
- username
selectorsOut:
- geolocation
- social-profile
status: degraded
pricing: free
costNote: Free to browse and view public profiles; account only needed to save places.
opsec: passive
opsecNote: Viewing public place-collections and profiles is passive. Do not follow or message a target from a real account — interaction is attributable. Use a sock puppet if you must sign in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legacy travel/places social app (launched ~2012) that appears maintained but low-activity; profile data is self-curated and may be stale.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- everplaces.com
tags:
- social-network
- travel
- places
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Everplaces

> A travel/places social app where users save and share locations they love — a small but literal map of a subject's geographic footprint.

## When to use
You have a `username` (or a candidate profile) and want to know *where* a subject goes: Everplaces profiles are collections of saved and recommended places — restaurants, hotels, cities, hangouts. When populated, that collection reveals home city, travel patterns, favourite venues and, by extension, associates who appear in shared lists. Low-activity platform, so treat a hit as a bonus corroboration layer rather than a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://everplaces.com and look up the `username`, or Google-dork `site:everplaces.com "<username>"`.
2. Open the profile and read the saved-places collections — each entry has a location and often a note or photo.
3. Map the clustering: repeated saves in one city suggest home/base; scattered international saves suggest travel.
4. Pivot: a reused `username` feeds cross-platform enumeration; venue names/geotags feed mapping and place-based OSINT; linked friends feed associate analysis.

## Inputs → Outputs
- **In:** `username`
- **Out:** `geolocation` (saved/visited places), `social-profile`, reused `username`, venue notes/photos
- **Empty/negative result looks like:** no profile for the handle, or an empty/one-item collection — common here given the platform's low activity, so absence is weak evidence.

## Gotchas & OpSec
- Low current activity: many handles won't exist and collections are often stale — don't over-read.
- Saved ≠ visited: a "want to go" pin is aspirational, not a confirmed location.
- Passive to browse; signing in to follow/save is attributable — sock puppet only.

## Overlaps ("do both")
- Pairs with other place/check-in and travel-social tools (Foursquare/Swarm-style) and with reverse-image on venue photos — cross-referencing pins across apps confirms real movement vs wishlist.

## Trust & verifiability
`trust: unverified` — a legacy consumer social app; the platform is real but self-curated and lightly used, so corroborate any location before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | everplaces |
| category | communities-forums |
| selectorsIn → selectorsOut | username → geolocation, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
