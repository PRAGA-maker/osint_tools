---
id: serviceobjects-reverse-number-lookup
name: ServiceObjects Reverse Number Lookup
description: Use when you have a `phone` number and want carrier, line type, geographic location, and (where available) the associated name — returns name, geolocation, and phone metadata via API.
url: http://www.serviceobjects.com/developers/lookups/geophone-plus
category: phone
path:
- phone
bestFor: Programmatic reverse-phone intelligence — validating a number and returning carrier, line type, region, and contact name.
selectorsIn:
- phone
selectorsOut:
- name
- geolocation
- phone
status: live
pricing: freemium
costNote: Commercial data API (DOTS GeoPhone Plus). A free trial key and a "Quick Lookups" demo (a record or two) exist, but production/volume use requires a paid API key.
opsec: passive
opsecNote: Server-side data lookup — the subject is not contacted or notified. Queries run through ServiceObjects with your API key, which ties usage to your account; use appropriate hygiene if attribution matters.
humanInLoop: true
humanInLoopReason:
- api-key
- payment-wall-partial
bestInteractionPattern: api
trust: community
trustNote: Established commercial data-validation vendor; results are compiled/licensed data, generally reliable for carrier/line-type/geo but name coverage is partial (best for US landlines).
missingPersonsRelevance: high
coverage:
- us
- global
auth: api-key
api: true
localInstall: false
registration: true
relatedTools:
- twilio-lookup
- numverify
aliases:
- DOTS GeoPhone Plus
- ServiceObjects GeoPhone
tags:
- toddington
- curated-directory
- telephone-numbers
- reverse-phone
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# ServiceObjects Reverse Number Lookup

> A commercial reverse-phone intelligence API (DOTS GeoPhone Plus): validate a number and return carrier, line type, geographic region, and — where data exists — the contact name.

## When to use
You have a `phone` number and want structured intelligence about it: is it valid and active, is it mobile or landline or VoIP, which carrier and which geographic region, and — mainly for US landlines — the associated name/address. It's an API-first tool, so it suits enrichment at scale or a quick demo lookup, rather than an interactive web search.

## How to use it (`bestInteractionPattern`: api)
1. For a one-off, use the "Quick Lookups" web demo on ServiceObjects' site (limited to a record or two).
2. For real use, register for a free trial API key, then a paid key for volume.
3. Call the GeoPhone Plus endpoint with the `phone` number (E.164 format).
4. Parse the response: validity, line type (landline/mobile/VoIP), carrier/SMS provider, latitude/longitude/region, and contact name where available.
5. Pivot: line type tells you whether the number is portable (mobile) and thus weakly geo-tied; a returned name feeds people-search; carrier feeds lawful-process planning.

## Inputs → Outputs
- **In:** `phone` (E.164)
- **Out:** `name` (where available, best for US landlines), `geolocation` (region/lat-long), `phone` metadata (validity, line type, carrier)
- **Empty/negative result looks like:** valid number but no name (common for mobiles and unlisted lines), or an invalid/disconnected flag — the metadata is still useful even when the name is blank.

## Gotchas & OpSec
- Name/address coverage is strongest for US landlines and thin for mobiles and non-US numbers — expect metadata, not always identity.
- It's an API product: beyond the trial/demo it's paid and needs a key.
- Human-in-the-loop: API-key registration and payment for volume.
- OpSec: passive; the subject is not contacted, but queries are logged to your API account.

## Overlaps ("do both")
- Pairs with [[twilio-lookup]] and [[numverify]] — line-type/carrier data from multiple vendors disagrees at the edges; cross-checking hardens the carrier/portability read, and each has different name coverage.

## Trust & verifiability
`trust: community` — an established commercial data vendor with reliable carrier/line-type/geo output; name results are licensed/compiled data with partial coverage, so treat a returned name as a lead to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | serviceobjects-reverse-number-lookup |
| category | phone |
| selectorsIn → selectorsOut | phone → name, geolocation, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key, payment-wall-partial) |
