---
id: drug-enforcement-administration
name: Drug Enforcement Administration
description: Use when you have a `name` and want DEA public records — returns fugitive listings, press-release arrest details and (via Diversion Control) registrant validation for a `name`/`employer-org`.
url: https://www.dea.gov/
category: public-records
path:
- public-records
bestFor: Checking DEA fugitive listings and press releases for a named person, and validating a DEA registrant number for a practitioner/business.
selectorsIn:
- name
- employer-org
selectorsOut:
- physical-description
- address
- employer-org
status: live
pricing: free
costNote: Free U.S. federal government resources. No account or payment for fugitive listings, press releases, or the public DEA registration validation.
opsec: passive
opsecNote: Browsing DEA.gov and its press releases is passive and discloses nothing about a subject. The Diversion Control registrant-validation page is meant to verify a DEA number you already have; querying it does not notify the registrant.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official website of the U.S. Drug Enforcement Administration; fugitive listings, press releases and registrant data are authoritative federal sources.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- DEA
- dea.gov
- justice.gov/dea
tags:
- toddington
- curated-directory
- law-enforcement
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Drug Enforcement Administration

> The DEA's public site is more than a brochure: its fugitive listings, named press-release arrests, and registrant validation are concrete, authoritative record sources for a person or a medical/pharmacy business.

## When to use
You have a `name` and want to check federal DEA-linked public records: whether the person appears on DEA's **fugitives** list (photo, physical description, last-known area, charges), whether they're named in a DEA **press release** (arrests, indictments, seizures — often with age, city, and role), or — for a practitioner/pharmacy `employer-org` — whether a **DEA registration number** validates. Useful for corroborating identity, criminal-nexus context, or a professional registration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.dea.gov/ (the older justice.gov/dea path redirects here).
2. For a wanted subject, browse **Fugitives** (dea.gov/fugitives) and search/scan by field division — entries carry a photo, `physical-description`, last-known location, and charges.
3. For arrest/indictment context, search the **Newsroom / press releases** by `name` — releases frequently give age, city (`address` hint), and the person's role/employer.
4. For registrants, use the **Diversion Control** registration validation to confirm a DEA number is active for a named practitioner/business.
5. Pivot: names/cities from releases feed people-search and court-record lookups; a validated registrant links a person to an `employer-org` and address.

## Inputs → Outputs
- **In:** `name` (person) or DEA number / `employer-org` (registrant)
- **Out:** fugitive `physical-description` + last-known location, press-release `address`/age/role, registrant validity + owning `employer-org`
- **Empty/negative result looks like:** no fugitive match, no press-release hit, or an invalid/inactive registration — none of which proves anything beyond "not in these particular DEA records."

## Gotchas & OpSec
- These are **specific record sets**, not a universal person database — a null result only rules out DEA fugitives/press coverage/registration, not any wrongdoing or existence.
- Press releases name people at the time of charging; treat charges as allegations and check current case status before drawing conclusions.
- OpSec: fully passive federal-site browsing; nothing is disclosed to the subject.

## Overlaps ("do both")
- Pair with U.S. court-records (PACER/state) and the FBI/US Marshals wanted lists — DEA covers drug-nexus fugitives and registrants, while those cover the broader case record and other federal wanted persons.

## Trust & verifiability
`trust: trusted` — an official U.S. federal agency site; fugitive, press-release and registrant data are authoritative, with the usual caveat that charges are allegations and listings are point-in-time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | drug-enforcement-administration |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → physical-description, address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
