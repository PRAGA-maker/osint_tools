---
id: search-the-open-information-catalogue
name: Search the Open Information Catalogue
description: Use when you have a name, organisation or topic and want proactively-released BC government records mentioning it — returns document-id, employer-org, and named individuals in disclosed FOI/briefing material.
url: https://www2.gov.bc.ca/gov/content/governments/about-the-bc-government/open-government/open-information
category: public-records
path:
- public-records
bestFor: Searching British Columbia's proactively disclosed FOI responses, briefing notes and released records by keyword or name.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- name
status: live
pricing: free
costNote: Free public government transparency portal; no account or payment.
opsec: passive
opsecNote: Passive — you are searching a government publication index, not touching the subject. Nothing you type is exposed to the person named; still use a puppet browser as routine hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of British Columbia Open Information portal; records are authoritative government disclosures.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- clicklaw
- cso
- search-for-open-information-documents
- security-licence-status-verification
aliases:
- BC Open Information
- Open Information Catalogue
tags:
- foi
- government-records
- canada
- british-columbia
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Search the Open Information Catalogue

> British Columbia's portal of proactively released government records — search disclosed FOI responses and briefing notes for a name, organisation or topic.

## When to use
Your subject has a plausible connection to the BC provincial government — an employee, contractor, applicant, licensee, someone named in a complaint, briefing or FOI response — and you want to find official documents that mention them. Also useful for building context on an organisation or program a person is tied to.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Open Information portal (https://www2.gov.bc.ca/gov/content/governments/about-the-bc-government/open-government/open-information).
2. Use "Search the information catalogue" and enter a `name`, `employer-org`, program or topic keyword.
3. Filter/browse the returned disclosures — proactively released FOI responses, previously completed FOI requests, and routinely released documents.
4. Open a matching record (usually a PDF) and read for names, roles, dates and reference/`document-id` numbers; note the FOI request number for follow-up.
5. Pivot: a disclosed document can corroborate employment, a program role, or an event, and its request number lets you request the full package.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or topic keyword.
- **Out:** matching released records with a `document-id`/FOI reference, associated `employer-org`/program, and any `name`s appearing in the disclosure.
- **Empty/negative result looks like:** zero catalogue hits — the subject/topic has not appeared in a proactively released BC record, which does not rule out non-BC or unreleased material.

## Gotchas & OpSec
- Coverage is **British Columbia only**; a miss says nothing about other jurisdictions.
- Released FOI packages are often heavily redacted — personal identifiers may be blacked out.
- Only *proactively released* and *previously requested* material is here; brand-new topics may require filing your own FOI request.

## Overlaps ("do both")
- Pairs with `[[cso]]` (BC court records) and `[[search-for-open-information-documents]]` — this surfaces disclosed executive/administrative records, while those cover court and document-level search; run both for a fuller BC picture.

## Trust & verifiability
`trust: trusted` — a first-party Government of British Columbia portal, so the documents themselves are authoritative government disclosures (subject to redaction).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-the-open-information-catalogue |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
