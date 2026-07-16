---
id: lefigaro-fr
name: Le Figaro Entreprises
description: Use when you have a French company `name`/`employer-org` or a director `name` and want free company records and leadership data — returns employer-org, officer names/associates and registered address.
url: https://entreprises.lefigaro.fr/
category: public-records
path:
- public-records
bestFor: Free French company and director lookups (financials, officers, registered address).
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
pricing: free
costNote: Free access to records for 8M+ French companies and establishments; no account required for basic company/director data.
opsec: passive
opsecNote: A public business directory; searching does not touch or alert any individual. Standard open-records browsing — no sock puppet strictly required, though a clean browser avoids personalization.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A Le Figaro media-affiliated directory that republishes official French registry (INSEE/RNE) data; reliable as a mirror of the official source, which remains the authority for disputes.
missingPersonsRelevance: high
coverage:
- fr
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- entreprises.lefigaro.fr
- Figaro Entreprises
tags:
- company
- france
- public-records
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Le Figaro Entreprises

> A free French company directory covering 8M+ entities — search a company or a director's name to get the corporate record, officers and registered address.

## When to use
You're tying a subject to a French business: you have a company `name`/`employer-org`, a registered `address`, or a director's `name`, and you want the corporate record — the registered address, the officers/leaders (`associate` links), and basic financials. Because it republishes official INSEE/RNE registry data for millions of French companies for free, it's a quick way to confirm an employer or map the companies a person directs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://entreprises.lefigaro.fr/.
2. Search by company name, or use director/leadership search to find entities linked to a person's `name`.
3. Read the company page: registered `address`, legal form and SIREN, list of dirigeants/leaders, and financial summary.
4. Pivot: officer names become `associate` leads; cross-check a company against the official `annuaire-entreprises.data.gouv.fr` for the authoritative record, and feed directors into people-search.

## Inputs → Outputs
- **In:** company `name`/`employer-org`, `address`, or director `name`
- **Out:** `employer-org` (company record), officer `name`s (`associate`), registered `address`
- **Empty/negative result looks like:** no matching company/person — means no French registry entity matches that string; try the exact legal name, the SIREN, or the government annuaire.

## Gotchas & OpSec
- French-language interface and French legal forms (SARL, SAS, SA).
- It's a media-affiliated mirror of official data — for anything contested, confirm against the state registry (annuaire-entreprises.data.gouv.fr / INPI).
- OpSec: passive public-records browsing; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with cross-border company tools like `[[companies-and-orgs-search-engine]]` and `[[advanced-registry-search]]` — use those to spot a French link, then come here (or the government annuaire) for the detailed officer/address record.

## Trust & verifiability
`trust: community` — a reputable media directory republishing official French registry data; accurate as a mirror, but the state registry is the authority for any disputed detail.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lefigaro-fr |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
