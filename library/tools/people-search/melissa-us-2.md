---
id: melissa-us-2
name: Melissa (US)
description: Use when you have a `name`, `address`, `phone` or `email` and want to verify and enrich it into full contact detail — returns matched name, address, phone and email.
url: https://www.melissa.com/v2/lookups/
category: people-search
path:
- people-search
bestFor: Verifying and standardizing a US/international address, name, phone or email and returning the linked contact fields from Melissa's reference data.
selectorsIn:
- name
- address
- phone
- email
selectorsOut:
- name
- address
- phone
- email
status: live
pricing: freemium
costNote: Free registration grants ~1,000 lookup credits topped up monthly; heavy or API use is paid. Basic single lookups sit comfortably inside the free credit pool.
opsec: passive
opsecNote: Melissa is a data-quality vendor; a lookup does not contact the subject. Your queries are tied to your registered account, so use a research identity and don't paste live-case PII beyond what the check needs.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial address/identity-verification firm using USPS/Canada Post and reference datasets. Reliable for validation; enrichment breadth varies by record.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- ukphonebook-com
aliases:
- MelissaData
- Melissa Lookups
- Personator
tags:
- address
- people-search
- data-verification
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
---

# Melissa (US)

> A data-quality vendor's public lookup suite, repurposed for OSINT: validate an address/name/phone/email and pull the linked contact fields.

## When to use
You hold one strong US selector — a `name`, a `address`, a `phone`, or an `email` — and want to (a) confirm it is real and correctly formatted and (b) pull the other contact fields Melissa associates with it. Best as a *verification and standardization* step: canonicalize a messy address to USPS form, confirm an email is live, or turn a name into a best-match address/phone before you commit to a more intrusive tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register a free account at https://www.melissa.com/v2/lookups/ (grants the monthly free credit pool).
2. Pick the lookup: Personator (name→contact), Address Check, Phone, Email, or Property.
3. Enter any single or combined input — `name`, `address`, `phone`, `email`, ZIP.
4. Read the match: standardized `address`, associated `phone`/`email`, deliverability/verification flags, and demographic hints where available.
5. Pivot: feed the cleaned `address` into property/records tools; take a verified live `email` into `[[epieos]]`-style reverse lookups.

## Inputs → Outputs
- **In:** `name`, `address`, `phone`, or `email` (single or combined)
- **Out:** matched/standardized `name`, `address`, `phone`, `email` plus verification flags
- **Empty/negative result looks like:** a "no match"/undeliverable/invalid flag. Melissa is conservative — a non-match often means the selector is bad or too sparse, not that the person doesn't exist. Add a second input to disambiguate.

## Gotchas & OpSec
- Human-in-the-loop: requires a (free) account login; credits are consumed per lookup, so batch thoughtfully.
- Strongest for US and Canada; international enrichment is thinner.
- It is built for marketing/mailing verification, so "best match" ≠ confirmed identity — treat an enriched field as a lead to corroborate.
- OpSec: passive; the subject isn't notified. Queries are logged against your account — use a research login.

## Overlaps ("do both")
- Pairs with `[[ukphonebook-com]]` for the UK equivalent of directory-style resolution — Melissa covers US/CA, ukphonebook covers UK.
- Use its address standardization *before* feeding an address into people-search/property tools so you don't miss records due to formatting.

## Trust & verifiability
`trust: community` — a reputable commercial verification provider (USPS/Canada Post certified data). Solid for validating and standardizing selectors; enrichment completeness varies per record, so confirm any newly-surfaced contact field independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | melissa-us-2 |
</content>
