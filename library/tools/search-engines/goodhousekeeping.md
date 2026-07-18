---
id: goodhousekeeping
name: Good Housekeeping
description: Use when you have a `name` featured or quoted in lifestyle/consumer media and want that mention — returns social-profile.
url: http://www.goodhousekeeping.com/product-reviews
category: search-engines
path:
- search-engines
bestFor: Searching a large consumer/lifestyle publication for a subject featured, quoted, or credited (expert, contributor, human-interest).
selectorsIn:
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, ad-supported (Hearst); no account required to read or search.
opsec: passive
opsecNote: Reading and searching published articles is invisible to any subject. Standard browsing hygiene is sufficient.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established Hearst consumer/lifestyle publication with an edited product-testing lab; bylined content is attributable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- goodhousekeeping.com
- Good Housekeeping Institute
tags:
- news-journalism
- lifestyle
- specialty-search
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Good Housekeeping

> A mass-market consumer/lifestyle publication — a low-yield source worth a name pass only when the subject is a quoted expert, contributor, or human-interest subject in lifestyle media.

## When to use
This is a narrow, low-priority source. Reach for it when the subject plausibly appears in consumer/lifestyle journalism — a quoted expert (a doctor, chef, tester, or product designer), a contributor/byline, or a human-interest feature. A hit ties a `name` to a dated article and an author/contributor page (`social-profile`). For most missing-person subjects there will be nothing here; do not spend long on it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the site's search, or a scoped engine query: `site:goodhousekeeping.com "Jane Doe"`.
2. Read matching articles for the subject as author, quoted expert, or feature subject.
3. Note the credited role, employer, and any people named alongside them.
4. Pivot: contributor page → `social-profile`/bio; stated role/employer → `employer-org`; co-named people → `associate`.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile` (author/mention/feature page)
- **Empty/negative result looks like:** no articles match — the expected outcome for the vast majority of subjects; means only that there is no footprint in this one publication.

## Gotchas & OpSec
- Very low base-rate of useful hits — treat this as a completeness check, not a primary lead source.
- Single-outlet coverage; a null result is meaningless.
- OpSec: passive read; safe.

## Overlaps ("do both")
- Only useful as one line in a broad `site:`-style media sweep across many publications; never rely on it alone.

## Trust & verifiability
`trust: trusted` — an edited, bylined publication, so any mention is attributable to a dated article; still corroborate the underlying facts against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goodhousekeeping |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
