---
id: yamli-arabic
name: Yamli (Arabic)
description: Use when you have a name a subject spells in Latin letters and want its Arabic-script results — returns social-profile and domain leads by transliterating a romanized name into Arabic and searching both.
url: https://www.yamli.com/
category: search-engines
path:
- search-engines
bestFor: Bridging a romanized Arabic name to its Arabic-script spellings and searching the Arabic web for it.
selectorsIn:
- name
selectorsOut:
- social-profile
- domain
- name
status: live
pricing: free
costNote: Free web tool and keyboard; no account. Browser extensions available for Chrome and Firefox.
opsec: passive
opsecNote: A search/transliteration service — your query passes through Yamli's servers, but nothing is sent to your subject. Use a clean/sock-puppet browser session as with any third-party search box.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Yamli is a long-established, reputable Arabic transliteration and search service; the transliteration is a smart-guess aid, so verify that the Arabic spelling it produces matches the intended name.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- yamii
aliases:
- yamli.com
- Yamli
tags:
- toddington
- curated-directory
- search-engines
- arabic
- transliteration
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Yamli (Arabic)

> Smart Arabic transliteration keyboard and search front-end — type an Arabic name in Latin letters ("Feiruz") and it generates the Arabic-script spellings (فيروز) and searches for them, closing the gap when you can't type or don't know the exact Arabic spelling.

## When to use
Your subject has an Arabic name that you only have romanized (from a passport, a Latin-script profile, or a source's phonetic rendering), and you need Arabic-language results — Arabic social profiles, news, and sites that a Latin-only query misses. Arabic names have many valid transliterations; Yamli maps the romanized `name` to plausible Arabic spellings and searches them, so you catch Arabic-web mentions you would otherwise never surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.yamli.com/.
2. Type the `name` phonetically in Latin letters; Yamli offers Arabic-script candidates as you type — pick the spelling(s) that match your subject.
3. Run the search across web/images/videos/news/Wikipedia; note the Arabic spelling it settled on for reuse in other engines.
4. Take the confirmed Arabic spelling into mainstream search, social platforms, and regional people-search — Yamli's job is to hand you the right Arabic string, then you search everywhere with it.
5. Pivot: Arabic-script `name`, plus any `social-profile`/`domain` hits, feed further OSINT in Arabic-language sources.

## Inputs → Outputs
- **In:** `name` (romanized Arabic).
- **Out:** Arabic-script `name` spelling(s), plus `social-profile`/`domain` results from the Arabic web.
- **Empty/negative result looks like:** transliteration candidates that don't match your subject, or thin results — the guessed spelling may be wrong; try alternate candidates or a known-correct Arabic spelling manually.

## Gotchas & OpSec
- Human-in-the-loop: none, though you must choose the correct Arabic spelling from the suggestions.
- OpSec: **passive** — an ordinary search query; the subject is not notified. Query strings pass through Yamli; keep sensitive identifiers minimal.
- Transliteration is probabilistic: one romanization maps to several Arabic spellings and vice-versa — try multiple candidates before concluding a name has no footprint.

## Overlaps ("do both")
- Pairs with mainstream and regional search engines — Yamli produces the correct Arabic string; feed that string into other engines and social platforms for full coverage.

## Trust & verifiability
`trust: community` — an established, reputable transliteration/search tool. Its transliteration is an aid, not an authority; confirm the Arabic spelling corresponds to your actual subject before relying on results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yamli-arabic |
| category | search-engines |
| selectorsIn → selectorsOut | name → social-profile, domain, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
