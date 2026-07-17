---
id: caselaw-access-project
name: Caselaw Access Project
description: Use when you have a `name` and want to find US court opinions that mention the person — returns case `document-id`, court/date, and `associate` parties.
url: https://case.law/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Full-text searching 360 years of digitized US published court opinions for a person's name.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
- name
status: live
pricing: free
costNote: Fully free and open. As of 2024 all use restrictions were lifted; the complete dataset (6.9M cases) is downloadable in bulk and via free viewers with no account.
opsec: passive
opsecNote: You search a static public archive of historical court opinions; the subject is never contacted and there is nothing for them to see. No login means no query trail tied to you beyond the host's server logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Digitized by Harvard Law School Library's Library Innovation Lab from official reporters; a primary, authoritative legal source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CAP
- case.law
- Harvard Caselaw Access Project
tags:
- court-records
- legal
- public-records
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Caselaw Access Project

> Harvard's free, complete archive of digitized US published court opinions (state and federal, 1658–2020) — a full-text haystack in which a person's name can surface litigation, addresses of record and named associates.

## When to use
You have a `name` and want to know whether that person appears in any US published court decision — as a party, witness, attorney or subject. Court opinions often anchor a person to a place, a date, a dispute and other named people (co-parties, family in probate/divorce, business partners in commercial suits). CAP covers ~6.9 million cases spanning 360 years, so it is strongest for historical and appellate records rather than fresh trial-court filings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://case.law/ and open the search/browse interface (the data also lives on static.case.law for bulk download and is mirrored on Hugging Face/Kaggle).
2. Search the person's `name` as an exact phrase; add a state to scope to a jurisdiction's reporters.
3. Open a matching opinion and read the caption and body: the caption gives the case `document-id` (citation), court and date; the body names parties and often `associate`s.
4. Note that coverage runs through **2020** and only **published** opinions — routine trial-court matters and anything after digitisation ended will not appear.
5. Pivot: take the court, date and county to that jurisdiction's live docket system (e.g. PACER for federal) for the full modern file, and feed named `associate`s into people search.

## Inputs → Outputs
- **In:** `name`
- **Out:** case `document-id` (citation), court/date, `associate` and other party `name`s
- **Empty/negative result looks like:** zero hits — meaning the person never appeared in a *published* opinion (most people never do), not that they have no court history. Absence here is weak evidence.

## Gotchas & OpSec
- OpSec: **passive** — a static historical archive; nothing reaches the subject.
- Coverage boundary: published opinions only, through 2020. It is not a criminal-background or current-docket tool.
- Common names produce many false matches; confirm identity from facts in the opinion (place, dates, related names).

## Overlaps ("do both")
- Pairs with live court-docket and criminal-records tools — CAP gives the historical, full-text appellate record; those give current filings and case status.

## Trust & verifiability
`trust: trusted` — sourced from official case reporters and digitised by Harvard; each hit is a citable primary document you can verify against the reporter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | caselaw-access-project |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, associate, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
