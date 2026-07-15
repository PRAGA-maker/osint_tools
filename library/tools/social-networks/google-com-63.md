---
id: google-com-63
name: Google site search — xing.com/profile
description: Use when you have a `name` (or employer) for someone in the German-speaking world and want their XING profile without logging into XING — returns `social-profile` links via Google's index.
url: https://www.google.com/search?q=site%3Axing.com%2Fprofile
category: social-networks
path:
- social-networks
bestFor: Finding XING (DACH professional network) profiles by name/employer using a Google `site:xing.com/profile` dork.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free — it is a Google web search; no XING account required to read the indexed snippets.
opsec: passive
opsecNote: You search Google, not XING, so XING's profile-visitor tracking is not triggered by the search itself. Google logs your queries — use a logged-out/sock-puppet session. Clicking through to the live XING profile IS a visit XING can log; read the snippet/cache first to stay off-platform.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's own web search with a `site:` operator — authoritative engine; results limited only by what Google has indexed from XING.
missingPersonsRelevance: high
coverage:
- de
auth: none
api: false
localInstall: false
registration: false
aliases:
- site:xing.com/profile
- Google XING dork
tags:
- linkedin
- LinkedIn & Similar Sites
- xing
- google-dork
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Google site search — xing.com/profile

> A Google `site:xing.com/profile` dork that surfaces XING profiles — the LinkedIn of the German-speaking world — by name or employer without logging into XING.

## When to use
Your subject is in Germany, Austria, or Switzerland, where **XING** is a major professional network (often more populated than LinkedIn for local/mid-market roles). You want their professional profile but don't want to search from inside XING (which reveals you and pushes a login wall). Restricting Google to `xing.com/profile` returns indexed public profiles with a headline snippet (name, role, employer), letting you identify the right person and read career context anonymously.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out / sock-puppet browser, run: `site:xing.com/profile "Full Name"` (add `"Employer"` or a city to disambiguate).
2. Read the result titles/snippets — each is a public XING profile headline.
3. To stay off XING, read the snippet or Google's cached copy rather than clicking through.
4. If you must open the profile, use a sock-puppet/logged-out session, knowing XING may log the visit.
5. Pivot: the confirmed name+employer feeds email-pattern guessing, LinkedIn cross-checks (`[[google-com-55]]`), and company-directory lookups.

## Inputs → Outputs
- **In:** `name` (plus optional `employer-org`, title, or DACH city)
- **Out:** `social-profile` (XING URL), current `employer-org` and role from the snippet
- **Empty/negative result looks like:** no results or only same-name strangers — Google hasn't indexed a matching XING profile, not proof the person has none (profiles can be private or on a different URL form).

## Gotchas & OpSec
- XING's public URL forms have changed over the years; also try `site:xing.com "Name"` without the `/profile` path.
- Google's index lags — a brand-new or renamed profile may not appear.
- OpSec: the Google search is passive toward XING; clicking into a profile is not. Prefer snippet/cache reading.

## Overlaps ("do both")
- Sibling to the `[[google-com-55]]` LinkedIn UK dork — same `site:` technique aimed at DACH. Run both when a subject spans UK and German-speaking employers.

## Trust & verifiability
`trust: trusted` — Google search itself; the operator only filters to one host. Confirm each hit is the right individual before acting (same-name collisions are common).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-63 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
