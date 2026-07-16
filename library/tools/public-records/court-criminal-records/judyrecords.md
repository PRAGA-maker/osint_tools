---
id: judyrecords
name: judyrecords
description: Use when you have a `name` and want free nationwide US court-case records — returns case filings, parties (associates), and document-id leads across 700M+ cases.
url: https://www.judyrecords.com/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free full-text search of 700M+ US court cases by party name to find litigation, filings, and connected parties.
selectorsIn:
- name
selectorsOut:
- document-id
- associate
- address
status: live
pricing: free
costNote: Free unlimited court-case search across US jurisdictions; no account required. Funded without paywalling searches.
opsec: passive
opsecNote: Court records are public; searching does not notify anyone and nothing is revealed about you. Note the subject's involvement in a case (victim, witness, party) may be sensitive — handle results discreetly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates real US court records from many jurisdictions; coverage and freshness vary by court, and indexing gaps mean absence is not proof of no record.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- judyrecords.com
- judy records
tags:
- court-records
- legal
- criminal-records
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# judyrecords

> A free, fast search across 700M+ US court cases: enter a name and find every indexed case where that person appears as a party, with links to filings and connected people.

## When to use
A high-value people-finding tool for US subjects. Search a `name` to surface civil, criminal, family, probate, and other court cases involving them — litigation, divorces, evictions, judgments, criminal matters. Case records name the other parties (`associate`s: spouses, co-defendants, plaintiffs), sometimes list addresses, and provide official case `document-id`s. In a missing-persons context, court filings can reveal family relationships, disputes, last-known addresses, and legal representatives to contact.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.judyrecords.com/.
2. Search the person's full name (use quotes for exact matching; add a middle name or jurisdiction to narrow common names).
3. Review the hit list; open a case to see the parties, court, case number, filing dates, and available document text.
4. Use its advanced/boolean search to combine name with location or case type.
5. Pivot: co-parties → `associate`s to trace; attorney names → contacts; case number/court (`document-id`) → the county court's own portal for full docket/PDFs; addresses in filings → mapping/people-search.

## Inputs → Outputs
- **In:** `name` (optionally jurisdiction/case-type filters)
- **Out:** matching court cases (`document-id`), the other `associate` parties, and occasionally an `address` from filings.
- **Empty/negative result looks like:** no cases for the name — the person has no indexed court record, OR their jurisdiction isn't covered; confirm on the relevant county/state portal before concluding "no record."

## Gotchas & OpSec
- Coverage is broad but not complete — some courts/states index poorly or not at all; absence ≠ no record.
- Common-name collisions are frequent; verify the specific person via middle name, jurisdiction, or case details.
- Data freshness varies by court; recent filings may lag.
- Treat sensitive case involvement (victim/minor/witness) with care and per applicable law.

## Overlaps ("do both")
- Pairs with `[[unicourt]]`/PACER and state court portals — judyrecords is fastest for a free nationwide name sweep; those give authoritative full dockets and documents for a specific case.

## Trust & verifiability
`trust: community` — it indexes genuine public court records, so hits are real, but coverage gaps and name ambiguity mean you should confirm any specific case on the originating court's official system before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | judyrecords |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id, associate, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
