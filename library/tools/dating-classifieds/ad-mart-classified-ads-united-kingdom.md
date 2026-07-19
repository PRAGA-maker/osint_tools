---
id: ad-mart-classified-ads-united-kingdom
name: Ad-Mart Classified Ads (United Kingdom)
description: Use when you have a `name`/`username` or item and want UK classified-ad activity — now UK Classifieds; returns ads exposing seller `phone`/location and `social-profile` handles.
url: https://www.ukclassifieds.co.uk/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Searching free UK regional classified ads (for-sale, vehicles, services, jobs, pets) for a subject's listings and the contact details they reveal.
selectorsIn:
- name
- username
selectorsOut:
- phone
- geolocation
- social-profile
status: live
pricing: free
costNote: Free to browse and post; account optional and free.
opsec: passive
opsecNote: Passive — browsing/searching public ads sends nothing to the seller. Contacting a seller (call/message) is active and exposes you; never engage the subject. Use a sock-puppet if you must register.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (18+ years) free UK classifieds platform (ad-mart.co.uk redirects here); user-posted ads, so details are self-reported and unverified.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UK Classifieds
- Ad-Mart
tags:
- toddington
- classifieds
- uk
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Ad-Mart Classified Ads (United Kingdom)

> A free UK classifieds site — search regional ads for a subject's listings and the phone numbers, locations, and handles they leak.

## When to use
Your subject may buy/sell/advertise on UK classifieds. Ads frequently expose a seller's first `name`, a contact `phone`, a rough location, and sometimes a reused `username`/handle — useful pivots for identity and locating. Search by their name, a known handle, or distinctive items they'd list.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ukclassifieds.co.uk/ (ad-mart.co.uk redirects here).
2. Browse by region/category or use the search box for a `name`, handle, or item keyword.
3. Read the output: matching ads with seller-provided contact details, location, and posting dates.
4. Pivot: reuse the phone/handle across other tools; reverse-image any ad photos; note the location as a residence clue.

## Inputs → Outputs
- **In:** a `name` / `username` / item keyword (+ region)
- **Out:** classified ads exposing seller `phone`, `geolocation`, and possible `social-profile` handles
- **Empty/negative result looks like:** no ads means the subject doesn't post here (or used a different name) — try other UK classifieds (Gumtree, Facebook Marketplace).

## Gotchas & OpSec
- Ad content is self-reported and can be stale or fake — corroborate contact details.
- Reading is passive; contacting a seller is active — do not engage the subject.
- Human-in-the-loop: none for browsing.

## Overlaps ("do both")
- Do both with Gumtree/Facebook Marketplace and phone-OSINT — classifieds leak phones/handles; those enrich them and widen coverage.

## Trust & verifiability
`trust: community` — user-generated ads; treat every detail as a lead to verify against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ad-mart-classified-ads-united-kingdom |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username → phone, geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
