---
id: alabama-medical-license-search
name: Alabama Medical License Search
description: Use when you have a physician's `name` and want to verify Alabama licensure — returns license number, status, issue/expiry, medical school, and any disciplinary actions.
url: https://www.albme.gov/consumers/licensee-search/
category: search-engines
path:
- search-engines
bestFor: Verifying a doctor's Alabama medical license, credentials, and disciplinary history by name.
selectorsIn:
- name
selectorsOut:
- employer-org
- document-id
status: live
pricing: free
costNote: Free official search from the Alabama Board of Medical Examiners / Medical Licensure Commission; no account or payment.
opsec: passive
opsecNote: Passive — you query an official state licensure database; the physician is not notified. Nothing to leak beyond your own lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Alabama Board of Medical Examiners data, uploaded directly from the Medical Licensure Commission database and updated daily — primary-source verified (except self-reported specialty).
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ALBME licensee search
- Alabama Board of Medical Examiners search
tags:
- toddington
- license-verification
- medical
- alabama
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Alabama Medical License Search

> The Alabama Board of Medical Examiners' official licensee lookup — confirm by name that a physician is licensed in Alabama, and see their credentials, status, and any public discipline.

## When to use
You have a `name` (a doctor or medical professional) and want to verify their Alabama licensure and standing — confirming credentials, checking a claimed medical background, or surfacing disciplinary/public actions. Useful for vetting a person who presents as a physician, corroborating an employment claim, or building a professional profile. It's authoritative for Alabama licensees specifically.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.albme.gov/consumers/licensee-search/.
2. Search by the practitioner's name.
3. Read the record: name, license number, license status, issue and expiration dates, medical school attended, controlled-substances certificate info, and collaborative-practice details.
4. Check the bottom-left of the results page for **disciplinary and public actions**.
5. Pivot: the medical school and license history corroborate identity/timeline; a confirmed `employer-org`/practice feeds further professional research; discipline records feed background work.

## Inputs → Outputs
- **In:** a physician `name`
- **Out:** license `document-id` (number) and status, issue/expiry dates, medical school, controlled-substance certs, collaborative practice, and disciplinary actions — professional `employer-org` context
- **Empty/negative result looks like:** no match means the person isn't an Alabama licensee under that name — they may be licensed in another state (check that state's board) or not a physician at all.

## Gotchas & OpSec
- **Alabama only:** for other states, use that state's medical board (each has its own verification tool).
- **What's withheld:** full addresses and DOB are hidden for security; patient complaints, malpractice, and open investigations are confidential and won't appear.
- Specialty is self-reported (not primary-source verified) — don't treat a listed specialty as confirmed.

## Overlaps ("do both")
- Complements other state licensing boards and national practitioner databases — this authoritatively verifies Alabama licensure, and those cover other jurisdictions and cross-state histories.

## Trust & verifiability
`trust: trusted` — official Board of Medical Examiners data pulled directly from the Medical Licensure Commission and refreshed daily; primary-source verified except for self-reported specialty.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alabama-medical-license-search |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
