---
id: san-francisco-copwatch-database
name: San Francisco CopWatch Database
description: Use when you have a `name` of an SF police/sheriff officer and want their public misconduct and disciplinary records — returns document IDs, incidents, and employer details.
url: https://airtable.com/embed/shreS9yA6eWiJAmHZ/tbl0A1AfPBOaPNBhH?backgroundColor=blue
category: public-records
path:
- public-records
bestFor: Looking up publicly released misconduct, use-of-force, and disciplinary records for named San Francisco police and sheriff officers.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- document-id
- associate
status: live
pricing: free
costNote: Free public database published by the SF Public Defender's Office as an Airtable; no account or payment required to browse or search.
opsec: passive
opsecNote: Passive — you browse a published Airtable of public records; nothing reaches the officers named. It is a public-interest transparency dataset, so accessing it carries no target-side signal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Compiled and published by the San Francisco Public Defender's Office from SB 1421 record releases, lawsuits, and complaints; an official-office source, though coverage is partial and lags records requests.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- buffalo-police
- simplescraper-osint-airtable
aliases:
- CopWatch SF
- SF Public Defender CopWatch
tags:
- police-accountability
- public-records
- airtable
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# San Francisco CopWatch Database

> The SF Public Defender's searchable Airtable of publicly available San Francisco police and sheriff misconduct records.

## When to use
You have a `name` (or badge/role) of a San Francisco Police Department or Sheriff's Department officer and want their public accountability record — officer-involved shootings, use-of-force resulting in injury, sexual-assault complaints, and other disciplinary or civil-suit documents released under California's SB 1421/SB 16. Use it to vet an officer named in a case, corroborate an incident, or find the source documents (`document-id`) behind a complaint. It is officer-focused, so its missing-persons value is indirect: vetting law-enforcement contacts connected to a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Airtable at the URL (it is an embedded, browsable grid).
2. Use Airtable's search/filter to enter the officer `name` or department (`employer-org`).
3. Read the matching rows: officer, incident type, date, disposition, and links/references to the underlying released records.
4. Open the linked source documents for the primary record behind each entry.
5. Pivot: an incident links other officers (`associate`) and case numbers; source documents feed court-record and news searches.

## Inputs → Outputs
- **In:** `name` (officer) or `employer-org` (SFPD/SF Sheriff)
- **Out:** `employer-org` (department/unit), `document-id` (case/record references), `associate` (co-named officers in an incident)
- **Empty/negative result looks like:** no matching row — the officer may simply not yet be in the dataset (the office has received only a fraction of requested records), which is not evidence of a clean record.

## Gotchas & OpSec
- Coverage is incomplete by design: at launch the office had received well under 10% of the records it requested, so absence means "not yet released/entered," not "nothing exists."
- Scope is San Francisco officers only; other jurisdictions need their own databases.
- Entries summarize public records — always open the underlying document before treating a claim as established fact.
- OpSec: passive; browsing public transparency data carries no target-side signal.

## Overlaps ("do both")
- Pairs with `[[buffalo-police]]` and `[[simplescraper-osint-airtable]]` — sibling police-accountability Airtable datasets and the scraper for pulling Airtable data programmatically; use them together to cover multiple jurisdictions.

## Trust & verifiability
`trust: trusted` — published by a government office (SF Public Defender) from official record releases; reliable as far as it goes, but partial coverage means it should be read as a floor, not a complete record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | san-francisco-copwatch-database |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, document-id, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
