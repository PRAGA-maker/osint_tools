---
id: financial-post
name: Financial Post
description: Use when you have a `name` or `employer-org` and want to search Canadian business-news coverage for mentions — returns article context linking a person to companies, roles, and events.
url: https://financialpost.com/
category: communities-forums
path:
- communities-forums
bestFor: Searching Canadian business/financial news for coverage tying a person to companies, deals, executives, or legal/financial events.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Free to search and read many articles; some premium/National Post content sits behind a metered paywall.
opsec: passive
opsecNote: Searching and reading news articles is passive and leaks nothing about the subject. Standard news-archive research — no account required for the free tier.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Financial Post is a long-established Canadian business newspaper (part of Postmedia's National Post); its reporting is professionally edited and citable.
missingPersonsRelevance: low
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- financialpost.com
- National Post Financial Post
tags:
- toddington
- curated-directory
- news-journalism
- canada
source: toddington-resources
lastVerified: '2026-07-20'
---

# Financial Post

> Canada's major business newspaper — a searchable archive for tying a person to companies, executives, deals, and financial/legal events in Canadian coverage.

## When to use
You have a `name` or an `employer-org` with a Canadian nexus and want news corroboration: executive appointments, company filings covered in the press, bankruptcies, lawsuits, deals, or profiles. Financial Post (Postmedia/National Post) is a solid source for Canadian business and financial reporting, which often names individuals alongside their roles, companies, and `associate` connections. Its direct missing-persons value is low, but it's useful for the biographical/financial layer of a subject with a business profile.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://financialpost.com/ and use the site search for the subject's `name` or company.
2. Alternatively dork it: `site:financialpost.com "Full Name"` (often faster and cache-friendly for paywalled pieces).
3. Read matching articles for role, company affiliation, quotes, dates, and named associates.
4. Note bylines and cross-reference with National Post (shared Postmedia archive) for fuller coverage.
5. Pivot: named companies feed corporate-registry lookups; named associates and roles feed further people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org` (Canadian nexus)
- **Out:** news context linking the person to `employer-org`, roles, events, and named `associate` connections
- **Empty/negative result looks like:** no articles — expected for anyone without a public business profile; absence is not evidence of anything.

## Gotchas & OpSec
- Metered paywall on some premium/National Post content; the `site:` cache or a reader view often surfaces the text.
- Coverage skews to business/finance and Canada — a low-profile private individual usually won't appear.
- OpSec: fully passive news research.

## Overlaps ("do both")
- Pairs with corporate-registry and broader news-archive tools — Financial Post supplies Canadian business context; registries confirm the corporate facts it references.

## Trust & verifiability
`trust: trusted` — professionally edited journalism from an established outlet; individual articles are citable, though always confirm dates and details against the primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | financial-post |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
