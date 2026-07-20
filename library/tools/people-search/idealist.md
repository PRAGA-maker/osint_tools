---
id: idealist
name: Idealist
description: Use when you have a `name` or `employer-org` in the nonprofit/social-impact world and want affiliation leads — returns employer-org, social-profile, and associate context from jobs, volunteers, and org listings.
url: http://www.idealist.org
category: people-search
path:
- people-search
bestFor: Linking a person to nonprofit organizations, roles, or volunteer activity via a large social-impact jobs/org directory.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- social-profile
- associate
status: live
pricing: free
costNote: Free for job/volunteer seekers to search jobs, volunteer opportunities, and 200k+ organizations; posting listings (org side) may cost, but searching does not.
opsec: passive
opsecNote: Browsing public org/job/volunteer listings; no one is contacted. Some personalized features prompt an account login — read anonymously where possible, and use a sock-puppet account if you must sign in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-established (30+ year) nonprofit-sector platform; org and listing data is real but self-posted, so treat affiliations as leads.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- idealist.org
tags:
- expert-search
- people-search
- nonprofit
- employment
source: awesome-osint
lastVerified: '2026-07-20'
enrichment: full
---

# Idealist

> A 30-year-old social-impact directory of nonprofit jobs, volunteer opportunities, and 200,000+ organizations — a niche way to tie a person to the nonprofit world.

## When to use
Your subject works, volunteers, or recruits in the nonprofit/NGO/social-impact sector, and you want to confirm an organizational affiliation, a role, or a location. Idealist maps the nonprofit landscape: an `employer-org` name resolves to an organization profile (mission, location, contacts), and job/volunteer listings can name coordinators or point to a subject's activity. Complements government-payroll tools, which cover public-sector but not nonprofit employment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://www.idealist.org and choose the Jobs, Volunteer, or Organizations search.
2. Search by `employer-org` to open an organization's profile (location, focus areas, listed contacts), or by keyword/location tied to your subject.
3. Read listings for named contacts/coordinators (`associate`), the posting org (`employer-org`), and links to the org's site/social (`social-profile`).
4. Cross-reference an org's staff/volunteer footprint with the subject's other known affiliations.
5. Pivot: an org + city narrows people-search and public-records queries; a named contact feeds direct person lookups.

## Inputs → Outputs
- **In:** `name` (via listings/keyword) or `employer-org`
- **Out:** `employer-org` profile, `social-profile`/org links, `associate` (named contacts in listings)
- **Empty/negative result looks like:** no matching org or listing — expected unless the subject is active in the nonprofit sector; it does not index the general population.

## Gotchas & OpSec
- Not a general people-directory: it only helps when there's a nonprofit/volunteer connection. Most subjects won't appear.
- Listings are self-posted and time-limited; older affiliations may have expired off the site.
- OpSec: passive; avoid signing in unless a feature requires it, then use a sock puppet.

## Overlaps ("do both")
- Pair with [[openpayrolls-com]] (government-sector) and LinkedIn-style searches: Idealist fills the nonprofit gap those leave, so run both to cover a subject's full employment footprint.

## Trust & verifiability
`trust: community` — an established platform, but org/listing content is self-submitted; verify a specific affiliation against the organization's own site or filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idealist |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
