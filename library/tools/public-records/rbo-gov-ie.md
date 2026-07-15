---
id: rbo-gov-ie
name: rbo.gov.ie
description: Use when you have an Irish `employer-org` and want its beneficial owners — the Register of Beneficial Ownership returns owner names, month/year of birth and nature of control, though public access is now restricted.
url: https://rbo.gov.ie/
category: public-records
path:
- public-records
bestFor: Identifying the natural persons who ultimately own/control an Irish company or society (beneficial ownership).
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- dob
- employer-org
status: live
pricing: free
costNote: The register itself is a free statutory service, but general public access was restricted after the November 2022 CJEU ruling — open searching by anyone is no longer available.
opsec: passive
opsecNote: Any lookup is a passive query against a government register — no signal to the company or owner. Access, however, now requires you to authenticate as a designated/competent person or establish legitimate interest, which ties the request to your identity.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Ireland's official statutory Register of Beneficial Ownership (RBO), operated under the Companies Registration Office — an authoritative first-party source.
missingPersonsRelevance: high
coverage:
- ie
auth: account
api: false
localInstall: false
registration: true
aliases:
- Register of Beneficial Ownership Ireland
- RBO Ireland
tags:
- companysites
- Company Related Sites
- beneficial-ownership
- ireland
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# rbo.gov.ie

> Ireland's Register of Beneficial Ownership — who *ultimately* owns or controls an Irish company. Authoritative, but public access was curtailed by the 2022 EU court ruling.

## When to use
You have an Irish `employer-org` (or a person you suspect is a hidden owner) and need the beneficial owners — the natural persons behind the corporate veil, with their names, month/year of birth, nationality and the nature/extent of their control. Essential for piercing shell structures in fraud and asset-tracing, and for linking a subject to companies they secretly control. Know before you start that you may not be able to access it openly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://rbo.gov.ie/ and read the current access rules.
2. Access route depends on who you are:
   - **Designated persons** (AML-obligated entities) and **competent authorities** have defined access.
   - **Members of the public** must now apply demonstrating *legitimate interest* — open ad-hoc search is no longer available since the Nov 2022 CJEU judgment.
3. Once granted, search by company to retrieve its beneficial owners.
4. Pivot: an owner name + DOB feeds people-search and cross-border company registers; the control structure feeds asset-tracing.

## Inputs → Outputs
- **In:** `employer-org` (Irish company/ICAV/society) / suspected owner `name`
- **Out:** beneficial owner `name`(s), `dob` (month & year), nationality/residence, and their linked `employer-org` and control interest
- **Empty/negative result looks like:** no accessible record — most often because your access request isn't granted, not because the company has no owners. A genuine "no beneficial owner filed" is itself a red flag worth noting.

## Gotchas & OpSec
- **Access is the main obstacle** (`legal-gate`): the register is live and complete, but the 2022 CJEU ruling ended unrestricted public search; plan for the designated-person or legitimate-interest route.
- Records show only month/year of birth (not full DOB) — a disambiguator, not a precise identifier.
- OpSec: the query is passive, but authenticated access attaches your identity to the request.

## Overlaps ("do both")
- Pairs with the Irish CRO company register and cross-border beneficial-ownership/leaks datasets (OpenCorporates, OCCRP Aleph) — CRO gives officers/filings openly; leaks datasets sometimes surface owner data the register now hides.

## Trust & verifiability
`trust: trusted` — an authoritative statutory register. Data is reliable where you can access it; the practical caveat is access, not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rbo-gov-ie |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, dob, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
