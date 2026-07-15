---
id: securities-administrators-ca
name: CSA National Registration Search (securities-administrators.ca)
description: Use when you have a person's or firm's `name`/`employer-org` and want to check whether they are registered to sell securities or give investment advice in Canada — returns name, employer-org, address, document-id.
url: https://info.securities-administrators.ca/nrsmobile/nrssearch.aspx
category: public-records
path:
- public-records
bestFor: Verifying whether an individual or firm is a registered securities dealer/adviser in any Canadian jurisdiction, and in what categories.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- address
- document-id
status: live
pricing: free
costNote: Free official tool run by the Canadian Securities Administrators; no account needed.
opsec: passive
opsecNote: Querying the public regulator database is passive and does not alert the person or firm searched. No login required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Canadian Securities Administrators (CSA) National Registration Search — the authoritative, multi-jurisdiction source for whether someone is registered to deal in or advise on securities in Canada.
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- National Registration Search
- NRS
- CSA Are They Registered
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# CSA National Registration Search (securities-administrators.ca)

> The Canadian Securities Administrators' authoritative registry: is this person or firm actually registered to sell securities or give investment advice in Canada — and in what categories, with what conditions?

## When to use
You have a `name` (individual) or `employer-org` (firm) presenting as a financial adviser, dealer, or investment firm in Canada and you need to confirm their registration status — a core check when vetting a subject's professional claims, investigating fraud, or corroborating an employer. Registration also ties an individual to the firm(s) they operate under and the jurisdictions they're authorised in.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the National Registration Search at info.securities-administrators.ca.
2. Search by individual `name` or firm `employer-org`.
3. Read the result: registration status, the firm(s) the individual is registered with, registration categories (e.g. dealing representative, adviser), the jurisdictions/provinces, and any terms or conditions on the registration.
4. Pivot: the associated firm becomes an `employer-org` lead; the firm's address is a `geolocation`; a "not registered" result is itself a strong red flag to escalate.

## Inputs → Outputs
- **In:** `name` (individual) or `employer-org` (firm)
- **Out:** registration status, `employer-org` (sponsoring firm), `name`, firm `address`, registration categories/jurisdictions, `document-id` (registration reference), any terms/conditions
- **Empty/negative result looks like:** "not registered" / no match — a meaningful finding (the person/firm is not authorised in the searched category), not merely a null; confirm spelling and check related name variants first.

## Gotchas & OpSec
- Covers registration under securities law only — many finance-adjacent roles (mortgage brokers, insurance) are registered elsewhere.
- Some IIROC/CIRO-regulated individuals may need the CIRO advisor report for full disciplinary history; cross-check.
- OpSec: passive; an official public tool, so no trace to the subject.

## Overlaps ("do both")
- Pairs with provincial regulator registrant searches (OSC, BCSC) and the CIRO advisor report — NRS gives the national registration snapshot, while those add disciplinary detail.

## Trust & verifiability
`trust: trusted` — the first-party CSA registry; the registration status is authoritative for Canadian securities law.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | securities-administrators-ca |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, address, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
