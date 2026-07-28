---
id: pic-cic-code-database
name: PIC/CIC Code Database
description: Use when you have a 4-digit North American Carrier Identification Code (PIC/CIC) from a phone record and want the carrier behind it — returns the telecom operator and its location.
url: https://www.allredtech.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Looking up a 4-digit PIC/CIC (Carrier Identification Code) to the long-distance carrier and location it belongs to.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- geolocation
status: live
pricing: free
costNote: Free searchable database (Allred Tech); no account. Updated daily.
opsec: passive
opsecNote: A reference-table lookup against Allred Tech's public database — no target infrastructure is touched and no subject is alerted. Standard third-party site logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing niche telecom reference billed as the most complete CIC database; useful for a specialised lookup, verify against the NANPA/telecom source if decisive.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Allred Tech
- Carrier Identification Code database
- CIC lookup
tags:
- telecom
- carrier-codes
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# PIC/CIC Code Database

> A niche telecom reference: turn a 4-digit Carrier Identification Code into the long-distance carrier it identifies — for making sense of phone bills and call records.

## When to use
Specialised and low-relevance. Reach for it when a phone bill, call detail record, or telecom document contains a 4-digit **PIC/CIC** (Carrier Identification Code, the digits after `101x` used to force a long-distance carrier) and you need to know which carrier — and where — that code belongs to. It attributes the code to an operator (a `employer-org`-style entity) and its jurisdiction; it is not a people-search tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.allredtech.com/.
2. Search by the 4-digit CIC, or filter/browse by company name, state/province, country, or postal code.
3. Read the result: the carrier that owns the code, plus its location details.
4. Pivot: knowing the carrier tells you who to approach for records (via proper legal process) and which network a call traversed.

## Inputs → Outputs
- **In:** a 4-digit PIC/CIC code (a telecom `document-id`)
- **Out:** the carrier/company (`employer-org`) and its `geolocation` (state/country)
- **Empty/negative result looks like:** no match for a code that's unassigned, reclaimed, or outside the North American numbering plan — absence means "not in this CIC registry."

## Gotchas & OpSec
- Very domain-specific — only meaningful when you actually have a CIC/PIC code from telecom records.
- Codes get reassigned over time; a current match may not reflect the carrier at the time of an old record — note the date.
- OpSec: **passive**, nothing reaches any subject.

## Overlaps ("do both")
- Use alongside general phone-number OSINT and carrier-lookup tools: those identify the carrier for a *phone number*, while this decodes the *CIC code* embedded in call/billing records.

## Trust & verifiability
`trust: community` — a long-standing specialist database that bills itself as the most complete CIC reference and updates daily. Reliable within its niche; for a decisive attribution, confirm against the authoritative telecom/NANPA source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pic-cic-code-database |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | document-id → employer-org, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
