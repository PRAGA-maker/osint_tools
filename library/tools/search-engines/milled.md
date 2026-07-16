---
id: milled
name: Milled
description: Use when you have a brand/`employer-org` name and want its marketing-email history — returns archived promotional emails revealing campaigns, dates, and contact details.
url: https://milled.com/search
category: search-engines
path:
- search-engines
bestFor: A search engine for companies' marketing emails/newsletters — "Google for promotional email" across 100,000+ brands.
selectorsIn:
- employer-org
- email
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Free tier covers recent emails (roughly last 30 days) and basic search; Milled Pro (~$99/mo) unlocks the full historical archive and advanced/boolean search and alerts.
opsec: passive
opsecNote: You search a public archive of brand marketing emails — no individual is queried and no one is notified. Passive. Milled sees your searches/IP; use browser hygiene, but there is no target-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established indie-run archive (since 2012) of brands' marketing emails; the emails are authentic captures, but it indexes company newsletters, not personal correspondence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Milled.com
tags:
- email-search
- marketing-emails
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# Milled

> A search engine over companies' marketing emails — archives newsletters/promotions from 100,000+ brands, so you can pull a business's campaign history and the contact details buried in its footers.

## When to use
You're investigating a *business* (an `employer-org`, a brand a subject runs or promotes) rather than a person, and want its outbound marketing footprint: what it sent, when, from which sending address, and the physical/contact details in email footers (CAN-SPAM requires a mailing address). Low direct relevance for locating an individual, but genuinely useful for verifying a company's activity, timeline, or contact info.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to Milled's search and enter a brand name, product, or keyword.
2. Browse matching archived emails; open one to see the full rendered message.
3. Read footers/headers for the sending `email` address, physical mailing address, and links — plus the send date to time-stamp a campaign.
4. Use filters (Pro adds boolean/quoted search and full history) to narrow by objective or period.
5. Pivot: a footer mailing address / sending domain feeds domain- and company-OSINT; campaign dates corroborate that a business was active at a given time.

## Inputs → Outputs
- **In:** a brand / `employer-org` name or keyword
- **Out:** archived marketing emails exposing the `employer-org`'s sending address, contact/footer details, and campaign dates
- **Empty/negative result looks like:** no emails for the brand — the company never mailed a list Milled captures, or the name/spelling is off; Milled only sees brands whose lists it subscribes to.

## Gotchas & OpSec
- It indexes *company* newsletters, not personal email — do not expect to find an individual's private mail here.
- Free tier is limited to recent emails; historical depth needs Pro.
- Coverage is opt-in/subscription-based on Milled's side — many small brands aren't indexed.
- OpSec: fully passive.

## Overlaps ("do both")
- Pairs with domain/company-registration OSINT — Milled shows a brand's marketing behavior and footer contacts; registry tools confirm the legal entity behind it.

## Trust & verifiability
`trust: community` — a long-running indie archive; the captured emails are authentic, but it's a niche, business-focused source with self-selected brand coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | milled |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, email → employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
