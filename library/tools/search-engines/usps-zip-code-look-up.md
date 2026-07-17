---
id: usps-zip-code-look-up
name: USPS ZIP Code Lookup
description: Use when you have a partial or claimed US `address` and want to verify/standardize it — returns the correct ZIP+4, standardized `address`, city/state, and whether the address is deliverable.
url: https://tools.usps.com/go/ZipLookupAction!input.action
category: search-engines
path:
- search-engines
bestFor: Verifying and standardizing a US address, or finding the ZIP for an address/city.
selectorsIn:
- address
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free official USPS tool; no account.
opsec: passive
opsecNote: A ZIP/address lookup queries USPS's public tool and discloses nothing to any subject. Passive. It validates address format only — it does not confirm who lives there.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US Postal Service address-matching system — authoritative for whether a US address is valid, deliverable, and correctly formatted.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- USPS Zip Code Lookup
- tools.usps.com zip lookup
tags:
- address-verification
- usps
- geolocation
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# USPS ZIP Code Lookup

> The US Postal Service's official address checker: turn a rough or claimed address into a standardized, deliverable one — or find the correct ZIP+4 for an address or city.

## When to use
You have a US `address` that is partial, misspelled, or unverified (from a form, a lead, a record) and need to confirm it is a real, deliverable address and standardize it. USPS's matcher corrects the format, appends ZIP+4, and tells you if the address exists in the postal system — a quick reality check on an address before you build on it, and a way to resolve a city/state to ZIP or vice versa.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tools.usps.com/zip-code-lookup.htm and choose "Find by Address" (or "Cities by ZIP", "ZIP by City").
2. Enter the street `address`, city, and state (a CAPTCHA may appear).
3. Read the result: the standardized address with ZIP+4, or "address not found" if USPS can't match it. Some matches note carrier route/delivery details.
4. Pivot: a validated, standardized address feeds people-search and property-record tools cleanly (many databases key on the USPS-standard form); the ZIP narrows `geolocation`.

## Inputs → Outputs
- **In:** a US `address` (or a city/ZIP to convert).
- **Out:** standardized `address` + ZIP+4, deliverability, city/state, approximate `geolocation` (ZIP area).
- **Empty/negative result looks like:** "we could not find a match" — the address as entered isn't in the USPS database (typo, non-existent, or non-standard). Try variants before concluding it's fake.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA can appear; solve it manually.
- It validates *deliverability/format*, not *occupancy* — a valid address says nothing about who lives there.
- US only; PO boxes and some new/rural addresses may match imperfectly.

## Overlaps ("do both")
- Standardize an address here before feeding it to property-records, voter, and people-search tools — they match better on the USPS-canonical form.

## Trust & verifiability
`trust: trusted` — the authoritative US postal address database. A "valid" result reliably means the address is deliverable; it does not verify any person's connection to it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usps-zip-code-look-up |
| category | search-engines |
| selectorsIn → selectorsOut | address → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
