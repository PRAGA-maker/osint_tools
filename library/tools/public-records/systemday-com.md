---
id: systemday-com
name: systemday.com
description: Use when you have a company `name` or number in an offshore/hard-to-reach jurisdiction and want an official registry search report — returns `employer-org` status, incorporation date, and registered `address`.
url: https://www.systemday.com/mauritius-company-search/
category: public-records
path:
- public-records
bestFor: Ordering official company-registry search reports for offshore jurisdictions (Mauritius, BVI, Seychelles, and others) where the registry has no free public search.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: freemium
costNote: Paid, agent-mediated service — a Mauritius company search report is ~£188 (expedited option ~£75 extra), delivered in 3-4 business days. There is no free self-serve search; System Day is an incorporation agent that pulls and resells registry data. For jurisdictions with a free public registry, use that registry directly instead.
opsec: passive
opsecNote: You are ordering a report about a company from a third-party agent, not touching the target. Passive with respect to the subject, but you disclose your interest (and payment/contact details) to System Day. Use a role-based email if you don't want the enquiry tied to you personally.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: System Day Ltd is a UK-based corporate-services/incorporation agent; reports are sourced from the official Mauritius Registrar of Companies but are resold via a paid intermediary rather than a first-party registry.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- b2bhint-com
aliases:
- System Day
- systemday Mauritius company search
tags:
- companysites
- Company Related Sites
- offshore
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# systemday.com

> A corporate-services agent that fetches official company-registry reports for offshore jurisdictions (Mauritius, BVI, Seychelles, etc.) that have no free public search.

## When to use
You are tracing an `employer-org` link and the company is registered somewhere the registry offers no free online lookup — classically Mauritius, but System Day also covers BVI, Seychelles, Ireland, the UK and others. Use it to confirm a company exists, its status (live/defunct/dissolving), type, incorporation date, and registered office/agent address. This corroborates a subject's stated business affiliation or the shell behind an address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the relevant jurisdiction page, e.g. https://www.systemday.com/mauritius-company-search/.
2. Provide the company `name` or registration number and order the search report (payment required, ~£188 for Mauritius; expedited option available).
3. Wait 3-4 business days for the human-prepared report.
4. Read the report for the company's status, type, incorporation date, and registered `address`/agent.
5. Pivot: registered-office `address` and agent details feed further corporate/property lookups; note that director and shareholder names for private companies are only disclosed **with authorisation** and are confidential under Mauritius law.

## Inputs → Outputs
- **In:** company `name` or registration number (an `employer-org` link)
- **Out:** confirmed `employer-org` (status, type, incorporation date), registered `address`/agent, sometimes company `name` normalisation
- **Empty/negative result looks like:** no matching company on the register — a paid report confirming non-existence is still an answer, but check spelling and jurisdiction first.

## Gotchas & OpSec
- Human-in-the-loop: this is a **paid, manually-fulfilled** service (payment wall + human report preparation), not an instant lookup — budget days and money.
- Confidential fields (private-company directors, shareholdings) are withheld without the subject's authorisation, so this is weaker than an open registry for beneficial-ownership work.
- Before paying, check whether the target jurisdiction actually has a free public registry — if so, use that first and reserve System Day for the genuinely closed registries.
- OpSec: passive toward the subject, but you reveal your interest and contact/payment details to the agent.

## Overlaps ("do both")
- Pairs with `[[b2bhint-com]]` and OpenCorporates-style aggregators — check the free aggregators first; fall back to System Day only when the jurisdiction is not covered for free.

## Trust & verifiability
`trust: community` — System Day is a legitimate corporate-services firm and its reports draw on the official Mauritius Registrar of Companies, but it is a paid reseller/intermediary, so verify anything critical against the first-party registry where one is publicly reachable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | systemday-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, manual-review) |
