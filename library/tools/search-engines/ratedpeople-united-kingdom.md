---
id: ratedpeople-united-kingdom
name: RatedPeople (United Kingdom)
description: Use when you have a UK tradesperson's `name`/`employer-org` or a `geolocation` and want their trade profile — returns `social-profile`, `employer-org`, reviews, and service area.
url: http://www.ratedpeople.com
category: search-engines
path:
- search-engines
bestFor: Finding a UK tradesperson's business profile, reviews, gallery, and coverage area.
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- social-profile
- employer-org
- geolocation
status: live
pricing: free
costNote: Free for homeowners to browse tradesperson profiles and post jobs; tradespeople pay for leads, but their public profiles are viewable without payment.
opsec: passive
opsecNote: Browsing tradesperson profiles is passive and does not notify them. Posting a job would generate outreach and expose you — don't post a job just to investigate; stay on the public profiles.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A large, active UK trade marketplace; reviews are user-submitted and profiles self-managed, so treat stated business details as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ratedpeople.com
- Rated People
tags:
- toddington
- curated-directory
- specialty-search
- uk
- trades
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# RatedPeople (United Kingdom)

> A large UK marketplace connecting homeowners with tradespeople — useful for profiling a subject who works a trade: their business name, reviews, work gallery, and the areas they cover.

## When to use
Your subject is (or may be) a UK tradesperson — electrician, plumber, builder, gardener, roofer, etc. — and you want their public footprint: trading name (`employer-org`), the region they serve (`geolocation`), a photo gallery of their work, and customer reviews that can reveal locations, dates, and even client names. This is a way to place a self-employed subject geographically and confirm an occupation when formal records are thin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open ratedpeople.com and use the location + trade search, or search a known business/`name`.
2. Open matching tradesperson profiles: read the business name, service area, review text, ratings, and job/photo gallery.
3. Mine reviews and galleries for incidental detail — town names, job dates, sometimes reviewer names and neighbourhoods.
4. Do **not** post a job to make contact — that triggers real outreach and reveals you; stay on public profiles.
5. Pivot: feed the trading name into UK Companies House / corporate tools, the service area into records/maps, and any linked website into WHOIS.

## Inputs → Outputs
- **In:** `name`/`employer-org` (trade business) or `geolocation` + trade
- **Out:** tradesperson `social-profile` (business name, reviews, gallery), `employer-org`, service-area `geolocation`
- **Empty/negative result looks like:** no matching tradesperson in the area/trade — the subject isn't on this platform (many use rivals like Checkatrade); weak negative evidence.

## Gotchas & OpSec
- Reviews and profiles are user-managed and can be curated/gamed — corroborate business details elsewhere.
- Coverage is UK-only and trade-focused; irrelevant for non-tradespeople.
- OpSec: passive when browsing; posting a job is active outreach — avoid it for investigation.

## Overlaps ("do both")
- Pairs with UK Companies House, WHOIS, and rival trade directories (e.g. Checkatrade) — RatedPeople gives the public trade profile; those confirm legal ownership and cross-check the business.

## Trust & verifiability
`trust: unverified` — a real, active marketplace, but profiles and reviews are user-submitted; treat business details as leads to confirm against official UK records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ratedpeople-united-kingdom |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org, geolocation → social-profile, employer-org, geolocation |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
