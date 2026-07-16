---
id: new-york-state-voter-records
name: New York State Voter Records (Steve Morse)
description: Use when you have a `name` in New York State and want their voter registration — returns address, dob, party and household associate voters.
url: https://stevemorse.org/nysvoters/nysvoters.html
category: public-records
path:
- public-records
bestFor: Searching New York State voter registration records (2002-2024) by name to get residential address, date of birth, party and voting history.
selectorsIn:
- name
selectorsOut:
- address
- dob
- associate
status: live
pricing: free
costNote: Free public search interface over the New York State voter file; no account or payment.
opsec: passive
opsecNote: You query a static, publicly released voter dataset via Steve Morse's search page — you never contact the subject, and the data is already public record. Fully passive; standard web-server logging by the host applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Steve Morse's One-Step tools are long-established and respected in the genealogy/OSINT community; the underlying data is the official New York State voter registration file, so records are authoritative (within the covered years).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- NYS Voter Records
- Steve Morse voter search
- One-Step voter records
tags:
- voter-records
- new-york
- public-records
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- brooklyn-genealogy
- chicago-cook-county-genealogy
- decoding-social-security-numbers
- encoding-and-decoding-driver-s-license-numbers
- familysearch-s-united-states-record-collections
- new-jersey-voter-records
- new-york-state-prison-records
- social-security-death-index
- street-name-changes
---

# New York State Voter Records (Steve Morse)

> A free One-Step search over New York State's voter file — turn a name into a registered voter's address, date of birth, party and voting history.

## When to use
You have a `name` you believe is (or was) a registered voter in New York State and you want hard identity/location data: current-or-recent residential `address`, exact `dob`, party registration, and which recent elections they voted in (a life-signs indicator). Voter records are high-value for missing-person work because they carry a precise birth date and address, and because everyone at the same address (`associate`) surfaces the household.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/nysvoters/nysvoters.html.
2. Enter at least a last name; add first name, and optionally city/county to narrow common names. The form supports "starts with"/"exact" matching.
3. Run the search and read results: full name, residential `address`, `dob`, party, and recent voting participation.
4. Search the same address to find co-registered household members (`associate`).
5. Pivot: the `dob` corroborates identity across other tools; the address feeds property/neighbour records; recent voting activity suggests the person was alive and local as of that election.

## Inputs → Outputs
- **In:** `name` (last name minimum; refine with first name / locality)
- **Out:** `address` (residential), `dob` (exact), `associate` (co-registered household), plus party and voting history
- **Empty/negative result looks like:** no match — meaning no NYS registration under that name in the covered years (2002-2024); the person may be unregistered, out of state, or registered under a variant spelling. Absence is not proof.

## Gotchas & OpSec
- **New York State only**, and bounded to the released years (~2002-2024); other states have their own voter tools.
- Common names need locality/DOB to disambiguate; try spelling variants and maiden names.
- OpSec: fully passive over already-public record data.

## Overlaps ("do both")
- Pairs with other Steve Morse voter tools and general US people-search — the voter record's exact DOB and address are strong anchors to confirm hits from aggregators like `[[white-pages]]`.

## Trust & verifiability
`trust: trusted` — a respected interface over the official NYS voter registration file; data is authoritative within its covered years, though registration details can lag real-world moves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | new-york-state-voter-records |
| category | public-records |
| selectorsIn → selectorsOut | name → address, dob, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
