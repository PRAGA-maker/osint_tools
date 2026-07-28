---
id: dorks-collections-list
name: Dorks collections list
description: Use when you have a `name`, `username`, `email`, or `domain` and want ready-made dork queries to hunt it across engines — returns curated dork sets pointing at `document-id`/exposed data.
url: https://github.com/cipher387/Dorks-collections-list
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A meta-index of Google/Shodan/GitHub/etc. dork collections to copy-paste when hunting a selector across search engines.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- document-id
- social-profile
status: live
pricing: free
costNote: Free and open-source reference repo; no install strictly needed (it's a Markdown link index), though you can clone it.
opsec: passive
opsecNote: The repo itself is passive to read. The dorks you then run execute on third-party search engines (Google, Shodan, Censys, GitHub) — those log your queries but the target isn't touched. Some dork categories (carding, cameras) point at sensitive/illegal content; stay within your investigative scope and law.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Curated by cipher387 (Cyber Detective), a well-known OSINT author; it's a link aggregator, so quality varies by the external lists it points to.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- advanced-search-operators-list
- apis-for-osint
- awesome-grep
- code-understanding-tools-list
- grep-for-osint
- maltego-transforms-list
- python-osint-automation-examples
aliases:
- cipher387 dorks list
- dorks collection
tags:
- google-dorking
- search-operators
- reference
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Dorks collections list

> A curated index of dork collections — pointers to repos and articles full of ready-made advanced-search queries for Google, Bing, Shodan, Censys, GitHub, and more.

## When to use
You have a selector — a `name`, `username`, `email`, or `domain` — and want proven advanced-search syntax to surface it: admin panels, exposed documents, leaked credentials, cameras, cloud buckets, LinkedIn X-Ray searches, CMS fingerprints. Rather than inventing operators, you copy a maintained dork and adapt it. It's a technique library, not a lookup tool, so it amplifies whatever search engine you already use for finding a person's footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/cipher387/Dorks-collections-list and skim the categorised table of dork sources.
2. Pick the category matching your need (e.g. Google dorks for documents, GitHub dorks for leaked secrets, Shodan/Censys for exposed devices, "LinkedIn X-Ray" for people).
3. Follow the link to the specific dork list, copy a query, and substitute your selector (`site:`, `intext:`, the target `domain`/`name`).
4. Run it in the relevant engine (Google, Shodan, GitHub search, etc.) and review hits.
5. Pivot: exposed `document-id`s feed metadata extraction; discovered profiles feed username/social search.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, or `domain` (dropped into the chosen dork)
- **Out:** the dork query itself, which yields `document-id` (indexed files/pages) and `social-profile` hits when run
- **Empty/negative result looks like:** a dork that returns nothing — either the target has no indexed exposure, or the operator needs narrowing/broadening; try a sibling dork from the list.

## Gotchas & OpSec
- It's a pointer collection, so some linked lists are stale or contain dead operators; verify a dork still works.
- Running aggressive dorks fast triggers CAPTCHAs/rate limits on Google and others — pace queries.
- Several categories (carding, private cameras) point at content that is unethical or illegal to exploit; use only what fits an authorised investigation.

## Overlaps ("do both")
- Sits alongside `[[advanced-search-operators-list]]` and `[[grep-for-osint]]`; pair with `[[apis-for-osint]]` and `[[python-osint-automation-examples]]` to automate the dorks you find here.

## Trust & verifiability
`trust: community` — maintained by a reputable OSINT author, but it's an aggregator of third-party lists; treat each linked dork as unverified until you run it and confirm the results yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorks-collections-list |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, email, domain → document-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
