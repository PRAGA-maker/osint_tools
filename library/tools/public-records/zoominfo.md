---
id: zoominfo
name: ZoomInfo
description: Use when you have a person `name` or `employer-org` and want their job title, company and colleagues — returns employer-org, address and associate links from public B2B profile pages.
url: https://www.zoominfo.com/
category: public-records
path:
- public-records
bestFor: Reading ZoomInfo's free, search-indexed B2B profile pages for a person's title/employer or a company's location and staff roster.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: freemium
costNote: The platform (bulk contacts, direct emails/phones) is a paid subscription, but individual person and company profile pages are free to view and indexed by search engines — that public layer is the OSINT value.
opsec: passive
opsecNote: Viewing an indexed public profile page is passive. The full platform requires an account and gates contact details behind login/payment; do not create an account tied to your identity if you want to stay clean.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial B2B data aggregator; titles/employers are often accurate but can be stale or auto-scraped — corroborate before relying.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- zoominfo.com
- DiscoverOrg
tags:
- toddington
- curated-directory
- company-search
- b2b-contacts
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# ZoomInfo

> A commercial B2B contact database whose free, search-indexed profile pages leak a person's title, employer and colleagues, and a company's HQ location and staff roster.

## When to use
You have a working-age subject with a professional/office job, or a company (`employer-org`), and want to establish their role, employer, and workplace network. ZoomInfo maintains public person pages (`/p/First-Last/...`) and company pages (`/c/company/...`) that surface job title, current employer, general location, and "colleagues/people also viewed" — usable via search engines without paying. The direct email and mobile number are the paid product, but the org/title/associate context is often free.

## How to use it (`bestInteractionPattern`: web-manual)
1. Don't log in. Instead, dork a search engine: `site:zoominfo.com "<Full Name>"` or `site:zoominfo.com/p <name> <company>`.
2. Open the indexed profile page. Read: current title, `employer-org`, city/region, and the listed colleagues/related people (`associate`).
3. For a company, open its `/c/` page for HQ `address`, phone, employee count, revenue band and a partial staff list.
4. If the page blurs contact fields behind "sign in / upgrade," stop — that's the paywall; harvest only what's public.
5. Pivot: title + employer → LinkedIn/company-site confirmation; colleagues → expand the associate network; company HQ → address OSINT.

## Inputs → Outputs
- **In:** person `name` (± company) or `employer-org`
- **Out:** job title, current `employer-org`, general location, colleague `associate` links; company HQ `address`, phone, size
- **Empty/negative result looks like:** no public profile, or a stub page with everything gated behind login — many individuals aren't covered, and B2B data skews to office/professional roles, missing most of the general public.

## Gotchas & OpSec
- Human-in-the-loop: contact details (email/phone) sit behind a payment/login wall — the free layer is title/employer/location only.
- Data can be stale — someone's listed employer may be several jobs out of date; always corroborate.
- Coverage bias: strong on US/EU corporate professionals, weak on non-office workers and private individuals.
- OpSec: passive when viewing indexed pages; creating an account leaves a footprint and may not help.

## Overlaps ("do both")
- Pairs with LinkedIn and company-website "team" pages — ZoomInfo often exposes a title/colleague set even when a LinkedIn profile is locked, and vice versa; cross-check to catch stale data.

## Trust & verifiability
`trust: unverified` — a commercial aggregator built partly from scraped/contributed data; treat title, employer and location as strong leads to confirm, not as authoritative facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zoominfo |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
