---
id: anonymous-ad-preview-tool
name: Google Anonymous Ad Preview Tool
description: Use when you have a `geolocation` and want to see Google search results/ads as they'd appear to someone in that place and device — returns localized SERP context.
url: https://ads.google.com/anon/AdPreview
category: social-networks
path:
- social-networks
bestFor: Viewing Google search results and ads for a specific location/language/device without a Google Ads account.
selectorsIn:
- geolocation
selectorsOut: []
status: live
pricing: free
costNote: Free, no Google Ads account or login needed (the /anon/ endpoint is the accountless version).
opsec: passive
opsecNote: You query Google's ad-preview endpoint, not the target. It does not touch the subject and does not count as a real ad impression/click. Passive; use a clean browser/VPN if you don't want the query tied to your identity, though no account is required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google tool; the returned SERP/ad eligibility reflects Google's own simulation for the chosen location and device.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google Ad Preview and Diagnosis (anonymous)
- accountless ad preview
tags:
- google
- serp
- geolocation
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Google Anonymous Ad Preview Tool

> Google's accountless Ad Preview endpoint — see the search results and ads a user in a chosen city/country and device would get, without warping your own results.

## When to use
You want to check what Google *shows* for a query in a specific `geolocation`, language and device — without your own account history, location or cookies skewing it, and without inflating an advertiser's impressions. In OSINT this is useful to reproduce a subject's likely local search view, to see which businesses/ads dominate a locale, or to confirm that a piece of localized content is actually served where someone claims. It characterises a locale's SERP; it does not identify people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ads.google.com/anon/AdPreview (no login required).
2. Enter your search term, then set the `geolocation` (city/region/country), language and device (desktop/mobile).
3. Run the preview to see the simulated search-results page and eligible ads for that exact context.
4. Read the output: the localized organic + ad results, and which advertisers/businesses appear for that place.
5. Pivot: businesses/domains that surface become leads for domain/company OSINT; compare previews across locations to spot geo-targeted differences.

## Inputs → Outputs
- **In:** a search term + `geolocation` (+ language, device)
- **Out:** the simulated Google SERP and eligible ads for that location/device. No person-level `selectorsOut`.
- **Empty/negative result looks like:** few/no ads and a sparse SERP — the query may have little commercial competition or little localized content for that place; that is itself a signal, not an error.

## Gotchas & OpSec
- OpSec: passive and impression-safe — the preview never counts as a real ad view/click and never touches the subject.
- It simulates a location; it does not prove where *you* are or geolocate anyone. Wrong tool for finding a person.
- Results are a point-in-time simulation and change as auctions/indexes change.

## Overlaps ("do both")
- Complements domain/business OSINT tools — the ad preview surfaces which businesses/domains dominate a locale, which you then run through WHOIS/company lookups for ownership.

## Trust & verifiability
`trust: trusted` — first-party Google endpoint; the SERP/ad simulation is Google's own, though it is a simulation of eligibility, not a guarantee of what any individual saw.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | anonymous-ad-preview-tool |
| category | social-networks |
| selectorsIn → selectorsOut | geolocation → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
