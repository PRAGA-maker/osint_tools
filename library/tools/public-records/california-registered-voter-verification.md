---
id: california-registered-voter-verification
name: California Registered Voter Verification (Alameda County / ACVote)
description: Use when you have a `name` + DOB and want to confirm California voter registration status — returns a registration confirmation, not a searchable voter file.
url: https://www.acvote.org/index
category: public-records
path:
- public-records
bestFor: Confirming whether a specific California (Alameda County) voter is registered, plus official county election information.
selectorsIn:
- name
- dob
selectorsOut:
- address
status: live
pricing: free
costNote: Free official county government election site; no account.
opsec: passive
opsecNote: The public "check my registration" tool is designed for a voter to confirm their OWN status and typically requires identifying details (name + DOB) that only match a specific record; it is not a browse-anyone database. Passive toward any third party. Do not attempt to misuse it; California voter-file data for others is restricted to authorized (e.g., election/campaign) users under state law.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Alameda County (California) Registrar of Voters site; authoritative for that county's registration status and election information.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ACVote
- Alameda County Registrar of Voters
- California voter registration check
tags:
- voter-records
- elections
- california
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# California Registered Voter Verification (Alameda County / ACVote)

> Alameda County's official Registrar of Voters site — a registration-status confirmation tool (not a searchable statewide voter file) plus authoritative county election info.

## When to use
You want to confirm whether a specific person is a registered voter in Alameda County, California, and you already have identifying details (`name` + date of birth) to match their record. This verifies registration status and can confirm the jurisdiction/precinct tied to their address; it does NOT let you browse or enumerate voters. Use it as a confirmation step, not a discovery tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.acvote.org/ and find the "Check my voter registration" / voter status tool.
2. Enter the required identifying details (typically name + DOB, sometimes address).
3. Read the result: registration status, and precinct/jurisdiction consistent with the person's address.
4. Pivot: a confirmed registration corroborates residency/`address` in the county; for statewide California data on others, note that access is legally restricted to authorized users (elections officials, campaigns, journalists per state rules).

## Inputs → Outputs
- **In:** `name` + `dob` (matching a specific record)
- **Out:** registration status confirmation, precinct/jurisdiction (`address` corroboration)
- **Empty/negative result looks like:** "no registration found" — the person isn't registered in Alameda County (may be registered elsewhere, or the details don't match). It won't return a list of candidates.

## Gotchas & OpSec
- Single-county (Alameda) and confirmation-only — it verifies a known record, it does not search the electorate.
- California restricts bulk/third-party voter data to authorized users; treat this as residency corroboration, not a people-search engine.
- OpSec: passive; requires details you already hold.

## Overlaps ("do both")
- Complements other states'/counties' voter-status tools and public-records/address tools — use this to confirm CA/Alameda residency, those to build the broader address history.

## Trust & verifiability
`trust: trusted` — an official county Registrar of Voters site; authoritative for Alameda County registration status and election information.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | california-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
