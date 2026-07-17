---
id: ibancalculator-com
name: ibancalculator.com
description: Use when you have an IBAN or national bank code (`document-id`) and want to identify the bank — returns the `employer-org` institution name and branch `address`.
url: https://www.ibancalculator.com/blz.html
category: financial-crypto
path:
- financial-crypto
bestFor: Validating an IBAN and resolving a bank/sort code (BLZ) to the institution name and BIC.
selectorsIn:
- document-id
selectorsOut:
- employer-org
- address
status: live
pricing: freemium
costNote: The interactive validator and bank-code lookup are free; bulk CSV calculation, a REST API and SSL access are paid.
opsec: passive
opsecNote: Checksum validation and bank-code resolution run against reference tables, not a live bank query — no one is contacted and no account is probed. Still, avoid submitting a real full account you have no right to; you only need the routing portion to identify the bank.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing IBAN/BIC reference site; bank-code directories are widely accurate but community-maintained, so confirm decisive facts with the bank's official registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- IBAN Calculator
- ibancalculator.com
tags:
- banksites
- Banking Related Sites
- iban
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# ibancalculator.com

> An IBAN validator and bank-code directory: paste an IBAN (or a national bank/sort code) and it tells you whether it's structurally valid and which bank — with BIC — it belongs to.

## When to use
You have an IBAN or a national bank code (German BLZ, UK sort code, etc.) from a document, invoice or profile and want to know two things: is it a well-formed, checksum-valid number, and which `employer-org` (bank) and branch it routes to. The routing portion of an IBAN encodes the country and institution, so without touching any account you can resolve it to a named bank, its BIC/SWIFT and often a branch `address` — a useful corroboration or lead when a financial identifier appears in an investigation. Covers ~30+ European countries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to ibancalculator.com; use "Check an IBAN" to validate, or the bank-code/BIC finder to look up an institution.
2. Enter the IBAN (or just the country + bank code portion) — you do not need the full personal account number to identify the bank.
3. Read the result: validity/checksum verdict, the bank name (`employer-org`), BIC/SWIFT, and branch/`address` details where available.
4. For many numbers at once, note that bulk CSV and the API are paid.
5. Pivot: take the resolved bank + BIC into further due-diligence (jurisdiction, sanctions exposure); a country/bank mismatch can flag a fabricated IBAN.

## Inputs → Outputs
- **In:** `document-id` — an IBAN or a national bank/sort code
- **Out:** validity verdict, bank `employer-org`, BIC/SWIFT, branch `address`
- **Empty/negative result looks like:** "invalid" (bad checksum/format → likely fabricated or mistyped) or an unresolved code (country not covered, or a very new/small institution not in the directory).

## Gotchas & OpSec
- OpSec: **passive** — reference-table lookup; no bank or account is contacted.
- A valid checksum means well-formed, **not** that the account exists or is active.
- Coverage is Europe-centric; non-European numbers may not resolve to a named bank here.

## Overlaps ("do both")
- Pairs with official national bank-code registries and BIC directories — this is the quick check; the registry is authoritative for a decisive attribution.

## Trust & verifiability
`trust: community` — a reliable long-running reference tool; checksum math is deterministic, but confirm a bank/branch attribution against the official registry before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ibancalculator-com |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org, address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
