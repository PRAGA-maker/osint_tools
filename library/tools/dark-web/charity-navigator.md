---
id: charity-navigator
name: Charity Navigator
description: Use when you have a US nonprofit `employer-org` (or a person's charity affiliation) and want its financials, ratings and leadership — returns EIN, finances and named officers/associates.
url: https://www.charitynavigator.org/
category: dark-web
path:
- dark-web
bestFor: Researching a US nonprofit's finances, rating, EIN and leadership from IRS-sourced data.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- associate
status: live
pricing: free
costNote: Free to search and view charity profiles, ratings, and financial summaries; no account required for lookups.
opsec: passive
opsecNote: A public nonprofit-research lookup drawing on IRS filings — nothing about any individual is queried live and no one is alerted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A 25+ year nonprofit evaluator rating 245,000+ charities using IRS Form 990 data; financials are sourced from public filings and are verifiable against the IRS.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- charitynavigator.org
tags:
- toddington
- curated-directory
- specialty-search
- nonprofit
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Charity Navigator

> The big US charity evaluator — a fast route from a nonprofit's name to its EIN, finances, rating, and the people who run it.

## When to use
Your subject is connected to a US nonprofit — as founder, officer, board member, employee, or donor — or you're vetting an organisation itself (a suspicious "charity," a fundraiser tied to a case). Charity Navigator turns the `employer-org` name into IRS-sourced financials, an accountability rating, the EIN, and often named leadership, letting you confirm an organisation is real, gauge its finances, and pull people connected to it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.charitynavigator.org/ and search the nonprofit's name.
2. Open its profile and read:
   - EIN, mission, category, and location,
   - financial summary (revenue, expenses, executive compensation) from Form 990,
   - accountability/transparency and (where rated) star rating,
   - listed leadership/officers where shown.
3. Cross-reference: use the EIN to pull the full Form 990 elsewhere (ProPublica Nonprofit Explorer, IRS TEOS) for complete officer lists and compensation.
4. Pivot: named officers/board (`associate`, `name`) → people-search; EIN → full filings; address → the org's physical footprint.

## Inputs → Outputs
- **In:** nonprofit `employer-org` name (or a person's charity affiliation)
- **Out:** EIN, financials, rating, and named leadership (`name`/`associate`) for that `employer-org`
- **Empty/negative result looks like:** not found or "not rated" — small nonprofits (under revenue thresholds), very new orgs, and non-501(c)(3) entities may be absent or unrated. Absence isn't proof the org is fake; check the IRS TEOS/ProPublica directly.

## Gotchas & OpSec
- US 501(c)-focused; foreign charities and tiny orgs may not appear.
- Financials lag (990s are filed annually, often a year+ behind) — treat figures as historical.
- Ratings are Charity Navigator's methodology; the raw financials come from the IRS and are the verifiable part.

## Overlaps ("do both")
- Do both with ProPublica Nonprofit Explorer and IRS Tax-Exempt Organization Search (full 990s, complete officer lists, EIN verification) and a business-registry/people-search for the individuals. Charity Navigator is the fast profile; those give the exhaustive record.

## Trust & verifiability
`trust: trusted` — an established evaluator built on public IRS Form 990 data; the underlying financials are authoritative and independently verifiable, while the star rating is an interpretive layer you can set aside if you only need the facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | charity-navigator |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
