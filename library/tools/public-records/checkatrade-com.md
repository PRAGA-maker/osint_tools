---
id: checkatrade-com
name: Checkatrade
description: Use when you have a tradesperson's `name`, business name or `address`/area and want their UK trade listing, reviews and contact/location — returns `employer-org`, `address`, `phone`, `social-profile`.
url: https://www.checkatrade.com/
category: public-records
path:
- public-records
bestFor: Locating and vetting a UK tradesperson via their Checkatrade business profile, reviews and service area.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- phone
- social-profile
status: live
pricing: free
costNote: Free to search and read profiles/reviews; membership (the listing side) is paid for traders, but browsing costs nothing.
opsec: passive
opsecNote: Public directory; browsing is passive and needs no login. Contacting a trader through the site is an active step — keep to reading unless you intend to engage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Checkatrade vets member traders and publishes verified customer reviews, but listing content (business name, area, description) is trader-supplied.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Check a Trade
tags:
- professionlicensing
- Profession & Licensing Sites
- trades
- reviews
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Checkatrade

> The UK's best-known vetted-tradespeople directory: a way to tie a name or trade business to a service area, reviews, contact details and often a photo/logo.

## When to use
You have a `name`, a trade business name, or an area, and think the subject works in the UK trades (builder, electrician, plumber, roofer, etc.). Checkatrade profiles map the trader to a business name, coverage area, contact route and a body of dated customer reviews — useful for locating a self-employed subject whose livelihood is a trade, corroborating employment, and building a timeline from review dates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.checkatrade.com/ and search by trade + location, business name, or member name.
2. Open a profile: business name, area covered, services, contact route, membership/verification status, and reviews.
3. Read reviews for pivots — reviewers sometimes name locations/jobs and dates that place the trader in time and space.
4. Note the business name and area as `employer-org`/`address` pivots.
5. Pivot: run the business name through Companies House and general search; reverse-image any logo/work photos.

## Inputs → Outputs
- **In:** `name`, trade `employer-org`, or `address`/area
- **Out:** `employer-org` (trade business), `address`/service area, `phone`/contact route, `social-profile`/website, dated reviews
- **Empty/negative result looks like:** no listing — the subject isn't a Checkatrade member (many traders use rivals like MyBuilder/TrustATrader or none), trades under another name, or works outside the UK.

## Gotchas & OpSec
- Covers only Checkatrade members — a blank result is common; check MyBuilder, TrustATrader, Rated People and Google Business too.
- Listing details are trader-supplied marketing; "area covered" is a coverage region, not a home address.
- Reviews are moderated but still one-sided marketing signal — read them for factual pivots, not as neutral truth.

## Overlaps ("do both")
- Pairs with Companies House and rival trade directories — this confirms the trade and area, those add ownership/registration and cross-cover missing members.

## Trust & verifiability
`trust: community` — Checkatrade vets traders and verifies reviews, but profile content is self-supplied; corroborate business name, area and identity against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | checkatrade-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, phone, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
