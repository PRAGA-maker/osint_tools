---
id: teachingprivacy-com
name: TeachingPrivacy "Ready or Not?"
description: Use when you have a `username` and want to visualise the geotagged posting history behind a public Twitter/Instagram account — was built to map `geolocation` and pattern-of-life from social posts.
url: http://app.teachingprivacy.com
category: image-video-face
path:
- image-video-face
bestFor: Demonstrating/mapping the location trail a person leaves through geotagged Twitter/Instagram posts.
selectorsIn:
- username
selectorsOut:
- geolocation
- social-profile
status: degraded
pricing: free
costNote: Free educational tool from ICSI / UC Berkeley (NSF-funded Teaching Privacy / Geo-Tube project); no account.
opsec: passive
opsecNote: It queries public post metadata for a handle; the target is not notified. Historically it hit Twitter/Instagram APIs, so its function now depends on those APIs — which have been heavily locked down.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Academic project by ICSI/UC Berkeley computer scientists (NSF-funded); trustworthy as built, but almost certainly degraded/defunct after Twitter and Instagram closed public API/geo access.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Ready or Not
- Teaching Privacy app
- app.teachingprivacy.org
tags:
- reverse-image
- face
- geolocation
- social-media
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# TeachingPrivacy "Ready or Not?"

> An academic privacy-demo tool that plotted a user's geotagged Twitter/Instagram posts on a map to show how much location data public accounts leak — conceptually a pattern-of-life mapper, but reliant on now-restricted social APIs.

## When to use
You have a `username` for a public Twitter/Instagram account and want to see where and when that person has been posting from — a location heat map / pattern-of-life built purely from public geotags. That was exactly this tool's purpose (built by ICSI/UC Berkeley to teach oversharing risks). Treat it as `degraded`: Twitter/X and Instagram have since shut down the public API and geo access it depended on, so it is likely non-functional today. Verify it loads and returns data for a test account before relying on it, and reach for maintained geo tools if it doesn't.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://app.teachingprivacy.com (or the `.org` mirror).
2. Enter the target's Twitter/Instagram `username`.
3. If functional, it renders a map of geotagged posts over roughly the last 30 days — locations and times.
4. Read the clusters: home/work candidates, routine, and recent movements.
5. Pivot: location clusters feed geolocation/address work; if the tool is dead, extract geotags manually or use a maintained social-geo tool.

## Inputs → Outputs
- **In:** `username` (public Twitter/Instagram account)
- **Out:** `geolocation` history (mapped geotagged posts), `social-profile` context
- **Empty/negative result looks like:** an empty map or an error — now the common case due to API lockdowns, or because the subject never geotagged posts (which is itself a finding).

## Gotchas & OpSec
- Likely defunct: the underlying Twitter/Instagram public-geo access has been closed; don't assume "no data" means "no travel."
- Only ever surfaced *public* geotags the user chose to attach — not a live tracker.
- Educational demo, not a maintained investigative product — expect no support.

## Overlaps ("do both")
- Pairs with manual geotag extraction and image-EXIF/geolocation tools — those still work when this API-bound demo does not.

## Trust & verifiability
`trust: trusted` — a credible academic project; the caveat is operational (API-dependent and probably retired), not authenticity. Confirm it still runs before citing any output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | teachingprivacy-com |
| category | image-video-face |
| selectorsIn → selectorsOut | username → geolocation, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
