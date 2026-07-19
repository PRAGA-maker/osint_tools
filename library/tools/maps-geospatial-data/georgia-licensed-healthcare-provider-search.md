---
id: georgia-licensed-healthcare-provider-search
name: Georgia Licensed Healthcare Provider Search
description: Use when you have a `name` of a healthcare provider in Georgia (US) and want to verify their license — returns license status, type, number, issue/expiry dates, and any public disciplinary action.
url: https://gcmb.mylicense.com/verification/
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Verifying a Georgia healthcare provider's license status, number, and disciplinary history by name.
selectorsIn:
- name
selectorsOut:
- document-id
- employer-org
status: live
pricing: free
costNote: Free official Georgia Composite Medical Board verification portal; no account needed.
opsec: passive
opsecNote: You query a state licensing board's public verification system; the provider is not notified. Fully passive.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Georgia Composite Medical Board license-verification system (MyLicense platform); license status and discipline are authoritative primary-source records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Georgia Composite Medical Board verification
- gcmb.mylicense.com
tags:
- license-verification
- healthcare
- public-records
- georgia
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Georgia Licensed Healthcare Provider Search

> The Georgia Composite Medical Board's official license-verification portal — confirm whether a doctor, PA, or other regulated healthcare provider holds a valid Georgia license, and see status, license number, dates, and any public discipline.

## When to use
You have a `name` of someone claiming to be (or reported to be) a healthcare provider in Georgia and want to verify it: is the license real and active, what type/specialty, when issued/expiring, and has the board taken public disciplinary action. Useful for vetting a professional identity, corroborating an employment/occupation claim, or checking a provider named in a case.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://gcmb.mylicense.com/verification/.
2. Search by `name` (last/first) — optionally narrow by license type or number.
3. Solve any CAPTCHA and open the matching provider record.
4. Read the fields: license type, number, status (active/expired/revoked/suspended), issue and expiration dates, and any linked disciplinary/board actions.
5. Pivot: the license type/status corroborates occupation; disciplinary actions feed news/court searches; the provider's practice info can feed address/employer lookups.

## Inputs → Outputs
- **In:** `name` (provider)
- **Out:** `document-id` (license record: type, number, status, dates, discipline) and associated practice/`employer-org` where shown
- **Empty/negative result looks like:** no match — the provider may be unlicensed in Georgia, licensed in another state, licensed under a different name, or the search terms differ; check name variants and the correct state board before concluding.

## Gotchas & OpSec
- Human-in-the-loop: a **CAPTCHA** may gate searches; solve it manually.
- OpSec: fully **passive** — an official public verification system; no notification to the provider.
- Scope: Georgia and the professions under the Composite Medical Board only (physicians, PAs, and certain others); nurses/pharmacists/other professions have separate Georgia boards. For providers outside Georgia, use that state's board.

## Overlaps ("do both")
- Pairs with other state medical/nursing boards, the NPI registry, and the NPDB-adjacent public sources — this verifies Georgia licensure and discipline; the NPI registry confirms the national provider identifier, and other-state boards cover multi-state practice.

## Trust & verifiability
`trust: trusted` — the official Georgia Composite Medical Board verification system; license and disciplinary data are authoritative primary records, refreshed by the board, and citable directly from the portal.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | georgia-licensed-healthcare-provider-search |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | name → document-id, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
