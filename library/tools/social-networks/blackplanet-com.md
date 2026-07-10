---
id: blackplanet-com
name: BlackPlanet
description: Use when you have a `username` or `name` and want to check a legacy BlackPlanet profile — but note the site has pivoted to a news platform, so profile search is largely degraded.
url: https://www.blackplanet.com/
category: social-networks
path:
- social-networks
bestFor: Checking for a legacy BlackPlanet member profile/handle (historically a major Black social network).
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free to access; historically required an account to view full member profiles.
opsec: passive
opsecNote: Browsing the public site is passive. If any legacy profile area still requires login, use a sock-puppet account rather than a real one, since viewing/following can be visible to members.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: BlackPlanet was a long-running social network but the current site presents as a news platform; whether the old member directory/profile search still works is uncertain. User-supplied profile data was always self-asserted.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-web
- google-com-90
aliases:
- blackplanet.com
tags:
- gsocialmedia
- General Social Media Sites
- legacy-social-network
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# BlackPlanet

> A once-major Black social network now presenting primarily as a news platform — of residual OSINT value mainly for legacy/archived profiles rather than live member search.

## When to use
You have a `username` or `name` and are chasing a subject's older online footprint. BlackPlanet was, for years, one of the largest social networks aimed at Black American users, so a legacy profile there can surface an old handle, photos, or connections. Treat it as a historical-footprint check — the current site has pivoted toward news aggregation and no longer clearly offers a public member directory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.blackplanet.com/ and look for any surviving member/profile search; much of the site now serves news content.
2. If a legacy profile URL or handle is known, try it directly.
3. Because live profile search is degraded, also query archives: search the subject's handle on `[[google-com-90]]` with `site:blackplanet.com`, and check the Wayback Machine for old profile snapshots.
4. Pivot: an old handle feeds cross-platform username enumeration; archived bio details feed name/location searches.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (legacy/archived), `name` — where any profile survives
- **Empty/negative result looks like:** the site returns only news content and no member match — expected given the pivot. Fall back to search-engine and archive lookups before concluding nothing exists.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; a legacy login wall, if present, needs a puppet account.
- OpSec: **passive** while browsing anonymously.
- Platform pivot: the classic profile-search premise is largely gone — lean on cached/archived copies, not live search.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-web]]` — enumerate the handle across many sites at once, including whatever BlackPlanet profile endpoint still resolves.
- Pairs with `[[google-com-90]]` — `site:blackplanet.com` dorking plus Wayback often recovers legacy profiles the live site no longer surfaces.

## Trust & verifiability
`trust: unverified` — the platform's current form and the status of its member search are uncertain, and historical profile data was always self-asserted; corroborate anything found here elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blackplanet-com |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
