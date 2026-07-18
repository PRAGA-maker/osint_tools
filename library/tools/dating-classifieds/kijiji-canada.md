---
id: kijiji-canada
name: Kijiji (Canada)
description: Use when you have a `name`, handle, or location and want a subject's classified ads — returns listings with seller display name, photos, area, and sometimes a phone.
url: https://www.kijiji.ca
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a person's for-sale / rental / services classified ads across Canada to surface photos, location, and contact leads.
selectorsIn:
- name
- geolocation
selectorsOut:
- social-profile
- image
- phone
status: live
pricing: free
costNote: Free to browse and search listings; posting or messaging a seller needs a free account.
opsec: passive
opsecNote: Passive while browsing/searching public ads — the seller is not notified. Messaging or replying to a seller is active and reveals your account; use a sock-puppet profile if you must make contact, and never post from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Canada's dominant classifieds marketplace (eBay-lineage, now Adevinta); listings are user-generated and unverified, so seller-provided details are leads rather than confirmed facts.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- kijiji-canada-classifieds
- kijiji-classified-ads-canada
aliases:
- kijiji.ca
- Kijiji Canada
tags:
- classifieds
- marketplace
- canada
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Kijiji (Canada)

> Canada's largest classifieds marketplace — a rich source of a subject's for-sale, rental, jobs, and services ads, each carrying photos, an area, and often a contact.

## When to use
You are locating or profiling someone in Canada and want to find their classified ads. People sell furniture, cars, and services under a display name and city, frequently attaching photos (of the item, sometimes revealing a home interior, plate, or address) and occasionally a phone number. Search by a known display name/handle, or browse a category within a suspected city to spot a subject's listings. Strong for building a current-location and lifestyle picture, and for image/phone pivots.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.kijiji.ca and set the location (city/region) if you have one.
2. Search a name, seller handle, business name, or a distinctive item; or browse the relevant category (cars, real estate, services, etc.).
3. Open a listing: note the **seller display name**, the **area** shown, **photos**, listing text, and any phone/contact in the body.
4. Reverse-search the listing photos and any phone number; check the item's background details for location clues (street signs, room interiors, plates).
5. Pivot: photos → reverse image search; a phone → reverse-phone lookup; a distinctive display name → username enumeration; the area → narrows geolocation.

## Inputs → Outputs
- **In:** a subject `name`/handle, or a `geolocation` (city/region) to browse
- **Out:** classified listings with seller display name (`social-profile`), `image`(s), area, and sometimes a `phone`
- **Empty/negative result looks like:** no listings for a name/area just means nothing is currently posted (ads expire) — it is not evidence the person is absent; try alternate spellings, nearby cities, and cached/archived copies.

## Gotchas & OpSec
- **Browsing is passive; contacting is not.** Messaging or replying to a seller exposes your account and alerts them — only do so from a sock puppet, if at all.
- Listings expire and are deleted, so a known ad may vanish; capture screenshots and check web archives promptly.
- User-generated and unverified: a display name or area can be fake — treat everything as a lead to corroborate.

## Overlaps ("do both")
- Pairs with `[[kijiji-canada-classifieds]]` and `[[kijiji-classified-ads-canada]]` (alternate search fronts for the same marketplace) and with reverse-image / reverse-phone tools that turn a listing's photo or number into an identity.

## Trust & verifiability
`trust: community` — a mainstream, real marketplace, but every listing is user-generated and unverified; the platform is legitimate while the individual data within it must be independently confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kijiji-canada |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, geolocation → social-profile, image, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
