---
id: kijiji-canada-classifieds
name: Kijiji - Canada Classifieds
description: Use when investigating a Canadian subject and you want to search local classifieds for their posts, sales, vehicles, or contact details by `name`, `phone`, or location.
url: https://www.kijiji.ca:443/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching Canadian local classifieds for a subject's posts, sales, or contact info
selectorsIn:
- name
- phone
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
costNote: Free to browse and search; account needed only to post or message.
opsec: passive
opsecNote: Browsing and searching are passive. Messaging a seller is active and can expose you; use a burner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Kijiji is Canada's leading classifieds platform (owned by Adevinta/eBay lineage); individual posts are user-supplied and unverified.
missingPersonsRelevance: medium
coverage:
- ca
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
- canada
- arf-seed
source: arf-seed
lastVerified: ''
enrichment: full
---

# Kijiji - Canada Classifieds

> Canada's dominant local classifieds site — the Canadian counterpart to Craigslist for finding a subject's listings, vehicles, and contact details.

## When to use
Use it when the subject is in Canada and you have a `name`, `phone`, `email`, or location. Listings can surface a `phone`/`email`, vehicle details, a city/region, and selling patterns that place or timeline a person. Strongest signal when the subject buys/sells vehicles, housing, or services.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kijiji.ca/, set the location to the subject's city/province, and search by keyword.
2. Also try Google site search (`site:kijiji.ca "<term>"`) to catch posts the on-site search misses.
3. Read listings for contact info, photos (check downloadable images for EXIF), and location.
4. Pivot: a recovered `phone`/`email` feeds reverse-contact tools; vehicle details feed plate/VIN workflows.

## Inputs → Outputs
- **In:** `name`, `phone`, `geolocation`, `email`
- **Out:** `phone`, `email`, `geolocation`, vehicle details (`vehicle-plate`), `associate`
- **Empty/negative result looks like:** no listings or only expired ones — Kijiji ages out old posts, so use archives for historical activity.

## Gotchas & OpSec
- Human-in-the-loop: none to browse/search.
- OpSec: passive while reading; messaging a seller exposes you — use a burner, never contact the subject. Capture evidence promptly before posts expire.

## Overlaps ("do both")
- Pairs with `[[craigslist]]` (US equivalent), reverse-phone tools, and Wayback/archive search for expired posts.

## Trust & verifiability
`trust: trusted` — Kijiji is an established, real Canadian platform; the accuracy of any individual post is user-supplied and must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kijiji-canada-classifieds |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, geolocation, email → phone, email, geolocation, vehicle-plate, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
