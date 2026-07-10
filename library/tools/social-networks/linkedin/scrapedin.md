---
id: scrapedin
name: ScrapedIn
description: Use when you have LinkedIn search targets and want bulk-extracted profile data via an authenticated session — returns structured profile records (name, title, employer, location).
url: https://github.com/dchrastil/ScrapedIn
category: social-networks
path:
- social-networks
- linkedin
bestFor: Bulk LinkedIn profile/company data extraction from search results using your own logged-in session (red-team recon style).
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- social-profile
status: degraded
pricing: free
costNote: Free, open-source (dchrastil). No fee, but it drives an authenticated LinkedIn session and LinkedIn's frequent changes/anti-automation routinely break such tools — expect maintenance or breakage.
opsec: active
opsecNote: This automates a logged-in LinkedIn account, which is directly against LinkedIn's ToS and detectable — accounts get warned, throttled, or banned. Use a burner LinkedIn account and residential-style pacing, never a real/valuable account, and be aware LinkedIn logs your activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: An older community LinkedIn scraper; effectiveness depends heavily on LinkedIn's current front end and anti-bot measures, which change often — treat as frequently-broken and verify it still works.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools:
- raven
- kaspr-io
aliases:
- ScrapedIn
- dchrastil ScrapedIn
tags:
- linkedin
- scraper
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# ScrapedIn

> An open-source LinkedIn scraper that drives your authenticated session to pull profile/company data in bulk from search results — powerful for recon, but ToS-violating and frequently broken by LinkedIn changes.

## When to use
You need structured data on many LinkedIn profiles or a company's employees at once (name, title, employer, location) for reconnaissance, and manual browsing won't scale. ScrapedIn automates search-result harvesting. Use it only with a burner account and full awareness that it violates LinkedIn's ToS and may be non-functional depending on LinkedIn's current defences.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/dchrastil/ScrapedIn` and install its dependencies.
2. Supply an authenticated LinkedIn session (cookies) from a **burner** account.
3. Configure the target search (keywords, company, `name`, `employer-org`) and run the tool.
4. It iterates search results and outputs structured profile records (often to CSV/HTML).
5. If it errors or returns nothing, assume LinkedIn changed something — check the repo's issues and consider whether the tool is still maintained before relying on it.

## Inputs → Outputs
- **In:** LinkedIn search queries / target `name` or `employer-org`
- **Out:** structured profile records — `name`, title, `employer-org`, location, profile URL (`social-profile`)
- **Empty/negative result looks like:** empty output, login/challenge errors, or a CAPTCHA wall — with LinkedIn scrapers this almost always means anti-automation defences, not that the targets don't exist.

## Gotchas & OpSec
- Status **degraded**: it is an older tool and LinkedIn's frequent changes break scrapers; verify current functionality before depending on it.
- **ToS-violating and detectable** — automating a logged-in account risks warnings/bans. Burner account only; pace requests; never use a real account.
- OpSec: **active** and higher-risk; your account and IP are directly exposed to LinkedIn's monitoring.

## Overlaps ("do both")
- Overlaps with `[[raven]]` (LinkedIn recon) and `[[kaspr-io]]` (LinkedIn contact enrichment) — prefer a maintained option if ScrapedIn is broken; cross-check any harvested data against the live profile.

## Trust & verifiability
`trust: unverified` — a community scraper whose reliability is hostage to LinkedIn's ever-changing anti-automation. Treat harvested records as leads to confirm on the actual profile, and expect breakage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scrapedin |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → name, employer-org, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
