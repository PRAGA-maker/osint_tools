---
id: guernseyregistry-com
name: Guernsey Registry
description: Use when you have a company `name`, a director `name`, or a Guernsey business connection and want official company/director records — returns registered company details, officers/associates and a registered address.
url: https://portal.guernseyregistry.com/
category: public-records
path:
- public-records
bestFor: Official Guernsey company and director/officer lookups from the States of Guernsey registry.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Basic company search/existence and some details are free; full filings, officer detail and document copies are typically charged per item or require a registry account.
opsec: passive
opsecNote: An official corporate registry; searching is passive and no one is notified. A free-text search is anonymous; ordering documents may require an account and payment tied to you — use a research identity if so.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the States of Guernsey (the official company registry for the Bailiwick of Guernsey); authoritative first-party corporate data.
missingPersonsRelevance: high
coverage:
- gg
auth: none
api: false
localInstall: false
registration: false
aliases:
- Guernsey Registry portal
- guernseyregistry.com
tags:
- companysites
- company-records
- corporate-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Guernsey Registry

> The States of Guernsey's official company registry — search Guernsey companies and their directors/officers to tie a person to corporate roles and a registered address in the Bailiwick.

## When to use
You have a company `name`, a director/officer `name`, or a Guernsey business nexus and want authoritative corporate records: which Guernsey companies a person is an officer of, co-officers (`associate`), and registered addresses. Guernsey is a common offshore/financial jurisdiction, so this is useful for asset/role mapping and due diligence on subjects with Channel Islands links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portal.guernseyregistry.com/.
2. Search by company name or officer/director name.
3. Read the company record: status, incorporation details, registered address, and officers.
4. Deeper filings/document copies may require payment or a registry account — decide whether the free detail already answers your question.
5. Pivot: officer records surface co-directors (`associate`) and a registered/service `address`; cross-reference with UK Companies House and other registries to map cross-jurisdiction structures.

## Inputs → Outputs
- **In:** company `name` or director/officer `name`
- **Out:** `employer-org` (company records), officer `name`s, registered `address`, co-officer `associate` links
- **Empty/negative result looks like:** no matching company/officer — the person may have no Guernsey company role, or the entity is dissolved/spelled differently. Offshore structures often use nominee directors, so a person's real involvement may be masked.

## Gotchas & OpSec
- **Nominee/opacity risk:** offshore registries frequently list nominee officers and holding structures — a name's absence doesn't rule out beneficial involvement, and a listed nominee isn't the beneficial owner.
- Some detail/documents are paywalled or account-gated.
- Guernsey (Bailiwick) scope only — Jersey and the UK are separate registries.
- OpSec: passive; use a research identity if ordering documents.

## Overlaps ("do both")
- Pairs with UK Companies House, Jersey's registry, and aggregators like `[[pomanda-com]]` — offshore structures span jurisdictions, so map the same people/entities across each official registry.

## Trust & verifiability
`trust: trusted` — first-party States of Guernsey registry; company/officer records are authoritative. The caveat is interpretive (nominees/structures), not data quality — read the actual filings to understand who really stands behind an entity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guernseyregistry-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
