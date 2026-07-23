---
id: zarebin-iran
name: Zarebin (Iran)
description: Use when you have a `name`/`username` or Persian-language query and want Iran-focused results — returns Persian web, news, and media content a Western engine misses.
url: https://zarebin.ir
category: search-engines
path:
- search-engines
bestFor: Searching Persian-language and Iran-hosted content that Google indexes poorly, especially during Iranian internet restrictions.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free public search engine; no account required to search.
opsec: active
opsecNote: Zarebin is an Iranian state-aligned engine operating inside Iran's National Information Network — assume queries are logged and monitored by the operator. Never search from an identity or connection tied to you or the subject; use a sanitized sock-puppet browser and appropriate network hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: State-affiliated Iranian search engine; useful for reach into Persian content but the operator curates/filters results, so treat rankings and omissions as potentially manipulated.
missingPersonsRelevance: low
coverage:
- ir
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Zarebin
- زره‌بین
- Iranian search engine
tags:
- national-search-engine
- persian
- iran
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Zarebin (Iran)

> Iran's domestic search engine ("the magnifying glass") — a way into Persian-language and Iran-hosted content that global engines index thinly, with the caveat that it's a state-aligned platform.

## When to use
You're researching a subject, organisation, or event connected to Iran and need Persian-language coverage — local news, forums, shopping, and media — that Google/Bing surface poorly, or that only remains reachable during an Iranian internet shutdown when Zarebin keeps working inside the National Information Network. Reach for it as a *complementary* Persian-language index, not a primary or neutral source. Missing-persons relevance is low/indirect (locating Persian mentions of a person).

## How to use it (`bestInteractionPattern`: web-manual)
1. From a sanitized/sock-puppet browser (see OpSec), open https://zarebin.ir.
2. Enter your query — a `name`, `username`, phone, place, or event. Prefer the Persian/Farsi spelling for best recall; transliterate names where possible.
3. Browse the web, news, and media verticals; Zarebin also bundles music/movie/shopping search that can surface a subject's local footprint.
4. Pivot: promising results feed translation, a `social-profile` lead, or a `domain` to investigate further with neutral tools.

## Inputs → Outputs
- **In:** `name`, `username`, or a Persian keyword query
- **Out:** Persian-language web pages, news, and media links (can surface `social-profile`s and `domain`s)
- **Empty/negative result looks like:** few or heavily-curated results — may reflect genuine absence OR state filtering; a blank on a sensitive query is not proof the content doesn't exist.

## Gotchas & OpSec
- **Filtering bias:** as a state-aligned engine, results can be censored or promoted; corroborate anything important with an independent index.
- Persian script matters — searching only the Latin transliteration will miss most content.
- OpSec: treat every query as **monitored**. Do not use a real or subject-linked identity/IP; use a clean browser profile and suitable network routing. This is an active exposure to a hostile-logging operator.

## Overlaps ("do both")
- Pair with global engines and other regional Iranian engines (e.g. Yooz/Gerdoo) — cross-run the same query, because each index and its censorship gaps differ, and the union catches what any one omits.

## Trust & verifiability
`trust: community` — genuinely useful for Persian reach, but the operator curates results and logs queries; use it to *find* leads, then verify them on neutral, independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zarebin-iran |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
