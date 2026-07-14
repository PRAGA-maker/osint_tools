---
id: google-com-54
name: LinkedIn X-Ray (Google site-scoped search)
description: Use when you have a name, employer or role and want to find LinkedIn profiles Google has indexed — returns public LinkedIn profile links without logging into LinkedIn.
url: https://www.google.com/search?q=site%3Alinkedin.com
category: social-networks
path:
- social-networks
bestFor: Finding LinkedIn profiles via a Google site-scoped dork, bypassing LinkedIn's login wall and search limits.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- name
- employer-org
status: live
pricing: free
costNote: Free — it's a Google query; no LinkedIn account needed to see the indexed public profile snippets.
opsec: passive
opsecNote: The search runs on Google, not LinkedIn, so you avoid LinkedIn's "who viewed your profile" signal at the search stage — a key advantage. But OPENING a LinkedIn profile while logged in can notify the person; view via a logged-out/sock-puppet session or Google's cache to stay unattributed. Google logs your query; use a VPN for sensitive names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Uses Google's first-party index over LinkedIn's own public profiles; the technique is reliable, though LinkedIn limits how much of a profile is indexed/visible when logged out.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- LinkedIn X-Ray search
- site:linkedin.com dork
- LinkedIn Google search
tags:
- linkedin
- LinkedIn & Similar Sites
- google-dork
- x-ray-search
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# LinkedIn X-Ray (Google site: search)

> The classic "X-ray" dork — search `site:linkedin.com/in` on Google to reach public LinkedIn profiles without LinkedIn's login wall, search caps, or view-notifications.

## When to use
You have a `name`, an `employer-org`, a job title, or a `username` and want the subject's LinkedIn presence — but LinkedIn's own search is gated, capped, and tells the person you looked. X-raying via Google sidesteps all three: Google has indexed LinkedIn's public profiles, so a `site:` dork surfaces the profile URL and a snippet (name, headline, company) from outside LinkedIn entirely.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run `site:linkedin.com/in "<Name>"` — add an `employer-org`, city, or job title to disambiguate (e.g. `site:linkedin.com/in "Jane Doe" "Acme Corp"`).
2. For company staff enumeration: `site:linkedin.com/in "Acme Corp" "Software Engineer"`.
3. Read the result snippets — often enough (name, current role, company) to confirm identity before you ever open LinkedIn.
4. To view the profile itself, open it **logged out** or in a sock-puppet session / Google cache — a logged-in view can notify the person.
5. Pivot: the profile confirms `employer-org` and role; company links feed org research; the name feeds cross-platform search.

## Inputs → Outputs
- **In:** `name`, `username`, plus optional `employer-org`/title/location to narrow
- **Out:** public LinkedIn `social-profile` URLs, `name`, headline, and `employer-org` from the indexed snippet
- **Empty/negative result looks like:** no LinkedIn hits — the person may have no profile, a locked-down/non-indexed one, or a very common name drowning the results. Add employer/location, and try `site:linkedin.com/pub` and country subdomains before concluding.

## Gotchas & OpSec
- **Don't view logged in** on your real account — that leaks your identity to the target. Snippet + logged-out/cache viewing keeps it passive.
- LinkedIn restricts how much of a profile is visible when logged out; the Google snippet is sometimes more than the page shows anonymously.
- Common names need an employer/title/location filter; otherwise you'll drown in false matches.

## Overlaps ("do both")
- Pairs with `[[google-com-77]]` (the general advanced-search form) and `[[usearchfrom-com]]` (localise the query to the subject's country).
- Complements dedicated LinkedIn X-ray/recruiting tools that build the `site:` query for you.

## Trust & verifiability
`trust: trusted` — it's Google's first-party index over LinkedIn's own public profiles, so a hit is a real profile; confirm the person via corroborating details (employer, location, photo) since same-named profiles are common.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-com-54 |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
