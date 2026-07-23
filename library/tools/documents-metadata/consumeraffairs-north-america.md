---
id: consumeraffairs-north-america
name: ConsumerAffairs
description: Use when you have an `employer-org` (a company or brand name) and want customer complaints, ratings, and reviewer detail — returns associate/contact leads and business reputation signals.
url: https://www.consumeraffairs.com
category: documents-metadata
path:
- documents-metadata
bestFor: Reading crowdsourced customer reviews and complaints about a North American business.
selectorsIn:
- employer-org
selectorsOut:
- associate
- address
status: live
pricing: free
costNote: Free to browse and search reviews; the site monetises via lead-gen and brand partnerships, not a reader paywall.
opsec: passive
opsecNote: Browsing is passive and unauthenticated — you read published reviews. Posting a review yourself would be active and identifiable, so stay a reader unless you deliberately want to engage.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial review aggregator; reviews are moderated but crowdsourced and can be gamed or incentivised, so individual entries are unverified.
missingPersonsRelevance: low
coverage:
- us
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- trustpilot
- better-business-bureau
aliases:
- ConsumerAffairs
- consumeraffairs.com
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- business-reviews
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# ConsumerAffairs

> Crowdsourced review and complaint aggregator for North American businesses — useful for profiling a company or surfacing named reviewers tied to it.

## When to use
You have an `employer-org` or brand a subject is connected to (their employer, a business they ran, a company named in a case) and want independent signal on it: is it a real, active company, what do customers say, and are there named reviewers or staff responses that give you people to pivot on? Reviews often include first names, cities, and dated experiences.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.consumeraffairs.com and search the company/brand name in the top search bar.
2. Open the matching business page: it aggregates a star rating, review volume, and dated individual reviews.
3. Read the reviews for pivotable detail — reviewer first name + city, dates, product/plan names, and official brand replies (which sometimes name staff or support handles).
4. Cross-check the company's own claimed contact `address`/phone against other records.
5. Pivot: named reviewers feed people-search; a confirmed business + address feeds corporate-registry lookups.

## Inputs → Outputs
- **In:** `employer-org` (company / brand name)
- **Out:** business reputation signals, dated customer reviews, reviewer first-name/city `associate` leads, claimed business `address`
- **Empty/negative result looks like:** "no results" for the brand, or a bare page with zero reviews — the company may be too small, too new, or trading under a different name.

## Gotchas & OpSec
- Reviews are crowdsourced and moderated for a US/Canada consumer audience; small or non-North-American firms may be absent.
- Reviews can be incentivised, astroturfed, or retaliatory — never treat a single review as fact; look for patterns across many.
- OpSec: passive read only. Do not create an account or post to "test" a business; that is active and attributable.

## Overlaps ("do both")
- Pairs with `[[trustpilot]]` and `[[better-business-bureau]]` — each has different review populations and dispute records, so a business absent on one often appears on another.

## Trust & verifiability
`trust: unverified` — a legitimate, long-running commercial platform, but the reviews themselves are user-submitted and gameable; corroborate any lead before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | consumeraffairs-north-america |
| category | documents-metadata |
| selectorsIn → selectorsOut | employer-org → associate, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
