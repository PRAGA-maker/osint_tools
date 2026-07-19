---
id: business-com
name: Business.com
description: Use when you have an `employer-org` and want B2B context — a business advice/reviews site that can corroborate a company's existence and category, but not look up people.
url: https://www.business.com
category: communities-forums
path:
- communities-forums
bestFor: Light corroboration of a small/mid-size US business's category and services; NOT a people-search or person-lookup tool.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free to read articles, guides and B2B service listings/reviews; it is ad/lead-generation funded.
opsec: passive
opsecNote: Read-only browsing of a public content/reviews site; nothing is attributed to your subject. It exposes company-level marketing content, not personal data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial B2B media and vendor-reviews site (business advice plus a services directory). Content is editorial/marketing and lead-gen; treat listings and reviews as promotional, not authoritative.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- business.com
tags:
- toddington
- curated-directory
- news-journalism
- b2b
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Business.com

> A B2B media and vendor-reviews site — useful only as thin corroboration that a business exists in a category, with essentially no person-level OSINT value.

## When to use
You have an `employer-org` (typically a US small/mid-size business or B2B vendor) and want a quick, low-value sanity check that it operates in the category it claims — via Business.com's guides, listings or service reviews. It does not let you search for a specific person and returns no personal data, so its missing-persons value is marginal. Reach for real company registries first; use this only as incidental supporting colour.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the web or Business.com for the company/category (e.g. a vendor listing or a "best X services" roundup).
2. Read any listing/review to confirm the business's stated category, services, and rough footprint.
3. Treat everything as marketing/lead-gen — listings and reviews are promotional, not vetted facts.
4. Do not expect owner/officer or contact-person data; it is company-level content only.
5. Pivot: a confirmed `employer-org`/category feeds proper registry lookups (e.g. [[creditrisk-monitor]], state registries) for authoritative detail.

## Inputs → Outputs
- **In:** `employer-org` (a business/category)
- **Out:** `employer-org` category/services corroboration (promotional)
- **Empty/negative result looks like:** no listing/article — the business simply isn't covered, which says nothing about whether it exists.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive**; nothing about your subject is disclosed.
- It is a lead-gen media property, not a registry or people index; do not rely on its listings/reviews as verified fact, and don't expect to find individuals here.

## Overlaps ("do both")
- Pairs with authoritative company sources — [[creditrisk-monitor]], national/state business registries — which actually verify a company and its officers; Business.com only offers promotional context.

## Trust & verifiability
`trust: unverified` — commercial B2B media with promotional listings and reviews; useful only as soft corroboration, with all substantive checks done via official registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | business-com |
| category | communities-forums |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
