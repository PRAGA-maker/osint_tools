---
id: ministry-of-corporate-affairs-india
name: Ministry of Corporate Affairs (India)
description: Use when you have an Indian company `name` or `employer-org` and want official registry master data — returns registered address, incorporation details and director leads.
url: https://www.mca.gov.in/content/mca/global/en/mca/master-data/MDS.html
category: public-records
path:
- public-records
bestFor: Official Indian company master-data lookup — registration number, status, registered address, and director signatories.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free company/LLP master-data view on the government MCA portal; no payment. Downloading full filed documents costs a fee, but the master-data summary is free.
opsec: passive
opsecNote: Official government registry lookup; the company/directors are not notified and nothing is revealed about you. All master data here is public corporate record by law.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Ministry of Corporate Affairs is India's official companies registrar; its master data is the authoritative record for Indian companies and LLPs.
missingPersonsRelevance: medium
coverage:
- in
auth: none
api: false
localInstall: false
registration: false
aliases:
- MCA India
- mca.gov.in
- MCA master data
tags:
- toddington
- curated-directory
- company-search
- india
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Ministry of Corporate Affairs (India)

> India's official companies registrar: look up a company or LLP by name to get its authoritative master data — registration number, status, registered address, and director details.

## When to use
Your subject is tied to an Indian company or LLP. MCA master-data lets you confirm the `employer-org` exists, see its registered `address`, incorporation date, and status (active/struck-off), and identify its directors/signatories (`associate`s) via their DIN. Strong for corporate-angle investigations in India, verifying a claimed business, or finding the people behind a company.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the MCA portal's "View Company/LLP Master Data" (under MCA Services → Master Data at https://www.mca.gov.in/).
2. Enter the company name or its CIN; solve the CAPTCHA and submit.
3. Read the master data: CIN, registration number, date of incorporation, registered office `address`, status, and authorized/paid-up capital.
4. For directors, use "View Signatory Details" / director (DIN) lookups to list the people associated with the company.
5. Pivot: registered `address` → mapping/local records; director names + DINs → `associate`s and their other directorships; company status → whether the entity is live.

## Inputs → Outputs
- **In:** Indian company/LLP `name` or CIN (`employer-org`)
- **Out:** master data → `employer-org` details, registered `address`, and director/signatory `associate`s.
- **Empty/negative result looks like:** no match — the name/CIN is wrong or the entity isn't MCA-registered (e.g. a sole proprietorship or unregistered business, which MCA doesn't cover).

## Gotchas & OpSec
- India only; covers MCA-registered companies and LLPs, not proprietorships/partnerships outside the registrar.
- The portal uses CAPTCHAs and occasionally changes URLs/UI; navigate from mca.gov.in's Master Data menu if a deep link breaks.
- Full incorporation documents require a paid download; master-data summary is free.
- Registered address may be a firm/CA office, not where directors live.

## Overlaps ("do both")
- Pairs with OpenCorporates and Indian director-search tools — MCA is the authoritative source, aggregators add cross-linking of directors across companies.

## Trust & verifiability
`trust: trusted` — the official Indian government registrar; master data is authoritative for registered entities, with the only caveats being scope (registered companies/LLPs) and occasional portal changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ministry-of-corporate-affairs-india |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
