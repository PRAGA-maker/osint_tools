---
id: tutorhunt-com
name: Tutor Hunt
description: Use when you have a subject you suspect tutors in the UK (a `name` or a subject+`geolocation`) and want to find their tutor profile — returns tutor name, area, subjects, qualifications, and often a photo.
url: https://www.tutorhunt.com/
category: public-records
path:
- public-records
bestFor: Finding a person's private-tutor profile (subjects, area, qualifications, photo) on the UK Tutor Hunt marketplace.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- image
- geolocation
- social-profile
status: live
pricing: freemium
costNote: Browsing and viewing tutor profiles is free; contacting a tutor through the platform requires a (free) account and messaging credits/registration.
opsec: passive
opsecNote: Browsing public tutor profiles is passive. Contacting a tutor via the site is active and reveals your account to them — stop at the profile unless you intend to make contact under a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial UK tutor marketplace; profile content is self-submitted by tutors (with DBS/ID checks claimed by the site) and should be treated as claims to corroborate.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- tutorhunt.com
- Tutor Hunt UK
tags:
- professionlicensing
- Profession & Licensing Sites
- uk
- tutoring
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Tutor Hunt

> A UK tutor marketplace used as a people-finding source: locate a subject's tutor profile with their subjects, area, qualifications, and photo.

## When to use
You suspect a subject offers private tuition in the UK and want to find their public profile. Searching by subject + `geolocation` (city/county) returns tutor listings; a profile can yield a first `name`, an approximate area (`geolocation`), the subjects they teach, self-declared qualifications/experience, feedback, and frequently a profile `image`. This is a useful niche source for confirming a person's side occupation, location, and appearance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tutorhunt.com/.
2. Search by subject and location (city or county), or use the site search to look for a specific tutor `name`.
3. Open candidate profiles and read: name/handle, area, subjects, qualifications, experience, feedback, and photo.
4. Pivot: the profile `image` feeds reverse-image/face search; declared qualifications feed licence/registry checks; the area narrows other location-based lookups. Do not message the tutor unless you deliberately intend active contact.

## Inputs → Outputs
- **In:** `name`, or subject + `geolocation`
- **Out:** tutor `name`, profile `image`, area `geolocation`, `social-profile` (subjects, qualifications, feedback)
- **Empty/negative result looks like:** no matching tutor — the subject may not advertise here, may use a different site (Superprof, MyTutor, etc.), or list under a partial/first-name-only handle.

## Gotchas & OpSec
- Profiles are **self-submitted**; the site claims DBS/ID checks, but treat qualifications and names as claims to verify, not facts.
- Profiles often show only a first name and an approximate area, not a full address.
- **OpSec:** browsing is passive; sending a message is active and exposes your account — use a sock puppet if you must make contact.

## Overlaps ("do both")
- Do both with other UK tutoring marketplaces (Superprof, MyTutor, First Tutors) since a person may only appear on one, and run any profile photo through reverse-image/face tools.

## Trust & verifiability
`trust: community` — a commercial marketplace with self-declared, lightly-verified profiles; corroborate identity, qualifications, and photo against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tutorhunt-com |
| category | public-records |
| selectorsIn → selectorsOut | name, geolocation → name, image, geolocation, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
