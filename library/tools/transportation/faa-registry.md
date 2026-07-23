---
id: faa-registry
name: FAA Registry
description: Use when you have a US aircraft tail number (N-number) or an owner `name` and want the registered owner and address — returns the owner `name`/`employer-org`, mailing `address` and aircraft details.
url: https://registry.faa.gov/aircraftinquiry/nnum_inquiry.aspx
category: transportation
path:
- transportation
bestFor: Resolving a US N-number to its registered owner (name/company + address), or finding aircraft registered to a person/company.
selectorsIn:
- document-id
- name
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official FAA aircraft registration inquiry; no account.
opsec: passive
opsecNote: Public government registry — you query the FAA, not any subject, so there is no target-side exposure. Standard web-server logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official FAA aircraft registration database; the owner-of-record and registration data is authoritative US government record.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- aircraft-registry
- federal-aviation-administration
aliases:
- FAA Aircraft Inquiry
- N-Number Inquiry
tags:
- aviation
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# FAA Registry

> The FAA's official aircraft-registration lookup: turn a US tail number (N-number) into the registered owner and address, or search by owner name to find their aircraft.

## When to use
You have a US aircraft tail number — spotted on a plane, in a photo, in flight-tracking data — and need the owner of record. Or you have a `name`/company and want to know what aircraft they register. Aircraft ownership ties a person or `employer-org` to a mailing `address` and, for high-net-worth or corporate subjects, to assets and movement patterns. It's a strong asset/attribution source in the US.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://registry.faa.gov/aircraftinquiry/.
2. Choose the inquiry type: "N-Number" (enter the tail number, minus the leading "N" as prompted) or "Name" (enter the owner/company name).
3. Submit and read the record: registered owner `name`/`employer-org`, mailing `address`, aircraft make/model/serial, registration status and dates.
4. For a name search, review the list of aircraft registered to that party.
5. Pivot: the mailing address feeds people/property search; a company owner feeds corporate-registry lookups; the aircraft feeds flight-tracking (e.g. ADS-B) for movement history.

## Inputs → Outputs
- **In:** aircraft N-number (`document-id`) or owner `name`
- **Out:** registered owner `name`/`employer-org`, mailing `address`, aircraft make/model/serial, registration status
- **Empty/negative result looks like:** "No records found" — the N-number is deregistered/reserved/invalid, or the name doesn't match a US registrant. Note that many aircraft are held by LLCs or trusts, so the "owner" may be a shell, not the beneficial owner.

## Gotchas & OpSec
- Ownership is frequently through LLCs, trusts (e.g. Delaware trustee arrangements) or management companies — the registered owner can mask the real principal; treat a corporate owner as a pivot, not the endpoint.
- US aircraft only (N-numbers). Other countries have their own registries.
- OpSec: passive — a public FAA database.

## Overlaps ("do both")
- Pairs with `[[aircraft-registry]]` and flight-tracking (ADS-B) services — the FAA record gives ownership and address, while ADS-B history shows where the aircraft actually flies, together tying an owner to movements.

## Trust & verifiability
`trust: trusted` — the FAA's own registration record, authoritative for US aircraft, with the standing caveat that registered ownership can be an LLC/trust rather than the true principal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | faa-registry |
| category | transportation |
| selectorsIn → selectorsOut | document-id, name → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
