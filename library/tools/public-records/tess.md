---
id: tess
name: USPTO Trademark Search (formerly TESS)
description: Use when you have a person or company `name`, a brand, or a serial number and want US trademark filings — returns employer-org, name and address of the trademark owner/attorney.
url: https://tmsearch.uspto.gov/
category: public-records
path:
- public-records
bestFor: Searching US federal trademarks by owner name, mark text or serial/registration number to reach an owner's legal name, address and attorney.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free public USPTO service; no account or payment required to search or view filings.
opsec: passive
opsecNote: Searching a public government registry; nothing touches the subject and no login is required. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US Patent and Trademark Office; filings are authoritative primary records. (The legacy TESS system was retired in 2023 and replaced by the current tmsearch.uspto.gov search.)
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- us-patent-office-search
- patent-attorneys-agent-search
aliases:
- TESS
- USPTO Trademark Search
- Trademark Electronic Search System
tags:
- Brand/trademark information search
- trademark
- business-registry
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# USPTO Trademark Search (formerly TESS)

> The USPTO's free federal trademark search — look up a brand, owner or serial number to reach the owner's legal name, mailing address and attorney of record.

## When to use
You have a person's or company's `name`, a brand/`employer-org`, or a trademark serial/registration number, and want the official filing behind it. A trademark application lists the owner's legal name, a correspondence/mailing `address`, and the attorney of record — a reliable pivot for confirming a business identity, tying an individual to a company, or finding a current mailing address. Especially useful when someone runs a branded venture.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://tmsearch.uspto.gov/ (this replaced the old "TESS" system).
2. Search by owner `name`, mark text (brand), or serial/registration number. Use the field/advanced search to constrain to the "Owner Name and Address" field for a person/company lookup.
3. Open a matching record. Read the owner's legal name, mailing `address`, filing dates, goods/services, status, and the attorney/correspondent.
4. Check the "Owner" history — assignments can reveal prior owners and successor entities.
5. Pivot: the attorney/correspondent → law-firm lookup; the owner address → address OSINT; the entity name → `[[us-patent-office-search]]` and state corporate registries.

## Inputs → Outputs
- **In:** `name`, brand/`employer-org`, or serial/registration number
- **Out:** trademark owner legal `name`, mailing `address`, attorney, filing/status details (`employer-org` context)
- **Empty/negative result looks like:** "no matching records" — the party holds no US federal trademark (many small businesses never register), or the mark is spelled/entered differently; try broader mark text or owner-name variants.

## Gotchas & OpSec
- Only federally registered/applied marks appear — unregistered brands and state-only trademarks won't.
- Owner addresses can be a business/agent address rather than a home address.
- The interface changed in 2023; old TESS/gate.exe links are dead — use tmsearch.uspto.gov.
- OpSec: passive, no account, no subject notification.

## Overlaps ("do both")
- Pairs with `[[us-patent-office-search]]` (same office, patents) and `[[patent-attorneys-agent-search]]`; combine with state corporate registries to fully resolve an owner's business footprint.

## Trust & verifiability
`trust: trusted` — a first-party USPTO registry; every field is an official filing you can cite, though owner-provided addresses should be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tess |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
