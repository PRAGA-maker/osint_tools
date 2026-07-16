---
id: usphonebook
name: USPhoneBook
description: Use when you have a US `phone` number (or a `name`) and want to identify the owner — returns the name, address, relatives/associates and phone type behind the number.
url: https://www.usphonebook.com/
category: phone
path:
- phone
bestFor: Free reverse-phone lookup that resolves a US number to a name, current/past addresses and named relatives.
selectorsIn:
- phone
- name
selectorsOut:
- name
- address
- associate
- phone
status: live
pricing: freemium
costNote: Basic reverse-phone and name lookups return a name/location for free; fuller reports (complete address history, all relatives, background details) push you toward paid data-broker tiers.
opsec: passive
opsecNote: Querying is passive — the subject is not notified. The site logs searcher IP/queries and runs ad retargeting; use a clean browser/VPN and never enter your own details into an "unlock report" upsell.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A US data-broker aggregator; results are compiled from public records and third-party data of variable freshness and can conflate same-name people — corroborate before relying on any field.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USPhoneBook.com
- US Phone Book
tags:
- phone-number-research
- reverse-phone
- data-broker
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- us-phonebook
---

# USPhoneBook

> A free US reverse-phone directory — turn a 10-digit number into a name, address and relatives, or run it forward from a name.

## When to use
You have a US `phone` number and need to know who it belongs to (reverse lookup), or you have a `name` and want a listed address and associated numbers (forward lookup). USPhoneBook aggregates billions of public records and returns the owner name, current/past addresses, phone type (landline/mobile/VoIP) and named relatives — a fast early step to attach an identity to a loose number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.usphonebook.com/ in a clean/VPN'd browser.
2. For a reverse lookup, enter the 10-digit `phone`; for a forward lookup, enter the `name` (+ state/city to narrow).
3. Read the result card: owner `name`, `address` history, phone type, and `associate` (relatives/associates).
4. Treat the free fields as leads; do not pay or enter your own PII to "unlock" a fuller broker report.
5. Pivot: relatives feed family-network mapping; an address feeds property/voter records; the phone type tells you whether to pursue carrier vs. VoIP angles.

## Inputs → Outputs
- **In:** `phone` (US, 10-digit) or `name` (+ location)
- **Out:** owner `name`, `address` history, `associate` (relatives), `phone` type/other numbers
- **Empty/negative result looks like:** "no results" or a name-only stub with no address — common for mobile-only, VoIP, ported, or privacy-suppressed numbers; absence does not prove the number is unassigned.

## Gotchas & OpSec
- Accuracy varies: aggregator data is often stale and can attach the wrong same-name person — verify every field against a primary source.
- Upsell traps: "full report" flows may charge or harvest your details; never enter the investigator's real PII.
- Coverage: US only, and weaker on mobile/VoIP than on landlines.
- OpSec: passive to the subject, but the site logs your queries — use a clean session/VPN.

## Overlaps ("do both")
- Pairs with `[[ufind-name]]` and other US aggregators — each indexes different records, so run several and reconcile.
- Pairs with carrier/Truecaller-style checks to cross-confirm the name attached to a number.

## Trust & verifiability
`trust: community` — a commercial data-broker aggregator, not an authoritative source; use its output as lead generation that must be corroborated against primary public records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usphonebook |
