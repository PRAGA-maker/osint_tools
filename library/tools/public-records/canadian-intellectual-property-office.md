---
id: canadian-intellectual-property-office
name: Canadian Intellectual Property Office (CIPO)
description: Use when you have a `name` or `employer-org` and want their Canadian patents/trademarks — returns filing `document-id`s, owner/inventor `name`s and `address`es.
url: https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en
category: public-records
path:
- public-records
bestFor: Searching Canada's official patent, trademark, copyright and industrial-design registers by owner/inventor name.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- address
status: live
pricing: free
costNote: Free public search of the Canadian Patents, Trademarks, Copyright and Industrial Design databases; no account. (Formal certified copies cost money; searching does not.)
opsec: passive
opsecNote: You query official government IP registers; the applicant/owner is not contacted and the records are public. Standard web hygiene applies for sensitive queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by CIPO (part of Innovation, Science and Economic Development Canada); the authoritative primary source for Canadian IP records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-patent-search
- canadian-business-research
- canadian-department-of-finance
- completed-access-to-information-requests
- federal-corporation-search-canada
- gov-data-canada
- government-of-canada-open-data
- canadian-trademarks-database
- canadian-importers-database
aliases:
- CIPO
- Canadian Patents Database
- Canadian Trademarks Database
tags:
- patent-records
- trademark-records
- public-records
- canada
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Canadian Intellectual Property Office (CIPO)

> Canada's official IP registry — free public search of patents, trademarks, copyrights and industrial designs, tying a `name` or company to their Canadian filings, owners and addresses of record.

## When to use
You have a `name` or company (`employer-org`) with a possible Canadian innovation/branding footprint and want the official record. Canadian patent and trademark filings publicly list inventors/applicants, owners/agents, and often an `address` of record, plus filing dates and status. This corroborates business activity, ties a person to companies and collaborators, and can surface a current mailing address — useful for due diligence and for locating people connected to Canadian businesses or inventions.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the CIPO hub (ised-isde.canada.ca) and open "Search intellectual property databases."
2. Pick the register: **Canadian Patents Database** (search by inventor/applicant/owner `name` or keyword) or **Canadian Trademarks Database** (search by owner name or mark).
3. Open a record: read inventor/applicant/owner `name`(s), agent, `address` of record, filing/registration dates and legal status.
4. Follow trademark owners and patent assignees to their other filings to build a picture of the entity.
5. Pivot: take owner `employer-org` into corporate registries, addresses into address lookups, and inventor names into `[[google-patent-search]]` for worldwide coverage.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** filing `document-id`s (patent/TM numbers), inventor/owner `name`s, `address` of record, status/dates
- **Empty/negative result looks like:** no filings — the person/company has no Canadian IP (common), filed under a variant/agent name, or holds rights via a subsidiary. Absence isn't proof of no business activity.

## Gotchas & OpSec
- OpSec: **passive** — official public registers; nothing reaches the subject.
- Canada-only; for other countries use the respective national office or the WIPO/Google aggregators.
- The CIPO site moved to the ised-isde.canada.ca domain — old ic.gc.ca links redirect here.

## Overlaps ("do both")
- Pairs with `[[google-patent-search]]` (worldwide patents) and WIPO Global Brand Database (worldwide trademarks) — CIPO is authoritative for Canada; the aggregators give international breadth.

## Trust & verifiability
`trust: trusted` — a first-party Canadian government registry; every result is an official public record you can cite directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-intellectual-property-office |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
