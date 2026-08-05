---
id: listify
name: Listify
description: Use when you have case data in a Google Sheet and want a fast searchable web listing of it — returns a formatted, filterable page from your spreadsheet (a presentation utility, no selectors).
url: http://listify.okfnlabs.org
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a Google Spreadsheet of records into a searchable, shareable web listing in seconds.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free tool from Open Knowledge Foundation Labs; you supply your own Google Sheet.
opsec: passive
opsecNote: Listify renders a listing from a Google Sheet you control. Anything you publish/embed becomes web-accessible, so never Listify sensitive case data you don't intend to expose. It is a presentation layer for data you already hold — no target is contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by the Open Knowledge Foundation; a simple, transparent spreadsheet-to-listing converter, not a data source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OKFN Listify
- listify.okfnlabs.org
tags:
- infographics-and-data-visualization
- data-presentation
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Listify

> An Open Knowledge Foundation utility that turns a Google Sheet into a searchable, filterable web listing — a way to make your own collected records browsable, not a lookup service.

## When to use
This is an organize-and-present tool, not an investigative source. Reach for it when you have already gathered structured records into a Google Sheet — a roster of leads, a catalog of profiles, a list of properties — and you want a quick searchable web view to navigate or share with a team. It does not find or enrich anything; it makes data you already own legible and filterable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Build a Google Sheet with the expected columns (title, description, URL, image URL, type, tags).
2. Publish the sheet and paste its link into Listify at http://listify.okfnlabs.org.
3. Generate the listing; you get a searchable page (or embeddable code) rendered from your rows.
4. Share the link internally, or embed it — mindful that a public listing is world-readable.
5. Pivot: use the searchable view to work through your own case data faster; the intelligence still comes from the tools that populated the sheet.

## Inputs → Outputs
- **In:** a Google Sheet of records (yours)
- **Out:** a formatted, searchable web listing — presentation only, no personal selectors
- **Empty/negative result looks like:** a broken/empty listing when the sheet columns don't match the expected schema — a formatting problem, not an intelligence result.

## Gotchas & OpSec
- Human-in-the-loop: none beyond preparing and publishing the sheet.
- OpSec: passive toward any subject, but publishing exposes the data — keep sensitive case material out of any Listify page you make shareable.
- It is a lightweight utility; it does not clean, verify, or enrich your data — garbage in, garbage listed.

## Overlaps ("do both")
- Pairs with data-collection/scraping tools — those fill the spreadsheet; Listify (or a similar sheet-to-page renderer) makes the collected rows browsable for the team.

## Trust & verifiability
`trust: community` — a transparent OKFN utility that simply reformats your data; there is nothing to verify in its output beyond the accuracy of the sheet you feed it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | listify |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
