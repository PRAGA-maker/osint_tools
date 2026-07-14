---
id: alumni-member-search
name: Alumni Member Search
description: Use when you have a `name` plus a school/affiliation and want the subject's classmate-network profile and contact leads — returns social-profile, address, associate.
url: http://www.alumni.net
category: people-search
path:
- people-search
bestFor: Finding a person through school/affiliation-based alumni networking, where members self-list to reconnect with former classmates.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
- address
status: degraded
pricing: free
costNote: Free membership-based directory; you register to search fully, and coverage skews to users who joined years ago (the site is legacy and traffic has declined).
opsec: passive
opsecNote: Searching the directory does not contact the subject, but any outreach through the site's messaging would. Register a sock-puppet account; do not use a real identity to look up or message members.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A legacy classmate-networking site; entries are self-submitted by members and may be stale, so treat everything as user-provided and unverified.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools: []
aliases:
- Alumni.NET
tags:
- toddington
- curated-directory
- people-search
- alumni
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Alumni Member Search

> A legacy classmate-networking directory — search by name, school, or affiliation to find people who self-listed to reconnect with former classmates.

## When to use
You have a `name` and a school, class year, employer, or location tied to the subject, and you want an alumni/affiliation angle that social media misses — especially for older subjects or long-cold cases where the person may have registered years ago. Members list where they studied/lived and often link to associates from the same cohort, giving you `associate` leads and rough location history.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.alumni.net and register a sock-puppet account (full search needs login).
2. Search by `name`, and narrow by school / group / affiliation / location.
3. Read member profiles: listed schools, years, locations, and connected classmates.
4. Pivot: a confirmed school/cohort feeds yearbook and classmate sites; listed associates feed the wider network; a location feeds address/records tools. Do not message members from a real identity.

## Inputs → Outputs
- **In:** `name` (+ school/affiliation/location to disambiguate)
- **Out:** `social-profile` (member entry), `associate` (fellow alumni), `address`/location history (self-listed)
- **Empty/negative result looks like:** no member match — very common, since the site is legacy and most people never joined. Absence tells you nothing about the person.

## Gotchas & OpSec
- The site is old and traffic has fallen; data is often years stale and self-reported — verify every field elsewhere.
- Human-in-the-loop: login is required for full access; the free tier without an account is limited.
- OpSec: searching is passive, but the platform's messaging is not — never reach out under your own identity.

## Overlaps ("do both")
- Pairs with Classmates.com and yearbook/alumni sites — coverage differs by region and era, so run more than one alumni source for the same school/cohort.

## Trust & verifiability
`trust: unverified` — a legacy directory of self-submitted entries with no validation; useful for leads and network structure, never as a sole source of fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alumni-member-search |
| category | people-search |
| selectorsIn → selectorsOut | name → social-profile, associate, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
