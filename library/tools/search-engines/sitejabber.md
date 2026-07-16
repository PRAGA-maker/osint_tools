---
id: sitejabber
name: Sitejabber
description: Use when you have a business `domain` or company name and want consumer reviews and reviewer profiles for it — returns review content and `social-profile` reviewer accounts.
url: https://www.sitejabber.com/
category: search-engines
path:
- search-engines
bestFor: Reading consumer reviews of a website/business and mining the reviewer profiles that wrote them.
selectorsIn:
- domain
- employer-org
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free to read reviews and reviewer profiles; the platform's paid products (now branded SmartCustomer) target businesses, not readers.
opsec: passive
opsecNote: Reading public reviews and profiles reveals nothing about your subject to the site or to the reviewers. Passive; normal browsing hygiene applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running consumer-review platform (business side now "SmartCustomer"); reviews are user-generated and can be gamed, so weigh them as leads, not proof.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- sitejabber.com
- SmartCustomer
tags:
- toddington
- curated-directory
- specialty-search
- reviews
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# Sitejabber

> A consumer-review platform for websites and businesses — read what buyers say about a company, and pull the reviewer profiles behind those reviews.

## When to use
You have a business `domain` or company name (`employer-org`) and want (a) consumer sentiment and complaints about it — useful for vetting a company tied to a subject or a suspected scam — or (b) the reviewer accounts (`social-profile`) who posted, which can themselves be pivot points. Review sites also sometimes surface names, locations and other detail volunteered in review text.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sitejabber.com/ (the homepage may redirect to the business-facing SmartCustomer brand; review and profile URLs remain on sitejabber.com).
2. Search for the company/website by name or domain, or open a `sitejabber.com/reviews/<business>` page directly.
3. Read the reviews and their verdicts/ratings; open reviewer profiles at `sitejabber.com/users/<username>` (`social-profile`).
4. Read the output: aggregated reviews, individual review text, and reviewer accounts with their review history.
5. Pivot: take a reviewer's `username` into cross-platform username searches; mine review text for names/locations; cross-check the business against other review sites.

## Inputs → Outputs
- **In:** `domain` / `employer-org` (business or website)
- **Out:** `social-profile` (reviewer accounts), plus review content and ratings
- **Empty/negative result looks like:** a business with no reviews returns an empty/placeholder page — it has not been reviewed here; try Trustpilot or the BBB.

## Gotchas & OpSec
- Reviews are user-generated and susceptible to fakes and paid manipulation in both directions — treat them as leads, corroborate before relying.
- The platform rebranded its business side to SmartCustomer; the consumer review corpus persists on sitejabber.com URLs.
- OpSec: passive; reading reviews signals nothing to anyone.

## Overlaps ("do both")
- Complements other review platforms (Trustpilot, BBB): cross-reference the same business across sites to separate genuine signal from manipulated ratings.

## Trust & verifiability
`trust: community` — a mainstream but user-generated review site. Individual reviews and profiles are unverified; use them as investigative leads, not evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sitejabber |
| category | search-engines |
| selectorsIn → selectorsOut | domain, employer-org → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
