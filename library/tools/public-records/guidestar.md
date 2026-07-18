---
id: guidestar
name: GuideStar
description: Use when you have an `employer-org` (nonprofit) or a `name` and want US nonprofit filings and leadership — returns officers, addresses, Forms 990, and financials.
url: https://www.guidestar.org
category: public-records
path:
- public-records
bestFor: Profiling a US nonprofit and the people who run it (CEO, board chair, key staff) via IRS Form 990 data.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- name
- address
- associate
status: live
pricing: freemium
costNote: Free registered account gives up to 3 years of Forms 990, current-year revenue/expense data, and CEO/board-chair info; deeper history and analytics are paid (Candid Pro).
opsec: passive
opsecNote: Passive — you read published nonprofit filings; no organization or person is notified. A free account is tied to your email, so register with a research identity rather than a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Candid (the GuideStar + Foundation Center merger); data comes from the IRS Business Master File and Forms 990 plus nonprofit self-reporting, making it authoritative for US nonprofit records.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- opencorporates
- corporationwiki
aliases:
- GuideStar by Candid
- guidestar.org
- Candid
tags:
- company-research
- nonprofit
- form-990
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# GuideStar

> Candid's database of US nonprofits — pull a charity's Form 990, finances, addresses, and the officers who lead it.

## When to use
You have an `employer-org` that is a US nonprofit/charity, or a `name` you suspect is a nonprofit officer, and want the organization's filings and leadership. GuideStar surfaces the CEO/executive director, board chair, mailing `address`, mission, and Forms 990 (which list officer names, compensation, and sometimes related parties). For a missing-persons case this connects a subject to a nonprofit role — as staff, board member, or founder — and gives an official address and a network of `associate`s from the filing.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://www.guidestar.org (needed to see filing data).
2. Search the nonprofit by name (or search a person's name to find orgs where they're listed).
3. Open the profile: read the summary (address, mission, EIN), leadership (CEO, board chair), and financials.
4. Open the Forms 990 (up to 3 years free) — these list officers/directors, their titles, hours, and compensation.
5. Pivot: officer names become `associate` leads for people-search; the EIN/address feeds corporate-registry and property tools.

## Inputs → Outputs
- **In:** `employer-org` (nonprofit) or `name`
- **Out:** `employer-org` (org profile), `name`/`associate` (officers, directors), `address` (org address), plus 990 financials
- **Empty/negative result looks like:** "No results" or a bare IRS-BMF stub with no 990 — the org may be too small to file a full 990, newly formed, or not US-registered; absence of filings is not proof the entity doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: a free account login is required to see the useful data.
- Form 990 data lags 1–2 years (filings are annual and posted after processing) — treat officer/address info as of the filing year, not "now."
- Only US 501(c) nonprofits are covered; for-profit companies and foreign charities are out of scope.
- OpSec: passive; reading public filings notifies no one.

## Overlaps ("do both")
- Pairs with `[[opencorporates]]` and `[[corporationwiki]]` — those cover for-profit corporate registrations and officer networks, while GuideStar is the authoritative source for the nonprofit side; run a name through all three to catch both worlds.

## Trust & verifiability
`trust: trusted` — Candid/GuideStar draws from IRS filings (990s, Business Master File); the filing-derived facts are authoritative, though self-reported profile fields should be sanity-checked against the actual 990.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guidestar |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → employer-org, name, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
