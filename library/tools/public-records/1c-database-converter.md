---
id: 1c-database-converter
name: 1C Database Converter
description: Use when you have a seized/leaked 1C accounting database file (.1CD, .cf, .epf, .efd) and want to read its records — returns grepable CSV that can surface name, address, phone and employer-org fields.
url: https://github.com/soxoj/1c-database-converter
category: public-records
path:
- public-records
bestFor: Extracting person/company records from CIS-region 1C enterprise database dumps into grepable CSV.
selectorsIn:
- document-id
selectorsOut:
- name
- address
- phone
- employer-org
status: live
pricing: free
costNote: Free and open-source (soxoj). No account or API key — you need Python 3 and the source files themselves.
opsec: passive
opsecNote: Fully offline — it parses local binary files on your machine and makes no network calls, so nothing reaches the data subject or any third party. The only real risk is legal — that you hold and process the 1C files lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Written by soxoj (author of Maigret and other well-known OSINT tooling); small, transparent, open-source repo. Community-trusted rather than institutionally audited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- marple
- osint-namecheckers-list
- socid-extractor
- username-generation-guide
aliases:
- onec-database-converter
- soxoj 1c converter
tags:
- Databases and data analyzes
- cis
- offline-parser
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# 1C Database Converter

> Offline parser that turns opaque 1C accounting/ERP binaries (the dominant enterprise software across Russia and other CIS countries) into flat, grepable CSV.

## When to use
You hold a 1C database file as a `document-id` — a `.1CD`, `.cf`, `.epf`, or `.efd` dump obtained from a leak, a lawful seizure, or a corporate disclosure — and you need to read the person and company records inside it. 1C stores accounting, HR, and document-management data for a large share of CIS enterprises, so one file can contain payroll rows, counterparties, addresses, and phone numbers. This tool flattens that binary into CSV you can `grep` for a target `name` or `employer-org`.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/soxoj/1c-database-converter && cd 1c-database-converter`.
2. Install dependencies: `pip3 install -r requirements.txt` (or `pip3 install .` to get the `onec_database_converter` entry point).
3. Run against a file: `onec_database_converter path/to/base.1CD` — or feed several with `--target-list files.txt`, or pipe paths with `--targets-from-stdin`.
4. It writes an unpacked directory of CSV files organised by internal table/type. Run `grep -ri "surname"` across that directory to locate your subject.
5. Pivot: names/phones/addresses recovered here feed people-search and username tooling such as `[[maigret]]` and `[[socid-extractor]]`.

## Inputs → Outputs
- **In:** a 1C binary file (`document-id`) — `.1CD`, `.cf`, `.epf`, `.efd`.
- **Out:** CSV tables containing `name`, `address`, `phone`, `employer-org` and other record fields as grepable text.
- **Empty/negative result looks like:** the tool warns that not all binary content converts cleanly to text; encrypted or proprietary blobs come out empty or garbled. An empty CSV means that table held non-text data — open those in official 1C software rather than treating the file as worthless.

## Gotchas & OpSec
- Human-in-the-loop: none — it is a batch CLI. Large `.1CD` files can be slow and produce many output files; work in a scratch directory.
- OpSec: **passive/offline**. No traffic leaves your machine, so there is zero target-side footprint. The genuine risk is legal — ensure lawful authority to hold and process the source database.
- Output is raw internal schema, not a clean report; expect cryptic table/column names and to do your own field mapping.

## Overlaps ("do both")
- Pairs with `[[maigret]]` and `[[socid-extractor]]` — this recovers offline identity fields (names, phones) from a seized database, and those tools then pivot those selectors into live online profiles.

## Trust & verifiability
`trust: community` — authored by soxoj, a well-known OSINT developer, and fully open-source so the parsing logic is inspectable. Not formally audited; verify any critical extracted record against the original file with official 1C software before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 1c-database-converter |
| category | public-records |
| selectorsIn → selectorsOut | document-id → name, address, phone, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
