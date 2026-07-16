---
id: nerdydata
name: NerdyData
description: Use when you have a code snippet, tracking ID, or tech string and want every website whose source contains it — returns the matching `domain`s (e.g. sites sharing a Google Analytics/AdSense ID).
url: https://www.nerdydata.com/reports/new
category: search-engines
path:
- search-engines
- code-search
bestFor: Source-code search across the web — finding all sites that contain a given snippet, library, or tracking/analytics identifier.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Limited free preview searches; full result sets and exports require a paid account. Registration required.
opsec: passive
opsecNote: Searches NerdyData's pre-built index of page source, not the target sites live, so the sites you research are not contacted and do not see you. Passive.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: An established commercial source-code search engine; results reflect its crawl coverage and freshness, which are good but not exhaustive.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- nerdydata-source-code-search-engine
aliases:
- nerdydata.com
tags:
- code-search
- tech-fingerprint
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# NerdyData

> A search engine for the *source code* of websites — find every site whose HTML/JS contains a given snippet, library, or tracking ID.

## When to use
You want to connect websites that share a fingerprint: the same Google Analytics/AdSense ID, a distinctive code snippet, a specific library, or a reused template. This is a core technique for tying a subject's multiple sites together — e.g. finding all `domain`s that embed the same analytics ID as a known site, revealing a network of properties under common control.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nerdydata.com/ and register an account.
2. Start a new source-code search; enter the snippet, library name, or identifier (e.g. `UA-XXXXXX`, `ca-pub-XXXX`, a unique class or comment).
3. Run the search against NerdyData's crawled index.
4. Read the output: a list of `domain`s whose source contains the string (fuller results/export behind the paid tier).
5. Pivot: cross-reference the returned sites; feed shared analytics/AdSense IDs into other reverse-analytics tools to widen the cluster.

## Inputs → Outputs
- **In:** `domain`/a code snippet or tracking identifier extracted from a known site
- **Out:** `domain` (other websites whose source contains the same string)
- **Empty/negative result looks like:** no sites match — the string is unique/rare or outside NerdyData's crawl; try a reverse-analytics tool for the same ID.

## Gotchas & OpSec
- Free tier is a limited preview; the complete result set/export is paywalled (login + paid plan).
- Coverage is a snapshot of NerdyData's crawl — recent or low-traffic sites may be missing, and modern GA4 IDs behave differently from legacy `UA-` IDs.
- OpSec: passive — it queries an index, so target sites are never contacted.

## Overlaps ("do both")
- Pairs with `[[nerdydata-source-code-search-engine]]` (same provider) and reverse-analytics tools (e.g. shared AdSense/Analytics ID lookups) — do both, since crawl coverage differs and each finds sites the other misses.

## Trust & verifiability
`trust: community` — a mature commercial code-search index. Matches are real code occurrences (verifiable by viewing the site's source), bounded only by crawl coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nerdydata |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
