---
id: lawyers-com
name: Lawyers.com
description: Use when you have a name (of an attorney) or a location + practice area and want a professional profile — returns employer-org (firm), address, phone and practice details drawn largely from state-bar records.
url: https://www.lawyers.com/
category: search-engines
path:
- search-engines
bestFor: Locating and profiling a US/Canada attorney by name, firm, or practice area.
selectorsIn:
- name
- address
selectorsOut:
- employer-org
- address
- phone
- physical-description
status: live
pricing: free
costNote: Free to search and to view attorney profiles; profiles are free listings partly auto-built from bar records. Attorneys pay to enhance their listing, but consumer search costs nothing.
opsec: passive
opsecNote: A public consumer directory; searching is anonymous browsing and does not notify the attorney. No login needed. Standard web hygiene (clean IP/browser) is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of Internet Brands' Martindale legal-marketing network (Martindale.com, Avvo, Nolo). Baseline data derives from state-bar records so it is reasonably reliable, but enhanced profiles are self-authored marketing.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- lawyers.com
- Martindale Lawyers.com
tags:
- toddington
- curated-directory
- legal
- professional-directory
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Lawyers.com

> Consumer-facing attorney directory in the Martindale-Hubbell network — profiles for over a million US lawyers, mostly seeded from state-bar records.

## When to use
Your subject is (or may be) a licensed attorney, or you have a `name` and want to confirm a legal profession and locate them. Lawyers.com resolves a name into a professional profile: the firm they work for (`employer-org`), office `address` and `phone`, practice areas, bar admissions, and often a photo (`physical-description`). It is also useful in reverse — to identify legal counsel connected to a case or a person of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lawyers.com/ and use "Find a Lawyer".
2. Search by attorney `name`, or by `address`/city + practice area if you only know location.
3. Open the matching profile: read firm, office address and phone, practice areas, jurisdictions of admission, education, and any peer/client ratings.
4. Cross-check the name + jurisdiction against the relevant state-bar "attorney lookup" for the authoritative licence status — the directory can lag on suspensions or moves.
5. Pivot: the firm (`employer-org`) and office address feed corporate/people-search tooling; the sibling network sites (Martindale, Avvo) may carry additional detail.

## Inputs → Outputs
- **In:** `name` (attorney) or `address`/location + practice area.
- **Out:** `employer-org` (firm), office `address`, `phone`, practice areas, bar admissions, photo (`physical-description`).
- **Empty/negative result looks like:** no matching profile — common for attorneys who have not claimed/enhanced a listing, are recently admitted, or practise outside the US. Absence here is not proof someone isn't a lawyer; confirm via the state bar.

## Gotchas & OpSec
- Human-in-the-loop: none — open consumer search, no CAPTCHA or login in normal use.
- OpSec: **passive** — anonymous browsing of a public directory; the attorney is not notified.
- Data quality is mixed: bar-sourced fields are trustworthy, but enhanced-profile content is self-written marketing and ratings can be paid-influenced. Treat the state bar as the source of truth for licence status.

## Overlaps ("do both")
- Pairs with state-bar attorney-lookup pages and other professional directories — Lawyers.com gives a rich marketing profile (photo, practice, firm), while the bar gives authoritative licence/discipline status; use both.

## Trust & verifiability
`trust: community` — a large, established directory in the Martindale/Internet Brands network. Baseline records come from state bars (reliable); enhanced profiles are self-authored, so verify anything decision-critical against the official bar record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lawyers-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, address → employer-org, address, phone, physical-description |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
