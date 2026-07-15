---
id: linkedin-search-engine
name: LinkedIn Search Engine
description: Use when you have a `name`, `employer-org` or `username` and want to find someone's LinkedIn profile without logging into LinkedIn — returns social-profile, name, employer-org.
url: https://cse.google.com/cse?cx=daaf18e804f81bed0
category: social-networks
path:
- social-networks
bestFor: Finding a subject's LinkedIn profile via a Google Custom Search Engine scoped to linkedin.com, without touching LinkedIn while logged in.
selectorsIn:
- name
- employer-org
- username
selectorsOut:
- social-profile
- name
- employer-org
status: live
pricing: free
costNote: Free Google Programmable/Custom Search Engine; no account required.
opsec: passive
opsecNote: Results come from Google's index of public LinkedIn pages, so you never visit LinkedIn while authenticated — the subject's "Who viewed your profile" is not triggered and no view is logged against you. Strongly preferred over searching inside a logged-in LinkedIn session. Heavy use may draw a Google CAPTCHA.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Google Custom Search Engine (config cx=daaf18e804f81bed0) scoped to LinkedIn; it is only as current as Google's index and the CSE owner's configuration, which can drift over time.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- LinkedIn CSE
- LinkedIn Google Custom Search
tags:
- linkedin
- google-cse
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# LinkedIn Search Engine

> A Google Custom Search Engine pre-scoped to linkedin.com — find a person's professional profile from Google's public index without ever logging into LinkedIn.

## When to use
You have a `name` (often plus an `employer-org`, title, or city) or a reused `username` and want the subject's LinkedIn profile, but you don't want to search from inside LinkedIn — which risks appearing in their "who viewed your profile" and ties the search to your account. This CSE queries only Google's cached/indexed public LinkedIn pages, giving you the professional layer passively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL.
2. Enter the `name`, refining with employer, job title, or location to disambiguate (e.g. `"Jane Okafor" "Acme" Lagos`).
3. Review the indexed LinkedIn results — public profile snippets show name, headline/employer and location.
4. Confirm identity from the snippet before opening; if you must open the live profile, do it logged-out or from a sock-puppet account.
5. Pivot: a confirmed employer/title feeds corporate-registry and email-format guessing; the person's name + city feeds people-search.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `username`
- **Out:** `social-profile` (LinkedIn URL), `name`, `employer-org`/title from the indexed snippet
- **Empty/negative result looks like:** no LinkedIn results (only generic Google links or nothing) — meaning Google hasn't indexed a matching public profile, not necessarily that none exists; private profiles are under-indexed.

## Gotchas & OpSec
- Coverage = Google's index of LinkedIn, which lags and misses profiles set to low visibility.
- As a community CSE, the configuration can be changed or break; if it returns off-topic results, fall back to a manual Google `site:linkedin.com/in "<name>"` dork.
- OpSec: passive and preferred — avoids LinkedIn's viewer notifications; a CAPTCHA may appear under heavy querying.

## Overlaps ("do both")
- Pairs with `[[social-search-engine]]` — this goes deep on the LinkedIn professional layer, while the broad aggregator catches the subject's presence on other networks.

## Trust & verifiability
`trust: community` — a third-party Google CSE, not an official LinkedIn product; the underlying data is real public LinkedIn content from Google's index, but freshness and scope depend on Google and the CSE owner.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin-search-engine |
| category | social-networks |
| selectorsIn → selectorsOut | name, employer-org, username → social-profile, name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
