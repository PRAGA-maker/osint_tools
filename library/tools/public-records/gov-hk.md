---
id: gov-hk
name: gov.hk
description: Use when you have a Hong Kong `employer-org`, `name`, or `address` and want official company/director records — routes to the Companies Registry e-Search / Cyber Search Centre returning `employer-org`, `address`, `name`, and `associate` (directors).
url: https://www.gov.hk/en/business/registration/deregistration/
category: public-records
path:
- public-records
bestFor: Reaching Hong Kong's official Companies Registry search to confirm a company, its address, and its directors/officers.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- name
- associate
status: live
pricing: freemium
costNote: The gov.hk information pages are free. Company searches run via the Companies Registry Cyber Search Centre / e-Search Services, which charge per-document/per-search fees (small HKD amounts) for detailed extracts; some basic index lookups are free.
opsec: passive
opsecNote: Searching the registry is passive — you query a government database, not the subject, and the company/director is not notified. Paid searches require registration/payment on the Companies Registry portal, which attributes the query to your account; use an appropriate identity for paid extracts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Government of Hong Kong SAR portal and Companies Registry; the company data is authoritative.
missingPersonsRelevance: high
coverage:
- hk
auth: none
api: false
localInstall: false
registration: false
aliases:
- GovHK
- Hong Kong Companies Registry
- Cyber Search Centre
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- integrated-companies-research-china-hong-kong
---

# gov.hk

> The Hong Kong government portal's business section — your entry point to the official Companies Registry e-Search / Cyber Search Centre for company and director lookups.

## When to use
Your subject is linked to a Hong Kong company and you have a company `name`/`employer-org`, a registered `address`, or a person's `name` you suspect is a director. Hong Kong is a common corporate-nexus jurisdiction, so confirming a company's existence, registered office, status, and officers is a frequent step in tracing business affiliations or shell structures.

## How to use it (`bestInteractionPattern`: web-manual)
1. Start at https://www.gov.hk/en/business/registration/ and follow "Access Companies Registry's e-Incorporation, e-Filing and e-Search Services" (the Cyber Search Centre / e-Search).
2. Search by company `name` or company number.
3. For free, view the basic index entry (name, number, status, incorporation date); for a fee, order the company particulars / annual return, which lists registered `address` and directors/officers (`associate`).
4. Read: confirm the entity is live, note its registered office and the named directors.
5. Pivot: director names feed HK/overseas people-search and other registries; the registered address feeds mapping and co-location checks.

## Inputs → Outputs
- **In:** `employer-org` / company number, or `name`/`address` to search
- **Out:** `employer-org` (registered name, number, status), `address` (registered office), `name` + `associate` (directors/officers, from paid documents)
- **Empty/negative result looks like:** no match — the company may be dissolved, registered under Chinese characters, or be an unregistered trade name. Director detail generally requires a paid extract, so a free index hit alone won't show officers.

## Gotchas & OpSec
- Two-tier access: free basic index vs. paid detailed documents (director lists, filings). Budget for the small per-document fees.
- Companies may be registered in Chinese; search both English and Chinese names where possible.
- The linked deregistration page is just the on-ramp; the actual search happens in the Companies Registry portal.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and `[[icris]]`-style HK aggregators — the official registry is authoritative and current, while aggregators add free cross-border linking and historical snapshots.

## Trust & verifiability
`trust: trusted` — first-party HK government registry; company and director data is authoritative (subject to filing compliance).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gov-hk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, name, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
