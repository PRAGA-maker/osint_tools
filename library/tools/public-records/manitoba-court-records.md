---
id: manitoba-court-records
name: Manitoba Court Records (name search)
description: Use when you have a `name` and want to check for court cases involving them in Manitoba, Canada — returns matching cases, file numbers, and parties/counsel.
url: https://web43.gov.mb.ca/registry/namesearch
category: public-records
path:
- public-records
bestFor: Searching Manitoba court files (family, criminal, civil, probate, bankruptcy) by a person's or company's name.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free name search of the Manitoba Courts registry. Ordering copies of the actual court documents may carry a fee.
opsec: passive
opsecNote: A public court-records search; parties are not notified and nothing is sent to them. Standard research-browser hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Government of Manitoba / Manitoba Courts; the authoritative index of that province's court files.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- Manitoba Courts registry search
- Manitoba name search
tags:
- court
- canada
- manitoba
- legal
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Manitoba Court Records (name search)

> The Manitoba Courts registry name search — look up a person or company across the province's court files (family, criminal, civil, probate, bankruptcy).

## When to use
You have a `name` and want to know whether that person (or business) appears in Manitoba court proceedings. Court files reveal disputes, criminal matters, family/probate proceedings, and — crucially for network mapping — the other parties, lawyers, and law firms tied to a case (`associate` links). Useful for background, locating litigation, or corroborating a person's presence in the province.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Manitoba registry name search (web43.gov.mb.ca/registry/namesearch).
2. Search by surname (or company name), optionally with a given name, lawyer/firm name, and a registration date range; choose a court division or "All Divisions."
3. Review matching case entries and open a file for its `document-id`/case number, division, and associated parties/counsel.
4. Pivot: opposing parties and counsel are `associate` leads; the file number lets you request the full record; the division/date frames the matter.

## Inputs → Outputs
- **In:** `name` (surname/company, optional given name, lawyer/firm, date range)
- **Out:** matching cases, case `document-id`/file numbers, court division, parties & counsel (`name`, `associate`)
- **Empty/negative result looks like:** no matches — the person has no Manitoba court file under that spelling, or your date range excluded it. Try name variants and "All Divisions"; absence isn't proof of no record elsewhere in Canada.

## Gotchas & OpSec
- Province-scoped: covers Manitoba only — other provinces have their own portals; CanLII covers reported *decisions* nationally (not the same as the docket index).
- Common names return many hits; narrow with given name, division, or date range.
- OpSec: passive public-records lookup; no notification.

## Overlaps ("do both")
- Pairs with CanLII (national case-law) and other provincial court registries — this indexes Manitoba filings; CanLII gives full judgment texts; sister-province portals extend coverage when you don't know the jurisdiction.

## Trust & verifiability
`trust: trusted` — first-party Manitoba Courts data; authoritative for that province's court index. Confirm you have the right individual (common names) before drawing conclusions, and pull the actual file for detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manitoba-court-records |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
