---
id: sapo
name: SAPO
description: Use when your subject is Portuguese or Portugal-based and you want a local web portal/search to surface localised results and profiles — returns `social-profile`, `domain`.
url: https://www.sapo.pt
category: search-engines
path:
- search-engines
bestFor: Portugal-focused web search and portal content that global engines under-rank.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to search and browse; a free SAPO account is only needed for its mail/webmail and personalised services.
opsec: passive
opsecNote: Searching is passive and anonymous. Do not sign into a SAPO account tied to your real identity; if you need account-gated services, use a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A major, long-established Portuguese web portal (Altice Portugal); reliable as a regional search/content gateway, though results are aggregated web content, not a vetted record.
missingPersonsRelevance: low
coverage:
- pt
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SAPO Portugal
- sapo.pt
tags:
- search
- international
- portugal
source: metaosint
lastVerified: '2026-07-18'
enrichment: full
---

# SAPO

> Portugal's long-standing web portal and search — a regional angle that surfaces Portuguese-language results, local sites, and profiles a global engine tends to bury.

## When to use
Your subject is Portuguese, lives in Portugal, or has a strong Portugal connection, and you want a search entry point tuned to that market. SAPO is a general portal (search, news, directory, webmail) widely used in Portugal, so a `name` or `username` run here can surface local news mentions, Portuguese social/community profiles, and regional sites that rank low internationally. Use it as a country-specific supplement to mainstream search, not a specialised person index.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sapo.pt.
2. Search the subject `name` or `username`; also try Portuguese spellings/diacritics and a site-scoped engine query for Portuguese domains.
3. Scan results for local news, `.pt` sites, and community/social profiles tied to the subject.
4. Read the output: candidate `social-profile` links and `domain`s worth pivoting on.
5. Pivot: feed a profile into username tools; feed a `.pt` domain into whois/domain tools; feed a news mention into wider news search.

## Inputs → Outputs
- **In:** `name` or `username`
- **Out:** `social-profile` (Portuguese profiles/mentions), `domain` (local sites)
- **Empty/negative result looks like:** only generic portal/news content with nothing tied to the subject — no local footprint surfaced; try Portuguese-language query variants before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none for search; account only needed for mail/personalised features.
- OpSec: passive; keep any SAPO login on a sock puppet.
- Portuguese-language content dominates — search with correct diacritics and local name forms to get useful hits.

## Overlaps ("do both")
- Pairs with mainstream and other regional search engines — SAPO adds Portugal-market coverage that global engines under-rank. Do both and reconcile the local vs global result sets.

## Trust & verifiability
`trust: community` — a major established Portuguese portal, reliable as a regional gateway; its output is aggregated web content, so verify anything it surfaces at the original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sapo |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
