---
id: linkedin-x-ray-search
name: LinkedIn X-Ray Search
description: Use when you have a `name` (and optionally an `employer-org`) and want to find someone's LinkedIn profile without logging in — returns a `social-profile` and current `employer-org`.
url: https://de.linkedin.com/pub/dir/bruno/mortier
category: social-networks
path:
- social-networks
bestFor: Locating a person's LinkedIn profile from outside the platform via the public directory and search-engine site: dorks.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
- name
status: live
pricing: free
costNote: Free technique — uses LinkedIn's public first-name/last-name directory (linkedin.com/pub/dir/) and general web search operators; no LinkedIn account required.
opsec: passive
opsecNote: X-ray searching via Google/Bing never touches the target's LinkedIn session and does not trigger "who viewed your profile." Opening the resulting public profile logged-out is low-risk; if you click through while logged into an attributable LinkedIn account, the target may see you in viewer/PYMK signals — use a sock-puppet or logged-out session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Not a product but a technique built on LinkedIn's own public directory plus search-engine operators; reliability varies as LinkedIn adjusts what it exposes to logged-out users and crawlers.
missingPersonsRelevance: high
coverage:
- global
aliases:
- LinkedIn public directory
- LinkedIn pub dir
- LinkedIn Google dork
tags:
- linkedin
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# LinkedIn X-Ray Search

> Finding LinkedIn profiles from the outside — via LinkedIn's public first/last-name directory and search-engine `site:` dorks — so you never have to log in or tip off the target.

## When to use
You have a `name`, ideally plus an `employer-org`, job title, or location, and want the person's LinkedIn profile without burning an account or appearing in their profile-viewer list. X-ray search is the standard passive way to resolve a name → `social-profile` → current employer and role, which then anchors identity across other tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Public directory:** the URL pattern `https://<cc>.linkedin.com/pub/dir/<firstname>/<lastname>` (e.g. the sample `.../pub/dir/bruno/mortier`) lists public profiles matching that name. Swap in your subject's first/last name.
2. **Search-engine X-ray (usually stronger):** run in Google/Bing:
   - `site:linkedin.com/in "First Last"`
   - `site:linkedin.com/in "First Last" "<employer-org>"` or `... "<job title>" "<city>"` to disambiguate.
3. Scan results: the profile snippet shows current `employer-org`, headline, and location even from the search result, before you click.
4. Open the profile logged-out (or from a sock puppet) to read the public portion.
5. Pivot: the confirmed name + employer feeds email-pattern guessing, `[[nqntnqnqmb]]` for deeper LinkedIn extraction, and cross-platform username checks.

## Inputs → Outputs
- **In:** `name` (+ `employer-org` / title / location to disambiguate)
- **Out:** `social-profile` (LinkedIn URL), current `employer-org`, confirmed display `name` and headline
- **Empty/negative result looks like:** the `/pub/dir/` page shows "no results" and `site:linkedin.com` dorks return nothing matching your qualifiers — the person may have a locked-down profile, a different name form, or no LinkedIn presence.

## Gotchas & OpSec
- Common names return many candidates; always add an employer, title, school, or city qualifier to avoid a wrong match.
- LinkedIn periodically limits what logged-out visitors and crawlers see, so the public directory and cached snippets can be thinner than the full profile.
- OpSec: the search itself is passive. The risk is clicking through while logged into an attributable account — do it logged-out or with a sock puppet.

## Overlaps ("do both")
- Pairs with `[[nqntnqnqmb]]` — X-ray finds the right profile passively; nqntnqnqmb (with session cookies) extracts richer detail and contact info from it. Also pairs with general people-search to corroborate the employer/location.

## Trust & verifiability
`trust: community` — this is a technique over LinkedIn's own public surface and web indexes, not a maintained product; results are only as fresh as the crawl. Verify a match by cross-checking employer, location, and photo, not name alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin-x-ray-search |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
