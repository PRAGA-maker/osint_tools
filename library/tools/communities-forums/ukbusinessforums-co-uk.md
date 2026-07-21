---
id: ukbusinessforums-co-uk
name: UK Business Forums (UKBF)
description: Use when you have a `username` or `name` of a UK small-business owner and want their forum footprint — returns the linked `social-profile`, `employer-org` and disclosed business detail.
url: https://www.ukbusinessforums.co.uk/
category: communities-forums
path:
- communities-forums
bestFor: Profiling UK small-business owners and sole traders through their posts on a large business community.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Free to read and search all public posts; membership upgrade (paid) adds a featured directory listing and extras. Reading requires no account.
opsec: passive
opsecNote: Reading and searching public posts is passive and does not alert the member. Members often name their own businesses/websites in signatures and posts. Do not register or post from a real identity; use a sock puppet if you need account features.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A large, long-running (since 2003) UK small-business community with 250k+ members. User-generated content — claims are unverified, but self-linked business names/sites are strong pivots.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- UKBF
- UK Business Forums
- ukbusinessforums.co.uk
tags:
- forums
- Forums
- business
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# UK Business Forums (UKBF)

> The UK's largest small-business community — a rich source where sole traders and SME owners discuss (and openly name) their businesses under searchable handles.

## When to use
Your subject is a UK small-business owner, sole trader, freelancer, or startup founder. UKBF members routinely name their own company, website, sector, and location while asking for advice — so a member profile and post history can hand you an `employer-org`, a business website/domain, a trading name, and self-disclosed location or contact detail. Strong for tying a person to a business and vice versa.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the member profile directly, or run a scoped search: `site:ukbusinessforums.co.uk "username"` or `"business name"`.
2. Open the profile for join date and activity; read their posts and especially signatures, where members often link their company site.
3. Extract the named business, website/domain, sector, and any location or contact details disclosed.
4. Correlate the handle and business against other sources to confirm identity.
5. Pivot: a named business/domain feeds Companies House and WHOIS lookups; the handle feeds `[[sherlock]]`/`[[whatsmyname]]`; a linked website feeds infrastructure OSINT.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (member page), `employer-org` (self-named business), business website/domain, disclosed location
- **Empty/negative result looks like:** no member or no posts for the handle — the person doesn't use UKBF or posts little. Absence is not proof of no business.

## Gotchas & OpSec
- Self-reported: business claims are unverified — confirm the company via Companies House. The self-linked domains/names, though, are excellent pivots.
- UK small-business scope; a non-UK or non-business subject won't appear.
- Fully passive to read; registering/posting from a real identity would create a footprint — avoid it.

## Overlaps ("do both")
- Pairs with Companies House and WHOIS — UKBF gives the person→business link and a website, those confirm the company's official record and the domain's ownership.

## Trust & verifiability
`trust: community` — a real, established community; accounts and posts are authentic artefacts, while the business claims within them should be corroborated against official registries.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ukbusinessforums-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
