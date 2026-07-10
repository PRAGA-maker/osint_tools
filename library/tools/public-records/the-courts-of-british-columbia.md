---
id: the-courts-of-british-columbia
name: The Courts of British Columbia
description: Use when you have a `name` and want British Columbia court judgments — returns published Court of Appeal/Supreme/Provincial Court decisions naming parties, with case details and dates.
url: https://www.bccourts.ca/search_judgments.aspx
category: public-records
path:
- public-records
bestFor: Finding published British Columbia court judgments/decisions that name a party for legal-history context.
selectorsIn:
- name
selectorsOut:
- name
- document-id
- associate
status: live
pricing: free
costNote: Free official BC courts judgment search; no account or payment. (Note: full case-file/party search — including criminal — lives in the separate Court Services Online (CSO) system, some of which charges per search.)
opsec: passive
opsecNote: An official public-judgments search — you query the courts' published decisions, not the subject, and nobody is notified. Judgments are public records. Use routine sock-puppet browsing hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Courts of British Columbia (Court of Appeal, Supreme Court, Provincial Court); an authoritative first-party source for published BC judgments.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- BC Courts judgment search
- bccourts.ca
tags:
- court
- inmate
- judgments
- british-columbia
- canada
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# The Courts of British Columbia

> The official search for British Columbia's published court judgments — find decisions that name a party, across the Court of Appeal, Supreme and Provincial Courts.

## When to use
You have a `name` and want to know whether the person appears in a published British Columbia court judgment — as a party in a civil, family, or criminal matter — and to read the decision for context. Court judgments expose disputes, relationships, addresses-in-record, and events that can materially advance a missing-person or background investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bccourts.ca/search_judgments.aspx.
2. Search by party `name`, case number, or keyword; filter by court (Court of Appeal / Supreme / Provincial) and date where offered.
3. Open a matching judgment and read it: named parties (subject plus `associate`s — opposing parties, counsel, sometimes family), the case citation (`document-id`), dates, and the facts recited.
4. For the underlying case file / party lists (incl. criminal/traffic and civil by party name), move to BC's Court Services Online (CSO) — some searches there charge a fee.
5. Pivot: co-parties/relationships feed the associate graph; a case citation anchors further legal research (CanLII); recited facts feed timeline/geolocation.

## Inputs → Outputs
- **In:** `name` (party), case number, or keyword
- **Out:** published judgment text naming parties (`name`/`associate`), case citation (`document-id`), court, and dates
- **Empty/negative result looks like:** no matching published judgment — most cases settle or aren't published, and this search covers *published decisions*, not every filing. Absence is weak evidence; check CSO and CanLII too.

## Gotchas & OpSec
- **Published judgments ≠ all cases.** Many matters never produce a published decision; for the full docket/party search use CSO (which may charge and is a different system).
- Some judgments anonymise parties (family/youth matters) — a name may be initials only.
- OpSec: **passive**, authoritative public records; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with CanLII (free Canadian case law), BC Court Services Online (party/docket search), and US/other court locators — published-judgment search, full-docket search, and cross-jurisdiction coverage each catch what the others miss. Do all three for a person with possible BC legal history.

## Trust & verifiability
`trust: trusted` — the official Courts of British Columbia judgment database; decisions are authoritative primary records. Confirm party identity from the judgment text, as names can coincide.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-courts-of-british-columbia |
| category | public-records |
| selectorsIn → selectorsOut | name → name, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
