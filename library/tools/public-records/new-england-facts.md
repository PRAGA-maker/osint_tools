---
id: new-england-facts
name: New England Facts
description: Use when you have a `name` in the US Northeast and want an address, phone, relatives and property links — returns an aggregated people/property profile for the six New England states.
url: https://newenglandfacts.com/
category: public-records
path:
- public-records
bestFor: Regional people- and property-search across CT, MA, RI, ME, NH and VT.
selectorsIn:
- name
- address
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Basic profile snippets (name, approximate location, relatives) are viewable free; full contact details and property/report data are gated behind a paid lookup like most data-broker people-search sites.
opsec: passive
opsecNote: Searching is passive and not shown to the subject, but you are querying a commercial data broker that logs lookups. Use a sock-puppet. Note this is also a site people opt out of — a missing/sparse result may mean suppression, not absence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A regional data-broker/people-search aggregator; data is compiled from public records and third-party brokers, so it can be stale, mismatched or merged across same-name individuals. Corroborate before relying on it.
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
aliases:
- NewEnglandFacts
- newenglandfacts.com
tags:
- people-search
- data-broker
- new-england
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# New England Facts

> A regional people- and property-search aggregator for the six New England states — name-to-contact plus real-estate and relatives, compiled from public records and data brokers.

## When to use
You have a `name` (or an `address`) tied to Connecticut, Massachusetts, Rhode Island, Maine, New Hampshire or Vermont and want a fast regional profile: current/past addresses, phone, email, relatives/associates, employment and property ownership. Its regional focus can surface small-town New England records (town-hall property, assessor data) that national people-search engines index thinly. Best as one input among several — treat as leads, not fact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://newenglandfacts.com/ in a sock-puppet browser.
2. Search by `name` (add a New England town/state to disambiguate) or by property `address`.
3. Read the free preview — name, approximate age, town, listed relatives.
4. For full contact details / property reports, the site pushes a paid lookup; decide whether the free preview already gives you enough to pivot elsewhere.
5. Pivot: relatives/associates feed network mapping; a property address feeds assessor/deed records; a phone/email feeds contact-based OSINT.

## Inputs → Outputs
- **In:** `name` (best with a New England locality) or property `address`
- **Out:** `address`, `phone`, `email`, `associate` (relatives), `employer-org`, `social-profile`, property records
- **Empty/negative result looks like:** no profile, or a thin stub with no contact data — which can mean the person isn't in the region's records *or* has opted out of this broker. Don't treat absence as proof.

## Gotchas & OpSec
- Data-broker accuracy caveats apply: stale addresses, merged same-name records, and phantom "relatives." Corroborate every field.
- Regional only — someone who moved out of New England may be missing or frozen at an old record.
- People can opt out, so suppression is common; cross-check a national people-search before concluding.

## Overlaps ("do both")
- Pairs with `[[truepeoplesearch]]` and `[[fastpeoplesearch]]` (free national people-search) and `[[whitepages]]` — run those alongside to catch what a regional broker misses and to sanity-check its addresses/relatives.

## Trust & verifiability
`trust: community` — a commercial regional aggregator, not an authoritative source. Useful for leads and regional property depth, but verify contact and relationship data against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-england-facts |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, phone, email, associate, social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
