---
id: netbootcamp-s-people-tool
name: NetBootCamp People Search
description: Use when you have a `name` (or screen name / phone / address) and want one console that fires the query into dozens of US people-search and social sites at once — returns `address`, `phone`, `email`, `associate`, `social-profile` and `dob` leads.
url: https://netbootcamp.org/peoplesearch.html
category: people-search
path:
- people-search
bestFor: Fanning a single name/handle out across many people-search, social and public-record sites from one form instead of visiting each site manually.
selectorsIn:
- name
- username
- phone
- address
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- dob
status: live
pricing: free
costNote: The query console itself is free. It hands off to third-party sites, several of which paywall the full report even though the search is free — cost lands downstream, not on NetBootCamp.
opsec: passive
opsecNote: The tool builds and opens searches on other sites in your browser; each downstream site sees your browser/IP. Run it in a sock-puppet browser. It does not contact the subject, but data brokers it forwards to may log your queries.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running investigator resource by Bob Brasich (@NetBootCamp), widely cited in OSINT tool lists; it is a query launcher, so result quality is entirely that of the destination sites.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- facebook-search-tool-2
- netbootcamp-org-websitetool-html
aliases:
- NetBootCamp People Search
- netbootcamp.org peoplesearch
tags:
- people-search
- aggregator
- query-launcher
source: metaosint
lastVerified: '2026-07-13'
enrichment: full
---

# NetBootCamp People Search

> A single web console that reformats one name/handle/phone into ready-to-fire searches across dozens of people-search, social and public-record sites.

## When to use
You have a `name` (or screen name, `phone`, or `address`) and want breadth fast — a first sweep that shows which of many US people-search and social platforms return a hit, before you invest time in any single one. It is a launcher, not a database: it saves the tedium of retyping the same query into 30 sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://netbootcamp.org/peoplesearch.html.
2. Enter the subject's name (and any known phone/address/screen name) into the relevant module's form.
3. Click a site button to fire that pre-built search; it opens the destination site's results in a new tab.
4. Work across the modules (people search, social/Facebook, Instagram, etc.), triaging which destinations returned real hits.
5. Pivot: promising hits move to the specific enrichment tool for that source; an `associate`/`address`/`dob` from one broker cross-checks another.

## Inputs → Outputs
- **In:** `name`, `username` (screen name), `phone`, or `address`
- **Out:** links into third-party results yielding `address`, `phone`, `email`, `associate`, `social-profile`, `dob`
- **Empty/negative result looks like:** the launched searches all land on "no records"/upsell pages — common for common names or non-US subjects; treat as coverage gaps of the destinations, not a definitive negative.

## Gotchas & OpSec
- Human-in-the-loop: you must read and judge each destination's results — the tool only builds and opens the queries, it does not aggregate or de-dupe.
- US-centric: most destinations are US data brokers; coverage drops sharply outside the US.
- OpSec: passive toward the subject, but every destination broker sees your session — use a sock-puppet browser and expect some sites to be paywalled.

## Overlaps ("do both")
- Pairs with any single people-search engine — NetBootCamp is the broad first pass that tells you *which* engine to go deep on next.

## Trust & verifiability
`trust: community` — a respected, long-standing investigator tool, but because it only launches searches, verifiability is inherited from each destination site; confirm findings on the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | netbootcamp-s-people-tool |
