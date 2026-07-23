---
id: guru-com
name: Guru.com
description: Use when you have a `name`/`username` and want a subject's freelance profile — returns social-profile, employer-org (freelance work history), skills, and stated location.
url: https://www.guru.com
category: documents-metadata
path:
- documents-metadata
bestFor: Finding a person's freelancer profile (skills, portfolio, work history, location) on the Guru marketplace.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- employer-org
- address
status: live
pricing: freemium
costNote: Browsing/searching public freelancer profiles is free. Hiring, messaging, and posting jobs require a (free-to-create) client account; some contact features sit behind the platform.
opsec: passive
opsecNote: Viewing public profiles is passive and doesn't notify the freelancer. Messaging or hiring requires an account and is attributable — use a sock-puppet client account if you must engage. Freelancer-stated location/skills are self-reported and may be aspirational or obscured.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A mainstream freelance marketplace; profile data is user-submitted, useful as a lead and for corroboration rather than proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Guru
- guru.com
tags:
- freelance-marketplace
- profile-search
- toddington
- curated-directory
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Guru.com

> A freelance marketplace whose public profiles expose skills, portfolios, work history, and stated location — a place to find and characterize a subject's gig-work presence.

## When to use
You have a `name` or `username` and suspect the subject does freelance/contract work. Guru profiles list skills, a portfolio, ratings, earnings/job history, and often a stated city/country — useful for confirming a profession, linking a handle to real work, geolocating loosely, and finding writing/design samples or an employer trail. A sibling to Upwork/Fiverr searches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.guru.com and use the freelancer search (by skill, keyword, or name/handle).
2. Match a candidate profile by `name`/`username`, avatar, or portfolio style.
3. Read the profile: skills, portfolio, work/earnings history, reviews, and stated location (`selectorsOut`).
4. Pivot: reuse the `username` across other marketplaces/social sites; treat the stated location as an approximate lead; portfolio links may expose personal sites or contact details.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (Guru profile), `employer-org` (freelance work/job history), `address` (self-stated city/country), skills/portfolio
- **Empty/negative result looks like:** no matching freelancer — the person may not use Guru or uses a different handle; check Upwork/Fiverr/LinkedIn instead.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing; engagement needs an account.
- OpSec: passive while reading; messaging/hiring is attributable — use a puppet account.
- Self-reported data: location and skills can be inflated or deliberately vague; corroborate before relying on them.

## Overlaps ("do both")
- Pairs with [[upwork]] and Fiverr/PeoplePerHour searches — freelancers often maintain profiles on several platforms with the same handle/portfolio, so cross-run to confirm identity and fill gaps.

## Trust & verifiability
`trust: unverified` — a legitimate marketplace, but profiles are user-authored; use them as leads and to corroborate identity/profession, not as authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guru-com |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, username → social-profile, employer-org, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
