---
id: facebook-com
name: Facebook Ad Library
description: Use when you have a `name`, `employer-org` or Page and want the ads that entity has run on Meta platforms — returns social-profile, employer-org and funding/contact metadata.
url: https://www.facebook.com/ads/library/?active_status=all&ad_type=political_and_issue_ads&country=GB
category: social-networks
path:
- social-networks
bestFor: Finding every ad a Facebook/Instagram Page or advertiser has run — including who paid for political/issue ads — via Meta's official transparency archive.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free, first-party Meta transparency tool; no account needed to view most ads (political/issue ad details are fully public).
opsec: passive
opsecNote: This is Meta's public archive; you search the advertiser, not the subject's personal account, and no login is required for the library. Standard passive browsing; use a sock puppet if you want to avoid any session correlation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Meta (Facebook) product; the ad-transparency data is authoritative because it comes from the platform that served the ads.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- facebook
- facebook-ad-s-link
- facebook-com-2
- facebook-directory-users-by-name
- facebook-live-map
- facebook-photos-by-id
- facebook-profile-directory
- facebook-watch
- fb-email-search
- fb-identify-requires-logout
- recover-fb-account
aliases:
- Facebook Ad Library
- Meta Ad Library
tags:
- facebook
- Facebook General Links
- ad-transparency
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Ad Library

> Meta's official ad-transparency archive — search any Page or advertiser and see every ad they run, with funding disclosure for political and issue ads.

## When to use
You have a `name`, `employer-org`, business, campaign, or Facebook Page and want to see their advertising footprint. For political/issue ads it also exposes the "paid for by" disclaimer, spend ranges, and reach — a strong lever for tying an organisation, campaign, or individual to funding sources and active Pages. Useful for corroborating that a business/entity is real and currently active.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Ad Library and set the country and ad category (all ads, or political & issue ads for the funded-disclosure data).
2. Search by advertiser `name`, Page, or keyword.
3. Read the results: active/inactive ads, launch dates, platforms shown, and — for political/issue ads — the funding entity, spend, and reach `metadata`.
4. Pivot: a linked Page feeds `social-profile` enrichment; a "paid for by" entity feeds `employer-org`/company records; ad creative may reveal contact details or locations.

## Inputs → Outputs
- **In:** advertiser `name` / `employer-org` / Page / keyword
- **Out:** `social-profile` (the Page), `employer-org` (funding entity), ad `metadata` (dates, spend/reach for political ads, creative)
- **Empty/negative result looks like:** "no ads to show" — the entity either never advertised or ran only non-political ads that have since expired (non-political ad history is limited).

## Gotchas & OpSec
- Full detail (spend, reach, funding) exists only for political/issue ads; commercial ads show far less and only while active (plus a short window).
- Country scoping matters — set the correct `country` parameter or you will miss ads.
- OpSec: passive; first-party public archive, no login.

## Overlaps ("do both")
- Pairs with company-records and domain tools — the funding entity revealed here becomes an `employer-org` to run through corporate registries.

## Trust & verifiability
`trust: trusted` — it is Meta's own transparency product, so the ad data is authoritative for the platform it covers; the disclosures are as accurate as what advertisers submitted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-com |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, metadata |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
