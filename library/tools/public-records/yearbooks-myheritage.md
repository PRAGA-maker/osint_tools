---
id: yearbooks-myheritage
name: Yearbooks - MyHeritage
description: Use when you have a `name` and want an older photo and school context — searches digitized US school yearbooks and returns yearbook images, school, graduation year, and an approximate age.
url: https://www.myheritage.com/research/category-10010/yearbooks
category: public-records
path:
- public-records
bestFor: Finding a historical/school-era photo of a person plus their school and approximate age from digitized yearbooks.
selectorsIn:
- name
selectorsOut:
- image
- name
- employer-org
- dob
status: live
pricing: freemium
costNote: MyHeritage indexes are searchable free (name/school hits), but viewing full yearbook images/records typically requires a paid MyHeritage subscription (free trial available).
opsec: passive
opsecNote: Searching an archival records collection is passive and does not notify the subject. A subscription account ties queries to you — use a research account if separation matters.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: MyHeritage is a major genealogy platform; yearbooks are digitized from real published school yearbooks, so the source images are authentic (indexing/name-matching can err).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- MyHeritage Yearbooks
tags:
- genealogy
- yearbooks
- photos
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Yearbooks - MyHeritage

> A searchable archive of digitized school yearbooks: a name in, an older photo + school + graduation year out — gold for face comparison and age/location anchoring.

## When to use
You have a `name` (US, historical-to-recent school era) and want what modern profiles rarely give: a verified older photograph, the school attended, and an approximate age. A yearbook hit yields a face `image` for reverse-image/face search across a person's life, places them at a school (`employer-org`) in a specific year (implying `dob`), and can surface classmates as `associate` leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.myheritage.com/research/category-10010/yearbooks.
2. Search by `name`; add a state, school, or approximate year to narrow.
3. Review index hits (name, school, year); open a record for the yearbook `image` — full images typically need a subscription (a free trial covers a quick look).
4. Pivot: the photo feeds face/reverse-image search across other sources; the school + graduation year give an approximate `dob` for people-search disambiguation; classmates are `associate` leads.

## Inputs → Outputs
- **In:** `name` (+ state/school/year)
- **Out:** yearbook `image`, `name`, school (`employer-org`), graduation year → approximate `dob`
- **Empty/negative result looks like:** no match — the person's school/year isn't digitized, or the name differs (nicknames, maiden names). Coverage is US-heavy and uneven by school/decade; absence is weak evidence, especially for non-US subjects.

## Gotchas & OpSec
- Paywall: index teases free, full images charge — use a trial or budget a subscription.
- Name matching can miss nicknames/maiden names — try variants and cross-reference the school/year.
- OpSec: **passive**; archival search notifies no one.

## Overlaps ("do both")
- Pairs with Ancestry/Classmates yearbook collections and `[[fold3-us-military-records]]` — different platforms digitized different schools/eras, so a miss on one is worth retrying on another; combine for a fuller photo timeline.

## Trust & verifiability
`trust: trusted` — images come from real published yearbooks, so a confirmed match is strong evidence; verify the index name-match against the actual page (misindexing happens) before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yearbooks-myheritage |
| category | public-records |
| selectorsIn → selectorsOut | name → image, name, employer-org, dob |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
