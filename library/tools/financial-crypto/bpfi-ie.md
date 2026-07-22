---
id: bpfi-ie
name: bpfi.ie Account Validation
description: Use when you have an Irish/UK `document-id` (account number + sort code) and want to confirm it is valid — returns a validity check and points to the owning bank via sort code.
url: https://bpfi.ie/customer-assist/account-validation/
category: financial-crypto
path:
- financial-crypto
bestFor: Confirming whether an account number / sort-code combination is structurally valid before acting on it.
selectorsIn:
- document-id
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public facility provided by the Banking & Payments Federation Ireland ("free of charge"). No account or payment.
opsec: passive
opsecNote: You validate a number against BPFI's checker, not against any bank account or its owner — nothing is disclosed to the account holder. It is a format/check-digit validation, not a live balance or ownership query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Banking & Payments Federation Ireland, the representative body for the Irish banking sector — an authoritative source for Irish sort-code/account validation.
missingPersonsRelevance: low
coverage:
- ie
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BPFI account validation
- Banking & Payments Federation Ireland
tags:
- banksites
- Banking Related Sites
- account-validation
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# bpfi.ie Account Validation

> The Irish banking federation's free checker that says whether an account number / sort-code combination is structurally valid — a sanity gate on financial identifiers found in an investigation.

## When to use
You have an account number and sort code (an Irish or UK-format `document-id`) from a document, invoice, or scam report and want to confirm it is a well-formed, valid combination before you build on it. Pair it with BPFI's separate Sort Code Database (`sortcode.bpfi.ie`) to map the sort code to the owning bank and branch. This validates and attributes an account identifier; it does not reveal the account holder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bpfi.ie/customer-assist/account-validation/ .
2. Enter the account number, or the account number + sort code combination, in the validation tool.
3. Read the result: valid / not valid for that combination.
4. Look up the sort code in the linked Sort Code Database (`sortcode.bpfi.ie`) to identify the `employer-org` (bank/branch) that owns it.
5. Pivot: a valid combo plus a known bank/branch narrows where an account sits — useful in fraud/scam attribution and corroborating documents.

## Inputs → Outputs
- **In:** `document-id` — account number (+ sort code)
- **Out:** validity result; via the sort-code database, the owning bank/branch (`employer-org`)
- **Empty/negative result looks like:** "not valid" for the combination — meaning the number fails the check digits/format, not necessarily that no such account ever existed. It never returns a name or balance.

## Gotchas & OpSec
- This is a **structural** validation (check digits / recognised sort code), not a confirmation that a live account exists or who owns it — do not overstate a "valid" result.
- Scope is Irish/UK sort-code + account formats; IBANs from other countries won't validate here (BPFI offers a separate Get-my-IBAN tool).
- OpSec: fully passive — no bank or account holder is contacted.

## Overlaps ("do both")
- Pair with the BPFI Sort Code Database and IBAN-decode references — validation tells you the number is well-formed, the sort-code lookup tells you which bank, and IBAN tools cover the international format.

## Trust & verifiability
`trust: trusted` — BPFI is the official representative body for banking in Ireland, so its validation and sort-code data are authoritative for the Irish/UK system, within the honest limit that it checks format, not ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bpfi-ie |
| category | financial-crypto |
| selectorsIn → selectorsOut | document-id → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
