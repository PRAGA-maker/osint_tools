---
id: sadoctorsapp-co-za
name: sadoctorsapp.co.za (Near Me Doctors)
description: Use when you have a doctor's `name` or a `geolocation`/`address` in South Africa and want their practice location and contact details — returns address, phone, employer-org.
url: https://www.sadoctorsapp.co.za/
category: public-records
path:
- public-records
bestFor: Locating a South African doctor's practice — address, phone, hours and map — from a name or an area.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- phone
- name
- employer-org
status: live
pricing: free
costNote: Free public directory / booking site ("Near Me Doctors"); no account needed to search.
opsec: passive
opsecNote: Browsing a public practitioner directory is passive and does not alert the doctor. Avoid using any "book appointment" flow, which would create a real interaction; stop at the listing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial doctor-directory/booking app, not the official HPCSA licensing register — listings are business info, so it confirms where a practitioner works but is not authoritative for verifying registration status.
missingPersonsRelevance: high
coverage:
- za
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Near Me Doctors
- SA Doctors App
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# sadoctorsapp.co.za (Near Me Doctors)

> A South African doctor-finder directory: turn a practitioner's name or an area into their practice address, phone number, hours and map location.

## When to use
You have the `name` of a doctor believed to practise in South Africa (or neighbouring countries), or you have an `address`/area and want to enumerate practitioners near it, and you need their practice location and contact details. Useful for confirming that a known doctor practises where the subject claims, or for locating a person via their professional practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sadoctorsapp.co.za/ (or /doctors).
2. Search by practitioner `name`, speciality, or town/suburb (`address`/`geolocation`).
3. Open a listing: it shows the practice name, physical address, phone, trading hours and a map with directions.
4. Pivot: the practice address/phone feeds geolocation and reverse-phone checks; the practitioner's full name feeds people-search and the official HPCSA register for licence verification.

## Inputs → Outputs
- **In:** `name`, `address`/area, or `employer-org` (practice/clinic name)
- **Out:** practice `address`, `phone`, `name`, `employer-org` (clinic), hours, map location
- **Empty/negative result looks like:** no listing for the name — meaning the doctor isn't in this commercial directory, which is not proof they aren't registered; verify against HPCSA separately.

## Gotchas & OpSec
- This is a directory/booking service, not a government licence register — use it to locate a practice, not to prove someone is a validly registered doctor.
- Contact/hours are self-listed business data and can be outdated.
- OpSec: passive; do not trigger the booking flow, which would be an active contact.

## Overlaps ("do both")
- Pairs with the official HPCSA practitioner register — this gives the practice's location and contact, while HPCSA authoritatively confirms registration and speciality.

## Trust & verifiability
`trust: community` — a real, functioning commercial directory (confirmed live), but listings are business-supplied and it is not an authoritative licensing source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sadoctorsapp-co-za |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, phone, name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
