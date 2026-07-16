---
id: zillow
name: Zillow
description: Use when you have a US `address` and want property details, sale/price history and interior photos — returns geolocation, physical-description of the property and prior-owner leads.
url: https://www.zillow.com/
category: public-records
path:
- public-records
bestFor: Pulling a US property's sale history, tax/assessment data, and listing photos from an address.
selectorsIn:
- address
selectorsOut:
- geolocation
- physical-description
- name
status: live
pricing: freemium
costNote: Free to browse property pages, sale history, and photos; no account needed. Some features (saved searches, contacting agents) require a free login.
opsec: passive
opsecNote: Browsing a public listing does not alert the property owner. Avoid clicking "contact agent"/"request a tour" or saving the home to a real account — those actions generate outreach and tie the search to you. Use a clean browser session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Major US real-estate platform; listing, sale-price, and tax data are sourced from MLS feeds and county records, so they are reliable though occasionally lagging.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- zillow.com
tags:
- real-estate
- property
- address
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- zillow-canada
- zillow-united-states
---

# Zillow

> The largest US real-estate portal, usable as a property-intel source: an address gives you sale history, tax/assessment data, and often interior and exterior photos of the home.

## When to use
You have a US `address` for a subject and want to understand the property: when it last sold and for how much (which can name a buyer/seller), its size and layout, and — via old listing photos — what the interior and exterior look like. Interior shots can leak vehicles, documents, or belongings; the sale/`price` timeline can corroborate when someone moved in or out.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.zillow.com/ and search the exact `address`.
2. Open the property page. Note: current status (for-sale/off-market), Zestimate, and the "Price history" and "Public tax history" sections.
3. Scroll to photos — listing galleries (current or archived) often show the home's interior and street view.
4. Cross-reference the "Price history" dates with when your subject was known to live there.
5. Pivot: sale records may name parties → `name`; geocoordinates and lot view → `geolocation`; photos → `physical-description` of the property and any visible clues; then confirm ownership via a county assessor / public-records tool.

## Inputs → Outputs
- **In:** US `address`
- **Out:** `geolocation` (map/parcel), `physical-description` of the property (beds/baths/sqft + photos), sale/tax history and occasionally a party `name`.
- **Empty/negative result looks like:** "This home isn't currently for sale and we don't have full details" / no page — the address is off-market with sparse public data, or the address string didn't match; try county records instead.

## Gotchas & OpSec
- Zestimate is an algorithmic estimate, not an appraisal — don't treat it as fact.
- Photos are usually from the last listing and may be years old or show a prior owner's furnishings.
- Zillow does not name current owners; use it for property facts and pair with an assessor/deed search for ownership.
- Do not trigger agent contact or tour requests — that sends real outreach and exposes your interest.

## Overlaps ("do both")
- Pairs with a county assessor / deed-record lookup (owner name) and with a reverse-address people-search — Zillow supplies the property picture, those supply the person behind it.

## Trust & verifiability
`trust: trusted` — a major platform pulling from MLS and county records; core facts (sale prices, tax history, dimensions) are reliable, though listings can lag reality and the Zestimate is only an estimate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zillow |
| category | public-records |
| selectorsIn → selectorsOut | address → geolocation, physical-description, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
