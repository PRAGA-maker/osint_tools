---
id: selective-service-online-registration
name: Selective Service Online Registration
description: Use when you have a US man's `name`, `dob`, and SSN and want to confirm draft registration — returns registration status and number.
url: https://www.sss.gov
category: public-records
path:
- public-records
bestFor: Verifying whether a US male is registered with the Selective Service and retrieving the registration number.
selectorsIn:
- name
- dob
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free US government service; no payment or account. The verification form is public but requires the subject's identifying data.
opsec: passive
opsecNote: Passive — you submit identifiers to a government verification form; it returns a yes/no plus registration number and does not notify the individual. Only run it on a subject you are authorized to check, since it requires their SSN.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Selective Service System; the registration-status result is authoritative for US draft-registration records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- national-archives-and-records
aliases:
- SSS registration check
- sss.gov verification
tags:
- toddington
- specialty-search
- government-records
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Selective Service Online Registration

> The US Selective Service System's own verification form — confirm whether a man is draft-registered, given his identifying details.

## When to use
You have a US male subject's last `name`, `dob`, and Social Security Number and need to confirm whether he is registered with the Selective Service (mandatory for most US men aged 18–25) and pull his registration number. Because it requires the SSN, it is a confirmation/verification tool for a subject you already have strong identifiers for — not a discovery search. In practice it corroborates that a person of that name/DOB/SSN exists in a federal system and is registered, which can validate an identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sss.gov and open the "Verify Registration" / check-registration form.
2. Enter the subject's last `name`, `dob`, and SSN as required.
3. Read the result: registered (with a registration number) or not found.
4. Record the registration number (`document-id`) as corroborating evidence.
5. Note this only confirms US draft registration — pivot to other identity/records tools for anything further.

## Inputs → Outputs
- **In:** `name` (last), `dob`, and SSN
- **Out:** registration status (yes/no) and Selective Service registration number (`document-id`)
- **Empty/negative result looks like:** "no record found" — the subject may never have registered, be outside the eligible cohort (women, older/younger men, some non-citizens), or the identifiers don't match; a null is not proof the person doesn't exist.

## Gotchas & OpSec
- **Requires an SSN** — you cannot use this to discover someone; it only verifies a subject you already identify. Ensure you have a lawful basis to query it.
- Scope is narrow: US men in the registration-age cohort; it says nothing about anyone outside that group.
- Returns only registration status/number — no address, employer, or contact data despite the stub's earlier field guesses.
- OpSec: passive; the individual is not notified.

## Overlaps ("do both")
- Pairs with `[[national-archives-and-records]]` and other US government-records tools — Selective Service confirms draft-registration status, while archival/vital-records sources add the broader identity and history around it.

## Trust & verifiability
`trust: trusted` — a first-party US government system; a positive result is an authoritative confirmation of draft registration, though it is a single narrow fact, not a full identity record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | selective-service-online-registration |
| category | public-records |
| selectorsIn → selectorsOut | name, dob → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
