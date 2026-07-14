---
id: school-or-university
name: Facebook "went to" school/university dork
description: Use when you have a `name` and a school/university and want to find the subject's Facebook profile via the education field — returns a `social-profile`.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Afacebook.com+%22went+to%22+%22Search+Term%22
category: social-networks
path:
- social-networks
bestFor: Finding a Facebook profile by pivoting on the "went to [school]" education text Facebook exposes publicly.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Google `site:` dork; no account on Google or Facebook required to read indexed public results.
opsec: passive
opsecNote: The query hits Google's index, not Facebook, so the subject is not alerted. Opening the profile logged-out is passive; if you click through while logged into a real Facebook account you may appear in "People You May Know" — use a sock puppet or logged-out session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A search-engine technique over Facebook's public education field, not a product; reliability depends on Google's index of facebook.com and what Facebook exposes publicly.
missingPersonsRelevance: high
coverage:
- global
aliases:
- Facebook school dork
- facebook went to school search
tags:
- facebook
- Facebook General Links
- google-dork
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook "went to" school/university dork

> A Google `site:facebook.com` dork that keys on the "went to [school]" education phrase Facebook shows publicly — a way to find a profile when a name alone is too common.

## When to use
You have a `name` plus a known school, college, or university for the subject, and a plain name search returns too many people. Facebook publicly renders education as "went to [School]," so pairing the name with the school in a Google dork narrows to the right `social-profile`. Strong for disambiguating common names in a missing-person or background workflow.

## How to use it (`bestInteractionPattern`: web-manual)
1. Replace the placeholder in the query with your target's school/university. In Google, run:
   - `site:facebook.com "went to" "<School Name>" "<First Last>"`
   - or broader: `site:facebook.com "studied at" "<School>"` / `site:facebook.com "<School>" "<town>"`.
2. Read the results: profile snippets show the person's `name`, education line, and often city/work.
3. Open a likely profile logged-out (or via sock puppet) to confirm.
4. Pivot: a confirmed profile feeds friend-list/photo review, username-reuse checks, and Facebook-specific tools.

## Inputs → Outputs
- **In:** `name` + school/university (and optional town)
- **Out:** `social-profile` on Facebook, confirmed display `name`, education/location context
- **Empty/negative result looks like:** no `site:facebook.com` hits pairing the name and school — the subject may keep education private, use a nickname, or not be on Facebook. Try alternate name forms and the school's own alumni/groups.

## Gotchas & OpSec
- Facebook increasingly hides fields from logged-out users and crawlers, so indexed snippets can lag the live profile.
- Common school + common name still collides; add town, employer, or middle name to sharpen.
- OpSec: passive against the target. Don't click through on a real account — logged-out or sock puppet only.

## Overlaps ("do both")
- Pairs with other Facebook dorks and general people-search — this keys on education, while location/employer dorks and people-search key on other fields. Combine to triangulate the right profile.

## Trust & verifiability
`trust: community` — a technique over Google's index of Facebook, not an authoritative source. Confirm a match by cross-checking photo, location, and mutual context, not the education line alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | school-or-university |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
