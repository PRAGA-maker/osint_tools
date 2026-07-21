---
id: us-institute-of-peace
name: United States Institute of Peace (USIP)
description: Use when a case touches conflict, extremism, or a fragile region and you need vetted research and named actors/organizations — returns reports and employer-org/associate leads, not individual records.
url: http://www.usip.org/publications/wwwterrornet-how-modern-terrorism-uses-the-internet
category: public-records
path:
- public-records
bestFor: Authoritative research on conflict, terrorism, and fragile states, and the actors/organizations involved.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free publications and research library; no account required. (The harvested deep link is an older report; browse usip.org for current material.)
opsec: passive
opsecNote: Reading a research institute's publications is passive and discloses nothing about a subject; this is background literature, not a targeted query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: USIP is a US congressionally funded national institute; its research is authoritative analysis, though secondary to primary records.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- USIP
- United States Institute of Peace
- usip.org
tags:
- toddington
- curated-directory
- academic-scholarly-research-tools
- conflict-research
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# United States Institute of Peace (USIP)

> The US national institute for conflict research — a trusted background source on wars, extremism, and fragile states, and the organizations and actors that shape them.

## When to use
A **context/literature** resource, not a person locator. When an investigation touches an armed conflict, extremist movement, or fragile region — relevant to some international missing-persons and trafficking cases — USIP's reports supply vetted analysis: the actors, armed groups, and organizations involved, regional dynamics, and named experts. It orients you and points to the right bodies; it does not hold records about individual missing persons.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to usip.org (the harvested URL is a specific older report; use the site search for current work).
2. Search by region, conflict, `name`, or organization.
3. Read reports for the groups, institutions, and experts named, plus regional context.
4. Note `employer-org`s (armed groups, NGOs, agencies) and expert `associate`s to pursue elsewhere.
5. Pivot: named organizations feed sanctions/registry checks and news search; experts feed academic/people search.

## Inputs → Outputs
- **In:** a region, conflict, organization, or expert `name`
- **Out:** research reports and `employer-org`/`associate` (groups, institutions, experts) leads
- **Empty/negative result looks like:** no relevant publication — USIP covers conflict/peacebuilding themes, so unrelated or purely domestic queries won't be served here.

## Gotchas & OpSec
- Literature only: expect analysis and named organizations, not individual case records.
- Secondary source: corroborate against primary reporting and official data.
- The old deep-linked report may 404 — search usip.org rather than relying on the stored URL.
- OpSec: passive research.

## Overlaps ("do both")
- Pairs with think-tank and IGO research (e.g. UNODC, ICG) and sanctions databases — USIP frames the conflict context; those add operational detail and named-entity records.

## Trust & verifiability
`trust: trusted` — a US congressionally funded institute producing authoritative conflict analysis; reliable as research, to be paired with primary sources for specifics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | us-institute-of-peace |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
