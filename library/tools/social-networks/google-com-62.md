---
id: google-com-62
name: Google site-search — Bayt.com professionals
description: Use when you have a `name` of someone likely working in the Middle East and want their professional profile — a Google `site:bayt.com` dork returning social-profile and employer-org.
url: https://www.google.com/search?q=site%3Abayt.com
category: social-networks
path:
- social-networks
bestFor: Surfacing a subject's professional profile on Bayt.com (the leading Gulf/MENA jobs network) via a Google site-search.
selectorsIn:
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free Google search; no account needed.
opsec: passive
opsecNote: A Google dork touches Google, not the target or Bayt — the person is not notified. Run it from a logged-out/sock-puppet browser so the query and any clicked Bayt profiles are not tied to your Google account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Uses Google's index over Bayt.com, a real regional professional network; the technique is reliable, though Bayt profile content is self-asserted by its users.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- site:bayt.com
- Bayt Google dork
tags:
- linkedin
- LinkedIn & Similar Sites
- dorking
- mena
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Google site-search — Bayt.com professionals

> A ready-made Google dork (`site:bayt.com`) for finding a subject's professional profile on Bayt, the dominant jobs/CV network across the Gulf and wider MENA region — the LinkedIn-equivalent Western tools miss.

## When to use
You have a `name` and reason to think the subject lives or works in the Middle East / North Africa (Gulf expats, regional professionals) and LinkedIn/US people-search is thin. Bayt.com hosts millions of CVs and company/employee profiles; a `site:bayt.com` Google search pulls indexed profiles that mention the name, exposing job title, employer, and location.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out browser, run `site:bayt.com "Full Name"` (add `"City"` or an employer to tighten).
2. Widen or narrow: drop to first/last name if zero hits; add `intitle:` or a job keyword if too many.
3. Open promising results directly from the Google cache/link to read the profile's role, employer, and location.
4. Combine with related dorks (`site:linkedin.com`, `site:xing.com`) to cover other regional networks.
5. Pivot: an `employer-org` → company registry / staff pages; a confirmed profile → wider identity OSINT.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile` (Bayt profile), `employer-org` (stated employer/role)
- **Empty/negative result looks like:** zero Google hits for `site:bayt.com "Name"` — the person may not be on Bayt, has a private/unindexed profile, or the name is transliterated differently (try Arabic spelling or alternates). Absence is not disproof.

## Gotchas & OpSec
- Only *indexed* Bayt pages appear; many CVs are login-gated and never show up — a null result is weak evidence.
- Name transliteration varies (Mohammed/Muhammad/Mohamed); try variants.
- Bayt content is self-asserted by users; corroborate role/employer claims.
- OpSec: passive; run from a sock-puppet browser so the dork and profile visits are not tied to you.

## Overlaps ("do both")
- Pairs with `[[seosly-com]]` (operator syntax) and LinkedIn/Xing site-dorks — same technique, different regional professional networks; run several for coverage.

## Trust & verifiability
`trust: trusted` — the method (Google indexing a real professional network) is dependable; the underlying Bayt profile data is user-supplied, so verify specifics before treating them as fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-62 |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
