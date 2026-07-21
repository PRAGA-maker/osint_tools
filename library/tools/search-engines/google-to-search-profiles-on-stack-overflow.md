---
id: google-to-search-profiles-on-stack-overflow
name: RecruitEm — Stack Overflow X-ray
description: Use when you have a `name`, skills or a location and want to find matching Stack Overflow profiles via a Google X-ray query — returns `social-profile`.
url: https://recruitin.net/stackoverflow.php
category: search-engines
path:
- search-engines
bestFor: Building a Google X-ray (site:) search to surface Stack Overflow profiles by name, skills, or location.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Completely free with no registration; it only assembles a Google search query for you to run.
opsec: passive
opsecNote: The tool just builds a query string; the actual search runs on Google under your session. Run it in a sock-puppet browser so the searches aren't tied to your identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: RecruitEm is a long-running free recruiter-sourcing tool; it does no data collection itself — it generates a Google dork, so result quality is entirely Google's.
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
- google-to-search-profiles-on-dribbble
- google-to-search-profiles-on-xing
- recruitem
aliases:
- RecruitEm Stack Overflow
- Stack Overflow X-ray search
tags:
- search-engines
- x-ray-search
- google-dork
- stack-overflow
- developer-osint
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# RecruitEm — Stack Overflow X-ray

> A boolean/X-ray query builder — fill in a name, skills and location and it hands you a `site:stackoverflow.com` Google search that surfaces matching developer profiles.

## When to use
Your subject is (or may be) a developer, and you want to find their Stack Overflow profile — a rich source of real name, location, employer, personal website, and other linked accounts that developers often fill in. This tool constructs the precise Google X-ray query (`site:stackoverflow.com/users ...`) from the fields you give it, so you don't have to hand-craft the dork. Handy when you have a `name` and a tech stack, or want to enumerate developers in a location/skill.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://recruitin.net/stackoverflow.php.
2. Fill in the fields: skills/keywords (comma-separated, or a `name` as a phrase), optional location (country or city), and the "exclude no-answer" filter.
3. Click to generate the Google query, then run it (the tool launches Google or gives you the query string).
4. Review the Google results — Stack Overflow profile pages (`social-profile`) matching your criteria.
5. Open a profile to read the real name, location, employer, personal site and linked GitHub/socials; pivot those into username and people tooling.

## Inputs → Outputs
- **In:** `name` and/or `username`, skills/keywords, location
- **Out:** `social-profile` — Stack Overflow profiles matching the query (each often exposing real name, location, employer, links)
- **Empty/negative result looks like:** few or irrelevant Google hits — meaning the query is too narrow/broad or the person isn't findable this way; loosen keywords or try the GitHub/Twitter X-ray variants.

## Gotchas & OpSec
- Human-in-the-loop: none, though you run the resulting Google search yourself (watch for CAPTCHAs on heavy querying).
- OpSec: passive — the tool builds a string; use a sock-puppet browser so the Google searches aren't linked to you.
- It finds nothing itself — quality depends on Google's index and on the developer having filled in their profile. A common name needs a skill/location to disambiguate.

## Overlaps ("do both")
- Part of the RecruitEm X-ray family — pair with `[[google-to-search-profiles-on-github]]`, `[[google-to-search-profiles-on-twitter]]` and the others to sweep the same person across developer and social platforms.

## Trust & verifiability
`trust: community` — a reputable free sourcing tool that merely generates a Google query; the results are Google's, so verify each profile directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-to-search-profiles-on-stack-overflow |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
