---
id: ukclassifieds
name: UKClassifieds
description: Use when you have a `name`, `phone`, or `username` and want UK classified ads a subject posted — returns phone, address-area, and associate leads.
url: http://ukclassifieds.co.uk
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding free UK classified ads (for-sale, vehicles, property, services, community, pets) a subject placed and the contact details attached.
selectorsIn:
- name
- phone
- username
selectorsOut:
- phone
- address
- associate
status: live
pricing: free
costNote: Free to browse and search; posting and messaging sellers require a free account, but reading listings does not. Premium listing upgrades exist for advertisers only.
opsec: passive
opsecNote: Browsing and searching listings is passive — you only read public ads. Do NOT message a seller from your own identity; that is active and alerts them. Register a sock-puppet account/IP if you must log in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running commercial UK classifieds marketplace (self-described 18+ years); listings are user-submitted and unvetted, so treat details as leads to corroborate.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- ukclassifieds.co.uk
tags:
- toddington
- specialty-search
- classifieds
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# UKClassifieds

> A long-running free UK classifieds marketplace, usable as an OSINT source for ads a subject placed and the seller details, location, and photos on them.

## When to use
You have a UK-linked subject and a `name`, `phone`, or reused `username`/seller handle, and you want classified ads they posted — a car for sale, a room to let, a service offered, a pet rehomed. Ads commonly carry a phone number, a first name/handle, a postcode or distance-filtered location, and photos, corroborating that a person is active and in a given area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://ukclassifieds.co.uk.
2. Use keyword search plus category and location/distance (0–200 km radius) filters to focus on the subject's suspected area.
3. Search the subject's `name`, a `phone` number, or a reused seller `username`; also try distinctive items they might sell.
4. Read each ad for the poster username, location/postcode, price/"check with seller", timestamp, and any images (run a metadata/EXIF check on photos).
5. Pivot: a phone number feeds phone-OSINT/reverse-lookup; a reused handle feeds username search; a postcode/area narrows an `address`.

## Inputs → Outputs
- **In:** `name`, `phone`, or `username`
- **Out:** `phone`, `address` (area/postcode), `associate` (co-posters, linked business)
- **Empty/negative result looks like:** no matches, or only stale/old listings — treat absence as weak evidence and cross-check other classifieds and marketplaces.

## Gotchas & OpSec
- User-submitted and unverified — a name/number on an ad may be a business, reseller, or spoofed; corroborate before trusting.
- Check timestamps; older ads may not reflect a current location.
- Reading is passive; messaging a seller is active and notifies them. Stay read-only.

## Overlaps ("do both")
- Pairs with `[[hallo-london-free-classified-ads]]` and other regional classifieds — cross-run the same `phone`/handle so one site's coverage gap is filled by another.

## Trust & verifiability
`trust: unverified` — a commercial classifieds host with no identity vetting; value is as a lead source (a real phone/photo/area to verify elsewhere), not an authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukclassifieds |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, phone, username → phone, address, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
