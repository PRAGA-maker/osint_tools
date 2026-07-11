---
id: public-info-directory-us
name: Public Records Directory (US)
description: Use when you have a US `name` and want a free aggregated people/public-records profile — returns addresses, phones, relatives, and record pointers (ad-heavy, verify).
url: https://publicrecords.directory
category: people-search
path:
- people-search
bestFor: A free US people-search aggregator for a quick address/phone/relatives sketch to corroborate elsewhere.
selectorsIn:
- name
- phone
- address
selectorsOut:
- address
- phone
- associate
- dob
status: degraded
pricing: freemium
costNote: Free to search with a viewable teaser, but the site is heavily monetized — it surfaces some data free and pushes upgrades/redirects to paid partner brokers for the rest. Not a Consumer Reporting Agency (not FCRA-usable).
opsec: passive
opsecNote: A broker-style aggregator of public records; searching does not notify the subject. It is ad- and redirect-heavy, so use a sock-puppet browser and be wary of partner links that hand you off to paid brokers or dubious sites.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A widely-listed but SEO/ad-driven free people-search; data provenance is opaque and quality uneven, so treat everything as an unconfirmed lead.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Public Info Directory
- publicrecords.directory
tags:
- people-search
- data-broker
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Public Records Directory (US)

> A free, ad-heavy US people-search aggregator — useful as one more free net to cast, but treat everything it returns as unconfirmed.

## When to use
You have a US `name` (or a `phone`/`address` to reverse) and want a quick, free sketch — address history, phones, approximate age, and likely relatives — to corroborate against better sources. It's recommended across several OSINT lists as a free option, but it's a monetized aggregator, so its value is as a cross-check, not a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://publicrecords.directory` and search the `name` (add city/state to disambiguate).
2. Open a matching result and read the free teaser: addresses, phones, age, relatives.
3. Ignore upsell/partner redirects; take only the freely-shown data.
4. **Cross-check every field** against a stronger source before using it.
5. Pivot: relatives → associate mapping; addresses → property/records; confirm on `[[searchpeoplefree]]` / `[[beenverified]]`.

## Inputs → Outputs
- **In:** `name`, `phone`, `address`
- **Out:** `address`, `phone`, `associate` (relatives), `dob`/age, record pointers
- **Empty/negative result looks like:** no match, a thin listing, or an endless redirect to a paid partner — treat as no usable free data, not as evidence about the person.

## Gotchas & OpSec
- Heavily monetized and SEO-driven; provenance is opaque and some links lead to low-quality partner sites — click carefully.
- Data is aggregated and can be very stale; never rely on it alone.
- OpSec: **passive** and anonymous; sock-puppet browsing recommended given the ad/redirect ecosystem.

## Overlaps ("do both")
- Pairs with `[[searchpeoplefree]]` and `[[beenverified]]` — use it only to corroborate what those return; different aggregators surface different records, so agreement across two is the useful signal.

## Trust & verifiability
`trust: unverified` — an opaque, ad-driven aggregator; treat every field as an unconfirmed lead that must be verified on a primary or higher-quality source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | public-info-directory-us |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → address, phone, associate, dob |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
