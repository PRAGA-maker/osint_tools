---
id: free-people-search-tool
name: Free People Search Tool
description: Use when you have a `name` (plus location or company) and want a one-box hub that fans a search across LinkedIn, Twitter, GitHub, and Dribbble — returns social-profile links.
url: https://freepeoplesearchtool.com
category: social-networks
path:
- social-networks
bestFor: A recruiter-style search hub that dispatches a name across multiple social platforms in one place.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free web tool; no account needed. Aimed at sourcers/recruiters; also documents opt-out and Boolean-search guidance.
opsec: passive
opsecNote: The tool builds and hands off search queries to Google and to each platform's own search — the subject is never contacted. Any exposure is to the search engines/platforms you land on, so use a sock-puppet browser and, where a platform needs login (e.g. LinkedIn), a sock-puppet account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenience front-end that assembles searches; it holds no data itself, so trust rests on the underlying platforms it queries.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- Free People Search Tool
- freepeoplesearchtool.com
tags:
- linkedin
- x-ray-search
- recruiter-tools
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Free People Search Tool

> A sourcer's launchpad — type a name (and maybe a company/location) and it fires the search across LinkedIn, Twitter, GitHub, and Dribbble in one motion.

## When to use
You have a subject's `name`, optionally with a location or `employer-org`, and want to sweep the professional/social platforms fast without hand-crafting each query. It's a convenience hub: rather than storing data, it constructs the right Google X-ray and per-platform searches and sends you to the results, which is handy early when you're casting wide for any `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open `https://freepeoplesearchtool.com`.
2. Enter any combination of name, location, phone, or company (e.g. "John Smith Los Angeles CA").
3. Run the general search, or use the dedicated LinkedIn / Twitter / GitHub / Dribbble buttons to X-ray a specific platform.
4. Work the results on each platform; confirm identity by corroborating details, not name alone.
5. Pivot: a confirmed LinkedIn/GitHub profile feeds employer/username pivots; a handle feeds cross-platform username tools like `[[nexfil]]`.

## Inputs → Outputs
- **In:** `name`, `employer-org` (+ location/phone as query terms)
- **Out:** `social-profile` links (LinkedIn/Twitter/GitHub/Dribbble), `employer-org` corroboration
- **Empty/negative result looks like:** the handed-off searches return nothing relevant — a common name with no distinguishing term, or a subject who isn't on these professional platforms. Narrow with company/location and retry.

## Gotchas & OpSec
- It's a query builder, not a database — results quality is entirely the underlying platforms'.
- LinkedIn results may require a (sock-puppet) login to view; be mindful LinkedIn shows "who viewed your profile."
- OpSec: **passive** toward the subject; your exposure is to Google/the platforms you land on.

## Overlaps ("do both")
- Pairs with `[[nexfil]]` and recruiter X-ray tools — this hub covers the big professional platforms; username enumerators cover the long tail of smaller sites.

## Trust & verifiability
`trust: community` — a thin convenience layer that holds no data; verify every profile it surfaces on the source platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-people-search-tool |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
