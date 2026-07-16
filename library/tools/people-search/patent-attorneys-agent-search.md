---
id: patent-attorneys-agent-search
name: Patent Attorneys/Agent Search
description: Use when you have a `name` and suspect they are a US-registered patent attorney or agent — returns confirmation plus their business address and registration document-id.
url: https://oedci.uspto.gov/OEDCI/
category: people-search
path:
- people-search
bestFor: Confirming and locating a US-registered patent practitioner (attorney or agent) by name, and pulling their listed contact info.
selectorsIn:
- name
selectorsOut:
- address
- employer-org
- document-id
status: live
pricing: free
costNote: Free official USPTO Practitioner Finder; no account or payment.
opsec: passive
opsecNote: An official government registry lookup; the practitioner is not notified and the query reveals nothing about you. The listed address is the practitioner's professional/registration address, which is public by design.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the USPTO Office of Enrollment and Discipline; this is the authoritative register of practitioners licensed to practice before the USPTO.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- USPTO OEDCI
- Practitioner Finder
- Patent Practitioner Search
tags:
- expert-search
- legal
- professional-license
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- tess
- us-patent-office-search
---

# Patent Attorneys/Agent Search

> The USPTO's official register of patent practitioners: search a name to confirm someone is a licensed patent attorney or agent and pull their registration details and business contact info.

## When to use
Your subject is (or claims to be) a US patent attorney or agent — a common professional angle when investigating inventors, IP firms, or someone asserting credentials. The OEDCI Practitioner Finder confirms whether the `name` is an active registered practitioner, and returns their registration number and listed professional `address`/firm (`employer-org`), which corroborates identity and gives a real-world location to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://oedci.uspto.gov/OEDCI/ and go to the Practitioner Finder / search.
2. Search by name (and optionally state/registration number) — results cover only active attorneys, agents, and limited-recognition practitioners.
3. Open a matching record for the registration number, practitioner type, and listed contact `address`/firm.
4. For confirming or excluding, note that suspended/excluded/inactive practitioners are omitted from the finder; disciplinary records back to 1997 are searchable in the separate OED disciplinary database.
5. Pivot: the firm/`employer-org` and `address` feed a broader people-search; the registration `document-id` corroborates a credential claim; cross-reference the name against patent filings via `[[us-patent-office-search]]`.

## Inputs → Outputs
- **In:** `name` (optionally state / registration number)
- **Out:** confirmation of active registration, registration number (`document-id`), practitioner type, and listed professional `address` / firm (`employer-org`).
- **Empty/negative result looks like:** no match — the person is not an active registered practitioner (they may be inactive, suspended, excluded, or never registered); check the disciplinary database before concluding "never a practitioner."

## Gotchas & OpSec
- The finder lists only *active* practitioners; absence is not proof someone was never registered — check disciplinary/historical records.
- The listed address is the professional/registration address, which may lag a move or be a firm HQ, not a home.
- US-only; foreign patent professionals are out of scope.

## Overlaps ("do both")
- Pairs with `[[us-patent-office-search]]` and `[[tess]]` — this confirms the practitioner's license and contact, those show the patents/trademarks they've actually filed.

## Trust & verifiability
`trust: trusted` — an authoritative USPTO government registry; registration status and details are official, subject only to the "active-only" listing caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | patent-attorneys-agent-search |
| category | people-search |
| selectorsIn → selectorsOut | name → address, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
