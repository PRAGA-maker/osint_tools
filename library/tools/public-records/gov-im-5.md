---
id: gov-im-5
name: Isle of Man Planning Applications Search
description: Use when you have an `address` (or `name`/keyword) on the Isle of Man and want planning-application records tied to a property or applicant — returns address, applicant/agent (name/employer-org) and application documents.
url: https://pbc.gov.im/online-applications/
category: public-records
path:
- public-records
bestFor: Searching Isle of Man planning applications and appeals by address, reference or keyword to link a property to applicants/agents.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free public planning register operated by the Isle of Man Government (DEFA); no account or payment to search.
opsec: passive
opsecNote: A public government planning register; searching is passive and the subject is not notified. No login required to search or read application documents.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Isle of Man Government's Department of Environment, Food and Agriculture (pbc.gov.im); authoritative first-party government planning data.
missingPersonsRelevance: high
coverage:
- im
auth: none
api: false
localInstall: false
registration: false
aliases:
- Isle of Man planning search
- pbc.gov.im
tags:
- propertysites
- planning-records
- property-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Isle of Man Planning Applications Search

> The Isle of Man Government's public planning register — search by address, reference or keyword to see who applied to build/alter a property, with the full application documents attached.

## When to use
You have an Isle of Man `address` (or an applicant `name`/keyword) and want to link a property to people: who submitted planning applications, which agents/architects (`employer-org`) acted, and what was proposed. Planning records tie individuals to specific properties and dates, useful for locate work, property/ownership corroboration and timeline building on the Isle of Man.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://pbc.gov.im/online-applications/.
2. Search by keyword, planning reference, postcode, or a single line of an address (appeals use the `AP24/NNNN` format).
3. Open a matching application to read details, status (determined or pending), applicant/agent names, and associated drawings/documents.
4. If document access glitches, retry — the register notes intermittent document issues.
5. Pivot: an applicant name + property address corroborates a person's link to that address and time; agent/architect firms give `employer-org` context; document metadata can add dates and further names.

## Inputs → Outputs
- **In:** `address`/postcode, planning `name`/keyword, or reference number
- **Out:** property `address`, applicant/agent `name` and `employer-org`, application status and documents
- **Empty/negative result looks like:** no matching applications — the property may have no planning history in the register, or your search term is too specific/misspelled. Absence isn't proof of no works.

## Gotchas & OpSec
- Isle of Man only — a small jurisdiction; don't expect UK-mainland properties here (use the relevant local authority planning portal for those).
- Not every property has planning history; a null result is common and weak evidence.
- OpSec: passive, authoritative government data; no subject notification.

## Overlaps ("do both")
- Pairs with UK mainland local-authority planning portals and land-registry tools (`[[e-justice-europa-eu]]` for EU equivalents) — planning records and ownership records together map a person to a property.

## Trust & verifiability
`trust: trusted` — first-party Isle of Man government planning register; applications and documents are the authoritative record. Read the actual application documents rather than relying on the summary line.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-im-5 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
