---
id: company-check
name: Company Check
description: Use when you have a `name` (director) or `employer-org` and want UK/Ireland company records — returns directorships, financials, and co-director `associate` links.
url: https://companycheck.co.uk
category: public-records
path:
- public-records
bestFor: Cross-referencing a person's name to the UK/Ireland companies they direct, and mapping their fellow directors and company financial history.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: freemium
costNote: Free membership gives basic company data (ad-supported); unlimited reports and financials/CCJ detail need a paid plan (~£35/month or £350/year).
opsec: passive
opsecNote: Queries a commercial aggregator of public registry data, not the subject — fully passive and the subject is not notified. Registering for the free tier ties searches to your account, so use an investigator/sock-puppet identity.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates official Companies House (UK) and CRO (Ireland) filings plus credit data; the underlying registry facts are authoritative, the derived risk scores are the vendor's own.
missingPersonsRelevance: low
coverage:
- uk
- ie
auth: none
api: false
localInstall: false
registration: true
aliases:
- companycheck.co.uk
- Company Check UK
tags:
- public-records
- company-registry
- uk
source: metaosint
lastVerified: '2026-07-22'
enrichment: full
---

# Company Check

> A UK & Ireland company/director lookup aggregating Companies House and CRO filings — good for turning a person's name into the businesses they run and who they run them with.

## When to use
You have a person's `name` (or an `employer-org`) with a UK/Ireland connection and want to know which companies they direct or own, the company's financial history, any County Court Judgements, and — most useful for network-building — who their fellow directors (`associate`) are. A strong corroboration and pivot step once you have a candidate identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://companycheck.co.uk and search by director name, company name, or company number.
2. For a director-name search, review the list of appointments to identify the right individual (match by DOB/location where shown).
3. Open a company report for registered `address`, directors list, filing/financial history and charges.
4. Note co-directors as `associate` links and other companies at the same address to expand the network.
5. Free tier covers basic data; financials/CCJs and unlimited reports are paywalled — for the authoritative free source, cross-check against Companies House directly.

## Inputs → Outputs
- **In:** `name` (director) or `employer-org`
- **Out:** `employer-org` appointments, co-director `associate`s, registered `address`, financial/filing history
- **Empty/negative result looks like:** no director/company match — the person may not hold a UK/Ireland directorship (many people don't), not that they don't exist.

## Gotchas & OpSec
- Human-in-the-loop: a partial paywall gates financial detail; basic identity/appointment data is free.
- Common names return many directors — confirm the right individual before drawing links.
- Coverage is UK & Ireland only.

## Overlaps ("do both")
- Pairs with the official Companies House and OpenCorporates lookups (authoritative, free) — Company Check's value-add is the aggregated credit view and quick co-director mapping.

## Trust & verifiability
`trust: community` — built on official registry filings (authoritative), but always confirm decisive facts against Companies House/CRO; the vendor's risk scores are derived, not official.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-check |
