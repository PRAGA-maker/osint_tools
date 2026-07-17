---
id: cronodump
name: cronodump
description: Use when you have a Cronos-format database (common in leaked CIS/Russian/Ukrainian government datasets) and want to read it — returns the tables exported to CSV for searching by name, address, etc.
url: https://github.com/alephdata/cronodump
category: public-records
path:
- public-records
bestFor: Converting proprietary Cronos database files into CSV so leaked CIS-region datasets become searchable.
selectorsIn:
- document-id
selectorsOut:
- name
- address
- document-id
status: live
pricing: free
costNote: Free, open-source Python utility maintained under the Aleph (OCCRP) organization. No account or key.
opsec: passive
opsecNote: Runs entirely offline on files you already have — nothing is sent anywhere, so it's technically passive. The legal/ethical weight is in the SOURCE data: leaked government/personal databases carry serious handling, jurisdiction, and privacy obligations. Only process data you are lawfully authorized to hold, store it securely, and treat every record as unverified until corroborated.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Maintained under the Aleph/OCCRP umbrella (reputable investigative-data org); the tool faithfully converts file formats, but the reliability of the OUTPUT depends entirely on the source database.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- aleph-occrp
- organized-crime-and-corruption-reporting-project
aliases:
- alephdata/cronodump
tags:
- databases
- data-analysis
- python
- cis
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# cronodump

> An open-source utility that reads the proprietary "Cronos" database format — used by many government/organizational systems across Russia, Ukraine and other CIS states, and frequently seen in leaked datasets — and exports its tables to plain CSV.

## When to use
You have obtained (lawfully) a database in the Cronos format — the software behind numerous CIS-region government and corporate registries, and a common format in leaked datasets — and you can't read it with ordinary tools. cronodump parses the Cronos structure and dumps each table to CSV so the records become searchable by `name`, `address`, ID, and other fields. It's a format-conversion step, turning an opaque binary into analyzable data, when investigating people connected to that region.

## How to use it (`bestInteractionPattern`: cli)
1. Confirm you are legally authorized to possess and process the data (see OpSec) before touching it.
2. Clone `https://github.com/alephdata/cronodump` and install its Python requirements.
3. Point it at the Cronos database directory/files; run the dumper to export tables to CSV (or to Aleph-ingestable formats).
4. Load the CSVs into your analysis tooling (grep, a spreadsheet, or `[[aleph-occrp]]`) and search by selector.
5. Pivot: treat every hit as an unverified lead — corroborate names/addresses against independent sources before relying on them.

## Inputs → Outputs
- **In:** a Cronos-format database (files you hold) — keyed by `document-id`/record fields
- **Out:** CSV tables containing `name`, `address`, `document-id`, and other record fields, now searchable
- **Empty/negative result looks like:** a parse error or empty export — the input isn't actually Cronos format, is corrupted, or is password/version-incompatible; it does not mean the records are absent.

## Gotchas & OpSec
- Human-in-the-loop / **legal-gate:** the tool is benign, but the *data* is the risk. Leaked government/personal databases carry heavy legal, jurisdictional, and ethical obligations — only process what you are authorized to hold, store it encrypted, and follow applicable law.
- Data provenance and accuracy are unknown: leaked datasets contain errors, staleness, and fabrications — never treat a record as fact without corroboration.
- OpSec: **passive** — fully offline; but handling of the source data is where exposure and liability live.

## Overlaps ("do both")
- Pairs with `[[aleph-occrp]]` — dump the Cronos DB to a supported format, then ingest into Aleph to cross-reference names/entities against its other datasets.

## Trust & verifiability
`trust: community` — maintained under the reputable Aleph/OCCRP project and reliable at its job (format conversion); the trustworthiness of any exported record rests entirely on the source database, which you must independently verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cronodump |
| category | public-records |
| selectorsIn → selectorsOut | document-id → name, address, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
