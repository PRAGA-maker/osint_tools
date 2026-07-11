---
id: linkedin-x-ray-search-tool
name: LinkedIn X-Ray Search Tool (LISearcher)
description: Use when you have a `name`, job title, employer, or location and want public LinkedIn profiles — builds a Google X-ray query and returns links to matching social-profiles without touching LinkedIn.
url: https://www.lisearcher.com/
category: social-networks
path:
- social-networks
bestFor: Finding public LinkedIn profiles by title/company/location via Google, without logging into LinkedIn.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free; no account or registration. It generates a Google search query you run (or it opens for you).
opsec: passive
opsecNote: Big OpSec win — you find LinkedIn profiles via Google, so you never appear in LinkedIn's "who viewed your profile," and the subject gets no signal. You do run a Google query (standard Google-session privacy applies); the actual profile visit, if you make one, is where LinkedIn could see you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A free recruiter-oriented X-ray query builder; it just constructs a Google `site:linkedin.com` boolean query, so results are as good as Google's index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- LISearcher
- LinkedIn X-Ray
tags:
- linkedin
- x-ray-search
- boolean
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# LinkedIn X-Ray Search Tool (LISearcher)

> A boolean query builder that finds public LinkedIn profiles through Google — reach a subject's professional profile without ever logging into LinkedIn.

## When to use
You want a subject's LinkedIn profile but don't want to search inside LinkedIn (which shows you to them and demands a login). Given a `name`, job title, `employer-org`, or location, LISearcher assembles a Google `site:linkedin.com/in` boolean query so you find the public profile via Google — quietly, with include/exclude keyword control to cut noise.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.lisearcher.com/.
2. Enter what you know — name and/or job title, keywords, company, location; add excluded keywords to filter.
3. Copy the generated Google query, or hit "Open Search in Google."
4. Review the Google results — links to public LinkedIn `social-profile`s matching your criteria.
5. Pivot: a confirmed profile yields employer/title/location and connections; read the public snapshot from Google's cache/preview first to stay off LinkedIn's radar.

## Inputs → Outputs
- **In:** `name`, job title, `employer-org`, location, keywords
- **Out:** Google links to matching public LinkedIn `social-profile`s
- **Empty/negative result looks like:** few/no Google hits. This means Google hasn't indexed a matching public profile — the person may have a private/limited profile, a common name buried under noise, or no LinkedIn at all. Refine keywords before concluding absence.

## Gotchas & OpSec
- It only builds a query — Google (not LISearcher) returns the results, bounded by Google's index of public LinkedIn pages.
- OpSec: **passive** and the big draw — finding via Google keeps you out of LinkedIn's "who viewed" tracking; only a direct logged-in profile visit would expose you, so prefer the Google preview.
- Private/out-of-network profiles are limited from Google too; you'll see the public slice.

## Overlaps ("do both")
- Pairs with RecruitEm and other X-ray builders (they template the same `site:` trick across networks) and with plain manual Google dorking — use LISearcher for speed, hand-craft dorks when you need finer control.

## Trust & verifiability
`trust: community` — a simple, widely-used query builder; the results are Google's, so verify each profile by opening it (ideally via cache/preview) and confirming identity details.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin-x-ray-search-tool |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
