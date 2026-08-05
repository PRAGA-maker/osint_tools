---
id: gerdoo-iran
name: Gerdoo (Iran)
description: Use when you have a `name`/`username` or Persian keyword and want Iran-focused web results — returns a Persian-language meta-search over major providers.
url: http://gerdoo.me
category: search-engines
path:
- search-engines
bestFor: Persian-language and Iran-focused web search via a meta-search engine that refines results from major providers.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free public search; no account required.
opsec: active
opsecNote: Queries are sent to Iranian-operated search infrastructure, which may log and be subject to state surveillance/filtering. Do not query from an attributable connection — use a VPN and a sock-puppet browser session, and assume searches are observed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-recommended active Iranian meta-search engine (cited in OSINT lists as a working replacement for the defunct Parsijoo, alongside Zarebin); it aggregates/refines third-party results rather than running its own index.
missingPersonsRelevance: low
coverage:
- ir
auth: none
api: false
localInstall: false
registration: false
aliases:
- gerdoo.me
tags:
- main-national-search-engines
- persian-search
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Gerdoo (Iran)

> A Persian-language meta-search engine — useful for surfacing Iran-focused and Farsi-language results that global engines localize away.

## When to use
Your subject is Iranian or Persian-speaking, or your leads point to Iranian sites/content, and Google/Bing under-surface local material. Gerdoo refines results from major providers with a Persian-language focus, so it can pull Farsi content, Iranian domains, and regionally-relevant pages that a default global search buries. Use it as a complementary engine, not a sole source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://gerdoo.me behind a VPN in a sock-puppet browser session (see OpSec below).
2. Enter the `name`, `username`, phone, or Persian keyword — try both Latin and Farsi-script spellings.
3. Read the aggregated results; open Iranian domains and profiles that global engines missed.
4. Cross-check anything important against another engine — meta-search relies on upstream providers and can rank differently.
5. Pivot: an Iranian `domain` → infrastructure/WHOIS tools; a `social-profile` → cross-platform enumeration; Farsi name variants → repeat searches with transliterations.

## Inputs → Outputs
- **In:** `name` / `username` / Persian keyword
- **Out:** Persian-focused web results → `social-profile` links and Iranian `domain`s
- **Empty/negative result looks like:** thin or irrelevant results — try Farsi-script spelling, a second Iranian engine (Zarebin), or a global engine with `site:.ir`; a miss here is not conclusive.

## Gotchas & OpSec
- OpSec: **active** in effect — you are sending queries to Iranian-operated infrastructure that may log and is subject to state monitoring/filtering; always use a VPN and never query from an attributable connection.
- Transliteration: Persian names have many Latin spellings — search variants, and prefer Farsi script when you have it.
- Meta-search caveat: results depend on upstream providers and can shift or degrade without notice.

## Overlaps ("do both")
- Pairs with other Iranian engines (Zarebin) and `site:.ir` queries on global engines — each surfaces different slices of Persian-language content; run several and merge.

## Trust & verifiability
`trust: community` — an active engine recommended in OSINT resource lists but operated within Iran's information environment; treat results as leads, corroborate elsewhere, and weigh the OpSec exposure of querying it at all.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gerdoo-iran |
