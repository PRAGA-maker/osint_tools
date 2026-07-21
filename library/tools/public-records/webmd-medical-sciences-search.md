---
id: webmd-medical-sciences-search
name: WebMD Physician Directory
description: Use when you have a doctor's `name` (US) and want their practice location, specialty and credentials — returns a practice `address`, `employer-org` and professional detail via WebMD's physician directory.
url: https://doctor.webmd.com/
category: public-records
path:
- public-records
bestFor: Locating a US physician's practice address, specialty, and affiliations from their name.
selectorsIn:
- name
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free public physician directory; no account needed to search or view a doctor's profile.
opsec: passive
opsecNote: Looking up a public physician listing is passive and invisible to the subject. No sock puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: WebMD is a major health-information company; its physician directory aggregates provider data (much from NPI/insurance sources) — generally reliable but occasionally stale, so confirm current practice.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- WebMD Find a Doctor
- doctor.webmd.com
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- physician-directory
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- pill-identifier
---

# WebMD Physician Directory

> WebMD's "Find a Doctor" directory — not a research search engine, but a way to tie a US physician's name to a practice address, specialty, and affiliations.

## When to use
Your subject is (or claims to be) a US physician/healthcare provider, and you have a `name`. WebMD's provider directory returns their specialty, practice location, education, and affiliated hospitals/groups — useful to confirm a professional identity, locate a workplace, or verify a medical claim. (WebMD's main site is consumer health content with no investigative value; the directory is the OSINT-relevant part.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://doctor.webmd.com/.
2. Search the doctor's `name`, optionally with city/state to disambiguate.
3. Open the matching profile: specialty, practice `address`, group/hospital affiliations, education, and languages.
4. Cross-check the provider against the state medical board and the NPI registry to confirm licensure and current practice.
5. Pivot: a practice `address` and `employer-org` (group/hospital) feed people-search and public-records; education/affiliations build a professional timeline.

## Inputs → Outputs
- **In:** a US physician's `name`
- **Out:** profile → practice `address`, specialty, `employer-org` (group/hospital), education
- **Empty/negative result looks like:** no listing — the person may not be a US-licensed provider, or the directory hasn't indexed them; confirm via the NPI registry / state board before concluding.

## Gotchas & OpSec
- US-only, physicians-only: irrelevant for non-medical subjects or non-US providers.
- Aggregated data can be stale (old address/affiliation) — verify current practice against a primary source.
- Common names collide — disambiguate with location and specialty.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with the NPI registry and state medical-board lookups — WebMD gives a convenient profile, while those are the authoritative licensure/identity sources.

## Trust & verifiability
`trust: trusted` — a major health company's directory built largely on official provider data; reliable for orientation, but confirm licensure and current practice against the NPI registry / state board.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webmd-medical-sciences-search |
| category | public-records |
| selectorsIn → selectorsOut | name → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
