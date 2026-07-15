---
id: google-com-55
name: Google site search — uk.linkedin.com
description: Use when you have a `name` (or `username`, employer, or town) and want to find a person's UK LinkedIn profile without logging into LinkedIn — returns `social-profile` links via Google's index.
url: https://www.google.com/search?q=site%3Auk.linkedin.com
category: social-networks
path:
- social-networks
bestFor: Finding UK LinkedIn profiles by name/employer using a Google `site:uk.linkedin.com` dork, bypassing LinkedIn's login wall.
selectorsIn:
- name
- username
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free — it is a Google web search; no LinkedIn account needed to see the indexed snippets.
opsec: passive
opsecNote: You search Google, not LinkedIn, so LinkedIn's "who viewed your profile" is not triggered by the search itself. Google logs your queries against your IP/account — use a sock-puppet/logged-out session. Clicking through to the actual LinkedIn page IS a visit and can be logged by LinkedIn; read the Google cache/snippet first if you want to stay off LinkedIn entirely.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: This is Google's own web search with a `site:` operator — the engine is authoritative; result quality is bounded only by what Google has indexed from LinkedIn.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- site:uk.linkedin.com
- Google LinkedIn UK dork
tags:
- linkedin
- LinkedIn & Similar Sites
- google-dork
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Google site search — uk.linkedin.com

> A Google `site:uk.linkedin.com` dork that surfaces UK LinkedIn profiles by name or employer without ever logging into LinkedIn.

## When to use
You have a `name` (optionally plus an employer, job title, or town) for someone likely based in the UK, and you want their LinkedIn profile but don't want to search from inside LinkedIn (which reveals you and pushes a login wall). Restricting Google to `uk.linkedin.com` returns indexed public profiles with a snippet of headline/employer, letting you identify the right person and read basic career context anonymously.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a logged-out / sock-puppet browser, run a Google search of the form: `site:uk.linkedin.com "Full Name"` (add `"Employer"` or a town to disambiguate).
2. Scan the result titles and snippets — each is a public LinkedIn profile headline (name, current role, employer).
3. To stay off LinkedIn, read the snippet or the Google cached copy rather than clicking through.
4. If you must open the profile, do it from a sock-puppet LinkedIn session (or logged out), knowing LinkedIn may log the visit.
5. Pivot: the confirmed name+employer feeds email-pattern guessing, company-directory lookups, and cross-platform username searches.

## Inputs → Outputs
- **In:** `name` (plus optional `employer-org`, title, or location)
- **Out:** `social-profile` (LinkedIn URL), current `employer-org` and role from the snippet
- **Empty/negative result looks like:** no results, or only unrelated same-name people — meaning Google hasn't indexed a matching UK profile, not that the person has no LinkedIn (they may use the global `linkedin.com/in/` path or have a private profile).

## Gotchas & OpSec
- `uk.linkedin.com` catches UK-localised profile URLs; many UK users' canonical URL is still `www.linkedin.com/in/…`, so also try `site:linkedin.com/in "Name" UK`.
- Google's index lags — a very new or recently-renamed profile may not appear.
- OpSec: the Google search is passive toward LinkedIn; clicking into a profile is not. Prefer snippet/cache reading.

## Overlaps ("do both")
- Pairs with the general `site:linkedin.com/in` dork (`[[google-com-46]]` is the sibling technique for other networks) and with email-to-LinkedIn tools — the dork finds the profile, those confirm identity and contact.

## Trust & verifiability
`trust: trusted` — it is Google search itself; the operator simply filters to one host. Verify each hit is the right individual (same-name collisions are common) before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-55 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username, employer-org → social-profile, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
