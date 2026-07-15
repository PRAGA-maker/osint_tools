---
id: rivoters-com
name: Rivoters.com
description: Use when you have a `name` and want a Rhode Island resident's registered-voter record — returns their address, year/date of birth and helps confirm identity from public voter rolls.
url: https://rivoters.com/
category: public-records
path:
- public-records
bestFor: Looking up a Rhode Island registered voter's address and birth year from the public voter roll, free and without login.
selectorsIn:
- name
- address
selectorsOut:
- address
- name
- dob
status: live
pricing: free
costNote: Free public-records site; no account, payment or login. Data derives from Rhode Island's public voter file (a February 2021 snapshot).
opsec: passive
opsecNote: Searching is a fully passive, anonymous lookup against a static published dataset — nothing reaches the subject or any authority. You disclose your query only to the site host; a normal browser session is adequate.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent site republishing Rhode Island's public voter roll (as of 4 Feb 2021). Accurate as of that snapshot but static and unaffiliated with the state; the official source is vote.sos.ri.gov.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Rhode Island voters
- RI voter records
tags:
- voter-records
- public-records
- rhode-island
- us
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Rivoters.com

> A free, browsable republication of Rhode Island's public voter roll (Feb 2021) — put a `name` in and get an `address` and birth year, a fast identity/location confirm for RI subjects.

## When to use
You have a `name` for someone likely in Rhode Island and want their registered address and age/birth year to confirm identity or generate a last-known address. Voter rolls are among the most reliable free people-locating datasets in the US, and this site exposes RI's without paywalls or logins — a strong early pivot in missing-persons and skip-tracing work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://rivoters.com/.
2. Type the subject's name into the search box, or browse the alphabetical A–Z indexes (e.g. `/index_pages/m.html`) or by ZIP (`/by_ZIP_Code/02864.html`).
3. Read the record: name, residential address, and birth year (exact DOB for older entries; newer ones show year only, per a state policy change).
4. Pivot: the address feeds property/neighbor lookups and reverse-address search; the birth year + name feeds broader people-search; corroborate against the official RI Voter Information Center.

## Inputs → Outputs
- **In:** `name` (optionally narrowed by ZIP)
- **Out:** `address`, confirmed `name`, `dob` (year, or full date for older records)
- **Empty/negative result looks like:** no matching name in the index. Because the dataset is a **2021 snapshot**, absence can mean the person registered later, moved, or was removed — not that they never lived in RI. Re-check the official state site for current data.

## Gotchas & OpSec
- **Static snapshot (4 Feb 2021):** anyone who registered, moved, or de-registered after that date won't reflect reality — treat addresses as "as-of-2021," not current.
- Newer records show only birth *year*, not full DOB, due to an RI Secretary of State policy change.
- Common names produce multiple hits — disambiguate by ZIP/address.
- OpSec: passive; a public dataset lookup with no subject-side signal.

## Overlaps ("do both")
- Pairs with the official [vote.sos.ri.gov] Voter Information Center and multi-state voter aggregators — those give *current* status; this gives a fast, free, browsable historical snapshot. Cross-check for moves.

## Trust & verifiability
`trust: community` — an independent republisher of genuine public voter data, accurate to its 2021 snapshot but unofficial and unmaintained-as-live. For anything decision-critical, confirm against the state's official voter search.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rivoters-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, name, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
