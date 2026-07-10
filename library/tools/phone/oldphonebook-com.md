---
id: oldphonebook-com
name: Oldphonebook.com
description: Use when you have a `name` or `phone` and want a historical US listing (back to ~1994) — returns the archived name, address and phone from old telephone directories.
url: http://www.oldphonebook.com/
category: phone
path:
- phone
bestFor: Finding a person's historical US address/phone from archived white-pages directories going back roughly two decades.
selectorsIn:
- name
- phone
selectorsOut:
- name
- address
- phone
status: live
pricing: freemium
costNote: Basic historical search is free; some full-detail/older records or bulk access are gated behind paid options.
opsec: passive
opsecNote: A directory-archive lookup; the subject is not notified. Nothing you search leaves a trace with the target. Use normal browser hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party historical phonebook archive. Data is old by design and only covers listed (non-ex-directory) numbers, so treat hits as period-accurate, not current.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- new-canada-411
aliases:
- Old Phone Book
- historical white pages
tags:
- phone
- historical
- reverse-lookup
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Oldphonebook.com

> A historical US white-pages archive: search names and numbers as they were listed going back roughly to 1994.

## When to use
You are reconstructing a subject's history and need a *past* US `address` or `phone` rather than a current one — to place someone at an address years ago, find a former number that unlocks other records, or resolve a lead that only makes sense against an older listing. Search by `name` to find historical listings, or reverse a `phone` to see who held it (bearing in mind area codes may have changed).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.oldphonebook.com/.
2. Search by `name` (person you're tracing) or enter a `phone` for a historical reverse lookup.
3. Read results: archived listings show name, address, and number as printed in directories of that era (coverage reaches back ~20 years).
4. Note the vintage — a match reflects where/when the person was *then*, not now.
5. Pivot: an old address feeds people-search and property tools; a former number can surface accounts tied to it historically.

## Inputs → Outputs
- **In:** `name` or `phone`
- **Out:** historical `name`, `address`, `phone` from archived directories
- **Empty/negative result looks like:** no listing. The person may have had an unlisted/ex-directory number (never printed), or predates/postdates coverage — absence is not proof they didn't live there.

## Gotchas & OpSec
- Data is intentionally historical; do not treat an address/number as current.
- Area codes and street names change over decades — a reverse-phone hit may map to an old area code split.
- Only listed numbers appear; unlisted subscribers are invisible.
- OpSec: passive; the subject is not alerted.

## Overlaps ("do both")
- Pairs with `[[new-canada-411]]` for the Canadian directory equivalent, and with current US people-search tools — old vs current listings together build an address timeline.

## Trust & verifiability
`trust: community` — a third-party archive of published directory data. The listings are authentic to their period but stale by design, so use them to establish history and confirm current details elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oldphonebook-com |
</content>
