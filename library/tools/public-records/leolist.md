---
id: leolist
name: LeoList
description: Use when you have a `phone`, `username` or city and want to find matching Canadian classified/personal ads — returns phone, social-profile and location leads.
url: https://www.leolist.cc/
category: public-records
path:
- public-records
bestFor: Searching Canadian classified and personal ads by city, keyword, phone or handle to locate a subject's postings.
selectorsIn:
- phone
- username
- geolocation
selectorsOut:
- phone
- social-profile
- address
status: live
pricing: freemium
costNote: Free to browse and search listings; posting/promoting ads is paid. No account needed to read.
opsec: passive
opsecNote: Browsing listings is passive, but content includes adult/personal ads — use a sock-puppet browser and never contact posters, register, or reply during research. In trafficking/missing-persons contexts, involve law enforcement; do not run stings yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An unmoderated classifieds platform; listings are user-generated, unverified, and often use burner contact details — treat everything as a lead to corroborate, not fact.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Leo List
tags:
- classifieds
- personals
- canada
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# LeoList

> A large Canadian classifieds/personals site — searchable by city and keyword, and a place where a subject's phone number, handle or photos may surface in an ad.

## When to use
You're working a Canadian case and have a `phone`, `username`, alias or city and want to know whether a subject appears in classified or personal ads. LeoList carries general classifieds plus personals/adult sections; because posters reuse phone numbers, handles and photos across ads, it can place a person in a city at a time, surface an alias, or link a reused number/image to other postings. It is a lead source used in locating and human-trafficking/missing-persons work — sensitive, and to be handled professionally.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.leolist.cc/ in a sock-puppet browser and select the relevant province/city (`geolocation`).
2. Search by keyword, alias/`username`, or scan a category; where a `phone` is known, search it (and via Google `site:leolist.cc "<number>"`).
3. Read matching ads for reused contact details, handles, photos and location/timing clues.
4. Cross-match a reused `phone`/image/handle across other ads and platforms (reverse image search, phone OSINT).
5. Pivot: corroborate any lead elsewhere; in trafficking/exploitation contexts, escalate to law enforcement rather than acting on it directly.

## Inputs → Outputs
- **In:** `phone`, `username`/alias, or city (`geolocation`) + keyword
- **Out:** matching ads exposing `phone`, `social-profile`/alias, photos, and `address`/area leads
- **Empty/negative result looks like:** no matching ads — the subject may not post here, may use different contact details, or the ad may have expired/been removed; absence proves nothing.

## Gotchas & OpSec
- OpSec: passive browsing only. Do **not** register, reply, or contact posters during research; use a sock puppet.
- Everything is user-generated and unverified; burner numbers, stock/stolen photos and false locations are common — corroborate before believing.
- Sensitive/legal terrain (adult content, possible exploitation): follow your legal and ethical obligations and hand exploitation indicators to law enforcement.

## Overlaps ("do both")
- Do both with reverse-image search and phone-OSINT tools — a reused photo or number on LeoList is the pivot; those tools connect it to other ads, platforms and identities.

## Trust & verifiability
`trust: community` — an unmoderated user-generated classifieds site; treat every listing as an unverified lead requiring independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leolist |
| category | public-records |
| selectorsIn → selectorsOut | phone, username, geolocation → phone, social-profile, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
