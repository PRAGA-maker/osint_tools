---
id: google-to-search-profiles-on-github
name: Google to Search Profiles on GitHub (Recruitin)
description: Use when you have a `name`, skill, or `employer-org` and want to find someone's GitHub profile — builds a Google X-ray search string to surface GitHub profiles by keyword/location.
url: https://recruitin.net/github.php
category: documents-metadata
path:
- documents-metadata
bestFor: Generating a Google X-ray query to find GitHub user profiles by name, skills, location, or employer.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- username
status: live
pricing: free
opsec: passive
opsecNote: The tool just assembles a Google search string; running that search is a normal, passive Google query — the GitHub user isn't contacted or alerted. The actual searching happens on Google, so do it from a sock-puppet/de-personalized session. No data about the subject is sent to Recruitin beyond the keywords you type into the builder.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running recruiter "X-ray"/sourcing helper (Recruitin, formerly Recruit'em); it just crafts Google dorks, so results are Google's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-to-search-profiles-on-dribbble
- google-to-search-profiles-on-stack-overflow
- google-to-search-profiles-on-twitter
- google-to-search-profiles-on-xing
- recruitem
aliases:
- Recruitin GitHub
- Recruit'em GitHub X-ray
tags:
- x-ray-search
- github
- google-dork
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Google to Search Profiles on GitHub (Recruitin)

> A form that builds a Google "X-ray" search string to find GitHub profiles — fill in name, skills, location, or employer and it hands you a Google query that surfaces matching github.com/<user> pages.

## When to use
You want to find a subject's GitHub presence (or developers matching certain attributes) but GitHub's own search is limited. This Recruitin builder constructs a `site:github.com` Google dork with your keywords — `name`, programming languages/skills, location, `employer-org` — so Google's index does the work of finding profiles. Good for pivoting from a real name or a tech stack to a developer's GitHub account and, from there, their repos, email, and other handles.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://recruitin.net/github.php (clear any Cloudflare check).
2. Fill in the fields — keywords/name, skills, location, employer — and generate the search string.
3. Click through to run it on Google (ideally in a de-personalized/sock-puppet session).
4. Read the Google results: matching GitHub profiles (`selectorsOut`); open profiles to pull repos, bio, linked email, and other usernames.

## Inputs → Outputs
- **In:** `name`, skills/keywords, location, or `employer-org`
- **Out:** `social-profile` (GitHub profiles) and `username` leads via Google results
- **Empty/negative result looks like:** Google returns nothing — the person may not be on GitHub, uses an unrelated handle, or your keywords are too narrow; loosen terms or try the Stack Overflow/Twitter variants.

## Gotchas & OpSec
- Human-in-the-loop: a Cloudflare check may gate the builder (`captcha`).
- OpSec: passive — it only builds a query; the search runs on Google, so use a de-personalized session. Nothing reaches the GitHub user.
- Results are only as good as Google's index and your keywords; it finds *public* profiles matching text, not a definitive person match — verify identity on the profile itself.

## Overlaps ("do both")
- Part of a family of Recruitin X-ray builders — pair with [[google-to-search-profiles-on-stack-overflow]], [[google-to-search-profiles-on-twitter]], and [[recruitem]] to sweep a subject across developer/social platforms; combine with GitHub-native OSINT tools once you have the username.

## Trust & verifiability
`trust: community` — a mature recruiter-sourcing helper that simply crafts Google queries, so the reliability is Google's. It surfaces candidate profiles; confirm any identity match by inspecting the profile's repos, bio, and linked accounts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-to-search-profiles-on-github |
| category | documents-metadata |
| selectorsIn → selectorsOut | name, employer-org → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
