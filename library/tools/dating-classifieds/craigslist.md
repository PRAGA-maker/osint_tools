---
id: craigslist
name: Craigslist
description: Use when you have a `phone`, `name`, or location keyword and want to search US local classifieds for a subject's posts, listings, or contact info.
url: https://charlotte.craigslist.org/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching US local classifieds for a subject's posts, sales, or contact details
selectorsIn:
- phone
- name
- geolocation
- email
selectorsOut:
- phone
- email
- geolocation
- vehicle-plate
- associate
status: live
pricing: free
costNote: Free to browse and search; most categories require no account.
opsec: passive
opsecNote: Browsing and searching are passive. Replying to a post (via the relay email or phone) is active and can reveal your identity; use a burner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Craigslist is a real, widely used US classifieds platform; individual post content is user-supplied and unverified.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags:
- classifieds
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# Craigslist

> The dominant US local classifieds site — searchable per-city listings that can tie a subject to a `phone`, an item for sale, a vehicle, or a neighborhood.

## When to use
Use it when you have a `name`, `phone`, `email`, or a location and want to find a subject's activity: items for sale, housing, services, or gigs. Posts often leak a `phone`/`email`, a vehicle (`vehicle-plate`/description), a neighborhood, and behavioral patterns useful for placing or timelining someone. Search the relevant city subdomain, not just the seeded Charlotte one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the city subdomain matching the subject's area (replace `charlotte` in the URL) and use the search box per category.
2. Search by keyword, phone fragment, or distinctive item; also try Google site search (`site:craigslist.org "<term>"`) to span cities.
3. Read posts for contact details, photos (check for EXIF if downloadable), and location hints.
4. Pivot: a recovered `phone`/`email` feeds reverse-phone/email tools; a vehicle description feeds plate/VIN workflows.

## Inputs → Outputs
- **In:** `phone`, `name`, `geolocation`, `email`
- **Out:** `phone`, `email`, `geolocation`, `vehicle-plate`/vehicle details, `associate`
- **Empty/negative result looks like:** no posts (most people never post), or expired listings — Craigslist purges old posts, so check archives for historical activity.

## Gotchas & OpSec
- Human-in-the-loop: none to browse/search.
- OpSec: passive while reading. Craigslist relays email, but replying still exposes you — use a burner and never contact the subject. Posts expire quickly, so capture evidence immediately.

## Overlaps ("do both")
- Pairs with `[[kijiji-canada-classifieds]]` (Canada equivalent), reverse-phone tools, and Wayback/archive search for expired posts.

## Trust & verifiability
`trust: trusted` — Craigslist itself is an established, real platform; the truthfulness of any individual post is user-supplied and must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | craigslist |
| category | dating-classifieds |
| selectorsIn → selectorsOut | phone, name, geolocation, email → phone, email, geolocation, vehicle-plate, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
