---
id: salespider-north-america
name: SaleSpider (North America)
description: Use when you have a business `name` or `employer-org` and a `geolocation` and want its listing/owner contact — returns `address`, `phone`, and `employer-org` detail.
url: http://www.salespider.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Looking up a North American small business's free directory listing, classifieds, and owner/contact details.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free B2B business-directory and classifieds/community site; free registration unlocks messaging and lead tools, but directory listings are readable without an account.
opsec: passive
opsecNote: You read public directory/classified listings; the business is not notified. The site sits behind a Cloudflare browser check, so use a normal (sock-puppet) browser session that can pass the JS challenge.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Aging but functional third-party business directory/classifieds network; listings are self-submitted and often stale, so confirm contact details against a second source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- sales-spider
aliases:
- salespider.com
- SaleSpider Media
tags:
- toddington
- curated-directory
- specialty-search
- business-directory
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# SaleSpider (North America)

> A free North American B2B business directory, classifieds, and small-business social network — useful for tying a subject to a business and pulling that business's address, phone, and owner contact.

## When to use
You have a business `name`/`employer-org` connected to the subject (a company they run, work for, or advertise through) plus a rough `geolocation`, and you want the listed `address`, `phone`, and any owner/contact detail. Small-business directories like this often carry contact info for sole proprietors and micro-businesses that never appear in formal corporate registries — a way to reach a person through their business footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open salespider.com in a normal (sock-puppet) browser so it can clear the Cloudflare "just a moment" check.
2. Use the business directory search for the `name`/`employer-org`, filtered by North American location.
3. Open the listing and read the `address`, `phone`, website, category, and any owner/contact name; also check the classifieds section for ads tied to the same seller.
4. Optionally register a free account for messaging/lead features — not needed just to read listings.
5. Pivot: run the `address` through property/records tools, the `phone` through reverse-phone lookup, and any owner `name` back through people-search.

## Inputs → Outputs
- **In:** business `name`/`employer-org` + `geolocation`
- **Out:** `address`, `phone`, `employer-org` detail, website, sometimes an owner/contact name
- **Empty/negative result looks like:** no matching listing — the business isn't registered here (many aren't), is outside North America, or has been removed; weak negative evidence.

## Gotchas & OpSec
- Cloudflare interstitial: a real browser passes it automatically; a bare CLI fetch will be blocked (HTTP 403).
- Listings are self-submitted and frequently outdated or duplicated — verify any contact detail before relying on it.
- Business/classifieds directory, not a people index — value is reaching a person *via* their business.

## Overlaps ("do both")
- Pairs with `[[sales-spider]]` (same provider) and with corporate-registry/property tools — the directory gives quick contact info; the registries give the legal ownership behind it.

## Trust & verifiability
`trust: unverified` — a real, long-running directory, but all listing data is user-submitted with no verification; treat address/phone as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | salespider-north-america |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, employer-org, geolocation → address, phone, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
