---
id: google-to-search-profiles-on-twitter
name: Google to search profiles on Twitter
description: Use when you have a `name`, keyword, or location and want to find matching X/Twitter profiles via a Google X-ray query — returns candidate `social-profile` links.
url: https://recruitin.net/twitter.php
category: social-networks
path:
- social-networks
bestFor: Building a Google site:x.com / site:twitter.com X-ray query to surface profiles by name, skill, or city.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Completely free, no registration; it is a query-builder front-end, the actual search runs on Google.
opsec: passive
opsecNote: The page only assembles a Google search string — no data is sent to the target. The search itself runs on Google under your session/IP; use a sock-puppet browser if you don't want the query tied to you. You never touch X's own infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: RecruitEm (recruitin.net) is a long-running recruiter X-ray tool; it does not hold data itself, so trust reduces to trusting Google's index.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- RecruitEm Twitter X-ray
- recruitin.net twitter
tags:
- twitter
- x-ray-search
- google-dork
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- google-to-search-profiles-on-dribbble
- google-to-search-profiles-on-github
- google-to-search-profiles-on-stack-overflow
- google-to-search-profiles-on-xing
- recruitem
---

# Google to search profiles on Twitter

> RecruitEm's X-ray builder: it turns a name/skill/location into a ready-made Google query that finds X (Twitter) profiles indexed by Google.

## When to use
You have a `name`, an `employer-org`, a job title, a skill, or a city and want to locate the subject's X/Twitter profile without using X's own (login-walled, throttled) search. Because it queries Google's cache of `twitter.com` / `x.com`, it can surface profiles and posts even when native Twitter search is unavailable to you. Good for a first-pass identity sweep on a partially-known subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://recruitin.net/twitter.php.
2. Enter what you know: a location (use a city, e.g. "New York"), keywords/skills to include, and optional keywords to exclude. For a person hunt, put the subject's name or handle fragments in the include field.
3. Click to generate the query; the tool opens (or hands you) a Google X-ray search like `site:twitter.com "name" "city"`.
4. Read Google's results for candidate `social-profile` / `username` matches; refine include/exclude terms to narrow.
5. Pivot: confirmed handles feed username-enumeration tools and `[[proxycurl]]`-style enrichment or manual profile review.

## Inputs → Outputs
- **In:** `name` (or handle fragment), keywords, location, `employer-org`
- **Out:** `social-profile` URLs and `username` handles from Google's index
- **Empty/negative result looks like:** Google returns unrelated pages or nothing — the subject isn't indexed under those terms, or the profile is too new/obscure for Google's cache. Broaden terms and retry.

## Gotchas & OpSec
- Human-in-the-loop: none for the builder; Google may throw a CAPTCHA if you run many queries.
- OpSec: **passive** — the target is never contacted. The query runs under your Google session; use a clean browser/IP for sensitive work.
- Google's Twitter index is partial and stale; absence here is not proof the profile doesn't exist. Confirm on X directly.

## Overlaps ("do both")
- Pairs with `[[proxycurl]]`-type enrichment and native handle-checkers — this finds the handle, they expand it.

## Trust & verifiability
`trust: community` — the tool holds no data of its own; results are only as good (and as current) as Google's crawl of Twitter/X. Always click through to the live profile to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-to-search-profiles-on-twitter |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
