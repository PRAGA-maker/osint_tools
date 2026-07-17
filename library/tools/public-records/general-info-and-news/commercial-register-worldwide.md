---
id: commercial-register-worldwide
name: Commercial Register — St. Gallen (Switzerland)
description: Use when you have an `employer-org` or `name` tied to a business in canton St. Gallen and want its registration details — returns `address`, `employer-org`, `associate` (officers).
url: https://www.sg.ch/recht/handelsregister-notariate.html
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Confirming a company registered in the Swiss canton of St. Gallen and pulling its legal form, registered address, and listed officers.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- employer-org
- associate
status: live
pricing: free
costNote: Free to search the register online; certified paper extracts (Auszug) cost a fee, but the free search returns the data you need for OSINT.
opsec: passive
opsecNote: A government-registry lookup — no contact with the target company or person. The register is a public record; querying it is not observable by the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official cantonal authority (Handelsregisteramt St. Gallen); the register is the legal source of truth for company records in that canton.
missingPersonsRelevance: medium
coverage:
- ch
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- company-registration-round-the-world
aliases:
- Handelsregister St. Gallen
- Commercial Register Worldwide
tags: []
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Commercial Register — St. Gallen (Switzerland)

> The official commercial register (Handelsregister) for the Swiss canton of St. Gallen — a first-party company-lookup for that jurisdiction, linking businesses to their address and officers.

## When to use
You have a company name (`employer-org`) or a person's `name` believed to be a director/officer of a St. Gallen–registered business, and you want authoritative registration data: legal form, registered street `address`, entry date, and the officers/signatories tied to it. Useful for anchoring a subject to a real, verifiable business address in eastern Switzerland.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the page and follow "Personen- und Firmensuche" (person and company search) — for canton-wide data it routes to the federal Zefix / cantonal register front end.
2. Enter the company name or a person's surname. For a national search, use the federal Zefix portal that this office feeds; for the cantonal record specifically, use the St. Gallen search.
3. Read the entry: legal form (AG, GmbH, Einzelfirma), registered `address`, purpose, and the list of persons with signing authority (`associate`).
4. Pivot: an officer's name feeds people-search; a registered address feeds mapping/records; the SHAB/publication history shows changes over time. For companies outside St. Gallen, jump to `[[company-registration-round-the-world]]`.

## Inputs → Outputs
- **In:** `employer-org` (company name/number) or `name` (officer)
- **Out:** `address` (registered seat), `employer-org` (exact legal name/form), `associate` (directors, signatories)
- **Empty/negative result looks like:** "no entries found" — the company is not registered in this canton (try another cantonal register or the national Zefix), or the spelling/legal form differs.

## Gotchas & OpSec
- Jurisdiction is canton-scoped: a Swiss company registered elsewhere won't appear here — use the national Zefix or the relevant cantonal office.
- The interface is in German; use the field labels above. Certified extracts cost money, but the free online search shows the substantive data.
- OpSec: fully passive public-records query; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with `[[company-registration-round-the-world]]` — that directory routes you to the correct national/cantonal register when the subject's company is outside St. Gallen.

## Trust & verifiability
`trust: trusted` — operated by the cantonal Handelsregisteramt; this is the legally authoritative source for company records in canton St. Gallen, not a third-party aggregator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commercial-register-worldwide |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → address, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
