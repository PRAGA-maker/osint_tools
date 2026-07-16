---
id: classifiedads-com
name: ClassifiedAds.com
description: Use when you have a `name`, `phone`, or `username` and want to find a subject's classified listings — returns a `social-profile`/ad with `phone`, `geolocation` and items for sale.
url: https://www.classifiedads.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching free regional classified ads for a subject's postings (items, jobs, services, personals) and the contact details attached.
selectorsIn:
- name
- phone
- username
selectorsOut:
- social-profile
- phone
- geolocation
status: live
pricing: free
costNote: Free to browse, search, and post; no account needed to read listings.
opsec: passive
opsecNote: Browsing and searching public ads is passive and needs no login — the subject isn't notified. Responding to an ad (email/phone the poster) is active and reveals you; stay at reading unless contact is justified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An open classified-ads platform; postings are self-submitted and unverified, and listings expire, so treat any detail as a time-bound lead.
missingPersonsRelevance: medium
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ClassifiedAds
- classifiedads.com
tags:
- toddington
- curated-directory
- classifieds
- specialty-search
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# ClassifiedAds.com

> A free, searchable classifieds board — people selling, renting, hiring, or posting personals leave behind names, phone numbers, and neighborhoods that don't appear on social media.

## When to use
You have a subject `name`, `phone`, `username`, or an item/service you think they're advertising, and you want their classified postings. Classified ads are a quiet OSINT surface: a listing can hand you a live `phone`, a rough `geolocation` (city/neighborhood), what someone owns or is selling, and an alternate handle — often placing a person somewhere at a specific time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.classifiedads.com and pick the relevant region/category (or use the site search).
2. Search the subject's `name`, `phone`, handle, or a distinctive item; also try a Google site search: `site:classifiedads.com "<phone or name>"`.
3. Open matching ads; note poster name/handle, contact `phone`/email, location, price, and posting date.
4. Reverse the contact details: run the `phone` through phone-OSINT and the email through email tools.
5. Pivot: a `phone`/email links to other listings and accounts; the city/category narrows local records.

## Inputs → Outputs
- **In:** `name`, `phone`, `username`, or item/service keyword
- **Out:** matching ad(s) — poster `social-profile`/handle, contact `phone`/email, `geolocation` (city), posting date
- **Empty/negative result looks like:** no current listings — ads expire and rotate, so a miss often just means nothing is live now (try Google's cache/site-search for expired ones) rather than that the subject never posted.

## Gotchas & OpSec
- Listings are ephemeral — a relevant ad may have expired; use search-engine cache/`site:` queries to recover older ones.
- Self-submitted and unverified; sellers use burner numbers and fake names — corroborate contact details before relying on them.
- Responding to an ad is **active** and exposes you to the poster; keep to passive reading unless contact is warranted.

## Overlaps ("do both")
- Pairs with Craigslist/Gumtree/Facebook Marketplace searches and with phone/email-OSINT — the same seller often reposts across boards; the shared `phone`/email is the through-line.

## Trust & verifiability
`trust: unverified` — a real, open classifieds platform of self-submitted ads; every name/number is a lead to verify, and listings are time-bound snapshots, not standing records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | classifiedads-com |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, username → social-profile, phone, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
