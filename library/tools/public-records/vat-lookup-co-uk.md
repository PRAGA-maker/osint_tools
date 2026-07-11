---
id: vat-lookup-co-uk
name: vat-lookup.co.uk
description: Use when you have a UK company `name` or a VAT number and want to resolve the other — returns the registered business name, VAT number, and address, plus VAT-registration history.
url: https://www.vat-lookup.co.uk/
category: public-records
path:
- public-records
bestFor: Reverse-looking-up a UK VAT number from a company name (or vice versa) and confirming the registered trading address.
selectorsIn:
- name
- employer-org
- address
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free third-party lookup covering 1.5M+ UK companies; no account. Occasionally returns HTTP 503 under load.
opsec: passive
opsecNote: A read-only lookup against a third-party VAT database; the business is not notified. Passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing third-party UK VAT database — useful, but not the official source; confirm critical VAT numbers against HMRC's own checker (gov.uk/check-uk-vat-number).
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- VAT Lookup UK
tags:
- companysites
- Company Related Sites
- vat
- uk
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# vat-lookup.co.uk

> A free reverse index of UK VAT registrations: name ⇄ VAT number ⇄ registered address, with registration history.

## When to use
You have a UK business — an `employer-org`/`name` tied to your subject — and you want its VAT number and registered trading `address`, or you have a VAT number and want to know which company it belongs to. VAT data confirms a business is real and trading, ties it to an address, and (via registration history) can reveal related companies sharing or transferring a number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vat-lookup.co.uk/.
2. Search by company `name` (reverse lookup) or by VAT number.
3. Read the result: registered business name, VAT number, address, and any registration-status/history notes (including companies linked to the same number).
4. **Verify** a critical VAT number against HMRC's official checker (gov.uk/check-uk-vat-number) before relying on it.
5. Pivot: the registered address feeds property/people work; the company name feeds `[[companies-house]]` for officers and filings.

## Inputs → Outputs
- **In:** company `name`/`employer-org`, or a VAT number, or `address`
- **Out:** registered `employer-org` name, VAT number, registered `address`, registration history
- **Empty/negative result looks like:** no match — meaning not VAT-registered (small businesses under the threshold aren't), deregistered, or a name-spelling miss. Absence of a VAT number does not mean the company doesn't exist.

## Gotchas & OpSec
- Third-party data can lag HMRC — treat it as a strong lead and confirm the actual number with HMRC's official checker.
- Only VAT-registered businesses appear; many legitimate small firms won't.
- OpSec: **passive**, read-only.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` and HMRC's official VAT checker — vat-lookup is fast for reverse lookup and history, Companies House gives officers/filings, and HMRC gives authoritative validity.

## Trust & verifiability
`trust: community` — a useful third-party aggregator, not the official register; verify the VAT number against HMRC for anything that matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vat-lookup-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, address → employer-org, address, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
