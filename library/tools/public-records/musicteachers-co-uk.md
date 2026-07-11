---
id: musicteachers-co-uk
name: MusicTeachers.co.uk
description: Use when you have a `name`, instrument or `address`/area and think the subject is a UK private music teacher — returns teacher `name`, `address`/area, qualifications and `social-profile`.
url: https://musicteachers.co.uk/music-lessons
category: public-records
path:
- public-records
bestFor: Finding a UK private music teacher's listing — name, instrument, service area and qualifications.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- name
- address
- social-profile
status: live
pricing: free
costNote: Free to search the directory (lesson fees are the teacher's, not the site's); no account needed to browse listings.
opsec: passive
opsecNote: Public directory; browsing is passive and needs no login. Contacting a teacher is an active step — stay in read-only unless you intend to engage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate UK music-tuition directory with a stated vetting process, but listings are teacher self-supplied, so details are claimed.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Music Teachers UK
tags:
- professionlicensing
- Profession & Licensing Sites
- music
- tuition
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# MusicTeachers.co.uk

> A UK directory of private music teachers: a niche way to tie a name to a teaching business, instrument, service area and qualifications when the subject gives music lessons.

## When to use
You have a `name`, or an area + instrument, and think the subject teaches music privately in the UK. The directory maps teachers to their instrument(s), coverage area, ability levels taught, qualifications and pricing — a targeted lead for a self-employed subject whose work is tuition, which general people-search rarely surfaces.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://musicteachers.co.uk/music-lessons and search/filter by instrument, location, day/availability, ability level, or name.
2. Open a teacher's profile: name, area covered, instruments, qualifications, teaching approach, pricing, and any linked site/socials.
3. Use the area as an `address`/location pivot and qualifications/instrument to corroborate identity.
4. Follow any linked website/social profiles.
5. Pivot: run the teacher/business name through general search and Companies House; the coverage area anchors geography.

## Inputs → Outputs
- **In:** `name`, instrument/`employer-org`, or `address`/area
- **Out:** teacher `name`, `address`/service area, qualifications, `social-profile`/website
- **Empty/negative result looks like:** no listing — the subject doesn't advertise here (many teachers use other directories or word-of-mouth), or teaches under a different name; absence doesn't rule out tuition work.

## Gotchas & OpSec
- Covers only teachers who list here — a narrow slice; check other tuition directories and local ads too.
- Listings are self-supplied marketing; "area covered" is a coverage region, not a home address.
- UK-only.

## Overlaps ("do both")
- Pairs with general search and other tuition/marketplace directories — this confirms the music-teaching angle and area; those cross-cover teachers who don't list here.

## Trust & verifiability
`trust: community` — a legitimate directory with vetting, but profile content is teacher-supplied; corroborate name, area and qualifications against an independent source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | musicteachers-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → name, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
