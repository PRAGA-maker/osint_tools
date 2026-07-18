---
id: uk-law-society
name: UK Law Society — Find a Solicitor
description: Use when you have a `name` or firm and want to confirm a solicitor in England & Wales — returns the solicitor's firm, practice areas, and regulated status.
url: https://solicitors.lawsociety.org.uk
category: search-engines
path:
- search-engines
bestFor: Confirming and locating a solicitor (or law firm) regulated in England & Wales via the official register.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
status: live
pricing: free
costNote: Free official register; no account required.
opsec: passive
opsecNote: You query the public register of solicitors, not the individual — nothing is signalled to the subject. Standard web logging applies on the Law Society's side.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official Law Society "Find a Solicitor" register, drawing on SRA-regulated records; authoritative for who is a practising solicitor in England & Wales.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Find a Solicitor
- Law Society solicitor register
- solicitors.lawsociety.org.uk
tags:
- toddington
- curated-directory
- legal
- professional-register
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# UK Law Society — Find a Solicitor

> The official register of solicitors in England & Wales — confirm a named solicitor, find their firm and practice areas, and verify they're currently regulated.

## When to use
You have a `name` that may be a solicitor, or a law firm (`employer-org`), and need to confirm the person is a genuine, currently-practising, SRA-regulated solicitor and locate their firm/office. Useful for vetting legal contacts, tracing which firm represents a party, or confirming a professional identity claim in an investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://solicitors.lawsociety.org.uk.
2. Use Quick Search (name/firm/location) or Pro Search (filter by practice area, language, etc.).
3. Enter the `name` or firm and any location to disambiguate.
4. Read the result: the solicitor's firm, office `address`, practice areas, and regulated status (or the firm's details).
5. Pivot: the firm/office `address` and colleagues feed corporate and people-search follow-ups; confirmed regulation corroborates a professional identity.

## Inputs → Outputs
- **In:** `name` (person) or `employer-org` (firm)
- **Out:** firm/employer, office `address`, practice areas, regulated status
- **Empty/negative result looks like:** no listing — the person isn't a solicitor regulated in England & Wales (they may be a barrister, a solicitor in Scotland/NI/other jurisdiction, non-practising, or not a lawyer at all), not proof they don't exist.

## Gotchas & OpSec
- Scope is **England & Wales solicitors** only — barristers (see the Bar Standards Board), Scottish/NI lawyers, and paralegals won't appear here.
- Listings reflect regulated practice; a common name may return several solicitors — confirm with firm/location.
- OpSec: passive; a public professional register.

## Overlaps ("do both")
- Pairs with the SRA register and the Bar Standards Board "Barristers' Register" — use those to cover regulation detail and barristers respectively, and Companies House for the firm as an entity.

## Trust & verifiability
`trust: trusted` — the official Law Society register backed by SRA regulation data, authoritative for practising solicitors in England & Wales.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-law-society |
