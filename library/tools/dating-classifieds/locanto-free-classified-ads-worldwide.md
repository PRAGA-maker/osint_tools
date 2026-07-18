---
id: locanto-free-classified-ads-worldwide
name: Locanto Free Classified Ads (Worldwide)
description: Use when you have a username, phone, or location and want to find a subject's classified ads (jobs, personals, sales) — returns social-profile, phone, and geolocation leads.
url: http://www.locanto.info
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching worldwide free classified ads (personals, services, jobs, for-sale) for a person's postings, contact details, and location.
selectorsIn:
- username
- geolocation
selectorsOut:
- phone
- social-profile
- geolocation
status: live
pricing: free
costNote: Free to browse and search ads; posting is free with an optional paid promotion tier.
opsec: passive
opsecNote: Browsing ads is passive and needs no login. Do NOT reply to or contact an advertiser from an attributable account — that would alert the subject. Use a sock-puppet browser; classifieds (especially personals) are sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large, established global classifieds network; content is user-posted and unverified, so treat ad details as claims, not facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Locanto
- locanto.info
tags:
- classifieds
- personals
- dating-classifieds
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Locanto

> A large worldwide free-classifieds network — search it for a subject's own postings (services, sales, jobs, personals), which often carry a phone number, location, and a reused handle.

## When to use
You have a `username`, a `geolocation` (city/region), or a phone number and want to find classified ads a subject placed. People selling items, offering services, seeking work, or posting personals frequently expose a `phone`, a rough `geolocation`, photos, and a `social-profile`-style handle. Locanto is broad and used globally, so it's worth checking alongside Craigslist/Gumtree-type sites when profiling someone's local activity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Locanto (locanto.info / your target's country domain) and pick the region, then use the keyword search.
2. Search a reused username, a phone number, a distinctive phrase, or browse the relevant category in the subject's city.
3. Open matching ads: note contact phone, listed location, photos, posting date, and any handle or external link.
4. Pivot: run a phone through phone-OSINT; reverse-image any photos; a reused handle extends username enumeration. Cross-check the same query on other classifieds sites.

## Inputs → Outputs
- **In:** `username`, `geolocation` (city/region), or a phone/keyword
- **Out:** `phone`, `geolocation` (ad location), `social-profile` (handles/links in ads), plus photos
- **Empty/negative result looks like:** no ads matching the term/area — the subject may not use Locanto, posted under a different handle, or the ad has expired (classifieds age out quickly).

## Gotchas & OpSec
- Human-in-the-loop: none to search; replying/contacting requires care and would expose you.
- OpSec: passive when browsing — but never contact an advertiser from an attributable account. Personals and adult sections are sensitive; handle discreetly.
- Unverified content: ads are self-posted and sometimes scams or reposts; corroborate any contact detail before relying on it.

## Overlaps ("do both")
- Pairs with other classifieds (Craigslist, Gumtree) and phone/reverse-image tools — Locanto surfaces the ad, and phone-OSINT / reverse-image turn its contact and photos into an identity.

## Trust & verifiability
`trust: community` — Locanto is a real, widely-used platform, but every ad is user-generated and unverified; treat listed details as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | locanto-free-classified-ads-worldwide |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, geolocation → phone, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
