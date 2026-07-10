---
id: classmates-canada-alumni-lookup
name: Classmates — Alumni / Yearbook Lookup
description: Use when you have a `name` and a school/graduation year and want alumni and digitized yearbook records — returns `social-profile`, classmate `associate`s and yearbook `image`s (photos). US-centric, paywalled.
url: https://www.classmates.com/registration/state.jsp
category: people-search
path:
- people-search
bestFor: Finding a person via their school/graduation year — Classmates hosts alumni lists and a large digitized-yearbook archive with names and old photos.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
- image
status: live
pricing: freemium
costNote: Browsing schools and some yearbook previews is free, but viewing full yearbooks/photos and contacting alumni generally requires a paid membership. Account/registration required for most useful features.
opsec: passive
opsecNote: Searching alumni/yearbooks doesn't notify the subject. Creating an account and messaging alumni ties activity to your (puppet) identity and can be visible to other members — use a sock puppet, not your real profile.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial alumni/yearbook site (primarily US, some Canada). Yearbook scans are authentic historical records; the alumni-networking data is user-contributed and dated. Much is paywalled.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Classmates.com
- classmates yearbook
tags:
- people-search
- alumni
- yearbook
- us-records
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Classmates — Alumni / Yearbook Lookup

> A school-based people finder: enter a name and school year and Classmates surfaces alumni listings and digitized yearbooks — old photos and classmate networks that predate the modern web.

## When to use
You have a `name` and know (or can guess) the person's school and graduation era. Classmates hosts alumni lists and one of the largest **digitized-yearbook** archives, so it can produce a real-name confirmation, a period photo (`image`), and a set of classmates (`associate`s) — invaluable for locating someone through their past, verifying age/identity, or finding people who knew them. Strongest for US subjects (some Canadian coverage).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open Classmates and browse by state → city → school, or search a school directly (the linked registration/state page is the entry to school browsing).
2. Locate the school and graduation year; open the alumni list and any digitized **yearbook** for that year.
3. Find the `name`: read the alumni entry and yearbook page — photos, full name, classmates. Expect a paywall/login for full yearbook viewing.
4. With a **puppet** account, you can view more and (paid) message alumni.
5. Pivot: yearbook photo → reverse-image/face search; classmates → `associate` graph and people who can be contacted; confirmed full name + age → other people-search and public records.

## Inputs → Outputs
- **In:** `name` + school/graduation year
- **Out:** `social-profile` (alumni listing), `associate` (classmates), `image` (yearbook photos), plus full name and approximate age
- **Empty/negative result looks like:** school not listed, year not digitized, or no alumni entry — coverage is uneven (many schools/years aren't scanned), and non-US schools are sparse. Absence often means "not digitized," not "no such person."

## Gotchas & OpSec
- **Paywall + login:** the genuinely useful content (full yearbooks, contact) is behind a paid membership and account — treat as an active, account-bound task.
- Alumni networking data is user-contributed and old; yearbook scans are the more reliable part.
- US-centric; thin outside the US/Canada.
- OpSec: **passive** search, but account/messaging exposes your puppet to other members.

## Overlaps ("do both")
- Pairs with reverse-image/face search on yearbook photos, and with US people-search aggregators (`[[spytox]]`, `[[peoplesearchnow]]`) to turn a confirmed name+age into current contact/address.

## Trust & verifiability
`trust: unverified` — authentic yearbook scans but dated, user-contributed alumni data and heavy paywalling. Corroborate identity (photo, age) and never assume the current-contact data is fresh.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | classmates-canada-alumni-lookup |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, associate, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login, payment-wall-partial) |
