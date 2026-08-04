---
id: json-to-csv
name: JSON to CSV
description: Use when you have JSON data (an API dump, a breach export, a scraped file) and want it flattened into a spreadsheet-friendly CSV — a data-wrangling utility, returns no selectors.
url: https://json-csv.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Quickly converting JSON exports into CSV for review in a spreadsheet during an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free for small files in the browser; larger files and batch/advanced conversion are behind a paid plan. The free tier covers routine one-off conversions.
opsec: passive
opsecNote: The browser-side converter processes data in-page, but treat any online converter as untrusted with sensitive data — do not upload breach dumps, PII, or case data containing real selectors to a third-party site. For anything sensitive, use a local tool (jq, pandas, csvkit) instead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A simple long-standing conversion utility; output is directly checkable against the input, but it is a third-party site with no security assurances for the data you feed it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- json-csv.com
tags:
- files
- data-conversion
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# JSON to CSV

> A no-setup web converter that flattens JSON into CSV — a data-prep utility for making machine-readable dumps reviewable in a spreadsheet.

## When to use
Investigations routinely produce JSON: API responses, scraper output, breach exports, social-media takeouts. When you want to eyeball, sort, or filter that data in Excel/Sheets rather than reading raw JSON, this flattens nested structures into columns and rows. It is a plumbing tool — it returns no selectors itself; it just makes the selectors already in your data easier to work with. For anything sensitive, prefer a local converter (see OpSec).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://json-csv.com/.
2. Paste your JSON or upload a `.json` file (mind the free-tier size limit).
3. The tool flattens nested objects/arrays into columns; preview the resulting table.
4. Download the CSV and open it in a spreadsheet for sorting/filtering/deduping.
5. Pivot: from the CSV, isolate columns of interest (emails, usernames, phones) and feed those selectors into the appropriate enrichment tools.

## Inputs → Outputs
- **In:** JSON text/file (no OSINT selector — it's your existing data)
- **Out:** a flattened CSV (no new selectors; a reformatting of what you supplied)
- **Empty/negative result looks like:** a parse error on malformed JSON, or an awkward/exploded table when the JSON is deeply nested or irregular. Deeply nested data may convert more cleanly with `jq`/pandas locally.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**, but this is a third-party site — never upload breach data, PII, or case files with real selectors. Use `jq -r`, `pandas`, or `csvkit` locally for sensitive conversions.
- Free tier is size-limited; nested/heterogeneous JSON can flatten messily. It's a convenience tool, not a data-engineering pipeline.

## Overlaps ("do both")
- Overlaps with local converters (`jq`, `pandas`, `csvkit`) which do the same job offline with no third-party exposure — use this only for small, non-sensitive quick conversions.

## Trust & verifiability
`trust: community` — a simple utility with no official backing. The conversion is trivially verifiable (compare CSV against source JSON), but there are no data-handling guarantees, so keep sensitive data off it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | json-to-csv |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
