---
id: nidirect-gov-uk
name: nidirect.gov.uk (DVA Northern Ireland)
description: Use when your subject is in Northern Ireland and you need the official channel for driver/vehicle records and NI government services — returns the authoritative contact/enquiry route for DVA and links to GRONI/PRONI records.
url: https://www.nidirect.gov.uk/contacts/driver-vehicle-agency-dva-northern-ireland
category: public-records
path:
- public-records
bestFor: Official Northern Ireland government gateway — DVA driver/vehicle enquiries plus links to civil-registration and archive records.
selectorsIn:
- name
- address
- vehicle-plate
selectorsOut:
- address
- name
- document-id
status: live
pricing: free
costNote: The portal and its guidance are free; some record requests (certificates, driver-record enquiries) carry a statutory fee paid to the relevant agency.
opsec: passive
opsecNote: Reading the official government portal is passive and unattributed. Actually requesting driver/vehicle records requires a lawful basis and a formal application that ties the request to you — treat that as an active, logged, gated step.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Northern Ireland government services website; authoritative for how to reach DVA (driver/vehicle records) and the GRONI/PRONI record offices.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- nidirect
- DVA Northern Ireland
- Driver and Vehicle Agency NI
tags:
- profession-licensing
- northern-ireland
- public-records
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# nidirect.gov.uk (DVA Northern Ireland)

> The official Northern Ireland government portal — the authoritative route to Driver & Vehicle Agency enquiries and to NI civil-registration and archive records.

## When to use
Your subject is in Northern Ireland (which has its own driver/vehicle authority, the DVA, separate from GB's DVLA) and you need the official channel to enquire about driver or vehicle records, or a gateway to NI birth/death/marriage certificates (GRONI) and historical records (PRONI). This is not a self-serve public database — it's the authoritative entry point that tells you which NI agency holds what and how to make a lawful request.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nidirect.gov.uk/contacts/driver-vehicle-agency-dva-northern-ireland for the DVA contact/enquiry details.
2. For record types beyond driving/vehicles, navigate to the GRONI (civil registration) or PRONI (archives) sections linked from the portal.
3. Follow the stated process: driver/vehicle record enquiries and certificate orders require a formal application (often with a fee and a lawful basis).
4. Pivot: use the correct NI agency identified here rather than the GB equivalent; a certificate or record obtained lawfully can yield `address`, full `name`, and `document-id` references.

## Inputs → Outputs
- **In:** subject `name`, `address`, or `vehicle-plate` (to route to the right NI record process)
- **Out:** the authoritative enquiry/application route; via GRONI/PRONI/DVA, `address`, `name`, and `document-id` (certificate/record references) — subject to a lawful request
- **Empty/negative result looks like:** the portal only gives process/contact info, never bulk lookups — "no self-serve search" is expected; the record itself comes from the downstream agency application.

## Gotchas & OpSec
- Human-in-the-loop: driver/vehicle and civil records are gated — they require a formal, often fee-bearing application with a lawful basis, not an anonymous lookup.
- NI is a distinct jurisdiction: use DVA/GRONI/PRONI, not DVLA/GRO England.
- OpSec: browsing the portal is passive; submitting a record request is attributable to you.

## Overlaps ("do both")
- Complements GB-wide public-records tools — when a trail crosses into Northern Ireland, this identifies the correct NI agency those GB tools don't cover.

## Trust & verifiability
`trust: trusted` — the official NI government website; authoritative for agency contacts and record processes, though the records themselves live with (and are certified by) the downstream agencies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nidirect-gov-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, vehicle-plate → address, name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
