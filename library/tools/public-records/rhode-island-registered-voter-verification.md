---
id: rhode-island-registered-voter-verification
name: Rhode Island Registered Voter Verification
description: Use when you have a `name` (with DOB) for a Rhode Island resident and want to confirm voter registration and district — returns address/district and registration status.
url: https://vote.sos.ri.gov
category: public-records
path:
- public-records
bestFor: Confirming a named Rhode Island resident's voter registration status and assigned polling district.
selectorsIn:
- name
- dob
selectorsOut:
- address
- geolocation
status: live
pricing: free
costNote: Free official Rhode Island Secretary of State voter-information lookup; no payment. Requires the person's name and date of birth to return a record.
opsec: passive
opsecNote: An official state lookup that does not notify the subject. It requires knowing the person's name and DOB, so it confirms/enriches an existing lead rather than discovering one. Use only for legitimate purposes; voter data use is legally constrained.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Rhode Island Department of State (Secretary of State); the registration status it returns is authoritative for RI.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- RI voter lookup
- vote.sos.ri.gov
tags:
- toddington
- curated-directory
- specialty-search
- voter-records
- rhode-island
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- rhode-island
---

# Rhode Island Registered Voter Verification

> Rhode Island's official voter-information lookup: given a person's name and date of birth, confirm whether they're a registered RI voter and see their assigned polling place/district.

## When to use
You have a `name` and `dob` for someone you believe lives in Rhode Island and want to confirm they are a registered voter and roughly where — the assigned polling location/district (`geolocation`) helps localize them. This is a confirmation/enrichment step (it needs identifying details up front), useful for verifying residency in RI and narrowing a person's area.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vote.sos.ri.gov and go to the voter-information / "Am I registered?" lookup.
2. Enter the person's name and date of birth (and any other required field).
3. Read the result: registration status, and typically the assigned polling place / district, which points to their locality.
4. Pivot: the district/polling location → `geolocation`/neighborhood lead; confirmed RI residency → focus other RI record searches (property, court) on that area.

## Inputs → Outputs
- **In:** `name` + `dob` (RI resident)
- **Out:** voter registration status and assigned polling place/district (`geolocation`, approximate `address` area).
- **Empty/negative result looks like:** "no record found" — the person isn't registered in RI, isn't a resident, or the name/DOB don't match the record exactly; recheck spelling/DOB.

## Gotchas & OpSec
- Requires name **and** date of birth — it can't be used to discover an unknown person, only to verify a known one.
- Rhode Island only; other states have their own separate lookups.
- Voter-data access and use are legally restricted in many jurisdictions — use only for lawful purposes.
- It generally returns district/polling info, not a full residential address — treat the location as approximate.

## Overlaps ("do both")
- Pairs with `[[rhode-island]]` state resources and property/court record tools — voter status confirms residency and district, those add address, ownership, and legal detail.

## Trust & verifiability
`trust: trusted` — an official RI Department of State system, so registration status is authoritative; the limitation is scope (RI only) and that it verifies rather than discovers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rhode-island-registered-voter-verification |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → address, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
