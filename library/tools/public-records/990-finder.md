---
id: 990-finder
name: 990 Finder
description: Use when you have an `employer-org`/nonprofit name and want its IRS Form 990 filings and profile — returns officer/director names, financials and EIN.
url: https://candid.org/research-and-verify-nonprofits/990-finder
category: public-records
path:
- public-records
bestFor: Locating a US nonprofit's Form 990 filings to surface its officers, directors and finances.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: freemium
costNote: Basic search of 1.9M organizations by name/EIN/keyword and links to Form 990 filings are free; detailed Candid profiles and analytics sit behind a paid subscription. For fully free 990 access, prefer ProPublica Nonprofit Explorer.
opsec: passive
opsecNote: Searching a nonprofit's public filings does not notify anyone at the organization. Candid may require a free login for some views and will log that account's activity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Candid (the merger of GuideStar and Foundation Center) is the long-standing authority on US nonprofit data; the underlying 990s are official IRS filings.
missingPersonsRelevance: medium
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- foundation-finder
- nonprofit-explorer
tags:
- Company information search
- nonprofit
- irs-990
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# 990 Finder

> Candid's search over ~1.9 million US nonprofits and their IRS Form 990 filings — the fastest way to tie a person to a charity's board, payroll, or leadership.

## When to use
Your subject is linked to a US nonprofit, foundation, church, or association — as a founder, board member, officer, or well-paid employee. The Form 990 an organization files with the IRS lists its officers and directors by name (often with compensation) and its address, giving you an `associate` network and an `employer-org` tie you can corroborate elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://candid.org/research-and-verify-nonprofits/990-finder.
2. Search by the organization's name, EIN, or a keyword (city, cause). If you only have a person's name, first find the org via another source, then search it here.
3. Open the matching organization; you may be prompted to create a free Candid account to view detail.
4. Open the linked Form 990 filings (PDFs). Read Part VII / Schedule J for the list of officers, directors, trustees, and key employees — names, titles, hours, and compensation.
5. Note the EIN, principal address, and fiscal data; cross-check officer names against your subject.
6. Pivot: officer names → people-search; the org's address → address lookups; EIN → other filing databases.

## Inputs → Outputs
- **In:** `employer-org` / nonprofit `name` (or EIN/keyword)
- **Out:** organization profile, EIN, address, financials, and — from the 990 itself — officer/director `name`s and `associate` relationships
- **Empty/negative result looks like:** no matching organization, or a profile with no attached 990 (very new, very small, or non-990-filing orgs like churches, which are exempt). Absence of a 990 does not mean the org isn't real.

## Gotchas & OpSec
- Freemium: basic search and the raw 990 PDFs are reachable free (often after a free login), but Candid's enriched profiles and analytics are paywalled. If you hit a wall, the same underlying 990s are fully free on ProPublica Nonprofit Explorer.
- 990s lag reality by 1–2 years and churches/small orgs may not file — board lists can be stale or absent.
- OpSec: passive against the subject; only Candid sees your (optionally logged-in) searches.

## Overlaps ("do both")
- Pairs with `[[nonprofit-explorer]]` (fully free 990 full-text and bulk data) and `[[foundation-finder]]` (grantmaker relationships) — use ProPublica for the unpaywalled filings and Candid for the polished org profile.

## Trust & verifiability
`trust: trusted` — Candid is the authoritative aggregator of US nonprofit data and the 990s it links are official IRS filings; the person-level detail (officer names/pay) comes straight from those filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | 990-finder |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
