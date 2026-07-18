---
id: goodfirms
name: GoodFirms
description: Use when you have a company name and want its B2B profile — returns employer-org details, location/address, services, and named leadership from a reviewed vendor directory.
url: https://www.goodfirms.co/
category: public-records
path:
- public-records
bestFor: Researching IT/software/marketing/agency companies — profiles, locations, services, client reviews, and sometimes named executives.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- address
- social-profile
status: live
pricing: freemium
costNote: Free to browse company profiles and reviews; vendors pay for premium listings, and full lead/contact data may be gated.
opsec: passive
opsecNote: Public directory browsing; the company is not notified. Reviews and profiles are on GoodFirms' servers — standard web logging. Use a clean browser for sensitive research.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established B2B research/reviews directory; listings are partly vendor-submitted and reviews can be solicited, so treat profile claims as leads to verify.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- GoodFirms.co
- goodfirms
tags:
- public-records
- company-research
- b2b-directory
- reviews
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# GoodFirms

> A B2B research and reviews directory of IT, software, and marketing companies — a quick source of a firm's location, services, size, client reviews, and sometimes its leadership.

## When to use
You have an `employer-org` — typically a software house, dev shop, digital agency, or IT vendor — and want to flesh it out: headquarters `address`, hourly rates, team size, service lines, portfolio, client reviews, and links to its site/social (`social-profile`). Useful for vetting a company a subject claims to run or work for, or for mapping a small B2B firm that isn't well covered by mainstream business databases.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.goodfirms.co/ and search the company name (or browse by service + location).
2. Open the profile: read the HQ location, founding year, team size, hourly rate, services, portfolio, and reviews.
3. Note the outbound links (company website, LinkedIn) and any named leadership in the profile or reviews.
4. Pivot: the website/LinkedIn (`social-profile`) and HQ `address` feed corporate-registry and people searches; reviews may name clients and staff to profile further.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** `employer-org` (profile details), `address` (HQ/office), `social-profile` (site/LinkedIn links)
- **Empty/negative result looks like:** no profile — the firm isn't listed (common outside IT/marketing verticals or for very small/new companies), or it's a bare unclaimed stub with little data.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; some contact/lead data is gated behind vendor plans.
- OpSec: passive — the company isn't notified.
- Vendor-submitted bias: profiles and reviews are partly self-supplied and can be marketing; corroborate size, location, and claims against an official registry and the company's own site.

## Overlaps ("do both")
- Pairs with Clutch (a similar B2B reviews directory), `[[crunchbase]]`, and official company registries — GoodFirms is strong on agency/IT reviews, the others add funding, filings, and directors.

## Trust & verifiability
`trust: community` — a real, useful directory, but listings are partly vendor-driven; verify company facts against authoritative registries before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | goodfirms |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, address, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
