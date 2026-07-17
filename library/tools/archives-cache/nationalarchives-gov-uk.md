---
id: nationalarchives-gov-uk
name: UK Government Web Archive (nationalarchives.gov.uk)
description: Use when you have a UK government `domain`/URL and want archived snapshots of it — returns historical page captures and `document-id` references.
url: https://www.nationalarchives.gov.uk/webarchive/
category: archives-cache
path:
- archives-cache
bestFor: Retrieving historical snapshots of UK central-government and public-body websites, including pages since removed.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public service of The National Archives (UK); no account needed.
opsec: passive
opsecNote: You browse an official archive of already-published government pages; nothing reaches any subject and there is no query trail beyond the host's logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by The National Archives, the UK government's official archive; captures are authoritative primary records of what government sites published.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- UK Government Web Archive
- nationalarchives.gov.uk webarchive
- TNA web archive
tags:
- archive
- Archive & Cached Related Sites
- uk-government
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# UK Government Web Archive (nationalarchives.gov.uk)

> The UK government's official web archive — a Wayback-style capture of gov.uk and public-body sites, the place to recover an official page that has since been changed or deleted.

## When to use
You have a UK government or public-body `domain`/URL (a department, agency, NHS trust, council, quango) and need a *past* version of a page — a since-removed guidance document, an old staff/contact listing, a policy as it stood on a date, or a deleted press release. Because government sites are regularly restructured and pages disappear, this archive is often the only way to cite what a public body published at a given time. Strong for provenance and timeline work on official UK sources; weaker as a people-locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nationalarchives.gov.uk/webarchive/.
2. Enter the target gov URL or browse by department/organisation.
3. Pick a capture date; open the archived snapshot and read the page as it appeared then.
4. Note the archived URL and capture date as your citation (`document-id`) for the historical record.
5. Pivot: if the UK archive lacks a capture, cross-check the Internet Archive Wayback Machine; use recovered old contact/staff pages as leads.

## Inputs → Outputs
- **In:** `domain`/URL (a UK government or public-body site)
- **Out:** archived page snapshots with capture dates; a citable `document-id` (archived URL + timestamp)
- **Empty/negative result looks like:** no captures for that URL — the page was never crawled, or it's a non-UK-government site outside this archive's remit. Try the general Wayback Machine instead.

## Gotchas & OpSec
- OpSec: **passive** — official archive of public pages; nothing reaches a subject.
- Scope is UK central government and public bodies; general/commercial sites are out of remit (use the Internet Archive).
- Capture frequency varies; the exact date you need may not have been crawled — pick the nearest snapshot and note the gap.

## Overlaps ("do both")
- Pairs with the Internet Archive Wayback Machine — the UK archive is authoritative for gov.uk; Wayback has broader (but unofficial) coverage.

## Trust & verifiability
`trust: trusted` — an official government archive; snapshots are authoritative primary records of what a public body published, citable by archived URL and date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nationalarchives-gov-uk |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
