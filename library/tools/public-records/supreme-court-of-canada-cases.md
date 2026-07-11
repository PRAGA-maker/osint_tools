---
id: supreme-court-of-canada-cases
name: Supreme Court of Canada - Case Information
description: Use when you have a party `name` and want to check for a Supreme Court of Canada case involving them — returns the docket, parties/counsel (associate), and case summary.
url: https://www.scc-csc.ca/cases-dossiers/search-recherche/
category: public-records
path:
- public-records
bestFor: Searching Canada's top-court docket by party name or case number for parties, counsel, and case status.
selectorsIn:
- name
selectorsOut:
- name
- associate
- document-id
status: live
pricing: free
costNote: Free official Supreme Court of Canada database. Copies of specific court documents may require a records request.
opsec: passive
opsecNote: A public court-records search; parties are not notified. Nothing is sent to the subject. Standard research-browser hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Supreme Court of Canada; the authoritative docket source for that court. (Full judgment texts live on the SCC Judgments / Lexum site.)
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- SCC Case Information
- Supreme Court of Canada case dossier
tags:
- court
- canada
- legal
- case-search
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# Supreme Court of Canada - Case Information

> The official docket search for Canada's top court — find a case by party name or number and read its parties, counsel, and status.

## When to use
You have a `name` and want to know whether that person (or company) has been a party before the Supreme Court of Canada, or you already have a case/file number and want its docket. A case links the subject to opposing parties, lawyers (`associate`/counsel), lower-court history, and a summary of the matter — useful context on litigation, disputes, and networks.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the SCC case-information search.
2. Search by the 5-digit SCC case number, by name/word in the style of cause, or by the lower court's file number.
3. Open a matching file for the docket: parties and counsel, case summary, status, and procedural history.
4. Pivot: opposing parties and counsel are `associate` leads; the style of cause and lower-court file link to appellate records; for the full ruling, read the judgment on the SCC Judgments/Lexum site.

## Inputs → Outputs
- **In:** party `name` (style of cause), SCC case number, or lower-court file number
- **Out:** case `document-id` (file/docket number), parties & counsel (`name`, `associate`), case summary/status, procedural history
- **Empty/negative result looks like:** "no results" — the person has no SCC matter under that spelling (most litigation never reaches this court), or the name differs from the style of cause. Try name variants or the appealed-court file number.

## Gotchas & OpSec
- Coverage is only the Supreme Court of Canada — the vast majority of cases sit in provincial/federal courts (CanLII and provincial court-record systems cover those).
- Style-of-cause names may be abbreviated, initialised (privacy cases), or corporate — search loosely.
- OpSec: passive public-records search; no notification.

## Overlaps ("do both")
- Pairs with CanLII (full-text Canadian decisions across courts) and provincial court-record portals — this covers only the SCC docket; those cover the courts a matter passed through on the way up (or that never reached the SCC).

## Trust & verifiability
`trust: trusted` — first-party Supreme Court of Canada data; the authoritative record of its own docket. For the reasoning/full judgment text, cross to the court's Judgments (Lexum) site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | supreme-court-of-canada-cases |
| category | public-records |
| selectorsIn → selectorsOut | name → name, associate, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
