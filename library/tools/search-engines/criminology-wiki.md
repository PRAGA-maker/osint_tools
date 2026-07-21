---
id: criminology-wiki
name: Criminology Wiki
description: Use when you have a `name` of a crime figure or case and want a crowd-sourced background summary — returns biographical and case details to corroborate elsewhere.
url: https://criminology.fandom.com/wiki/Main_Page
category: search-engines
path:
- search-engines
bestFor: Getting a quick crowd-sourced background sketch of a known criminal, case, or criminological topic as a lead-generation starting point.
selectorsIn:
- name
selectorsOut:
- associate
- name
status: live
pricing: free
costNote: Free Fandom-hosted wiki; ad-supported, no account needed to read.
opsec: passive
opsecNote: Passive reading of a public wiki; no interaction with any subject. Fandom serves ads/trackers, so use a clean browser, but there is no target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A crowd-sourced Fandom wiki with no editorial vetting; treat every claim as a lead to verify against primary sources, never as fact.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wikiaentertainment
- wowwiki-world-of-warcraft-wiki
- itlaw
- familypedia
aliases:
- Criminology Fandom wiki
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Criminology Wiki

> A crowd-sourced Fandom wiki on criminals, cases, and criminology — a fast, low-trust lead generator for background on a named crime figure or case.

## When to use
You have a `name` associated with a notable crime, criminal, or criminological topic and want a quick orientation — a summary of the case, dates, co-offenders/associates, and links to dig into. Useful only as a starting sketch: it points you at names, dates, and events to then confirm against court records, news archives, and primary sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://criminology.fandom.com/ and search the subject name or case.
2. Read the article for biographical details, timeline, `associate`/co-offender names, and locations.
3. Note every specific claim (dates, names, places) as an unverified lead.
4. Pivot: run the harvested names/dates through court-records, news-archive, and authoritative case databases to confirm; discard anything you can't corroborate.

## Inputs → Outputs
- **In:** `name` (person, case, or topic)
- **Out:** background summary, `associate`/co-offender `name`s, dates and locations to verify
- **Empty/negative result looks like:** no article, or a stub with no citations — treat absence as "not covered here," and never treat a thin article as confirmation.

## Gotchas & OpSec
- Zero editorial oversight; articles can be inaccurate, biased, or fabricated. Verify everything.
- Coverage skews toward sensational/notorious cases; ordinary subjects won't appear.
- OpSec: passive read only.

## Overlaps ("do both")
- Complements authoritative case/court-record sources — use this only to generate names and leads, then confirm with primary records.

## Trust & verifiability
`trust: unverified` — crowd-sourced Fandom content with no vetting; strictly a lead source, never evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | criminology-wiki |
| category | search-engines |
| selectorsIn → selectorsOut | name → associate, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
