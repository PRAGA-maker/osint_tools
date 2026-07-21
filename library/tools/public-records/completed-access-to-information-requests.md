---
id: completed-access-to-information-requests
name: Completed Access to Information Requests
description: Use when you have a topic, agency, or `name` and want to search summaries of already-completed Canadian federal ATI (freedom-of-information) requests — returns request summaries and `document-id`s you can order copies of.
url: https://open.canada.ca/en/search/ati
category: public-records
path:
- public-records
bestFor: Searching the Government of Canada's index of completed Access to Information request summaries to find records already released (or requestable) across federal institutions.
selectorsIn:
- name
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search summaries; ordering a previously-released package is free or a nominal fee. No payment to run the search.
opsec: passive
opsecNote: Passive — you search a public government portal, not the subject. Ordering a specific released package is logged by the institution but concerns a document, not a live person; use a sock-puppet email if you order and want to stay unattributed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Canada open-data portal; the summaries are authoritative records of processed ATI requests across federal institutions.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- canadian-business-research
- canadian-department-of-finance
- federal-corporation-search-canada
- gov-data-canada
- government-of-canada-open-data
- canadian-intellectual-property-office
- canadian-trademarks-database
- canadian-importers-database
- canadian-copyrights-database
aliases:
- ATI Summaries
- open.canada.ca ATI search
tags:
- public-records
- foia
- canada
- government
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# Completed Access to Information Requests

> The Canadian federal government's searchable index of *already-completed* ATI (freedom-of-information) requests — a shortcut to records someone has already pried loose, which you can then re-order for free.

## When to use
You're investigating something touching a Canadian federal institution — an agency's dealings, a program, or a named entity in government records — and want to see what has already been released under Access to Information. Rather than filing your own slow ATI request, search the summaries of completed ones and re-order any relevant package.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://open.canada.ca/en/search/ati and enter keywords: a topic, program, institution, or `name`.
2. Filter by institution and year to narrow.
3. Read each result's summary — it describes the records the request covered and gives a request/`document-id` number.
4. Use "make an informal request" to order a copy of that already-released package (institutions must re-release previously-disclosed records).
5. Pivot: released packages can contain names, correspondence, contracts and dates that feed the rest of an investigation.

## Inputs → Outputs
- **In:** a topic / institution / `name`
- **Out:** completed-request summaries + `document-id`s (orderable released packages)
- **Empty/negative result looks like:** no matching summaries — no completed ATI request on that topic is indexed (or it predates the index); consider a fresh ATI request or provincial FOI portals.

## Gotchas & OpSec
- Scope is **Canadian federal** institutions only — provinces/municipalities run separate FOI systems.
- Summaries are brief; the useful content is in the ordered package, which can take time to arrive.
- OpSec: passive; searching reveals nothing about your subject.

## Overlaps ("do both")
- Pairs with `[[government-of-canada-open-data]]` and `[[federal-corporation-search-canada]]` — use this to harvest records *already* released before spending weeks filing a new request.

## Trust & verifiability
`trust: trusted` — first-party Government of Canada portal; the summaries and released packages are authoritative primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | completed-access-to-information-requests |
| category | public-records |
| selectorsIn → selectorsOut | name → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
