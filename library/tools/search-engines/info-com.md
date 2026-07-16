---
id: info-com
name: info.com
description: Use when you have a `name` or other keyword and want an alternate general web search engine to surface pages a mainstream engine ranks differently — returns web results linking to name mentions and social-profiles.
url: https://info.com/
category: search-engines
path:
- search-engines
bestFor: A secondary general web search engine (System1) for cross-checking name/keyword results against Google/Bing.
selectorsIn:
- name
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free web search; no account. Ad-supported (operated by System1).
opsec: passive
opsecNote: A general search engine; typing a name is passive and does not notify the subject. As with any search engine, your queries are logged by the operator — use a clean/sock-puppet session and avoid clicking through to anything that would deanonymise you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A real, operational search portal run by System1; results are drawn from mainstream indexes with heavy ad monetisation, so it offers modest OSINT value beyond a ranking-diversity cross-check.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- info.com search
tags:
- searchengines
- metasearch
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- info-com-meta-search-engine-united-kingdom
---

# info.com

> A secondary general-purpose search engine (System1-operated) — worth a pass mainly because a different engine surfaces and ranks pages differently than Google, occasionally floating a mention the big engines bury.

## When to use
You have a `name` or keyword and you've already run the mainstream engines; info.com is a cheap cross-check to catch differently-ranked results. Use it as ranking diversity in a search sweep, not as a primary or specialised OSINT tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://info.com/.
2. Enter the `name` (in quotes for exact match) plus any qualifier — location, employer, username.
3. Scan the web results for pages the mainstream engines didn't rank prominently.
4. Open promising results and read them; note any `social-profile` links or corroborating name mentions.
5. Pivot: feed discovered profiles/handles into username and social-network tools; treat unique hits as leads to verify on the source page.

## Inputs → Outputs
- **In:** `name` or keyword query
- **Out:** general web results — links to pages mentioning the `name` and any `social-profile`s they reference
- **Empty/negative result looks like:** thin or ad-heavy results with nothing new beyond what Google/Bing already returned — common, since it draws on mainstream indexes. Low added value is the usual outcome.

## Gotchas & OpSec
- **Limited OSINT edge:** it's a general engine with heavy ads, not a specialised people/index tool — expect overlap with Google, occasional differences.
- No advanced OSINT operators beyond standard search syntax; don't expect Google-dork-level control.
- OpSec: passive; queries are logged by the operator — use a clean session.

## Overlaps ("do both")
- Pairs with mainstream and alternative engines (Google, Bing, `[[duckduckgo]]`, Yandex) — run a name across several so ranking differences don't hide a key result; info.com is one more angle, not a replacement.

## Trust & verifiability
`trust: community` — a legitimate, operational search portal, but commercial and ad-driven with no special OSINT features. Verify any finding on the destination page itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | info-com |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
