---
id: federal-aviation-administration
name: FAA Aircraft Registry (N-Number Inquiry)
description: Use when you have a US aircraft tail number (N-number) and want its registered owner — returns owner `name`/`address`, aircraft make/model and registration status.
url: https://registry.faa.gov/aircraftinquiry/NNum_inquiry.aspx
category: transportation
path:
- transportation
bestFor: Resolving a US N-number tail marking to the registered owner's name and address, plus aircraft particulars.
selectorsIn:
- vehicle-plate
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official US-government public record; no account needed.
opsec: passive
opsecNote: You query a US-government database, not the owner — the aircraft owner is not notified. Only the FAA sees your lookup. Nothing is disclosed to the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official FAA aircraft registry — the authoritative US registration record. Note that owner data can be an LLC, trust, or dealer rather than the actual operator/pilot.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- aircraft-registry
- faa-registry
- adsb-exchange
aliases:
- FAA N-Number inquiry
- FAA aircraft registry
- registry.faa.gov
tags:
- bellingcat-toolkit
- transport
- aircraft
- vehicle-registration
source: bellingcat-toolkit
lastVerified: '2026-07-29'
enrichment: full
---

# FAA Aircraft Registry (N-Number Inquiry)

> The US government's official aircraft ownership record: enter an N-number tail marking, get the registered owner's name and address.

## When to use
You have a US aircraft's tail number — an "N-number" like `N12345`, visible in a photo, on a hangar, or from a flight-tracking hit — and you need to know who it is registered to. The FAA registry returns the registered owner's name and mailing address, the aircraft's make/model/serial, airworthiness class, and registration status. Treat the tail number as this library's `vehicle-plate` selector for aircraft.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://registry.faa.gov/aircraftinquiry/ and choose **N-Number Inquiry**.
2. Enter the tail number without the leading "N" as prompted (e.g. `12345`) and submit.
3. Read the record: **Registered Owner** name and address, aircraft manufacturer/model/serial, year, engine type, airworthiness, and registration issue/expiry dates.
4. Note the owner *type* — many aircraft are registered to LLCs, trusts (e.g. "… OWNER TRUSTEE"), or dealers that mask the real operator.
5. Pivot: run the owner `name`/`address` through people-search and business-registry tools; if the owner is a trust/LLC, chase the registered agent. Cross-reference live movements with `[[adsb-exchange]]`.

## Inputs → Outputs
- **In:** `vehicle-plate` (US N-number tail marking).
- **Out:** owner `name`, `address`, `employer-org` (if registered to a company/trust), plus aircraft particulars and status.
- **Empty/negative result looks like:** "No records found" — the N-number is unassigned/deregistered, foreign-registered (non-US), or mistyped. Non-US aircraft need that country's registry, not the FAA.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — the owner is never notified; you touch only the FAA.
- Ownership ≠ operator: trust/LLC registrations (very common for privacy) hide the real user; the name shown may be a legal shell. Owner-on-record can also lag a recent sale.
- Addresses are the registration mailing address, which may be an agent or PO box, not a residence.

## Overlaps ("do both")
- Pairs with `[[adsb-exchange]]` — ADS-B trackers tie the same tail number to real-time and historical flight paths, turning "who owns it" into "where has it been."
- Overlaps with `[[aircraft-registry]]` / `[[faa-registry]]` — sibling registry front-ends; use whichever surfaces the cleaner record.

## Trust & verifiability
`trust: trusted` — the authoritative first-party US registry. The registration is fact; just remember the registered owner may be a deliberate legal proxy rather than the person flying the aircraft.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-aviation-administration |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
