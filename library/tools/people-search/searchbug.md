---
id: searchbug
name: SearchBug
description: Use when you have a US `name`, `phone`, `email` or `address` and want cross-linked contact and background data — returns addresses, phones, emails and associates.
url: https://www.searchbug.com/
category: people-search
path:
- people-search
bestFor: US contact-data lookups (people, reverse phone, reverse email, reverse address) with batch/API options for higher-volume work.
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- email
- associate
status: live
pricing: freemium
costNote: Some basic lookups return limited free info (e.g. line type / carrier on a phone); detailed people reports, reverse email/address and bulk/API access are paid.
opsec: passive
opsecNote: Queries hit SearchBug's aggregated data sources, not the subject, so no alert is sent. Paid reports and API calls tie to your account; use an appropriately attributed account and handle results lawfully (some data is FCRA-restricted for permissible-purpose use only).
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing US data broker offering consumer lookups and business/API data services; reliable for leads, but like all aggregators it carries stale records and same-name collisions.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- 411-us
- reverse-phone-lookup-2
aliases:
- searchbug.com
tags:
- people-investigations
- reverse-phone
- data-broker
- us
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# SearchBug

> A US data-broker toolkit — people search plus reverse phone/email/address lookups, with batch and API options for scaling — turning any one contact selector into the rest.

## When to use
You have a US `name`, `phone`, `email`, or `address` and want to pivot to the other contact details plus relatives/associates. It's strong when you already hold one solid selector and need to expand: reverse a phone to a name+address, reverse an email to a person, or enrich a name into contact history. The API/batch features make it useful when you have many identifiers to process, not just one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.searchbug.com/ and pick the matching tool (People Search, Reverse Phone, Reverse Email, Reverse Address).
2. Enter your known selector; review the free/preview result (e.g. phone line-type and carrier often show free).
3. Purchase the detailed report for full contact/associate data, or use the API/batch service for volume.
4. Disambiguate with age/location before paying, to avoid same-name reports.
5. Pivot: new `phone`/`email`/`associate` values feed `[[411-us]]`, `[[reverse-phone-lookup-2]]`, and messaging/social checks.

## Inputs → Outputs
- **In:** `name`, `phone`, `email`, or `address` (US)
- **Out:** `address`, `phone`, `email`, and `associate`/relative links
- **Empty/negative result looks like:** "no records" or thin data — the selector may be new, non-US, or unlisted; absence isn't conclusive.

## Gotchas & OpSec
- US-focused aggregator; weak outside the US and subject to stale records/collisions.
- Some data is FCRA-regulated — only use for permissible purposes; don't rely on it for eligibility decisions.
- Human-in-the-loop: detailed data is behind a **paywall**; free previews confirm a match and often the phone line-type.

## Overlaps ("do both")
- Pairs with `[[411-us]]` and `[[reverse-phone-lookup-2]]` — different brokers hold different records; run several and reconcile. SearchBug's API is the one to reach for on bulk lists.

## Trust & verifiability
`trust: community` — an established US broker, reliable for leads but not authoritative; corroborate any contact/relationship against a second aggregator or primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchbug |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, email, address → address, phone, email, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
</content>
