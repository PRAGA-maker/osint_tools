---
id: nzdoctor-free-classified-ads-new-zealand
name: NZ Doctor Classifieds (New Zealand)
description: Use when you have a `name` or clinic in the NZ health sector and want employment/recruitment ads — returns employer-org, contact names, and location.
url: https://www.nzdoctor.co.nz/classifieds
category: dating-classifieds
path:
- dating-classifieds
bestFor: Placing a doctor, nurse, or practice manager in New Zealand via medical-sector job and locum ads.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Classifieds/vacancy listings are free to browse without an account; the wider NZ Doctor news site has some subscriber-only content.
opsec: passive
opsecNote: Passive read-only browsing of a public recruitment board. No login and no notification to any listed contact; a standard clean browser session is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Published by NZ Doctor / The Health Media, a legitimate NZ medical-sector publisher; ads are advertiser-submitted.
missingPersonsRelevance: medium
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- NZDoctor classifieds
- New Zealand Doctor jobs
tags:
- toddington
- curated-directory
- specialty-search
- classifieds
- employment
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# NZ Doctor Classifieds (New Zealand)

> New Zealand medical-sector recruitment board, used to tie a health worker to a clinic, region, and named hiring contact.

## When to use
You are working an `employer-org` (a NZ practice, PHO, or clinic) or a `name` in the New Zealand health workforce — GPs, nurse practitioners, urgent-care, police medical officers — and want current or recent vacancy ads. Listings name the hiring organisation, its town/region, and often a named contact person, which places a clinic geographically and surfaces `associate`-style contacts (recruiters, practice managers).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nzdoctor.co.nz/classifieds.
2. Filter by region and job type, or scan the listings for the clinic/organisation you care about.
3. Read each ad for: hiring organisation, town/DHB region, role, and the named contact person plus their email/phone.
4. For a specific person, also run `site:nzdoctor.co.nz "<name>"` in a web search to catch older ads and article mentions.
5. Pivot: a named contact becomes a new `name`; the clinic becomes an `employer-org` + `address`; feed those into NZ company/registration lookups and people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (hiring clinic/practice), `address` (town/region), `name` (contact person)
- **Empty/negative result looks like:** no current ad for that clinic or person — expected, since only organisations actively recruiting appear, and only recently. Absence says nothing about whether the person works in NZ health.

## Gotchas & OpSec
- Coverage is New Zealand health sector only and skews to whoever is currently hiring; it is a corroboration source, not a directory of all clinicians.
- Ads rotate and expire, so a name may only be findable via cache or a site-scoped search.
- Contact details belong to recruiters/employers, not necessarily the subject — treat as organisational leads.

## Overlaps ("do both")
- Pairs with the NZ Companies Register and the Medical Council register — this gives the current vacancy/contact, those confirm the organisation and the clinician's registration.

## Trust & verifiability
`trust: community` — a legitimate NZ medical publisher, so the board is authentic, but individual ads are advertiser-supplied and should be verified against an official register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nzdoctor-free-classified-ads-new-zealand |
| category | dating-classifieds |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
