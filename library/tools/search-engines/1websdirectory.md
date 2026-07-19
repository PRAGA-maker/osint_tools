---
id: 1websdirectory
name: 1WebsDirectory
description: Use when you have an `employer-org`/business name and want a directory listing — returns the business's website and category/country classification.
url: http://www.1websdirectory.com/
category: search-engines
path:
- search-engines
bestFor: Looking up a small business in a browsable web directory to find its website, category, and country.
selectorsIn:
- employer-org
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free general web directory browsable by category, keyword, and country; free (often paid-featured) business submissions.
opsec: passive
opsecNote: Passive browsing of a public directory; no subject interaction. Low-traffic directory site — use a clean browser for ad/tracker hygiene, but there is no target footprint.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A general-purpose, submission-driven web directory of the early-2000s type; listings are self-submitted and unvetted, so treat any entry as a lead to verify.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- 1WebsDirectory
- 1websdirectory.com
tags:
- web-directory
- business-directory
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# 1WebsDirectory

> A general submission-based web directory — a low-signal way to find a small business's website and category, and occasionally to cluster related listings.

## When to use
You have an `employer-org`/business name (often a small or older business) and general search isn't surfacing its site. Browsable directories like this sometimes hold listings — with the business's `domain`, category, and country — that never ranked well elsewhere. It's a supplementary lead source, not a primary one; expect thin, dated data.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.1websdirectory.com/ and browse by category/country, or search by keyword/business name.
2. Open a listing for the business's website (`domain`), category, description, and country.
3. Note the linked site and any contact details in the listing.
4. Pivot: the `domain` feeds WHOIS/DNS and site analysis; the category/country narrows further searches; corroborate the listing against the business's own site.

## Inputs → Outputs
- **In:** `employer-org`/business name (or keyword)
- **Out:** business website (`domain`), category, country
- **Empty/negative result looks like:** no listing — most businesses aren't in any given small directory; absence means nothing, so don't over-read it.

## Gotchas & OpSec
- Self-submitted, unvetted, and often stale — listings can be years out of date or SEO spam.
- Low coverage; use only as a supplementary lead alongside mainstream search and registries.
- OpSec: passive browsing.

## Overlaps ("do both")
- Complements business registries and general search — this occasionally surfaces an old listing others miss, but confirm everything against authoritative sources.

## Trust & verifiability
`trust: unverified` — a submission-driven directory with no vetting; every listing is a lead to confirm, never evidence on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 1websdirectory |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org → domain, employer-org |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
