---
id: transsearcher-com
name: transsearcher.com
description: Use when you have a `username` or a location and want matching adult-creator (OnlyFans) profiles — returns creator `social-profile` links filterable by area and category.
url: https://transsearcher.com/free
category: dating-classifieds
path:
- dating-classifieds
bestFor: Discovering trans/adult OnlyFans creator profiles by username, location or category, as a pivot toward a subject's linked handles.
selectorsIn:
- username
- address
selectorsOut:
- social-profile
- username
- image
status: live
pricing: free
costNote: The aggregator is free to browse; the underlying OnlyFans creator pages may charge for content, but discovery here costs nothing.
opsec: passive
opsecNote: A third-party aggregator that indexes public OnlyFans creator pages; browsing does not notify the creator. Clicking through to OnlyFans or subscribing would expose your account — stay on the index for discovery, and use a sock puppet if you must visit the source profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An independent third-party directory, not affiliated with OnlyFans. Listings are scraped/aggregated and may be stale or promotional; treat matches as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- transsearcher
tags:
- onlyfans
- OnlyFans Related Sites
- adult
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# transsearcher.com

> A free third-party index of trans-focused OnlyFans creators, searchable by username, location and category — a discovery layer for adult-platform handles that OnlyFans itself does not expose to search.

## When to use
You have a `username` a subject may reuse on adult platforms, or you are trying to confirm whether a person maintains an OnlyFans/adult-creator presence in a given area. OnlyFans has no public search, so aggregators like this are one of the few ways to surface a creator `social-profile` and the display name, photos and location they advertise — useful for tying an alias to a person and corroborating location or appearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://transsearcher.com/free .
2. Filter by location (country/region), category, or search the `username`/display name a subject may use.
3. Review candidate creator cards — display name, thumbnail `image`, advertised location, and the link to the OnlyFans page.
4. Do not subscribe or message from a real account; reverse-image-search thumbnails and cross-check the handle elsewhere to confirm it is your subject.
5. Pivot: a confirmed handle feeds [[whatsmyname-app]] and other username sweeps; thumbnails feed reverse-image/face search.

## Inputs → Outputs
- **In:** `username` or `address` (location filter)
- **Out:** `social-profile` (OnlyFans creator link), `username`/display name, `image` (thumbnails)
- **Empty/negative result looks like:** no creators match your filters/handle — the subject may not be indexed here, may use a different name, or may not be an adult creator. Absence is not disproof.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing the index.
- OpSec: **passive** on the index itself; visiting/subscribing to the source OnlyFans page is self-exposing — use a burner and never subscribe from a real identity.
- Aggregator data is scraped and can be stale or promotional (SEO-spam creators); verify a handle independently before attributing it to a person.

## Overlaps ("do both")
- Pairs with [[whatsmyname-app]] and reverse-image tools, which independently confirm a handle/photo surfaced here belongs to your subject.

## Trust & verifiability
`trust: unverified` — an unaffiliated third-party scraper of public adult-platform pages; useful for discovery but every match must be corroborated before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | transsearcher-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, address → social-profile, username, image |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
