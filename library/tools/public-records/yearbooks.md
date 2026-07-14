---
id: yearbooks
name: E-Yearbook.com
description: Use when you have a `name` and an approximate school/year and want a historical school/college/military yearbook photo and entry — returns a period `image`, confirmed `name` spelling, and school/year context.
url: https://www.e-yearbook.com/
category: public-records
path:
- public-records
bestFor: Putting a face and school/year to a name from digitized yearbooks — useful for older subjects and long-cold cases.
selectorsIn:
- name
selectorsOut:
- image
- name
status: live
pricing: freemium
costNote: Browsing/searching and low-res previews are free; full-resolution page access, printing, and downloads require a paid subscription.
opsec: passive
opsecNote: Searching is passive and does not touch the subject. Creating an account for full access ties activity to that login — use a sock-puppet account if attribution matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A large commercial yearbook-digitization archive; the scans are authentic primary sources, though coverage is uneven by school/year and OCR name-indexing can miss entries.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases:
- e-yearbook
- eyearbook
tags:
- yearbook
- genealogy
- school
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# E-Yearbook.com

> A large archive of digitized US high-school, college, and military yearbooks — search a name/school/year to pull a period photo and biographical crumbs.

## When to use
You have a `name` and roughly where/when they went to school, and you want a face from that era, confirmation of the name's spelling, activities/clubs, or classmates. Yearbooks are strong for older subjects, adoptees/relatives in genealogy work, and cold cases where recent imagery is scarce. A photo here can anchor a facial-recognition or reverse-image pass on decades-old identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.e-yearbook.com/ and search by school name, state, and type (high school/college/military), or by name where indexed.
2. Narrow to the right institution and year; browse to the person's grade/section.
3. Read the entry: portrait (`image`), full `name`, activities, and classmates (potential `associate`s).
4. For a full-resolution image or print, a paid subscription is required (previews are free).
5. Pivot: the period photo → reverse-image/face tools; classmates and clubs → contemporaries who may know the subject; school+year → alumni directories.

## Inputs → Outputs
- **In:** `name` + school/year (or browse by school)
- **Out:** period `image` (portrait), confirmed `name`, activities, classmates
- **Empty/negative result looks like:** the school/year isn't digitized, or the name isn't OCR-indexed — browse the volume manually before concluding they're absent.

## Gotchas & OpSec
- Coverage is patchy: many schools/years aren't scanned; absence ≠ "not enrolled."
- Name-search relies on OCR and is incomplete — browsing the actual volume often finds what search misses.
- Full images sit behind a paywall; budget for a subscription for serious use.

## Overlaps ("do both")
- Pairs with `[[classmates-com]]`-style alumni sites and Ancestry/genealogy tools — those add records and contacts; this adds the contemporaneous photo.

## Trust & verifiability
`trust: community` — a commercial archive of authentic primary-source scans; the images are genuine, but indexing gaps and uneven coverage mean you should verify by browsing, not just searching.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yearbooks |
| category | public-records |
| selectorsIn → selectorsOut | name → image, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
