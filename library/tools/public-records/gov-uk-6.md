---
id: gov-uk-6
name: gov.uk (Teaching Regulation Agency misconduct)
description: Use when you have a teacher's `name` (or `employer-org` school) and want to find UK professional-misconduct panel outcomes — returns name, employer-org and document-id.
url: https://www.gov.uk/search/all?parent=&keywords=panel+outcome+misconduct&level_one_taxon=&manual=&organisations%5B%5D=teaching-regulation-agency&organisations%5B%5D=national-college-for-teaching-and-leadership&public_timestamp%5Bfrom%5D=&public_timestamp%5Bto%5D=&order=updated-newest
category: public-records
path:
- public-records
bestFor: Finding published teacher-misconduct / professional-conduct panel decisions for a named individual in England.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- document-id
status: live
pricing: free
costNote: Free UK-government service; no account, payment or API key required.
opsec: passive
opsecNote: You are searching the public GOV.UK website, not the subject's own accounts, so nothing is disclosed to the target. GOV.UK may log your IP like any web server; use a clean browser if you want to keep the query off your work profile, but there is no leakage to the person of interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UK Government (GOV.UK) and the Teaching Regulation Agency; misconduct decisions are first-party official publications, not third-party aggregation.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Teaching Regulation Agency search
- TRA misconduct outcomes
- GOV.UK teacher misconduct
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# gov.uk (Teaching Regulation Agency misconduct)

> A pre-filtered GOV.UK search that surfaces published teacher-misconduct panel decisions from the Teaching Regulation Agency — an official England-wide professional-discipline paper trail on a named individual.

## When to use
You have a `name` you believe belongs to (or once belonged to) a teacher in England, and you want to know whether the Teaching Regulation Agency (TRA, formerly the National College for Teaching and Leadership) has published a professional-conduct panel outcome about them. A misconduct decision is a rich, dated, official document that typically confirms full name, teacher reference number, the `employer-org` school(s) involved, dates, and the panel's findings — corroborating identity, timeline and last-known workplace for a person who may have dropped off other records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL — it is pre-scoped to the `teaching-regulation-agency` and `national-college-for-teaching-and-leadership` organisations with keywords `panel outcome misconduct`, sorted newest-first.
2. Replace the `keywords=` value with the subject's surname (or full name), or add it alongside `misconduct`, and re-run the search.
3. Narrow with the date filters (`public_timestamp[from]/[to]`) if you already know an approximate hearing period.
4. Open matching results — each decision is a PDF/HTML notice carrying the teacher's name, reference number, employing school, and the finding (`document-id`, `employer-org`).
5. Pivot: the named school feeds employer/associate research; the teacher reference number is a stable `document-id`; the hearing date anchors a timeline.

## Inputs → Outputs
- **In:** `name` (teacher), optionally `employer-org` (school)
- **Out:** `name`, `employer-org` (school), `document-id` (teacher reference number / decision reference)
- **Empty/negative result looks like:** "0 results" or only generic guidance/policy pages with no named decision — treat as "no published TRA misconduct outcome", NOT as proof the person was never a teacher.

## Gotchas & OpSec
- Coverage is England only and only for cases that reached a *published* panel outcome; most teachers never appear here, so absence is meaningless.
- The search returns guidance and news alongside decisions — filter to the "Guidance and regulation" / decision notices and confirm the name matches; common names produce false positives.
- OpSec: fully passive — this is a public government site and touches nothing the subject controls.

## Overlaps ("do both")
- Pairs with `[[gov-uk-6]]`-style sibling regulator searches and general UK people/records tools — a misconduct notice gives you an official name+school, which you can then run through electoral-roll or company-director lookups.

## Trust & verifiability
`trust: trusted` — decisions are first-party official publications by the UK Teaching Regulation Agency on GOV.UK; the data is authoritative and the documents are the primary source, not a scrape.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-uk-6 |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
