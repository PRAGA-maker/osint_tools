---
id: canadian-industrial-designs-database
name: Canadian Industrial Designs Database
description: Use when you have a name or company and want registered Canadian industrial designs they own — returns proprietor name and address plus linked design records.
url: https://www.ic.gc.ca/app/opic-cipo/id/bscSrch.do?lang=eng
category: public-records
path:
- public-records
bestFor: Searching Canada's registered industrial designs by proprietor/interested party to tie a person or company to filed design IP.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- address
- employer-org
status: live
pricing: free
costNote: Free official CIPO (Canadian Intellectual Property Office) database; no account required.
opsec: passive
opsecNote: Reads public IP-registry records; the proprietor is not notified. Standard government-site logging only. Use a clean browser for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada (CIPO) register of industrial designs dating to 1861; authoritative for Canadian design filings.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CIPO Industrial Designs
- Canadian Industrial Designs Database
- ic.gc.ca industrial designs
tags:
- public-records
- intellectual-property
- canada
- industrial-designs
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Industrial Designs Database

> CIPO's free, official search of registered Canadian industrial designs — link a person or company to the design IP they've filed, complete with proprietor name and address.

## When to use
You have a `name` or `employer-org` and want to know whether they hold registered industrial designs in Canada. The register lists the proprietor and interested parties with their address, plus the design images and dates — useful for tying an individual/company to a product line, establishing a business footprint, or corroborating an address through a filing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the basic search at https://www.ic.gc.ca/app/opic-cipo/id/bscSrch.do?lang=eng (advanced search offers more fields).
2. Search by proprietor / interested parties (a person or company name); you can also search by classification, description, or application/registration number.
3. Open a matching design record: read the proprietor name and address, the agent, filing/registration dates, and the design images.
4. Pivot: the proprietor address and any co-parties are leads; the company name feeds a corporate-registry search; design dates place business activity on a timeline.

## Inputs → Outputs
- **In:** `name` or `employer-org` (proprietor/interested party)
- **Out:** `name`, `address` (proprietor), `employer-org`, plus design records and dates
- **Empty/negative result looks like:** no registered designs — the person/company simply hasn't filed Canadian industrial designs (most people never do), or the name is spelled differently. Absence is expected, not meaningful, for ordinary individuals.

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — public IP records, no proprietor notification.
- Scope: Canadian **industrial designs** only (product appearance), not patents or trademarks — use CIPO's separate patent/trademark databases for those. Coverage is Canada.

## Overlaps ("do both")
- Pairs with CIPO's patent and trademark databases and corporate registries — this covers design filings, the others cover inventions, brands, and corporate structure for the same subject.

## Trust & verifiability
`trust: trusted` — it is the official Government of Canada register; records are authoritative and verifiable by their application/registration number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-industrial-designs-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
