---
id: sotugas-net
name: SóTugas
description: Use when you have a `username` or `name` and want a Portuguese creator profile — returns a directory listing of Portugal-based OnlyFans creators with linked handles.
url: https://sotugas.net/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding and cross-referencing Portugal-based OnlyFans creators by handle, name, or region.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to browse the directory; it only indexes/links external OnlyFans creators, who set their own subscription fees.
opsec: passive
opsecNote: Passive browsing of a public directory that only links out to OnlyFans; you do not touch the creator's account. Do not subscribe or message from a real identity, and treat linked adult content as sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party fan-made directory ("no connection with onlyfans.com"); listings are curated/self-submitted and unverified, and profiles can be mislabeled.
missingPersonsRelevance: medium
coverage:
- pt
auth: none
api: false
localInstall: false
registration: false
aliases:
- sotugas.net
- SoTugas
tags:
- onlyfans
- OnlyFans Related Sites
- creator-directory
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# SóTugas

> A Portuguese-language directory of Portugal-based OnlyFans creators — a regional index for confirming and cross-referencing an adult-creator handle by name, region, or category.

## When to use
You have a `username` or `name` possibly linked to a Portuguese adult-content creator and want to confirm the profile exists and find the associated OnlyFans handle and any linked socials. Because it is region-scoped (Portugal) and organised by category, it is useful for narrowing a `geolocation`, linking an alias to a creator identity, and pivoting to reverse-image search on preview media. Use it as a directory/index, not a content source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sotugas.net/ and browse or search by handle, name, category, or region.
2. Open a matching listing to read the display name, linked OnlyFans handle, and any other socials referenced.
3. Note reused handles and preview images; save previews for reverse-image search.
4. STOP at the directory/preview level — do not subscribe or message from a real identity.
5. Pivot: a reused `username` feeds a cross-site enumerator; the OnlyFans handle feeds other OnlyFans-related tools; preview `image`s feed face/reverse-image search.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (directory listing + linked OnlyFans/other handles)
- **Empty/negative result looks like:** no listing matches — the creator isn't indexed here (the directory is Portugal-focused and incomplete). Absence proves nothing about other platforms or regions.

## Gotchas & OpSec
- Third-party, self-submitted directory with no OnlyFans affiliation — listings can be inaccurate, mislabeled, or stale; corroborate identity before relying on it.
- Region-scoped to Portugal, so coverage is narrow.
- Handle linked adult content and previews as sensitive; do not redistribute.

## Overlaps ("do both")
- Pairs with broader OnlyFans-related lookup tools and cross-site username enumerators — SóTugas gives a region-scoped index; those confirm the handle exists elsewhere and reverse-image search ties previews to other profiles.

## Trust & verifiability
`trust: unverified` — a fan-made, unaffiliated directory of self-submitted listings; treat every entry as a lead to confirm on the linked platform, not as verified fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sotugas-net |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
