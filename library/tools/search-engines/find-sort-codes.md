---
id: find-sort-codes
name: Find Sort Codes
description: Use when you have a UK bank `document-id` (sort code) or a bank name and want to resolve the other — returns the bank/branch behind a sort code, or the sort codes for a bank.
url: http://findsortcodes.co.uk/
category: search-engines
path:
- search-engines
bestFor: Looking up which UK bank and branch a six-digit sort code belongs to, and the reverse (sort codes for a named bank).
selectorsIn:
- document-id
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free public lookup site, no account. Ad-supported; occasionally slow/unavailable, but the sort-code data itself is free to query.
opsec: passive
opsecNote: You look up reference banking data (a sort code → branch mapping); nothing is sent to or about a person, so this is fully passive. No sock-puppet needed beyond normal hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party UK sort-code directory. Sort-code→bank mappings are public reference data; cross-check important results against the official bank or another sort-code checker.
missingPersonsRelevance: low
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- findsortcodes.co.uk
- Sort Code Finder
tags:
- toddington
- curated-directory
- specialty-search
- uk-banking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Find Sort Codes

> A free UK sort-code directory: turn a six-digit sort code into the bank and branch it belongs to, or find the sort codes for a named bank.

## When to use
You've encountered a UK bank `document-id` — a sort code, e.g. on a payment, invoice, receipt, or leaked document — and want to know which bank and branch it maps to. Or you have a bank name and want its sort-code range. In an investigation this is a small corroboration step: confirming the institution/branch behind a number tied to a subject, or sanity-checking a document's authenticity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://findsortcodes.co.uk/ (retry if slow — the site is ad-supported and sometimes lags).
2. Enter the six-digit sort code (with or without dashes) to look up the owning bank/branch, or search by bank name for the reverse.
3. Read the result: the bank, branch name, and often a branch address for that sort code.
4. Pivot: a branch `address` can localise where an account was opened; the bank name corroborates document provenance.

## Inputs → Outputs
- **In:** UK sort code (`document-id`) or bank name (`employer-org`)
- **Out:** owning bank (`employer-org`) + branch name/`address`
- **Empty/negative result looks like:** "not found" / no match — the code may be new, reassigned, or mistyped; a branch address may be a central/administrative one rather than a high-street location.

## Gotchas & OpSec
- UK-only — sort codes are a British construct; irrelevant for non-UK banking.
- Branch data can be dated as banks merge/close branches; a mapped branch may no longer physically exist.
- A sort code identifies a bank/branch, not an account holder — it does not reveal who owns an account.
- OpSec: fully passive reference lookup.

## Overlaps ("do both")
- Cross-check important mappings against a second UK sort-code checker or the bank directly, since third-party directories can lag official reassignments.

## Trust & verifiability
`trust: unverified` — an independent directory of public banking reference data. Reliable enough for orientation, but confirm anything material against the bank's own details or an alternate checker.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-sort-codes |
| category | search-engines |
| selectorsIn → selectorsOut | document-id, employer-org → employer-org, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
