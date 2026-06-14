---
id: hib-ransomed
name: HIB Ransomed
description: Use when you want to check whether an email/domain appears in ransomware-leak or breach datasets.
url: https://haveibeenransom.com/
category: email
path:
- email
bestFor: Checking an email or domain against ransomware-leak / breach data.
selectorsIn:
- email
- domain
selectorsOut:
- email
- metadata-exif
status: unknown
pricing: free
costNote: Appears to be a free breach/ransomware-leak lookup; confirm on the live site.
opsec: passive
opsecNote: Queries a leak/breach index; the target is not notified. You disclose the searched value to the site operator.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A 'Have I Been Ransomed?'-style breach-search engine. Dataset provenance, operator, and current uptime are unconfirmed without checking the live site; treat hits as leads, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Have I Been Ransomed
- haveibeenransom.com
tags:
- data-breach-search-engines
relatedTools:
- have-i-been-pwned
- heroic-now
- iknowyour-dad
source: awesome-osint
lastVerified: ''
enrichment: full
---

# HIB Ransomed

> A "Have I Been Ransomed?"-style breach-search engine: check whether an email or domain appears in ransomware-leak / breach datasets.

## When to use
You have an `email` or `domain` for a missing person or associated organisation and want to know if it surfaced in ransomware dump sites or breach compilations — useful as an alternate aggregator that may index leaks the mainstream services miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://haveibeenransom.com/.
2. Enter the `email` or `domain`.
3. Read returned hits — which leak/dump the value appeared in.
4. Pivot any associated service or breach name to account-enumeration tools.

## Inputs → Outputs
- **In:** `email`, `domain`
- **Out:** leak/breach hit names and exposed-data indications (`metadata-exif`-style)
- **Empty/negative result looks like:** no records found; means the value isn't in this index (does not rule out exposure elsewhere).

## Gotchas & OpSec
- Operator and dataset provenance are unverified — corroborate hits with a trusted source before acting.
- OpSec: passive toward the target; you disclose the queried value to an unknown operator, so consider OpSec for sensitive lookups.

## Overlaps ("do both")
- Corroborate with `[[have-i-been-pwned]]` (authoritative) and other aggregators `[[heroic-now]]` / `[[iknowyour-dad]]`.

## Trust & verifiability
`trust: unverified` — niche breach-search engine with unknown provenance; useful as a lead generator but verify any hit against a trusted index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hib-ransomed |
| category | email |
| selectorsIn → selectorsOut | email, domain → email, metadata-exif |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
