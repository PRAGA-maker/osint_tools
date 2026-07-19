---
id: brb-public-records
name: BRB Public Records
description: Use when you need to find the authoritative source for a US public record and want to know which agency holds it — returns links and access instructions by record type and jurisdiction.
url: https://www.brbpublications.com/
category: public-records
path:
- public-records
bestFor: A directory that points you to the correct government agency or database for a given US public record by state and record type.
selectorsIn:
- name
- address
selectorsOut:
- address
- document-id
status: live
pricing: freemium
costNote: BRB's Free Public Records Directory of government record-source links is free to browse; its in-depth research guides and the Public Record Retriever Network are paid products.
opsec: passive
opsecNote: You're reading a directory of where records live, not querying any record about the subject, so this step leaks nothing. OpSec considerations apply only when you follow a link to an actual agency search.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: BRB Publications has been a respected authority on public-record sources for decades; its directory is a curated, well-maintained map of official access points.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- public-records
- state-appellate-and-supreme-courts
tags:
- public-records
- directory
- record-sources
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# BRB Public Records

> A veteran directory that answers "where does this US record live?" — mapping record types and jurisdictions to the actual government agency or database that holds them.

## When to use
You know what record you need (a criminal history, a court case, a property deed, a vital record, a business filing) for a US subject but not which office or online portal holds it. BRB's directory points you to the authoritative source and how to access it, so you go straight to the primary record instead of relying on a broker's aggregate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.brbpublications.com/ and open the free public-records directory / resources section.
2. Navigate by jurisdiction (state → county) and/or record category (courts, recorders, criminal, vital records, DMV, business entities, etc.).
3. Read the entry for the source: the responsible agency, its online search URL if any, coverage dates, and access notes (free, fee, in-person, mail).
4. Follow the link to the actual agency/database and run your search there.
5. Pivot: the record you retrieve (address, case number/`document-id`, filing) feeds people-search, court, or property tools.

## Inputs → Outputs
- **In:** a record type + jurisdiction (and the subject's `name`/`address` to search once you reach the source)
- **Out:** the authoritative agency link and access instructions; downstream, the primary record itself (`address`, case/`document-id`)
- **Empty/negative result looks like:** no online source listed for a given county/record type — many US records are still offline or in-person only. That's a routing answer (go in person / mail request), not a dead end.

## Gotchas & OpSec
- It's a pointer, not a search engine: BRB tells you where to look; the actual record search happens on the linked agency site, which may charge or require a visit.
- The richest research guides and the retriever network are paid; the source directory itself is the free, high-value part.
- OpSec: browsing BRB is passive; apply OpSec only when you reach an agency portal that logs searches.

## Overlaps ("do both")
- Pairs with `[[public-records]]` portals and `[[state-appellate-and-supreme-courts]]` — use BRB to find the right source, then those tools/portals to actually pull the record.

## Trust & verifiability
`trust: trusted` — BRB Publications is a long-established, curated authority on public-record sources; its directory reliably routes you to official access points, which are themselves the authoritative record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | brb-public-records |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
