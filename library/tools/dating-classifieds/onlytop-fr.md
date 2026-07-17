---
id: onlytop-fr
name: OnlyTop (onlytop.fr)
description: Use when you have a `username`, `name`, or location and want to find a matching OnlyFans creator profile — returns `social-profile`, location, and content-category leads.
url: https://onlytop.fr/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching for OnlyFans creator profiles by username, name, location, or content niche via a third-party directory/finder.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to search; creators can pay for extra visibility. No account needed to browse.
opsec: passive
opsecNote: Searching a third-party directory is passive — you don't touch OnlyFans or contact the creator. The subject matter is adult; use a sock-puppet browser and handle any findings with discretion and legal/ethical care.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An independent, unofficial directory with no affiliation to OnlyFans; listings are self-promoted/scraped and unverified, so treat matches as leads to confirm.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- OnlyTop
- onlytop.fr
tags:
- onlyfans
- OnlyFans Related Sites
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# OnlyTop (onlytop.fr)

> A third-party OnlyFans creator finder — search by username, name, location, or niche to locate a subject's adult-content presence when that's part of an investigation.

## When to use
You have a `username`, `name`, or location and need to check whether a subject has an OnlyFans presence — relevant in missing-persons, trafficking, exploitation, or fraud contexts where a person's adult-content activity is investigatively significant. Because OnlyFans itself has no public search, third-party finders like this are one of the few ways to locate a creator profile from a handle or name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlytop.fr/ in a sock-puppet browser.
2. Search by full name, username, location, or content category; apply filters (niche, location).
3. Open a candidate profile for the linked OnlyFans handle, stated location, and displayed details.
4. Corroborate the match — a reused `username`/avatar is the strongest link — before concluding it's the same person.
5. Pivot: the OnlyFans handle feeds cross-platform username search; a reused avatar feeds reverse-image tools; a stated location narrows geography.

## Inputs → Outputs
- **In:** `username`, `name`, or location/niche filter
- **Out:** `social-profile` (OnlyFans handle/link), `geolocation` (self-stated location), and content-category leads.
- **Empty/negative result looks like:** no matching creator — the person isn't listed here (the directory is partial and self-promoted), or uses a different handle; try other OnlyFans-search sites and a general username search.

## Gotchas & OpSec
- Unofficial and unverified: listings are self-promoted or scraped, locations are self-stated, and impersonation/fakes exist — never assume a match is genuine without corroboration.
- Adult content: handle findings with care, mindful of consent, exploitation indicators, and legal boundaries.
- OpSec: passive, but use a persona browser and keep results confidential.

## Overlaps ("do both")
- Complements other OnlyFans-finder sites and cross-platform username tools — no single directory is complete, and a reused handle/avatar is what actually ties the profile to your subject.

## Trust & verifiability
`trust: unverified` — an unofficial directory with no OnlyFans affiliation and self-submitted data; every match must be independently corroborated (handle reuse, avatar, other platforms) before you rely on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlytop-fr |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
