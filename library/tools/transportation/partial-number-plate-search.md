---
id: partial-number-plate-search
name: Partial Number Plate Search
description: Use when you have only part of a UK `vehicle-plate` (from a witness or dashcam) and want to shortlist the full plate — narrow candidates with make, model and colour.
url: https://www.partialnumberplate.co.uk/
category: transportation
path:
- transportation
bestFor: Reconstructing a likely full UK registration from a partial plate plus vehicle description, when only 2–3 characters are known.
selectorsIn:
- vehicle-plate
selectorsOut:
- vehicle-plate
status: live
pricing: freemium
costNote: Basic partial-plate search is free; deeper filtering / full vehicle checks are offered as optional premium features.
opsec: passive
opsecNote: Searching by partial plate against publicly available UK vehicle data is legal and does not notify any owner. It only narrows to candidate plates — pulling a full DVLA vehicle/owner record afterward is a separate, more regulated step. Use a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A UK-focused partial-plate matching service using public vehicle data. It shortlists candidates; it does not authoritatively return an owner, so treat matches as leads.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- partialnumberplate.co.uk
- UK partial reg checker
tags:
- vehicle
- license-plate
- uk
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Partial Number Plate Search

> A UK tool for the classic "I only caught part of the reg" problem — enter a partial plate plus what the vehicle looked like, and it shortlists the likely full registrations.

## When to use
You have a fragment of a UK `vehicle-plate` — a few characters from a witness, dashcam or CCTV — and a rough description (make, model, colour) and want to narrow it to candidate full plates. This is the front half of a vehicle investigation: it reconstructs likely registrations from public data, which you then take to a proper DVLA/vehicle-check step for tax/MOT/history (owner data is separately regulated).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.partialnumberplate.co.uk/ in a sock-puppet browser (the page needs JavaScript).
2. Enter the known characters of the plate; use wildcards (e.g. `?` for one unknown, `*` for several) where supported.
3. Filter the candidate list by make, model, and colour to shrink it toward the vehicle you saw.
4. Take the shortlisted full plate(s) to a DVLA vehicle-enquiry / MOT-history check to confirm make/model/colour match.
5. Pivot: a confirmed full `vehicle-plate` feeds vehicle-history tools and, via lawful DPPA/DVLA channels, owner enquiries.

## Inputs → Outputs
- **In:** partial `vehicle-plate` + make/model/colour description
- **Out:** a shortlist of candidate full `vehicle-plate`s matching the fragment and description
- **Empty/negative result looks like:** too many or zero candidates — add more known characters or description detail; a fragment that is too short simply won't narrow usefully.

## Gotchas & OpSec
- Human-in-the-loop: none, but results are candidates, not confirmations — you must verify each against the vehicle description.
- OpSec: **passive** and legal for the partial search itself. Retrieving the registered keeper's details is a separate, DPArP/DVLA-regulated step — don't assume this tool gives you an owner.
- Matching quality depends on the completeness of the public dataset; treat the shortlist as leads to confirm.

## Overlaps ("do both")
- Pairs with DVLA vehicle-enquiry/MOT-history checks (to confirm a shortlisted plate) and UK-OSINT vehicle-research guides; complements US-focused plate tools like [[license-plate-lookup]].

## Trust & verifiability
`trust: community` — a UK partial-plate matcher on public data; it reliably shortlists candidates but does not authoritatively identify a vehicle or owner, so every match needs confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | partial-number-plate-search |
| category | transportation |
| selectorsIn → selectorsOut | vehicle-plate → vehicle-plate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
