---
id: allpeople
name: AllPeople
description: Use when you have a `name` or `employer-org` and want US business-contact details — returns work `email`, `phone`, title and company `address`.
url: https://allpeople.com/
category: public-records
path:
- public-records
bestFor: Finding a US business professional's company, title, work email and phone from a name or company.
selectorsIn:
- name
- employer-org
selectorsOut:
- email
- phone
- address
- employer-org
status: live
pricing: freemium
costNote: Free directory of US business contacts; browsing and basic contact details are free. Some fields/lead-export features are gated behind sign-up or paid tiers.
opsec: passive
opsecNote: You are querying an aggregated public business directory, not the subject; nobody is alerted. Contact details are B2B-oriented — treat them as professional, not necessarily personal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large aggregated B2B contact directory; data is scraped/compiled from many sources and can be stale or mismatched — verify a hit before acting on it.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- AllPeople.com
tags:
- people-search
- business-directory
- b2b
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# AllPeople

> A large free directory of US *business* contacts — the angle when your subject has a job title and company, not just a home address.

## When to use
You have a `name` (or the `employer-org` they work for) and want their professional footprint: company, role, work email, and phone. Useful for confirming employment claims, finding a work contact route to a subject, or mapping colleagues at an organization. It leans B2B — think "find the person at this company" rather than "find this individual's home details."

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://allpeople.com/ and search the subject's `name`, or browse by company/`employer-org`.
2. Open the matching profile card and read: full name, job title, company, work `email`, `phone`, and company `address`.
3. Cross-check the company and title against LinkedIn / the company's own site to confirm it's the right person (name collisions are common).
4. Pivot: work `email` → email-OSINT and breach checks; `employer-org` → colleague enumeration; `phone` → phone lookup tools.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** job title, company `employer-org`, work `email`, `phone`, company `address`
- **Empty/negative result looks like:** no card, or only same-name people at unrelated companies — the person may not be in the B2B dataset (self-employed, non-corporate, or simply not scraped). Absence here doesn't mean they're not employed.

## Gotchas & OpSec
- Aggregated/scraped data: entries can be outdated (people change jobs) or wrongly merged. Always corroborate before treating a contact as current.
- Business-oriented — good for work contacts, weak for personal/home details. Use a dedicated people-search source for the latter.
- Some contact fields and any bulk export require sign-up or payment; single-record browsing is free.

## Overlaps ("do both")
- Do both with LinkedIn/company directories (authoritative for current role) and a personal people-search tool. AllPeople gives you a fast free B2B contact; the others confirm currency and add the personal side.

## Trust & verifiability
`trust: community` — an aggregated commercial directory with no authoritative sourcing; treat records as leads and verify title/employer against a first-party source before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | allpeople |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → email, phone, address, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
