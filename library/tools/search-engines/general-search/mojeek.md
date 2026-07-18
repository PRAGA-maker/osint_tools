---
id: mojeek
name: Mojeek
description: Use when you have a `name`, `username` or keyword and want results from a truly independent, non-Google/Bing crawler — returns web pages, `social-profile` and `domain` hits the mainstream engines rank differently.
url: https://www.mojeek.com/
category: search-engines
path:
- search-engines
- general-search
bestFor: A genuinely independent search index (own crawler, no tracking) for cross-checking Google/Bing on a name/username/keyword sweep.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free to search; a paid API is offered for programmatic use, but manual web searching needs no account.
opsec: passive
opsecNote: Mojeek states it does no IP tracking, no logging and no personalisation, so it leaks little about the investigator and returns an unpersonalised view. Still a third-party server that receives your query text; use a sock puppet/VPN for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Mojeek runs its own independent crawler and index (not a Google/Bing reseller), which is exactly why it's valuable as a second opinion; its index is smaller, so treat blanks as coverage gaps, not proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mojeek-search-engine-united-kingdom
- swisscows
- stract
aliases:
- Mojeek search
- mojeek.com
tags:
- search-engine
- privacy-search
- independent-index
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Mojeek

> A UK-based search engine with its **own** crawler and index — one of the few genuinely independent of Google/Bing, and a no-tracking second opinion for any query.

## When to use
You're sweeping a `name`, `username`, or keyword and want results from an index that isn't derived from Google or Bing. Because Mojeek crawls the web itself and doesn't personalise, it ranks pages differently and can surface a `social-profile` or personal `domain` the mainstream engines bury — while not tying the query to your identity. Best used as a deliberate cross-check alongside Google, Bing and other independents, not as a sole source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.mojeek.com/.
2. Search the selector — quote a `name`, enter a `username`, or combine keywords.
3. Use operators to sharpen: `site:`, `intitle:`, `inurl:`, exact quotes, and `-` to exclude.
4. Check the Images/News tabs too; read results for independent hits (indie blogs, forums, personal sites) the big engines rank low.
5. Pivot: feed discovered handles/domains into specialist tools; run the identical query on Google/Bing/Yandex to compare what each index holds.

## Inputs → Outputs
- **In:** `name`, `username`, or keywords
- **Out:** independent-index web results → `social-profile`, personal `domain`s, page mentions
- **Empty/negative result looks like:** few or no results — expected, since Mojeek's index is smaller than Google's. A blank means "not in Mojeek's crawl," not "not online"; always cross-run mainstream engines.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** with strong privacy posture (no logging/tracking/personalisation), so it's a low-exposure way to search; the Mojeek server still sees the query itself.
- **Smaller index**: its value is *independence and difference*, not exhaustiveness — use it to catch what Google missed, never as your only engine.
- No personalisation means results won't reflect your locale automatically; add location terms yourself when disambiguating.

## Overlaps ("do both")
- Do both with `[[swisscows]]`, `[[stract]]` and mainstream Google/Bing — each independent crawler surfaces pages the others miss, and Mojeek's separate index is one of the few not downstream of Big Tech.

## Trust & verifiability
`trust: trusted` — a legitimate independent search engine with its own index; results are real crawled pages (verify each directly), limited only by index size, not by data provenance.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mojeek |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
