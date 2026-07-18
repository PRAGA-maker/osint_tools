---
id: google-dork-cheatsheet
name: Google Dork Cheatsheet
description: Use when you want to sharpen a Google/search query into a targeted dork — a reference of operators and ready-made queries that turn a selector into precise page/document hits.
url: https://github.com/robyfirnandoyusuf/Google-Dork-Cheatsheet
category: search-engines
path:
- search-engines
bestFor: A quick-reference of Google search operators and ready-to-adapt dork queries for OSINT.
selectorsIn:
- name
- domain
selectorsOut:
- document-id
- domain
status: live
pricing: free
costNote: Free open reference on GitHub; no account, nothing to install (it's a document, not an app).
opsec: passive
opsecNote: The cheatsheet itself is just a reference — reading it does nothing observable. OpSec applies to the dorks you then run: exact-string and site-scoped queries can hit sensitive/exposed pages, so run them logged-out via a sock puppet, and remember clicking a result contacts that server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained GitHub cheatsheet; the operators are standard and reliable, but any specific canned dork should be understood before use, not run blindly.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google
- google-custom-search
aliases:
- Google dorks cheatsheet
- Google hacking operators
tags:
- google-dorks
- reference
- search-operators
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# Google Dork Cheatsheet

> A reference of Google search operators and prebuilt "dork" queries — the lookup table for turning a plain search into a surgical one.

## When to use
Whenever a plain Google search is too noisy and you want to construct a **dork** — a query using operators to pin down exactly what you need. Reach for this cheatsheet to remember the operator syntax (`site:`, `inurl:`, `intitle:`, `intext:`, `filetype:`, `AROUND(n)`, exact quotes, `-exclusions`) and to borrow ready-made patterns for finding exposed documents, directories, login pages, or a person's mentions on a specific platform. It's a companion to the search itself, not a search engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the cheatsheet at https://github.com/robyfirnandoyusuf/Google-Dork-Cheatsheet.
2. Find the operator or example that matches your goal (scope to a site, filter by file type, find exposed pages, etc.).
3. Adapt the query with your selector — e.g. `site:linkedin.com "Firstname Lastname"`, `filetype:pdf "Firstname Lastname" CV`, `intext:"john@example.com"`, `inurl:"target.com" filetype:xlsx`.
4. Run it in Google (logged out / sock puppet); iterate — combine operators, add a location or employer, exclude noise.
5. Pivot: exposed documents/pages become new selectors and evidence; refine the dork as you learn the target's naming patterns.

## Inputs → Outputs
- **In:** a selector to build a query around — `name`, `domain`, email/handle, etc.
- **Out:** the *technique* to retrieve `document-id` files, specific `domain`/URL patterns, and precise page hits from a search engine
- **Empty/negative result looks like:** the cheatsheet always "works" (it's a reference); the failure mode is a dork returning nothing — over-constrained, or the content simply isn't indexed. Loosen operators and retry.

## Gotchas & OpSec
- Human-in-the-loop: none to read; aggressive dorking in Google triggers CAPTCHAs/rate limits.
- OpSec: **passive** to read, but the dorks you run can surface sensitive material — search logged-out via a sock puppet, and open risky results through an archive rather than clicking straight through.
- Understand a canned dork before running it; some published dorks target genuinely sensitive exposures, and clicking through can touch systems you didn't intend to.
- Operators evolve — some (notably `cache:`) have been retired by Google; verify a rare operator still works.

## Overlaps ("do both")
- Pairs directly with `[[google]]` (where you run the dorks) and `[[google-custom-search]]` (to save a scoped multi-site dork as a reusable engine).

## Trust & verifiability
`trust: community` — a community GitHub reference; the operator syntax is standard and dependable, but treat specific prebuilt queries as examples to understand and adapt, not to run blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-dork-cheatsheet |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → document-id, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
