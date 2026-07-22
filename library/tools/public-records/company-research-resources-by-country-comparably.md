---
id: company-research-resources-by-country-comparably
name: Comparably
description: Use when you have an `employer-org` or an executive `name` and want company culture, pay and leadership data — returns `employer-org` detail, named executives and `social-profile` links.
url: https://www.comparably.com
category: public-records
path:
- public-records
bestFor: Researching a company's culture, salary bands and named leadership, or verifying an executive's role.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- social-profile
- associate
status: live
pricing: freemium
costNote: Free to browse company profiles, culture ratings, named executives and salary ranges; some detailed data is gated behind an account/premium.
opsec: passive
opsecNote: Browsing company/executive profiles is passive and reveals nothing to any subject. Reviews are anonymous; do not attempt to deanonymise a reviewer or post from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A workplace-culture and compensation site built on employee-submitted reviews plus aggregated data; ratings are self-reported and can be gamed, so treat as indicative not authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Comparably
- comparably.com
tags:
- company-research
- salary
- workplace-reviews
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Comparably

> A workplace-culture, compensation and leadership database — useful for putting flesh on an `employer-org`: who runs it, what it pays, and how insiders describe it.

## When to use
You have an `employer-org` tied to a subject (their current/claimed employer) or an executive `name`, and want context: named leadership and their roles, salary bands for a title, culture/rating signals, and company size/HQ. Good for verifying an employment or seniority claim, identifying decision-makers/associates at a company, or building background before approaching or profiling someone connected to it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.comparably.com and search the `employer-org` (or an executive `name`).
2. On a company profile read: executive team (named, with titles), culture/rating scores, salary ranges by role, demographics and HQ/size.
3. On an executive page, note title, tenure and any linked profile; cross-reference to LinkedIn.
4. Pivot: named executives feed `associate`/leadership mapping and LinkedIn lookups; salary bands sanity-check a claimed income; HQ/location feeds registry checks.

## Inputs → Outputs
- **In:** `employer-org` or executive `name`
- **Out:** `employer-org` detail (leadership, size, HQ), named executives (`associate`), salary bands, `social-profile` links
- **Empty/negative result looks like:** a thin or absent profile — smaller/private firms may have little data, and salary/review coverage is sparse for low-headcount employers.

## Gotchas & OpSec
- Reviews and ratings are employee-submitted and can be manipulated (positively or negatively); treat culture scores as indicative.
- Executive lists may lag reality (departures, new hires) — confirm current roles elsewhere.
- Passive; anonymous reviewers should stay anonymous — do not attempt deanonymisation.

## Overlaps ("do both")
- Pairs with LinkedIn, Glassdoor, Crunchbase and corporate registries — Comparably adds culture/pay and a leadership roster; those confirm legal entity, funding and current employment.

## Trust & verifiability
`trust: community` — a legitimate aggregator of employee-submitted and public company data; useful for leads and context, but self-reported content must be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-research-resources-by-country-comparably |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
