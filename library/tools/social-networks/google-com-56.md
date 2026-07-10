---
id: google-com-56
name: google.com (site:rocketreach.co dork)
description: Use when you have a `name` or `employer-org` and want a subject's professional contact/role details via Google over RocketReach profiles — returns `social-profile`, `employer-org`, job title, and email/phone leads.
url: https://www.google.com/search?q=site%3Arocketreach.co&ie=utf-8&oe=utf-8&client=firefox-b-ab
category: social-networks
path:
- social-networks
bestFor: Using Google's site: operator over RocketReach to surface a person's employer, job title, and contact leads (a LinkedIn-adjacent source).
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: The Google search is free; RocketReach itself gates full contact data (emails/phones) behind a paid account, so the dork surfaces the indexed teaser/role info, not the full record.
opsec: passive
opsecNote: You search Google's index, not RocketReach or the target — passive. Opening a RocketReach page is ordinary browsing; it may prompt signup. Use a sock-puppet browser and avoid logging into RocketReach with an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Native Google `site:` results; authoritative for what Google indexed of RocketReach, though the underlying RocketReach data is aggregated and can be stale.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- site:rocketreach.co Google search
- RocketReach Google dork
tags:
- linkedin
- LinkedIn & Similar Sites
- google-dork
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# google.com (site:rocketreach.co dork)

> A Google `site:rocketreach.co` dork — pull a subject's employer, job title, and professional-contact leads from RocketReach without paying, by reading Google's indexed profile pages.

## When to use
You have a `name` or `employer-org` and want professional/contact intelligence (current employer, role, likely work email/phone) on a subject. RocketReach aggregates this LinkedIn-adjacent data but paywalls it — Google's index of RocketReach profile pages often exposes the role/employer teaser for free.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, search `site:rocketreach.co "<Full Name>"` (add `"<Company>"` to disambiguate).
2. Read the result snippets — often the person's name, title, and employer appear without opening the page.
3. Open a matching RocketReach page (sock-puppet browser) for more; note full emails/phones are paywalled.
4. Pivot: confirmed employer/title → LinkedIn and `[[chartloop]]`-style org mapping; a revealed work-email pattern → email-permutation and verification tools.

## Inputs → Outputs
- **In:** `name` or `employer-org` (as a `site:rocketreach.co` Google query)
- **Out:** `social-profile` (RocketReach page), `employer-org`, job title, and email/phone *leads* (often partial/paywalled)
- **Empty/negative result looks like:** no indexed RocketReach page — the person may not be in RocketReach, or Google hasn't indexed their page. Try the same `site:` dork on other contact aggregators.

## Gotchas & OpSec
- RocketReach's full contact data is paywalled; the dork gives teasers/roles, not guaranteed emails.
- Aggregated data can be stale (old employer/title) — verify against LinkedIn/company site.
- The `site:` technique generalizes to other contact aggregators (`site:zoominfo.com`, `site:apollo.io`).

## Overlaps ("do both")
- Pairs with `[[google-com-67]]` (same `site:` technique, different platform) and LinkedIn/org-mapping tools — the dork surfaces role/employer, those confirm and expand the professional network.

## Trust & verifiability
`trust: trusted` — genuine Google results; authenticity is fine, completeness/freshness of the RocketReach data behind them is the caveat. Verify contact details before use.
