---
id: ama-assn-org
name: ama-assn.org
description: Use when you have a physician `name` and a US city/state/ZIP and want to verify they are a real, licensed doctor — returns specialty, practice location and credentialing details.
url: https://find-doctor.ama-assn.org/#
category: public-records
path:
- public-records
bestFor: Verifying that a named person is a real US physician and pinning down their specialty and practice location.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free directory operated by the American Medical Association; a free account/sign-in may be prompted for full result detail but basic lookup is open.
opsec: passive
opsecNote: Read-only lookup against the AMA's public physician directory. You are not contacting the subject; the AMA cannot tie a search to the person searched-for. Still, use a clean browser session if you create an account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the American Medical Association (AMA), the primary US physician professional body — the authoritative source for "is this person actually an MD".
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thentiacloud-net
aliases:
- AMA Find a Doctor
- AMA DoctorFinder
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ama-assn.org

> The American Medical Association's official "Find a Doctor" directory — an authoritative check on whether a named US physician is real.

## When to use
You have a `name` that a subject claims (or is claimed) to be a physician, plus at least a US city/state or ZIP, and you want to confirm the person exists as a licensed doctor and learn their specialty and practice location. Useful for corroborating identity of a medical professional, disproving a fake "doctor" claim, or geolocating a subject to a known practice.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://find-doctor.ama-assn.org/ in a browser.
2. Enter the physician's `name` (first, last, or both) together with a city/state combo or ZIP code (`address`). You can also filter by specialty.
3. Read the results: a matching physician record shows name, specialty, and practice location (`employer-org` / `address`). Physicians can "claim" and verify their own page, so a claimed page is higher-confidence.
4. Pivot: a confirmed practice address feeds mapping/people-search; the specialty and org name feed employer/licensing checks like `[[thentiacloud-net]]`.

## Inputs → Outputs
- **In:** `name` + US `address` (city/state/ZIP); optional specialty
- **Out:** `name`, specialty, `employer-org` (practice), `address` (practice location)
- **Empty/negative result looks like:** no matching physician for that name/location — meaning either the person is not an AMA-listed US physician, the name/location is off, or they practice elsewhere. Absence is not proof they never held a license.

## Gotchas & OpSec
- US-only. A non-match for a claimed foreign-trained or non-US doctor is expected and not disqualifying.
- A free account/sign-in may be requested to see full detail; basic name+location lookup is generally open.
- OpSec: **passive** — a directory read that does not touch the subject.

## Overlaps ("do both")
- Pairs with `[[thentiacloud-net]]` and other licensing-board tools — the AMA directory confirms the person is a physician and gives specialty/location, while board-licensing sites confirm the active license status and any disciplinary record.

## Trust & verifiability
`trust: trusted` — first-party AMA data; the most authoritative "is this a real US doctor" source, with physician-claimed pages adding confidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ama-assn-org |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
