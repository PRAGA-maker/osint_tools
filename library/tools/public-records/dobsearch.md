---
id: dobsearch
name: DOBSearch
description: Use when you have a `name` and want date of birth, addresses, phone and relatives — returns an aggregated US people-search profile including age/DOB signals.
url: https://www.dobsearch.com
category: public-records
path:
- public-records
bestFor: US name-to-DOB/age plus address, phone and relative links.
selectorsIn:
- name
- phone
- address
- email
selectorsOut:
- dob
- address
- phone
- associate
- name
status: live
pricing: freemium
costNote: Search and previews are free; full reports (complete DOB, background, contact details) are gated behind a paid lookup, like most people-search aggregators.
opsec: passive
opsecNote: Passive — searching isn't shown to the subject, but you query a commercial data broker that logs lookups. Use a sock-puppet. The site itself states it is not an FCRA consumer-reporting agency; don't use it for employment/tenant/credit decisions.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial US public-records aggregator (originally date-of-birth focused). Data is compiled from many sources and can be stale or merged across same-name people; corroborate before relying on it.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truepeoplesearch
- fastpeoplesearch
- whitepages
- dob-search-death-records
aliases:
- DOBSearch
- dobsearch.com
tags:
- genealogy
- family
- people-search
- date-of-birth
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# DOBSearch

> A US people-search aggregator with a date-of-birth heritage — good for pinning an age/DOB to a name alongside the usual address/phone/relatives.

## When to use
You have a `name` (or a `phone`/`address`/`email`) for a US subject and want an approximate or exact date of birth to disambiguate common names, plus the standard people-search payload: current/past addresses, phone numbers, and relatives/associates. DOB is the key disambiguator when several people share a name, so this is worth a pass early in identity resolution. Treat outputs as leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dobsearch.com in a sock-puppet browser.
2. Search by `name` (add a state/city to narrow), or use reverse phone/address/email search.
3. Read the free preview — matched name, approximate age/DOB, location, listed relatives.
4. Full details (exact DOB, complete background/contact) push to a paid report; decide whether the free signal already disambiguates your subject.
5. Pivot: a DOB narrows every downstream search; relatives feed network mapping; addresses feed property/neighbour checks.

## Inputs → Outputs
- **In:** `name` (best with location), or `phone`/`address`/`email`
- **Out:** `dob`/age, `address`, `phone`, `associate` (relatives), `name`
- **Empty/negative result looks like:** no profile, or a thin stub with age withheld behind the paywall — which can mean no record, an opt-out, or that the free tier simply doesn't show the DOB. Corroborate before concluding.

## Gotchas & OpSec
- Data-broker caveats: stale addresses, merged same-name records, and speculative "relatives." Verify every field.
- The exact DOB is usually paywalled; the free tier often gives only an age range.
- Not an FCRA consumer report — legally prohibited for employment/credit/tenant screening.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]` and `[[fastpeoplesearch]]` (free national people-search) and `[[whitepages]]` — cross-run to confirm the DOB/age and catch addresses this one misses.

## Trust & verifiability
`trust: community` — a commercial aggregator, not authoritative. Useful for a fast DOB/age signal, but verify the date and relationships against primary records or a second aggregator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dobsearch |
| category | public-records |
| selectorsIn → selectorsOut | name, phone, address, email → dob, address, phone, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
