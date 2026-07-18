---
id: gumtree-classified-ads-united-kingdom
name: Gumtree Classified Ads (United Kingdom)
description: Use when you have a `name`, `username` or `phone` and want a subject's UK classified listings — returns their ads, rough `geolocation`, contact `phone` and `social-profile` seller pages.
url: https://www.gumtree.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Finding a UK subject's for-sale/rental/service listings and the location and contact details they attach to them.
selectorsIn:
- name
- username
- phone
selectorsOut:
- geolocation
- phone
- social-profile
status: live
pricing: free
costNote: Free to browse and search all listings; a Gumtree account (free) is only needed to message sellers or post.
opsec: passive
opsecNote: Browsing and searching listings is passive and does not notify the seller. Contacting a seller, replying to an ad, or viewing a phone number behind a "reveal" button crosses into active engagement and may alert them — stop at reading public listing content unless engagement is authorised.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Gumtree is an established, legitimate UK marketplace, but listings are user-generated — seller-supplied names, locations and prices are unverified and can be deliberately vague or false.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Gumtree UK
- Gumtree classifieds
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Gumtree Classified Ads (United Kingdom)

> The UK's big general classifieds site — search it to surface a subject's for-sale, rental, job or services ads and the location and contact details they publish alongside them.

## When to use
You have a subject linked to the UK and a `name`, `username`/seller handle, or a `phone` number, and you want to find what they've advertised. Classified ads are a rich, often-overlooked footprint: a seller reveals a town/postcode district, an item photographed at their home, a contact number, and sometimes a linked profile. Useful for placing someone geographically, spotting recent activity (ad post dates), or matching a phone/handle across sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.gumtree.com.
2. Search by keyword — the subject's `name`, seller `username`, a distinctive item, or a `phone` number — and set the location filter to their suspected area.
3. Open matching ads and read: the listed location (town / postcode district), the description, photos (check backgrounds and reflections for location clues), the post date, and the seller's public profile (their other live ads).
4. To pivot on a phone number: paste it into the search box; the same number often recurs across a seller's ads and other classifieds.
5. Pivot: feed the seller handle into username tools, the location into mapping, and the phone into phone OSINT — do **not** message the seller unless engagement is sanctioned.

## Inputs → Outputs
- **In:** `name`, `username`/seller handle, or `phone`
- **Out:** listing content, approximate `geolocation` (town/postcode area), contact `phone`, seller `social-profile` (their ad history)
- **Empty/negative result looks like:** no listings for the term, or only unrelated generic ads — the subject may not sell on Gumtree, may use a different handle, or the ad has expired (listings drop off after a period).

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; only messaging/posting needs a (sock-puppet) account.
- OpSec: **passive** while reading — but replying to an ad or revealing a hidden phone number can notify the seller. Keep to public content.
- Listings are unverified user content: the stated location can be a nearby town rather than home, and names/handles may be pseudonymous. Corroborate before treating any field as fact.
- Ads expire and are removed, so absence today isn't proof the subject never listed — check cache/archive tools for old ads.

## Overlaps ("do both")
- Run the same handle through `[[whatsmyname]]`/`[[sherlock]]` to check the seller username across other platforms, and the phone through dedicated phone OSINT — Gumtree gives the lead, those confirm the identity.

## Trust & verifiability
`trust: community` — a genuine, well-known marketplace, but every field is seller-supplied and unverified; use listings as leads, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gumtree-classified-ads-united-kingdom |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, username, phone → geolocation, phone, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
