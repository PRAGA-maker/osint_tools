---
id: offshorealert-com
name: OffshoreAlert
description: Use when you have a `name` or `employer-org` and want offshore-finance, fraud and litigation intelligence — returns investigative reports and a database of civil/criminal actions, judgments and leaked documents naming the parties.
url: https://www.offshorealert.com/
category: public-records
path:
- public-records
bestFor: Digging up offshore fraud, asset and litigation records tied to a person or company in secrecy jurisdictions.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- document-id
status: live
pricing: freemium
costNote: A subscription-based investigative service. Headlines and some articles are free, but the searchable document database and full investigative reports sit behind a paid subscription; some documents are sold individually.
opsec: passive
opsecNote: Searching and reading are passive against OffshoreAlert's own archive — no subject is contacted. A subscription ties your research to an account and payment method; use a sock-puppet identity you are willing to expose to the vendor. Handle any third-party financial PII lawfully.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: OffshoreAlert is a well-known, long-running investigative outlet (founded by David Marchant) specializing in offshore financial fraud, with a track record of breaking major cases and hosting primary-source litigation documents. Reports are edited journalism; documents are primary sources.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Offshore Alert
- offshorealert.com
tags:
- companysites
- Company Related Sites
- offshore
- fraud
- litigation
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# OffshoreAlert

> A specialist investigative outlet and document archive on offshore finance, fraud and litigation — where you find the lawsuits, judgments and leaked filings that name a subject operating through secrecy jurisdictions.

## When to use
You have a `name` or `employer-org` connected to offshore structures, cross-border business, or suspected fraud, and you want reporting and primary documents: civil/criminal complaints, receiverships, regulatory actions, judgments and leaked corporate filings. Strong for financial-motive investigations, asset tracing, and mapping the `associate`/entity network behind a shell company — a niche most people-search and company registries don't cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.offshorealert.com/ and search the `name`/`employer-org`.
2. Read the free headlines/summaries to gauge relevance.
3. Subscribe (or buy individual documents) to open full reports and the searchable document database.
4. Extract the parties, entities, case numbers (`document-id`) and jurisdictions named in filings.
5. Pivot: named `associate`s and entities feed corporate-registry lookups (OpenCorporates), court-record searches, and sanctions/PEP screening; case numbers open the underlying court dockets.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** linked entities/`employer-org`, co-parties as `associate`, case/document identifiers (`document-id`), jurisdictions
- **Empty/negative result looks like:** no coverage — the subject simply isn't in OffshoreAlert's fraud/litigation archive (most ordinary people aren't). Absence here says nothing about the person generally; it's a specialist source.

## Gotchas & OpSec
- Coverage is narrow and financial-crime focused — it will not locate an ordinary missing person, only those touched by offshore litigation/fraud.
- The valuable material (documents, full reports) is behind a **subscription/paywall**; budget for it.
- Reports are journalism (allegations may be unproven) — treat named parties as leads and check the actual court outcome.

## Overlaps ("do both")
- Pairs with OpenCorporates, `[[icij-offshore-leaks]]`-style leak databases, court dockets and sanctions lists — OffshoreAlert adds edited investigation and documents those raw registries lack, while they add breadth OffshoreAlert doesn't.

## Trust & verifiability
`trust: trusted` — an established investigative outlet with a strong track record and primary-source documents. The caveat is that reporting states allegations; verify final legal outcomes against the courts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | offshorealert-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
