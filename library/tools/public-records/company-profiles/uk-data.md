---
id: uk-data
name: UK Data
description: Use when you have a UK `employer-org` (company name or number) and want its registration, financials, and directors — returns `employer-org` details and `associate` (director) links.
url: https://ukdata.com/
category: public-records
path:
- public-records
- company-profiles
bestFor: Pulling a UK company's registration, credit/financial health, and directors from a name or company number.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: freemium
costNote: Free-to-browse council/company economic reports and article content; detailed company credit reports and full financials are the paid product. Underlying registration data originates from Companies House (itself free at gov.uk).
opsec: passive
opsecNote: Queries go to UK Data's servers, not to the company or its directors, so there is no subject-side footprint. It aggregates public Companies House records; nothing you look up here notifies the target.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: unverified
trustNote: A commercial data aggregator repackaging Companies House and third-party (Beauhurst) data; useful as a convenience layer, but confirm any specific figure against the authoritative Companies House record.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- opencorporates
- companies-in-the-uk
aliases:
- UK Data
- ukdata.com
tags:
- company-profiles
- uk-companies
- credit-check
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# UK Data

> A commercial UK company-data aggregator: resolve a company name or number into registration details, financial/credit health, and named directors — a convenience layer over Companies House.

## When to use
Your subject is linked to a UK limited company — as a director, shareholder, or employee — and you want the corporate side of the picture: registered office `address`, incorporation status, financial/credit summary, and the list of directors (`associate` links to co-directors). Useful for confirming a claimed business, mapping who a person runs a company with, or getting a registered address as a contact lead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://ukdata.com/ and search by company name or Companies House registration number.
2. Read the free company summary: status, registered address, incorporation date, and headline financials.
3. For the full credit report / detailed financials, note that these are behind a paid product — decide whether the free summary and Companies House suffice first.
4. Note the directors and pivot to the people layer: co-directors are strong `associate` leads.
5. Cross-check the registration facts against the free authoritative source, Companies House (gov.uk), before relying on them.

## Inputs → Outputs
- **In:** `employer-org` (UK company name or registration number)
- **Out:** `employer-org` (status, registered `address`, financials) and `associate` (directors/officers)
- **Empty/negative result looks like:** no company match — the name/number is wrong, the entity is dissolved and dropped, or it's not a UK-registered company; verify on Companies House.

## Gotchas & OpSec
- Partial paywall: the free tier is a summary; full credit reports and deep financials cost money. Much of the same registration data is free at Companies House.
- Aggregator lag/error: repackaged data can be stale or mis-merged — treat figures as leads and confirm at source.
- UK scope only.
- OpSec: passive; you query the aggregator, never the company or its directors.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` (open, cross-jurisdiction company data) and `[[companies-in-the-uk]]` — cross-check the same company across sources, and go straight to Companies House for the authoritative filing.

## Trust & verifiability
`trust: unverified` — a commercial reseller of public and third-party data; convenient but not authoritative, so verify specific registration/financial claims against Companies House.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-data |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, associate, address |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
