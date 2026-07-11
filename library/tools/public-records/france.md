---
id: france
name: Infogreffe (French Company Registry)
description: Use when you have a French `employer-org` or a director's `name` and want official company records — returns company registration, filings, and named officers/directors (dirigeants).
url: https://www.infogreffe.com/
category: public-records
path:
- public-records
bestFor: Official French business records — resolving a company to its registration, status, accounts and named directors, or finding companies a person directs.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: Basic company identity, status and officer names are viewable free; full documents (statutes, annual accounts, extrait Kbis) are paid per-document official extracts.
opsec: passive
opsecNote: Infogreffe is an official public registry — searches are passive and notify no one. Director records expose business roles and a registered business address, not necessarily a home; treat named individuals' data per GDPR.
humanInLoop: false
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official online portal of the greffes des tribunaux de commerce (French commercial court registries); authoritative for French company data.
missingPersonsRelevance: medium
coverage:
- fr
auth: none
api: true
localInstall: false
registration: false
aliases:
- Infogreffe
- infogreffe.fr
- greffe tribunal de commerce
tags:
- companysites
- Company Related Sites
- france
- corporate-records
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Infogreffe (French Company Registry)

> France's official commercial-court registry portal — the authoritative route from a French company (or a director's name) to registration, filings and named officers.

## When to use
Your subject has a French business footprint. You have an `employer-org` (a French company name/SIREN) and want its official status, registered address and directors; or you have a `name` and want to find the companies that person legally directs (a corporate-network pivot common in fraud and asset tracing). Infogreffe is the French analogue of Companies House — reach for it whenever French corporate records are in scope.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.infogreffe.fr/ (infogreffe.com redirects here).
2. Search by company name/SIREN (`employer-org`), or by a director's `name` to list their mandates.
3. Read the free identity block: legal form, SIREN/SIRET, status (active/struck off), registered `address`, and named directors (dirigeants).
4. For evidence-grade documents, purchase the official extrait Kbis, statutes, or annual accounts.
5. Pivot: named directors become new `name` subjects; the registered `address` and co-directors (`associate`s) feed network mapping; SIREN links to other French open-data (e.g. INSEE/annuaire-entreprises).

## Inputs → Outputs
- **In:** `employer-org` (company name/SIREN) or a director `name`
- **Out:** company registration, status, registered `address`, and named officers/directors (`name`)
- **Empty/negative result looks like:** no company/officer match — the entity isn't a registered French commercial company (could be an association, sole trader, or foreign entity), the name is spelled differently, or it predates digitised records.

## Gotchas & OpSec
- Paywall for documents: identity data is free, but official extracts and accounts cost money per document.
- Scope: French commercial registrations — associations and some structures live in other registers.
- OpSec: passive official registry; handle directors' personal data under GDPR.

## Overlaps ("do both")
- Pairs with the free annuaire-entreprises / INSEE open data — cross-check SIREN and officer lists at no cost.
- Pairs with `[[rics-org]]`/`[[charteredaccountants-ie]]`-style credential checks when a French director also claims a UK/IE professional status.

## Trust & verifiability
`trust: trusted` — the official portal of the French commercial-court registries; company and officer data are authoritative, with paid official extracts available when evidence-grade proof is needed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | france |
