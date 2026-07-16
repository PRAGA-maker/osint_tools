---
id: bloomberg-com
name: bloomberg.com
description: Use when you have a company `name`/ticker or an `employer-org` and want executives, filings-level corporate data and officer profiles — returns employer-org, name and address details.
url: https://www.bloomberg.com/markets/stocks?cic_redirect=fallback
category: public-records
path:
- public-records
bestFor: Researching a public company, its executives and its registered/HQ details when a subject is tied to that organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- address
status: live
pricing: freemium
costNote: Company overview pages, executive lists and basic market data are viewable free (metered — a paywall/registration prompt appears after several articles). Deep analytics and news archives require a Bloomberg subscription; the free company/exec profile layer is what has OSINT value here.
opsec: passive
opsecNote: Passive — you browse a public financial-news site; no subject is contacted. Bloomberg is aggressive with tracking, paywalls and bot detection; use a clean browser and expect a metered-access wall. Nothing you look up reaches the person you're investigating.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Bloomberg is an authoritative financial-data and news organisation; company/executive facts are well-sourced. It is a corporate-intelligence source, not a people-finder — relevance is via a subject's employer/officer role.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- bloomberg
- bloomberg-business-news
- bloomberg-public-companies-search
- lei-bloomberg-com
aliases:
- Bloomberg
- Bloomberg Markets
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# bloomberg.com

> Bloomberg's markets/company data — the authoritative angle on a public company, its executives and its corporate footprint.

## When to use
Your subject is linked to a company — as an executive, officer, director, or employee — and you want to research that `employer-org`: who runs it, where it's headquartered, its ticker and filings-level facts. Bloomberg's company profiles list named executives and board members, which can confirm a subject's role, tenure and professional network. Best when the person is reachable through their business identity rather than personal records.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bloomberg.com/markets/stocks in a clean browser.
2. Search the company `name` or ticker; open its quote/company page.
3. Read the Profile / People / Executives tabs for officer `name`s, titles, and HQ `address`; check the news feed for context.
4. When the metered paywall appears, back off (clear cookies / use reader view) — the core profile data usually loads before the wall.
5. Pivot: a named executive feeds people-search and LinkedIn; the HQ/registered address feeds corporate-registry lookups; the ticker feeds SEC/regulatory filings for signed disclosures.

## Inputs → Outputs
- **In:** company `name`/ticker or `employer-org`
- **Out:** `employer-org` details, executive/officer `name`s, HQ/registered `address`, market data
- **Empty/negative result looks like:** private companies and individuals return little or nothing — Bloomberg indexes public/listed entities; a missing company usually means it isn't publicly traded, not that it doesn't exist.

## Gotchas & OpSec
- Metered paywall and bot detection: expect to be gated after a few page views; registration or subscription unlocks more, but the free profile layer covers most OSINT needs.
- It's a corporate source — don't expect personal addresses or non-executive individuals.
- OpSec: **passive**; no target contact.

## Overlaps ("do both")
- Pair with a corporate registry (Companies House / OpenCorporates-style) and SEC filings — Bloomberg gives the polished executive/market view, registries give the legally-filed officers and addresses; cross-referencing catches roles Bloomberg omits.

## Trust & verifiability
`trust: trusted` — Bloomberg is an authoritative, well-sourced financial organisation. Facts are reliable; just confirm officer roles against primary filings when they matter, since profiles can lag personnel changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bloomberg-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
