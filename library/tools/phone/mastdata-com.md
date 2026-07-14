---
id: mastdata-com
name: Mastdata
description: Use when you have a `geolocation` or `address` and want to know which UK mobile operators/masts serve it and where coverage gaps are — returns cell-mast `geolocation` and coverage `metadata`, not personal data.
url: https://www.mastdata.com/
category: phone
path:
- phone
bestFor: Understanding UK mobile coverage and cell-mast infrastructure around a location — which operators reach an area and where the not-spots are.
selectorsIn:
- geolocation
- address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free coverage maps and reference material; detailed analysis tools, line-of-sight modelling and corporate features sit behind paid subscriptions / user accounts.
opsec: passive
opsecNote: You query infrastructure data, not a person — nothing touches or notifies any subject. Creating an account ties usage to that login; browse the free maps anonymously where possible.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Industry/crowdsourced UK telecoms resource (coverage partly from a crowdsourced Android app plus infrastructure records); good for planning-grade coverage insight, not a precise real-time source.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- mastdata.com
- UK mobile base station resource
tags:
- mobilephone
- Mobile & Phone Related
- cell-tower
- coverage
- uk
- infrastructure
source: uk-osint
lastVerified: '2026-07-13'
enrichment: full
---

# Mastdata

> A UK mobile base-station and coverage resource — a map of which operators and masts serve a location, and where the not-spots are. Infrastructure intelligence, not a phone-number lookup.

## When to use
You have a `geolocation` or `address` and a signal/coverage question: which UK operators (EE, O2, Three, Vodafone, BT, CTIL) reach a rural spot, where the coverage gaps are, or line-of-sight between masts. In a missing-person context this is niche and indirect — e.g. sanity-checking whether a "no signal" account is plausible in an area, or which network a location would use — not a way to find a person from a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.mastdata.com/.
2. Use the coverage maps for the area of interest, selecting operator(s).
3. For not-spot analysis or line-of-sight/mast detail, create a user account and/or use the paid analysis tools.
4. Pivot: a coverage/not-spot finding contextualises phone-activity or last-contact assumptions; it does not itself yield identity.

## Inputs → Outputs
- **In:** `geolocation` / `address` (an area of interest)
- **Out:** cell-mast `geolocation` and coverage `metadata` (operators serving the area, gaps, planning/operator contacts)
- **Empty/negative result looks like:** an area with no plotted data, or free-tier limits blocking detailed layers — infrastructure gaps in the dataset, not evidence about any individual.

## Gotchas & OpSec
- This is NOT a phone-number or personal-location tool — despite sitting in the phone category, it returns infrastructure data only. Do not expect `name`/`address` for a number.
- Coverage is partly crowdsourced and approximate; treat as planning-grade, not authoritative real-time.
- OpSec: fully passive; no subject contact.

## Overlaps ("do both")
- Pairs with true phone-number lookups and carrier-metadata tools — those resolve a number to carrier/line-type, while Mastdata only explains coverage geography.

## Trust & verifiability
`trust: community` — a sector resource with crowdsourced inputs; useful for coverage context but verify anything critical against operator data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mastdata-com |
