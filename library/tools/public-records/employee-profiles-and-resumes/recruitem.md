---
id: recruitem
name: RecruitEm
description: Use when you have a `name`/`employer-org`/skills and want to X-ray-search LinkedIn, GitHub, Xing, Twitter etc. for a person's profile — returns a ready Google boolean query and `social-profile` links.
url: https://recruitin.net/
category: public-records
path:
- public-records
- employee-profiles-and-resumes
bestFor: Building Google X-ray (site:) boolean queries to find a person's LinkedIn/GitHub/Xing/Stack Overflow/Twitter profile without logging into those platforms.
selectorsIn:
- name
- employer-org
- username
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Totally free, no registration; it only builds and launches a Google query, so the only "cost" is Google's normal rate limits.
opsec: passive
opsecNote: RecruitEm itself just constructs a Google search string — the actual search runs on Google, and you never touch LinkedIn's servers, so the target gets no "who viewed your profile" signal. Run the resulting query in a sock-puppet Google session for full separation.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing, widely used recruiter X-ray tool (recruitin.net); it generates standard Google site: dorks, so results are only as good/fresh as Google's index of the target platform.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-to-search-profiles-on-github
- google-to-search-profiles-on-twitter
- google-to-search-profiles-on-xing
aliases:
- RecruitEm
- recruitin.net
tags:
- x-ray-search
- linkedin
- google-dork
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# RecruitEm

> A free query-builder that turns a name/role/employer into a polished Google X-ray (`site:`) search for LinkedIn, GitHub, Xing, Stack Overflow, Twitter and more — find profiles without ever logging into those platforms.

## When to use
You want a subject's professional `social-profile` (LinkedIn especially) but don't want to log in and leave a "profile view" footprint. Given a `name`, `employer-org`, job title, location, or skills, RecruitEm assembles a boolean `site:linkedin.com/in` (or GitHub/Xing/etc.) Google query so you can find and read the public profile snippet via Google instead of the platform itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://recruitin.net/ and pick the target platform tab (LinkedIn, GitHub, Xing, Stack Overflow, Twitter, Dribbble…).
2. Fill in what you know — job title (with synonyms), location/keywords to include, keywords to exclude, current employer, education. For a specific person, put their `name` in the keyword field.
3. Click to generate the boolean query; launch it on Google (ideally in a sock-puppet session), or copy the string to refine.
4. Read the Google results — profile titles/snippets often reveal the person even when the platform would gate the full page.
5. Pivot: a confirmed `social-profile` feeds username enumeration and cross-platform search; `employer-org` from the snippet feeds company/colleague mapping.

## Inputs → Outputs
- **In:** `name`, `employer-org`, job title/skills, location
- **Out:** a Google boolean query and resulting `social-profile` links (LinkedIn/GitHub/Xing/etc.), plus `employer-org` context from snippets
- **Empty/negative result looks like:** the query returns no relevant profiles — the person may not be on that platform, uses a different name/handle, or Google hasn't indexed their page. Try other platforms and name variants.

## Gotchas & OpSec
- It only builds a query — all data comes from Google's index, which can lag behind the live platform.
- Google may throw a CAPTCHA on aggressive boolean queries; solve it or slow down.
- OpSec: passive toward the target (no platform login), but tie the Google search to a sock puppet if attribution matters.

## Overlaps ("do both")
- Pairs with `[[google-to-search-profiles-on-github]]`, `[[google-to-search-profiles-on-twitter]]`, `[[google-to-search-profiles-on-xing]]` and direct username-search tools — RecruitEm centralises the query-building while those target single platforms.

## Trust & verifiability
`trust: community` — a reputable, established recruiter tool; it introduces no data of its own, so verifiability reduces to Google's index and the target platform's public content.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | recruitem |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org, username → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
