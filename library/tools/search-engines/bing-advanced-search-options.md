---
id: bing-advanced-search-options
name: Bing Advanced Search Options
description: Use when you have any selector to query and want to search Bing precisely — a reference to Bing's advanced operators (site:, filetype:, contains:, ip:) for sharper OSINT dorking.
url: https://help.bing.microsoft.com/#apex/bing/en-us/10002/0
category: search-engines
path:
- search-engines
bestFor: Learning Bing's operator syntax so you can build targeted dorks that surface results Google filters out.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- document-id
- domain
status: live
pricing: free
costNote: Free reference documentation from Microsoft; Bing search itself is free and needs no account.
opsec: passive
opsecNote: Reading the operator reference is passive. Running the resulting queries touches Microsoft/Bing (which logs searches) but does not contact your target directly; use a sock-puppet browser/IP for sensitive dorks and avoid clicking through to attacker-controlled result pages from a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft help documentation for the Bing search engine; the operator list is authoritative even if some operators are quietly deprecated over time.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Bing search operators
- Bing dorking reference
tags:
- toddington
- curated-directory
- search-engines
- dorking
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bing Advanced Search Options

> Microsoft's own reference for Bing's advanced search operators — the syntax cheat-sheet behind effective Bing dorking, a useful complement to Google when the two indexes diverge.

## When to use
You are running search-engine reconnaissance on any selector (a `name`, `username`, `email`, or `domain`) and want to narrow Bing with operators instead of scrolling generic results. Bing indexes and surfaces some pages Google buries, and it supports a few operators (notably `contains:`, `ip:`, `feed:`) that Google lacks — so this reference lets you build precise queries to find profiles, documents and site-specific mentions of a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the reference to learn the current operators: `site:`, `filetype:`/`ext:`, `intitle:`, `inbody:`, `url:`, `contains:` (pages linking a given file type), `ip:` (pages hosted on an IP), and boolean `AND`/`OR`/`NOT`, quotes and parentheses.
2. Compose a dork against your selector, e.g. `"Firstname Lastname" site:linkedin.com`, `"jdoe" filetype:pdf`, or `ip:203.0.113.5` to enumerate co-hosted sites.
3. Run it at bing.com (ideally from a sock-puppet session) and iterate — swap operators when a query is too broad or empty.
4. Compare against the same dork on Google; treat differing result sets as complementary, not contradictory.
5. Pivot: found profiles feed username/social tools; `filetype:` hits yield documents whose `metadata-exif` may leak more.

## Inputs → Outputs
- **In:** any query built from `name` / `username` / `email` / `domain`
- **Out:** matching web pages — `social-profile` links, `document-id` (PDFs/docs), co-hosted `domain`s via `ip:`
- **Empty/negative result looks like:** zero results for a tight dork; loosen operators or try Google — Bing's index is smaller in some verticals, so absence is engine-specific, not global.

## Gotchas & OpSec
- Human-in-the-loop: none, but heavy automated querying can trip a CAPTCHA — throttle manual searches.
- OpSec: **passive** toward the target; Bing logs your searches, so use a burner session for sensitive work.
- Microsoft occasionally deprecates or changes operators; if one returns nothing unexpectedly, verify it still exists rather than concluding the subject is absent.

## Overlaps ("do both")
- Pairs with Google advanced-operator dorking because the two engines index different corners of the web — run the same query on both.

## Trust & verifiability
`trust: trusted` — first-party Microsoft documentation for its own engine; authoritative, though the live operator set drifts, so re-test operators periodically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bing-advanced-search-options |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, document-id, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
