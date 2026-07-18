---
id: hong-kong-securities-and-futures-commission
name: Hong Kong Securities & Futures Commission
description: Use when you have a person or firm name and want to check Hong Kong financial licensing — returns employer-org licence status and any disciplinary/enforcement record.
url: https://www.sfc.hk/en/
category: search-engines
path:
- search-engines
bestFor: Verifying whether a person or firm is licensed by Hong Kong's SFC, plus checking disciplinary/enforcement actions.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
status: live
pricing: free
costNote: Free official SFC public register and enforcement listings; no account required.
opsec: passive
opsecNote: Reads a public regulatory register; the licensee is not notified. Standard web logging only. Use a clean browser for sensitive subjects.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Hong Kong Securities and Futures Commission; authoritative for HK licensing and enforcement.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SFC Hong Kong
- HK SFC public register
- sfc.hk
tags:
- public-records
- financial-regulation
- hong-kong
- licensing
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Hong Kong Securities & Futures Commission

> Hong Kong's financial regulator — its public register lets you confirm whether a person or firm is SFC-licensed, and its enforcement pages record disciplinary actions.

## When to use
You have a `name` (individual) or `employer-org` (firm) tied to financial services in Hong Kong and want to verify their regulatory standing. The SFC's "Register of licensees & registered institutions" confirms licence type and status; the enforcement/disciplinary listings record sanctions. Useful for vetting a claimed financial professional, spotting unlicensed operators (a fraud red flag), and anchoring a person to a licensed firm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sfc.hk/en/ and open Regulatory functions → Intermediaries → Licensing → "Register of licensees & registered institutions" (or use the "see if a firm or a person is licensed" quick link).
2. Search by person or firm name to check licence type, status, and the firm(s) an individual is accredited to.
3. Separately check the SFC's enforcement news / disciplinary action listings for the same name.
4. Pivot: the accredited firm links a person to an `employer-org`; a disciplinary record is a lead to news and court coverage; unlicensed status where a licence is claimed is a strong red flag.

## Inputs → Outputs
- **In:** `name` (individual) or `employer-org` (firm)
- **Out:** `employer-org` (licence type/status, accredited firm), `name` (verified licensee), plus any disciplinary record
- **Empty/negative result looks like:** not on the register — the person/firm isn't SFC-licensed (may operate in another jurisdiction, be unlicensed, or the name differs). Absence of a licence claimed to exist is itself significant.

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — the licensee isn't notified.
- Scope: Hong Kong securities/futures licensing only. Banking is regulated by the HKMA; other activities by other regulators — check the right register.

## Overlaps ("do both")
- Pairs with other financial regulators' registers (FCA, SEC, MAS) and company registries — SFC confirms the HK licence, the others cover other jurisdictions and the corporate entity behind the person.

## Trust & verifiability
`trust: trusted` — it is the official HK regulator's register; licence status and enforcement records are authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hong-kong-securities-and-futures-commission |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
