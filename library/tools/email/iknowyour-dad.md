---
id: iknowyour-dad
name: IKnowYour.Dad
description: Use when you want to check an email/username against an aggregated breach-data search engine for leaked records.
url: https://iknowyour.dad/
category: email
path:
- email
bestFor: Searching an email or username against aggregated breach/leak datasets.
selectorsIn:
- email
- username
selectorsOut:
- email
- metadata-exif
status: unknown
pricing: free
costNote: Appears to be a free breach-search front end; confirm pricing/availability on the live site.
opsec: passive
opsecNote: Queries an aggregated leak index; the target is not notified. You disclose the searched value to an unknown operator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Listed under "data-breach-search-engines" on awesome-osint. Operator identity, dataset provenance, and current uptime are unknown; the playful domain suggests a hobby/community project. Treat hits as leads, verify against a trusted index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- data-breach-search-engines
relatedTools:
- have-i-been-pwned
- heroic-now
- hib-ransomed
source: awesome-osint
lastVerified: ''
enrichment: full
---

# IKnowYour.Dad

> A community breach-data search engine: check an email or username against aggregated leak datasets. Provenance is unknown — use as a lead generator, not as proof.

## When to use
You have an `email` or `username` for a missing person or associate and want an additional breach aggregator that may index dumps the mainstream services miss. Best as a corroborating source alongside an authoritative index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://iknowyour.dad/.
2. Enter the `email` or `username`.
3. Read returned hits — which leaks/datasets the value appears in and any exposed attributes.
4. Pivot breach/service names to account-enumeration tools.

## Inputs → Outputs
- **In:** `email`, `username`
- **Out:** breach/leak hits and exposed-data attributes (`metadata-exif`-style)
- **Empty/negative result looks like:** no records found — not in this index (does not rule out exposure elsewhere).

## Gotchas & OpSec
- Operator and data provenance are unverified — do not treat hits as confirmed; corroborate.
- OpSec: passive toward the target, but you reveal the queried value to an unknown third party — consider OpSec for sensitive lookups (use a sock-puppet network/VPN).

## Overlaps ("do both")
- Corroborate with `[[have-i-been-pwned]]` (authoritative) and alternate aggregators `[[heroic-now]]` / `[[hib-ransomed]]`.

## Trust & verifiability
`trust: unverified` — niche/community breach-search engine of unknown origin; useful for leads, but verify every hit against a trusted source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iknowyour-dad |
| category | email |
| selectorsIn → selectorsOut | email, username → email, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
