---
id: federal-register
name: Federal Register
description: Use when you have a `name` or `employer-org` and want to find their appearance in US federal rules, notices, or agency actions — returns names, organizations, and document IDs.
url: https://www.federalregister.gov/
category: search-engines
path:
- search-engines
bestFor: Full-text searching the daily journal of the US government for a person or organization named in regulations, notices, sanctions, or agency actions.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- document-id
- address
status: live
pricing: free
costNote: Fully free, official US government service; no payment ever required. Registration only adds email alerts and saved searches.
opsec: passive
opsecNote: Passive — you search a public government publication; nothing reaches the subject. The site blocks bulk scraping (CAPTCHA/redirect), so use the official API for automation rather than hammering the web UI.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Office of the Federal Register / GPO; it is the authoritative primary publication for federal rules and notices.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- us-government-printing-office
aliases:
- federalregister.gov
- Daily Journal of the United States Government
tags:
- toddington
- specialty-search
- government-records
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Federal Register

> The official daily journal of the US government, full-text searchable for anyone named in federal rules, notices, and agency actions.

## When to use
You have a `name` or `employer-org` and want to know whether they surface in US federal proceedings — a person named in an agency notice, a company subject to a rulemaking, a sanctioned entity, a grant recipient, a licence action, or an individual appointed to a federal board. It is a strong corroboration source: appearances here are dated, attributable, and tied to a specific agency, which can pin a person to a place, role, or organization at a point in time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.federalregister.gov/ and use the search bar (or the advanced search for date, agency, and document-type filters).
2. Enter the subject `name` in quotes, or the `employer-org`. Narrow by agency or date range if there are many hits.
3. Read each result: title, publishing agency, publication date, and a unique document number (`document-id`); the full text often names people, companies, and mailing addresses.
4. For automation, use the free API at https://www.federalregister.gov/developers/documentation/api/v1 — the web UI redirects/blocks scrapers.
5. Pivot: an org or address in a notice feeds corporate-registry and people-search tools; a document number is a stable citation for your case file.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (agencies/companies named), `document-id` (FR document number/citation), `address` (contact or filing addresses in the notice)
- **Empty/negative result looks like:** "0 documents" — the subject has no federal-publication footprint, which is the norm for most private individuals; absence is not evidence of anything.

## Gotchas & OpSec
- Coverage is federal only (since 1994 for full text, 1936+ via linked archives) — it does not include state or local actions, court records, or non-published agency activity.
- Common names generate noise; use exact-phrase quotes and agency/date filters.
- The web UI actively blocks scraping with a CAPTCHA redirect — respect it and use the API for anything programmatic.
- OpSec: passive; no subject notification.

## Overlaps ("do both")
- Pairs with `[[us-government-printing-office]]` — the GPO/govinfo corpus carries the broader body of US federal publications (congressional records, court opinions, CFR), while the Federal Register is the fastest route to dated agency notices and rulemakings.

## Trust & verifiability
`trust: trusted` — first-party US government publication (Office of the Federal Register/GPO); results are authoritative primary records, not third-party aggregations.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | federal-register |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, document-id, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
