---
id: csvkit
name: csvkit
description: Use when you have a bulk data dump (CSV/Excel/JSON) and want to slice, search, join, and query it from the command line to pull out records tied to a subject — an analysis aid, not a lookup source.
url: https://github.com/wireservice/csvkit
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Command-line wrangling and SQL-querying of tabular data dumps during analysis.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source Python toolkit; install via pip.
opsec: passive
opsecNote: Runs entirely offline on data you already hold — it touches no network and reveals nothing about a target. OpSec concerns are about how you obtained and store the underlying dataset, not about running csvkit on it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Mature, widely-used open-source toolkit by the Wireservice/data-journalism community; stable and well-documented.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- wireservice csvkit
tags:
- infographics-and-data-visualization
- data-wrangling
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# csvkit

> A suite of command-line tools for converting, cleaning, searching, and SQL-querying tabular data — the workhorse for pulling a subject's records out of a large dump.

## When to use
You have obtained a bulk dataset — a leaked CSV, a voter file, an exported spreadsheet, a JSON export — and need to find, filter, or cross-reference records for a subject without loading it into a heavyweight database or spreadsheet that would choke on the size. csvkit lets you grep, cut, join, and run SQL against it from the shell.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install csvkit`.
2. Inspect structure: `csvlook data.csv | head` and `csvstat data.csv` for column stats.
3. Convert other formats in: `in2csv data.xlsx > data.csv` (also JSON, fixed-width).
4. Search/filter: `csvgrep -c email -m "target@example.com" data.csv`; select columns with `csvcut`.
5. Query with SQL: `csvsql --query "SELECT * FROM data WHERE last_name='Smith'" data.csv`; join two files with `csvjoin`.
6. Pivot: the extracted rows (names, emails, phones, addresses) feed the relevant per-selector lookup tools.

## Inputs → Outputs
- **In:** none as a selector — a tabular dataset you already possess
- **Out:** none as a selector — filtered/joined records (whatever fields the source contains)
- **Empty/negative result looks like:** a query returning zero rows means the subject is not in that dataset (or you filtered on the wrong column) — check column names with `csvcut -n`.

## Gotchas & OpSec
- Large files: csvkit loads some operations into memory; for multi-GB dumps use its streaming tools or a real database.
- Garbage-in: dirty/mixed encodings need cleaning first (`csvclean`).
- OpSec: **passive/offline**; the sensitivity is entirely in the provenance and storage of the dataset you feed it.

## Overlaps ("do both")
- Complements spreadsheet and database tools; use csvkit for fast shell triage, then hand cleaned extracts to visualisation or per-selector lookup tools.

## Trust & verifiability
`trust: community` — long-standing open-source project; deterministic transformations you can re-run and verify against the source file.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | csvkit |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
