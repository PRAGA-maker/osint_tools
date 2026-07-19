---
id: lawyerratingz-north-america
name: Lawyerratingz (North America)
description: Use when you have a `name` you believe is an attorney and want to confirm the practice and location — returns firm/city listing plus consumer ratings and reviews.
url: https://www.lawyerratingz.com
category: search-engines
path:
- search-engines
bestFor: Confirming whether a named person practices law in the US/Canada and locating their firm/city via a consumer ratings directory.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free to search and read listings and reviews; part of the ad-supported "Ratingz Network." No account needed to view.
opsec: passive
opsecNote: Public directory browsing — no login, nothing written, the subject is not notified. Reading a listing is passive; do NOT post a review, as that writes attributable content and could constitute harassment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced, anyone-can-add directory of consumer reviews; the existence/location fields are useful leads but reviews are unverified and have drawn complaints about moderation, so corroborate against a state bar record.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- LawyerRatingz
tags:
- toddington
- curated-directory
- specialty-search
- attorney
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Lawyerratingz (North America)

> A crowd-sourced consumer-review directory of US and Canadian attorneys — a quick way to confirm someone practices law and to find their firm and city.

## When to use
You have a `name` and a reason to think the person is (or was) a practising attorney in North America, and you want to confirm it and pin down where: firm, city, practice area. Lawyerratingz lists lawyers with location and consumer ratings, so it can corroborate a professional identity and surface a business `address` to pivot on. Because it is open-submission, treat the listing as a lead and the reviews as unverified opinion — confirm the licence itself against the relevant state/provincial bar.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lawyerratingz.com and search the attorney's name (or browse by state/city).
2. Open the matching listing: note the firm, city, practice area, and any rating/review text.
3. Cross-check the person against the official state bar / law-society "find a lawyer" record to confirm the licence and current status.
4. Pivot: a confirmed firm becomes an `employer-org` and office `address` for further lookups; review text occasionally names a case or associate.

## Inputs → Outputs
- **In:** `name` (suspected attorney, US/Canada)
- **Out:** `employer-org` (firm), business `address`/city, practice area, consumer ratings
- **Empty/negative result looks like:** no listing, or only unrelated same-name entries — meaning the person isn't in this crowd directory, which does NOT prove they aren't a lawyer (many aren't listed).

## Gotchas & OpSec
- Human-in-the-loop: none to read; do not submit a review (attributable, potentially harassing).
- Anyone can add or review a lawyer, so entries can be stale, wrong, or planted — always verify against the official bar record.
- Common names produce collisions; disambiguate by city/practice area.

## Overlaps ("do both")
- Pairs with an official state-bar / law-society lookup — that is the authoritative licence record; this adds location and consumer-facing context around it.

## Trust & verifiability
`trust: community` — open-submission consumer directory; treat listings as leads and reviews as unverified, confirming the underlying facts against a primary bar record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawyerratingz-north-america |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
