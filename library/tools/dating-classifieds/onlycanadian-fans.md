---
id: onlycanadian-fans
name: onlycanadian.fans
description: Use when you have a `username`/`name` and think the subject is a Canadian OnlyFans creator — returns matching creator `social-profile`s filtered by Canadian `geolocation`.
url: https://onlycanadian.fans/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding Canadian OnlyFans creators by handle, name, or city/category.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to browse and search the directory; it aggregates public profile links (the linked OnlyFans accounts themselves may be paid).
opsec: passive
opsecNote: Passive — you query a third-party aggregator, not OnlyFans, so the creator is not notified. The operator logs your searches; it indexes only public profile data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent Canadian-focused OnlyFans directory, explicitly unaffiliated with OnlyFans; coverage and accuracy are unverified against the source.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- fanslist-com
aliases:
- Only Canadian Fans
tags:
- onlyfans
- OnlyFans Related Sites
- canada
- creator-search
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# onlycanadian.fans

> A Canada-focused directory of OnlyFans creators, searchable by handle, name, city, or category.

## When to use
You have a `username` or `name` and reason to think the subject is an OnlyFans creator based in Canada, or you want to filter creators by a Canadian city (Toronto, Vancouver, Montreal, etc.). A regional narrowing of the broader OnlyFans-directory approach — a hit provides a creator `social-profile` and a `geolocation` (stated city) to corroborate location and open cross-platform handle pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlycanadian.fans/.
2. Search by `username`/`name`, or filter by location (Canadian city) and category.
3. Open a matching creator entry to see the linked OnlyFans profile, stated city, and any cross-linked handles.
4. Pivot: the handle feeds username-enumeration across platforms; the stated city is a `geolocation` lead to corroborate.

## Inputs → Outputs
- **In:** `username` or `name` (optionally city/category filter).
- **Out:** matching creator `social-profile`(s), canonical handle, and stated Canadian `geolocation`.
- **Empty/negative result looks like:** no matching entry — the handle/name isn't in this Canada-scoped index (try the broader `[[fanslist-com]]`).

## Gotchas & OpSec
- Canada-scoped: coverage is limited to creators the site tags as Canadian; non-Canadian or unlisted creators won't appear.
- Third-party index: possibly stale; absence isn't proof of no account.
- Stage names: creators use pseudonyms — a handle match is a lead, not identity confirmation.
- Adult content: results are NSFW; handle within your authorization and evidence rules. OpSec: passive, no target notification.

## Overlaps ("do both")
- Pairs with `[[fanslist-com]]` (global OnlyFans index) — use this for the Canadian regional filter and FansList for broader coverage; run both when location is uncertain.

## Trust & verifiability
`trust: community` — an independent aggregator not affiliated with OnlyFans; treat listings as unverified public-data mirrors and confirm any live profile directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlycanadian-fans |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
