---
id: classmates
name: Classmates
description: Use when you have a `name` and a US school (`employer-org`) and want yearbook photos and alumni profiles — returns image, social-profile and associate links.
url: http://www.classmates.com
category: people-search
path:
- people-search
bestFor: Finding a US person's high-school yearbook photo, era and classmates via a large digitised yearbook and alumni directory.
selectorsIn:
- name
- employer-org
selectorsOut:
- image
- social-profile
- associate
status: live
pricing: freemium
costNote: Free registration lets you search schools, alumni directories and view yearbooks. A paid Classmates+ membership unlocks full messaging, "who viewed you", and hardcover reprints; yearbook reprints are sold separately.
opsec: passive
opsecNote: Searching and browsing yearbooks is passive toward the subject. However, Classmates requires a registered account and a paid membership can reveal profile visitors, so operate from a sock-puppet account — never a personal one that could surface you to the target.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established US alumni/yearbook platform with 480k+ digitised yearbooks; yearbook scans are authoritative, but user-created alumni profiles are self-asserted.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
aliases:
- Classmates.com
tags:
- people-investigations
- yearbook
- alumni
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Classmates

> A vast US yearbook and alumni directory — put a name and a school together and get a period photo, graduation year, and a roster of the people around them.

## When to use
You have a US `name` and at least a rough idea of where/when they went to school (`employer-org` = school, plus an era), and you want a confirmed historic photo (`image`), a graduation year to anchor age/timeline, or a list of classmates (`associate`) to expand the network. Yearbook photos are especially valuable for missing-person work: they give a verified face for reverse-image search and a firm identity anchor from before the trail went cold.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free (sock-puppet) account at classmates.com — required to search fully.
2. Search by the subject's `name` (try maiden names) or search for the school directly, then browse its yearbooks by year.
3. Locate the subject's yearbook photo and page; note the graduation year and any activities/clubs.
4. Scan the same class for classmates (`associate`) and any linked alumni profiles (`social-profile`).
5. Pivot: the yearbook photo feeds reverse-image/face search; the graduation year fixes approximate `dob`; classmates become new `name` leads.

## Inputs → Outputs
- **In:** `name` (+ school/era as `employer-org`)
- **Out:** `image` (yearbook photo), `social-profile` (alumni profile), `associate` (classmates)
- **Empty/negative result looks like:** no matching yearbook or profile — meaning that school/year isn't digitised or the person isn't captured; US coverage is broad but not complete, so absence isn't conclusive.

## Gotchas & OpSec
- US-focused; weak outside the United States.
- Alumni profiles are user-created and can be stale or impersonated; yearbook scans are the reliable part.
- Some features (messaging, visitor lists) are paid and can expose you — stay on the free search from a puppet account.

## Overlaps ("do both")
- Pairs with reverse-image/face tools (feed the yearbook photo in) and other US people-search — the yearbook gives a verified young face and firm identity that current-data tools lack.

## Trust & verifiability
`trust: community` — authoritative yearbook imagery from a long-running platform, but treat user-submitted alumni profile details as self-asserted until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | classmates |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → image, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
