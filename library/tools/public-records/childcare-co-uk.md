---
id: childcare-co-uk
name: childcare.co.uk
description: Use when you have a `name` or postcode and want to find a subject who works in UK childcare/tutoring — returns provider profiles with area, experience, qualifications, and reviews.
url: http://www.childcare.co.uk/
category: public-records
path:
- public-records
bestFor: Locating a UK childminder, nanny, babysitter, or tutor's public profile and working area by name or postcode.
selectorsIn:
- name
- address
selectorsOut:
- social-profile
- address
- name
status: live
pricing: freemium
costNote: Browsing and searching provider profiles is free; contacting providers via the on-site messaging and some features require a (free or paid) member account.
opsec: passive
opsecNote: Searching and viewing public provider profiles is passive. Messaging a provider goes through the site's system and reveals you to them — use a sock-puppet account and never contact a subject directly. Providers can sometimes see profile-view activity if you're logged in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Large, established UK childcare/tutor marketplace; profiles are self-authored (with optional document validation), so treat details as claimed until corroborated.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- Childcare.co.uk
tags:
- professionlicensing
- Profession & Licensing Sites
- childcare
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# childcare.co.uk

> A large UK marketplace for childminders, nannies, babysitters, nurseries, and tutors — use it to find a subject who advertises childcare/tutoring services and pull their working area, experience, and reviews.

## When to use
You have a `name` or a postcode/area and reason to think the subject works (or advertised) in UK childcare or private tutoring. A provider profile yields a working location (postcode radius), stated experience and qualifications, fees, photos, and reviews from families — strong locate and identity leads, and a geographic anchor. Reach for it when a subject's employment is (or is claimed to be) in this sector, or when working outward from an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.childcare.co.uk/.
2. Search by **postcode** (choose a 1–40 mile radius) to list local providers, and/or filter by role (nanny, childminder, babysitter, tutor, nursery).
3. Scan results for the subject's `name`; open the profile.
4. Read: advertised area, experience/qualifications, fees, uploaded documents/certs, photos, and reviews.
5. Pivot: the working area anchors `geolocation`; reviews name families/associates; reused handles/photos feed cross-platform and reverse-image tools.

## Inputs → Outputs
- **In:** `name` / `address` (postcode)
- **Out:** `social-profile` (provider profile), `address` (working area), `name`, plus experience, quals, reviews
- **Empty/negative result looks like:** no matching provider in the area — the subject isn't advertising here (or uses a different name/area). Not proof they don't work in childcare; check Ofsted's childminder register and other directories.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; messaging a provider needs an account (sock puppet) and exposes you — don't contact the subject.
- Profiles are **self-authored**; qualifications may be unverified unless the site validated documents. Corroborate before relying.
- OpSec: passive when browsing; logged-in activity/messaging is attributable.

## Overlaps ("do both")
- Pairs with the Ofsted childminder register (authoritative registration) and general people-search — this gives self-advertised area/experience; Ofsted confirms official registration status.

## Trust & verifiability
`trust: community` — a big, real marketplace, but provider profiles are self-published; use them as leads and confirm registration/identity via authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | childcare-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → social-profile, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
