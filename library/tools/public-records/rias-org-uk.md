---
id: rias-org-uk
name: rias.org.uk
description: Use when you have an architect's or firm `name` (or a Scottish location) and want to confirm the practice and its address — returns a chartered architectural-practice profile.
url: https://www.rias.org.uk/for-the-public/practices
category: public-records
path:
- public-records
bestFor: Confirming and locating a chartered architectural practice in Scotland by name, area or specialism.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free public directory operated by the Royal Incorporation of Architects in Scotland; no account needed.
opsec: passive
opsecNote: Passive — browsing the directory is anonymous and not attributed to you. It only exposes business (practice) contact details, not private home addresses, so leakage risk is low.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by RIAS, the professional body for architects in Scotland; the "Chartered Practice" designation is authoritative, though individual profile text is self-supplied.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- arb-register
aliases:
- RIAS practice directory
- Royal Incorporation of Architects in Scotland
tags:
- professionlicensing
- Profession & Licensing Sites
- architects
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# rias.org.uk

> The Royal Incorporation of Architects in Scotland's public directory of chartered architectural practices — a way to confirm and geolocate an architecture firm in Scotland.

## When to use
You have a practice or architect `name`, or you know someone works in architecture in a Scottish town and want to pin down the firm. This directory lists RIAS architectural practices across Scotland, searchable by name, by location (radius from a place), or by one of 40+ specialisms (conservation, sustainability, residential, etc.). It confirms a firm exists, whether it holds "Chartered Practice" status, and gives its business address — a solid anchor for locating a working professional.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.rias.org.uk/for-the-public/practices.
2. Search by practice `name`, by "near you" with a mileage radius, or by specialism; or open the alphabetical address list of all practices.
3. Open a result to read the practice name, city/`address`, chartered status and any listed contacts.
4. Pivot: the practice address feeds a geolocation; the firm name plus a person's name feeds employment/associate confirmation and the ARB register for individual architect registration.

## Inputs → Outputs
- **In:** `name` (person or firm), `employer-org`, or `address`/location
- **Out:** `employer-org` (practice), `address` (business location), `name`
- **Empty/negative result looks like:** no listing for the searched name or area — meaning the firm isn't RIAS-registered (it may still exist; individual architects are on the UK-wide ARB register instead).

## Gotchas & OpSec
- This lists *practices/firms*, not individual architects — for a named person's registration, use the ARB (Architects Registration Board) register.
- RIAS is Scotland-specific; a practice elsewhere in the UK won't appear.
- Addresses are business premises, not homes — useful for locating where someone works, not where they live.

## Overlaps ("do both")
- Pairs with `[[arb-register]]` — ARB is the statutory UK-wide register of individual architects (confirms a *person* is a registered architect), while RIAS confirms and locates the *practice* in Scotland.

## Trust & verifiability
`trust: trusted` — maintained by RIAS. Chartered-practice status and firm existence are authoritative; descriptive/specialism text is self-declared by the practice.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rias-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
