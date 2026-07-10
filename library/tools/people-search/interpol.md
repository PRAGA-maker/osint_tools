---
id: interpol
name: INTERPOL Notices
description: Use when you have a `name` and want to check INTERPOL's public Red (wanted) and Yellow (missing persons) notices — returns name, dob, image, physical-description and notice document-id.
url: http://www.interpol.int
category: people-search
path:
- people-search
bestFor: Searching INTERPOL's public notices — Yellow Notices for missing persons and Red Notices for internationally wanted persons — by name/nationality.
selectorsIn:
- name
selectorsOut:
- name
- dob
- image
- physical-description
- document-id
status: live
pricing: free
costNote: Free public search of the notices INTERPOL chooses to publish; no account or payment.
opsec: passive
opsecNote: Searching the public notices database does not contact the subject — passive. The data is officially published by INTERPOL/member countries; standard web-server logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official INTERPOL website; published notices are authoritative, issued via member countries' law-enforcement — though only a subset of notices are made public.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Interpol
- INTERPOL Red Notices
- INTERPOL Yellow Notices
tags:
- people-search
- missing-persons
- law-enforcement
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# INTERPOL Notices

> INTERPOL's public notices database — directly relevant to missing-persons work via **Yellow Notices** (missing persons) and **Red Notices** (internationally wanted), searchable by name and nationality.

## When to use
You have a `name` and want to check whether the person is the subject of an international law-enforcement notice: a **Yellow Notice** (a missing person, often a strong direct hit for this domain), a **Red Notice** (wanted internationally), or others. Published notices carry a photo (`image`), date of birth (`dob`), physical description, nationality and a notice number (`document-id`) — high-quality, authoritative identity data for confirming or locating a subject across borders.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to interpol.int and open the public notices section (View Red Notices / Yellow Notices / etc.).
2. Search by `name`, and filter by nationality/age where offered.
3. Open a matching notice: full name and aliases, `dob`, nationality, `physical-description`, photo (`image`), and the notice number (`document-id`).
4. For a missing person, the Yellow Notice may include distinguishing marks and circumstances; for a wanted person, the Red Notice lists the charges and requesting country.
5. Pivot: the photo feeds reverse-image/face search; aliases feed name/username searches; nationality + DOB anchor identity in national records.

## Inputs → Outputs
- **In:** `name` (optionally nationality/age)
- **Out:** `name` (+ aliases), `dob`, `image` (photo), `physical-description`, `document-id` (notice number)
- **Empty/negative result looks like:** no matching notice — meaning no *public* INTERPOL notice under that name; most people have none, and many notices are not published, so absence says little.

## Gotchas & OpSec
- **Only public notices are searchable** — a large share of INTERPOL notices are restricted and won't appear; absence is not exoneration or proof of no case.
- Names/aliases vary across scripts and transliterations; try variants.
- OpSec: fully passive over officially published data.

## Overlaps ("do both")
- Pairs with national missing-persons databases and wanted-persons registries (FBI, national police) — INTERPOL is the cross-border layer; combine with the relevant country's own databases for coverage.

## Trust & verifiability
`trust: trusted` — official INTERPOL data issued via member states; published notices are authoritative, with the caveat that the public set is only a subset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | interpol |
| category | people-search |
| selectorsIn → selectorsOut | name → name, dob, image, physical-description, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
