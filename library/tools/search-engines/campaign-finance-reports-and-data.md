---
id: campaign-finance-reports-and-data
name: Campaign Finance Reports and Data
description: Use when you have a `name` and want US federal political donation records — returns address, employer-org, and occupation from FEC filings.
url: https://www.fec.gov/data/
category: search-engines
path:
- search-engines
bestFor: Finding a US person's political contributions, and the city/state, employer, and occupation they self-reported when donating.
selectorsIn:
- name
selectorsOut:
- address
- employer-org
- associate
status: live
pricing: free
costNote: Free, taxpayer-funded first-party US government data; no account or payment required. A bulk API is also available with a free api.data.gov key.
opsec: passive
opsecNote: Read-only public disclosure search; no login and the subject is never notified. Queries hit fec.gov directly, so use a sock-puppet IP if you want no fec.gov log tie-back, but there is no target-facing footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Federal Election Commission's official disclosure portal — authoritative primary-source records that donors are legally required to file.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- us-federal-election-commission
aliases:
- FEC campaign finance data
- fec.gov/data
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Campaign Finance Reports and Data

> The FEC's official contribution search — a free, authoritative way to tie a name to a US city/state, employer, and occupation via itemized political donations.

## When to use
You have a `name` (ideally with a rough US location) and want to confirm identity details or build a life pattern. Federal donors of more than $200 must itemize with their address, employer, and occupation — so a single donation record can hand you a subject's city/state, current employer, and job title, all self-reported and legally required to be accurate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fec.gov/data/receipts/individual-contributions/.
2. Enter the subject's name in "Individual contributor name"; narrow with city/state or employer filters if the name is common.
3. Read each result row: contributor name, city/state (`address`), `employer-org`, occupation, contribution date, amount, and the recipient committee (an `associate`/affiliation signal).
4. Pivot: an employer feeds people-search and LinkedIn work; the recipient committee/candidate hints at political affiliation; a confirmed city/state narrows other searches. For bulk work, use the OpenFEC API with a free api.data.gov key.

## Inputs → Outputs
- **In:** `name`
- **Out:** `address` (city/state), `employer-org`, occupation, political-committee `associate` links
- **Empty/negative result looks like:** "no results" — means no itemized federal contribution over $200 under that name, NOT that the person is apolitical or nonexistent. Small donors and state/local giving won't appear here.

## Gotchas & OpSec
- Only US FEDERAL elections; state and local contributions live in separate state portals.
- Employer/occupation are self-reported at donation time and can be stale, blank, or "retired"/"self-employed."
- Common names return many donors — always corroborate with city/state or employer before attributing a record.
- OpSec: fully passive public-records search; no subject notification.

## Overlaps ("do both")
- Pairs with `[[us-federal-election-commission]]` — same underlying FEC source; use whichever entry point exposes the field you need, and cross-check both when a name is ambiguous.

## Trust & verifiability
`trust: trusted` — first-party FEC disclosure data, legally mandated and primary-source; the highest-confidence tier for employer/occupation/location on a US person who donates federally.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | campaign-finance-reports-and-data |
| category | search-engines |
| selectorsIn → selectorsOut | name → address, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
