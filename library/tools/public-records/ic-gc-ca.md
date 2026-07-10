---
id: ic-gc-ca
name: ic.gc.ca (Corporations Canada)
description: Use when you have a Canadian federal company `name` or an `employer-org` link and want the official registry — returns corporate status, directors (`associate`), and registered `address`.
url: https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html
category: public-records
path:
- public-records
bestFor: Searching Canada's federal corporations register for status, directors, and registered office.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free official Government of Canada (Corporations Canada / ISED) search; no account needed. Note the service now lives under ised-isde.canada.ca — the ic.gc.ca URL may redirect.
opsec: passive
opsecNote: Searching an official company register is passive and does not notify anyone. Standard sock-puppet browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Government of Canada corporate registry; status/director/address data is authoritative for federally-incorporated companies (provincial companies use provincial registries).
missingPersonsRelevance: high
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- business-govt-nz
- companieshouse-im
aliases:
- Corporations Canada
- ISED corporations search
- ic.gc.ca
tags:
- companysites
- Company Related Sites
- canada
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ic.gc.ca (Corporations Canada)

> The Government of Canada's federal corporations register — confirm a federally-incorporated company, its status, its directors, and its registered office.

## When to use
You are tracing a Canadian `employer-org` and want the official record: whether a federal corporation exists, its status (active/dissolved), incorporation details, registered office `address`, and its directors — who are strong `associate` links tying a person to the company. Use it to corroborate a subject's business affiliation, resolve a corporate address, or map a director network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the Corporations Canada search (via ic.gc.ca / ised-isde.canada.ca) and search the company `name` or corporation number.
2. Open the corporate profile: status, incorporation date, registered office `address`, and the list of current/former directors.
3. Note director names (`associate`) and the registered address as pivots.
4. Remember scope: this is **federal** incorporation — provincially-incorporated companies are in provincial registries.
5. Pivot: director names feed people-search; the registered address feeds property/address work; other companies sharing a director extend the network.

## Inputs → Outputs
- **In:** company `name` or corporation number (an `employer-org` link)
- **Out:** `employer-org` status/details, registered `address`, directors (`associate`)
- **Empty/negative result looks like:** no match — the company may be provincially (not federally) incorporated, dissolved under a different name, or misspelled; check the relevant provincial registry too.

## Gotchas & OpSec
- **Federal** corporations only — a Canadian company may instead be registered provincially (Ontario, BC, Quebec, etc.); use the correct registry.
- Director lists reflect filings and can lag real changes.
- The ic.gc.ca URL may redirect to the current ISED domain — follow it.
- OpSec: passive; an official public register, no notification.

## Overlaps ("do both")
- Sits beside other national registries like `[[business-govt-nz]]` and `[[companieshouse-im]]` — for a subject with multi-jurisdiction corporate ties, check each; pair with provincial registries for full Canadian coverage.

## Trust & verifiability
`trust: trusted` — a first-party government registry, so federal corporate data is authoritative. Its only limit is scope (federal vs provincial); confirm the incorporation level and cross-check provincial registries as needed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ic-gc-ca |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
