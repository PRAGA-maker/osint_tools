---
id: usa-gov
name: USA.gov
description: Use as the official gateway to US government services and agencies — a directory/portal to find the right federal/state agency and record system for a lookup, not a people-search itself.
url: https://www.usa.gov/
category: search-engines
path:
- search-engines
bestFor: Finding the correct US government agency, benefit, or records system to pursue an official lookup (vital records, benefits, agency contacts).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free official US government portal; no account.
opsec: passive
opsecNote: Passive — you browse a public government directory, transmitting nothing about a subject. It only points you to agencies; any actual record request happens through the linked agency's own channels.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The US federal government's official web portal (GSA); authoritative as a directory of agencies/services, but it is a signpost, not a records database.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- state-local-tribal-gov-page-search
- us-data-and-statistics
aliases:
- USA.gov
tags:
- toddington
- government
- directory
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# USA.gov

> The US government's official front door — use it to find which agency holds the record you need, then go there.

## When to use
You know an official US record or service could advance a case (vital records, voter/benefit systems, agency contacts, how to request documents) but not which agency or portal to use. USA.gov is the authoritative directory that routes you to the correct federal or state resource. It does not itself return personal records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.usa.gov/.
2. Search or browse topics (e.g. "birth certificate", "voter registration", "find a government agency").
3. Read the output: links to the correct federal/state agency, service, or record-request process.
4. Pivot: follow the link to the agency's own portal and make the actual lookup/request there (e.g. state vital-records office, SoS voter lookup).

## Inputs → Outputs
- **In:** a topic/service question (no personal selector)
- **Out:** authoritative links to the right government agency/service/record system
- **Empty/negative result looks like:** no direct match means the service is state/local — use its state-government finder to drill down.

## Gotchas & OpSec
- **Signpost, not a database** — it points you to record holders; it returns no personal data itself.
- Human-in-the-loop: none here; the linked agency may require forms/ID.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with `[[state-local-tribal-gov-page-search]]` and `[[us-data-and-statistics]]` — USA.gov routes to the agency; those drill into state/local pages and datasets.

## Trust & verifiability
`trust: trusted` — official federal portal; its agency links are authoritative, though the data itself lives at the destination agency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usa-gov |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
