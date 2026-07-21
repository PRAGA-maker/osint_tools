---
id: ezilon
name: Ezilon
description: Use when you have an `employer-org` or business `name` in a specific world region and want a human-curated directory listing to confirm it exists and find its site/address — returns business links and regional context.
url: http://www.ezilon.com
category: public-records
path:
- public-records
bestFor: A region-organized web directory for locating and corroborating a business or organization by country/region.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- domain
- address
status: live
pricing: free
costNote: Free to browse and search; ad-supported directory, no account needed.
opsec: passive
opsecNote: Directory browsing is passive and reveals nothing to the subject. It relies on manual editorial submissions, so treat listings as leads to confirm, not authoritative records.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running (since 2002) human-edited regional web directory; entries are self-submitted and can be stale, so corroborate anything you rely on.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ezilon.com
- Ezilon regional directory
tags:
- company-research
- web-directory
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Ezilon

> A human-curated, region-organized web directory — a Yahoo-Directory-style index for finding and cross-checking businesses and organizations by world region.

## When to use
You have a business or organization name (`employer-org`) — perhaps a subject's employer or a company tied to a lead — and want an independent, region-scoped listing to confirm it exists, find its website, or place it geographically. Editorial directories like Ezilon can corroborate a small or regional business that isn't well-covered by mainstream search, and its regional organization helps when you know the country but not the exact entity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.ezilon.com.
2. Drill down by region (North America, Europe/UK, Asia, Africa, Middle East, South America, Oceania) or use the directory search.
3. Narrow into a topical category (Business, Health, Travel, News, etc.) matching the entity.
4. Read the listing for the organization's `domain`, description, and sometimes `address`/region.
5. Pivot: the linked site or address feeds domain/WHOIS tools and public-records lookups; a confirmed regional presence supports or refutes a lead about where a subject works or operates.

## Inputs → Outputs
- **In:** `employer-org` / business `name` (with a region in mind)
- **Out:** directory listing → `domain`, regional `address`, corroboration the entity exists
- **Empty/negative result looks like:** no matching listing — expected for many entities, since it's an editorial directory with partial coverage; absence is not evidence the business doesn't exist.

## Gotchas & OpSec
- Editorial + self-submitted: coverage is uneven and listings can be years out of date — verify the linked site is live and current.
- It is a directory, not a records database — no ownership, filings, or personal data; use it to find and place an entity, then pivot to authoritative registries.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with company-registry and WHOIS/domain tools — Ezilon helps you locate and place a business; the registry/WHOIS then gives authoritative ownership and infrastructure detail.

## Trust & verifiability
`trust: unverified` — a long-lived but manually curated directory of self-submitted listings; useful as a corroborating lead, not a primary source. Confirm anything material against an official registry or the entity's own site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ezilon |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, domain, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
