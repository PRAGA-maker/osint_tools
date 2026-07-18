---
id: clinicaltrials-gov
name: ClinicalTrials.gov
description: Use when you have an investigator/sponsor `name` or a study and want the people and places behind it — returns principal investigators, sponsoring `employer-org`s, trial sites and contact `address`/`phone`.
url: https://clinicaltrials.gov/
category: public-records
path:
- public-records
bestFor: Finding the investigators, sponsoring organizations and site locations tied to a clinical study.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free U.S. government registry (NIH/NLM); no account or payment, with a free public API for bulk access.
opsec: passive
opsecNote: Searching a public government registry is passive and anonymous; investigators and sponsors are named in the public record, and querying does not notify anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official registry operated by the U.S. National Library of Medicine (NIH); submissions are legally required for many trials, making it an authoritative record.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- ClinicalTrials.gov
- clinicaltrials.gov
- NIH clinical trials registry
tags:
- Science
- public-records
- medical
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# ClinicalTrials.gov

> The U.S. National Library of Medicine's registry of 400k+ clinical studies worldwide — a public record that names principal investigators, sponsoring institutions and trial-site contacts.

## When to use
Your subject is a clinician, researcher, or works in pharma/biotech, and you have a `name` (or a study/drug/condition). ClinicalTrials.gov exposes the principal investigators and study staff, the sponsoring/collaborating organisations (`employer-org`), the institutions running each trial, and often site-level contact `address`/`phone` — corroborating a person's professional role, affiliations and the colleagues (`associate`) they run studies with. It documents professionals in the record, not patients.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://clinicaltrials.gov/ and search the investigator/sponsor `name`, or a condition/drug/organisation.
2. Open a matching study; read the Sponsor/Collaborators, Investigators, and Locations sections for named people, institutions and site contacts.
3. Use filters (status, location, sponsor) or the API to pull many studies for one investigator/organisation and build a timeline of their work.
4. Pivot: a named institution feeds `employer-org` research; co-investigators feed `associate` mapping; a site's contact details feed address/phone OSINT; the study record corroborates a claimed medical/research role.

## Inputs → Outputs
- **In:** `name` (investigator/sponsor), or a study/condition/drug/organisation
- **Out:** `employer-org` (sponsors/institutions), `associate` (co-investigators/staff), site `address`/`phone`, plus the study record
- **Empty/negative result looks like:** no studies for a name — the person may not run registered trials (or uses a different name form); absence bounds their trial activity, it doesn't disprove a research career.

## Gotchas & OpSec
- Human-in-the-loop: none; fully public.
- OpSec: passive — a public government registry; nothing is exposed to a target.
- Names can collide and records vary in completeness (contact fields are sometimes redacted after enrollment closes); verify affiliation against the institution or a publications index.

## Overlaps ("do both")
- Pairs with academic indexes (`[[scinapse-io]]`, `[[research-rabbit]]`) and institution directories — trials give roles, sponsors and co-investigators, while publication indexes give the person's papers and affiliations; together they confirm a researcher's identity and network.

## Trust & verifiability
`trust: trusted` — an authoritative NIH-operated registry with legally-mandated submissions; individual records are only as complete as sponsors filed them, so corroborate key facts against the institution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | clinicaltrials-gov |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
