---
id: national-archives-and-records
name: National Archives and Records (NARA)
description: Use when you have a `name` or `employer-org` tied to US federal history and want archived government records — returns document records (`document-id`) that can yield `address` and affiliation details.
url: http://www.archives.gov/research/search/index.html
category: public-records
path:
- public-records
bestFor: Searching the US National Archives Catalog for federal records — military, immigration, census, and agency documents — about a person or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- address
status: live
pricing: free
costNote: Free to search the online National Archives Catalog; some records are digitized and viewable online, others require an on-site or written request to obtain.
opsec: passive
opsecNote: Searching a public government archive reveals nothing about your subject and alerts no one. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US government archive (National Archives and Records Administration); records are primary-source and authoritative, though indexing/digitization is uneven.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- access-to-archival-databases
- archives-library-information-center-alic
aliases:
- NARA
- National Archives Catalog
- archives.gov
tags:
- toddington
- curated-directory
- specialty-search
- government-records
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# National Archives and Records (NARA)

> The search front-end to the US National Archives — the authoritative store of federal records (military service, immigration, census, agency files) about people and organizations.

## When to use
You have a `name` or an `employer-org`/agency connected to US federal history and want primary-source documents about them: military service and pension files, immigration and naturalization records, census schedules, and records of federal agencies. Especially useful for older/historical subjects, veterans, immigrants, and anyone with a federal footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the National Archives Catalog (from archives.gov/research; the modern catalog is at catalog.archives.gov).
2. Search by `name`, organization, or keyword; filter by record group, type, date and location.
3. Open a matching record's description.
4. Read the output: the archival description (`document-id`), any digitized images, and details that may include residence/service `address`, dates and affiliations.
5. Pivot: request non-digitized records via the listed access path; take names/addresses/dates into genealogy and vital-records tools.

## Inputs → Outputs
- **In:** `name` or `employer-org` (person, unit, or agency)
- **Out:** `document-id` (archival record descriptions/scans), `address` and affiliation details within records
- **Empty/negative result looks like:** no catalog match, or a description with no digitized image — the record may exist only on paper and require a formal request, or simply not be indexed online.

## Gotchas & OpSec
- Much of the collection is described but NOT digitized — a catalog hit often means "request this in person or by mail," not "read it now."
- Strongest for historical/federal matters; it is not a modern people-finder.
- Indexing quality varies by record group; try name variants and record-group browsing.
- OpSec: passive; searching a public archive signals nothing.

## Overlaps ("do both")
- Pairs with `[[access-to-archival-databases]]` and `[[archives-library-information-center-alic]]` — do both; AAD queries structured federal datasets while the main catalog covers described holdings, and each surfaces records the other doesn't.

## Trust & verifiability
`trust: trusted` — the official US federal archive. Records are authoritative primary sources; the main caveat is coverage/digitization gaps, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-archives-and-records |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
