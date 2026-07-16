---
id: spain
name: Registro Mercantil (Spain)
description: Use when you have a Spanish company `name`, director `name` or `address` and want official mercantile-registry records — returns employer-org, associated officers, registered address and filing data.
url: https://sede.registradores.org/site/mercantil
category: public-records
path:
- public-records
bestFor: Official Spanish company and director records from the state mercantile registry.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: The portal is free to browse and basic company lookups are free, but full mercantile extracts, certifications and beneficial-ownership (titularidad real) reports are paid per document and require a registered account.
opsec: passive
opsecNote: This is a public government registry; querying it does not touch or alert the subject. Detailed/paid requests require account registration, which ties the lookup to your identity/payment — use an appropriately attributed account for sanctioned work.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Colegio de Registradores de España (CORPME), the official body for Spain's Property and Mercantile Registries — authoritative primary-source data.
missingPersonsRelevance: high
coverage:
- es
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Registradores de España
- Registro Mercantil
- sede.registradores.org
tags:
- company
- public-records
- spain
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Registro Mercantil (Spain)

> Spain's official mercantile registry portal — the authoritative source for company records, directors and beneficial ownership across all Spanish provinces.

## When to use
You're linking a subject to a Spanish company: you have a company `name`, a director/officer `name`, or a registered `address`, and you need official corporate records — who the officers and beneficial owners are, the registered address, and filing history. Because it's the state registry (CORPME), the data is primary-source rather than a scraped aggregate, making it strong for corroborating employer-org and associate links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sede.registradores.org/site/mercantil.
2. Choose the mercantile ("Mercantil") service and search by company name; for officer or ownership detail, use "Consulta de Titularidades Reales" (beneficial ownership).
3. Free basic results confirm a company exists and its province/registry; detailed extracts, certifications and ownership reports require registering an account and paying a per-document fee.
4. Read the output for `employer-org` details, registered `address`, and officer/beneficial-owner `name`s (your `associate` links), then pivot officer names into people-search and cross-jurisdiction registries.

## Inputs → Outputs
- **In:** company `name`, director/officer `name`, or `address`
- **Out:** `employer-org` (company record), officer/owner `name`, registered `address`, `associate` links (directors/beneficial owners)
- **Empty/negative result looks like:** "no records" for the searched term — means no Spanish mercantile entity matches that string, not that the person has no company (try name variants, the trade name, or a different registry).

## Gotchas & OpSec
- Human-in-the-loop: the free tier confirms existence; anything beyond a basic lookup is behind account registration and a payment wall.
- The interface is Spanish-language; company data uses Spanish legal forms (S.L., S.A.).
- OpSec: passive and lawful public-records access; paid requests are tied to your registered identity.

## Overlaps ("do both")
- Pairs with cross-border company tools like `[[companies-and-orgs-search-engine]]` and `[[advanced-registry-search]]` — use those to spot a Spanish link, then come here for the authoritative filing.

## Trust & verifiability
`trust: trusted` — the official CORPME state registry; the data is authoritative primary source, subject only to the usual lag between a corporate event and its filing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spain |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
