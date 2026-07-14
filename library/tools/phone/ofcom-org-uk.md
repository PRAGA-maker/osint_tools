---
id: ofcom-org-uk
name: ofcom.org.uk
description: Use when you have a UK `address`/postcode (or a `geolocation`) and want to know which mobile networks cover it — returns per-operator signal/coverage for that location.
url: https://checker.ofcom.org.uk/mobile-coverage
category: phone
path:
- phone
bestFor: Checking which UK mobile networks (and broadband) serve a specific address/postcode.
selectorsIn:
- address
- geolocation
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free official UK regulator tool; no account.
opsec: passive
opsecNote: You query a government regulator's coverage database by location, not by person — no target is contacted or notified. Ofcom logs the query; use a sock-puppet browser if you want to avoid attribution. This checks infrastructure coverage, not any individual's phone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Ofcom, the UK communications regulator — authoritative first-party coverage data supplied by the networks.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- cellular-towers-map-canada
aliases:
- Ofcom coverage checker
- ofcom mobile coverage
tags:
- mobilephone
- Mobile & Phone Related
- coverage
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# ofcom.org.uk

> Ofcom's official UK mobile (and broadband) coverage checker: enter an address/postcode, see which networks have signal there.

## When to use
You have a UK `address` or `geolocation` and need supporting context about mobile connectivity there — for example to corroborate or challenge a claim ("no signal at that location"), to understand which operators a device could plausibly have used at a place, or to assess coverage near a last-known location. This is infrastructure/coverage intelligence, not a people or phone-number lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://checker.ofcom.org.uk/mobile-coverage (redirects to the current Ofcom coverage-checker page).
2. Enter the UK postcode or address (or pin the location on the map).
3. Read the per-operator results: indoor/outdoor voice and data coverage for each major UK network.
4. Pivot: use the coverage picture alongside a number's network (from a UK number-allocation check) to reason about plausibility; for tower-site context in other countries see analogous tools like `[[cellular-towers-map-canada]]`.

## Inputs → Outputs
- **In:** `address`/postcode or `geolocation` (UK)
- **Out:** `geolocation`-scoped coverage — which networks serve that spot and at what strength
- **Empty/negative result looks like:** an invalid/none-UK postcode returns no data; a valid rural spot may show weak/no coverage for some networks (a genuine finding, not an error).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — a location query against a regulator database; no subject involvement.
- Scope: **UK-only**, and it answers "does signal exist here", not "where is this person/number" — don't over-read it as tracking.

## Overlaps ("do both")
- Conceptually pairs with tower/coverage maps like `[[cellular-towers-map-canada]]` for other regions — same infrastructure-context role, different country.

## Trust & verifiability
`trust: trusted` — first-party Ofcom data reported by the networks. Coverage is modelled/predicted, so treat edge-of-signal areas as approximate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ofcom-org-uk |
| category | phone |
| selectorsIn → selectorsOut | address, geolocation → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
