---
id: the-tribal-court-clearinghouse
name: The Tribal Court Clearinghouse
description: Use when a case touches a US tribal jurisdiction and you need to identify the right tribal court and its records/contacts — a reference portal that routes you to tribal, state and federal justice resources.
url: http://www.tribal-institute.org/index.htm
category: public-records
path:
- public-records
bestFor: Identifying the correct Native American / Alaska Native tribal court and jurisdiction, and the resources/contacts to request its records.
selectorsIn:
- name
- address
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public resource operated by the Tribal Law and Policy Institute; no account or payment.
opsec: passive
opsecNote: Browsing the clearinghouse and its resource links is passive and anonymous. Any subsequent records request to a specific tribal court is a separate, potentially attributable action governed by that court's own rules.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Tribal Law and Policy Institute since 1997; an established, authoritative clearinghouse for tribal-justice information — though it is a reference hub, not a searchable case database.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Tribal Law and Policy Institute
- tribal-institute.org
tags:
- court
- inmate
- tribal-court
- us
- reference
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# The Tribal Court Clearinghouse

> A reference portal for the US tribal-justice system — not a records search, but the map that tells you *which* tribal court has jurisdiction and how to reach its records.

## When to use
Your case involves someone connected to a Native American or Alaska Native nation, and standard state/county court and inmate searches come up empty because the matter sits in tribal jurisdiction. Tribal courts operate outside the state systems most people-search tools cover, so this clearinghouse is how you find the right court, understand its structure, and locate the contacts and resources to request records — a genuine blind spot in US public-records OSINT.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.tribal-institute.org/ and browse the resource areas (tribal courts, tribal law, VAWA, publications, links to nations and agencies).
2. Identify the tribe/nation relevant to your subject and follow the links to that nation's justice system and court contacts.
3. Use the aggregated law, policy and directory resources to determine jurisdiction and the correct venue.
4. Pivot: with the right court identified, submit a records request to that court (its own process/`manual-review`), and combine with federal/state searches for cases that cross jurisdictions.

## Inputs → Outputs
- **In:** `name` / `address` (used to determine the relevant nation/jurisdiction)
- **Out:** the correct tribal court/jurisdiction and routes to its records (`document-id` reachable via that court, not this site)
- **Empty/negative result looks like:** the portal is reference material — it never returns a person's record directly. "Nothing here" means you must go to the identified tribal court itself; don't mistake the clearinghouse's lack of a case result for the absence of a record.

## Gotchas & OpSec
- **Portal, not a database:** it aggregates knowledge, publications and links; individual case/inmate records live with each tribal court, many of which are not online.
- Requesting records from a tribal court follows that court's own rules and review (`manual-review`) and may not be public at all.
- OpSec: browsing is passive; downstream records requests are attributable.

## Overlaps ("do both")
- Pairs with federal (PACER/BOP) and state court/inmate searches — tribal matters can also surface in federal court, so run both once the clearinghouse tells you which nation and venue are involved.

## Trust & verifiability
`trust: trusted` — an authoritative, long-standing institute resource for tribal justice. The routing and legal information are reliable; the actual records still require verification at the specific tribal court it points you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-tribal-court-clearinghouse |
| category | public-records |
| selectorsIn → selectorsOut | name, address → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
