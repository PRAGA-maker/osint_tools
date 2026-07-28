---
id: wordstat-yandex-ru
name: Wordstat.yandex.ru
description: Use when you have a `name`/keyword/brand and want its Yandex search demand — returns query volumes, related terms, and regional interest across Russian-speaking regions.
url: https://wordstat.yandex.ru/
category: search-engines
path:
- search-engines
bestFor: Gauging how often and where a term/name is searched on Yandex (Russia/CIS keyword intelligence).
selectorsIn:
- name
selectorsOut:
- geolocation
status: live
pricing: free
costNote: Free, but requires a Yandex account login to view results.
opsec: passive
opsecNote: Passive keyword research — you query Yandex's own tool, not any subject. A Yandex login is required, so use a puppet Yandex account; assume queries are logged under Russian jurisdiction. The person you research is never contacted.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Yandex keyword-planning tool; the search-volume figures are Yandex's own and authoritative for the Yandex ecosystem.
missingPersonsRelevance: low
coverage:
- ru
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- rasp-yandex-ru-map-trains
- yandex-people-search
aliases:
- Yandex Wordstat
- wordstat
tags:
- Keywords, trends, news analytics
- yandex
- russia
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Wordstat.yandex.ru

> Yandex's keyword-demand tool — how many times a term (a name, brand, handle) is searched on Yandex, broken down by related queries and region.

## When to use
You are researching something with a Russian/CIS footprint and want to gauge public search interest — is a `name`, alias, brand, or event being searched, how much, and *where*. Wordstat also surfaces the co-occurring queries people run alongside your term, which can reveal associated names, products, or spellings to pivot on.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in at https://wordstat.yandex.ru/ with a (puppet) Yandex account.
2. Enter the term/`name`/keyword.
3. Read the two columns: queries containing your term (with monthly volumes) and "what people also searched" (related terms).
4. Switch to the **regional** ("По регионам") view to see which oblasts/cities drive the interest — a rough `geolocation` signal.
5. Pivot: related queries feed new search terms and transliteration variants; regional skew hints at where a subject/topic is based.

## Inputs → Outputs
- **In:** `name` / keyword / brand term
- **Out:** Yandex search volumes, related queries, regional interest breakdown (`geolocation` signal)
- **Empty/negative result looks like:** near-zero volume and no related queries — the term isn't searched on Yandex (common for obscure individuals), not proof of non-existence.

## Gotchas & OpSec
- Requires a Yandex login — use a sock-puppet account, and be aware of Russian jurisdiction/logging.
- It measures *search demand*, not people — a high-volume name tells you interest exists, not who the person is.
- Volumes are Yandex-only; meaningless for Western-search-dominated topics.
- Cyrillic/transliteration matters — test multiple spellings of a name.

## Overlaps ("do both")
- Pairs with [[yandex-people-search]] — Wordstat tells you whether/where a term is searched, while Yandex people-search tries to resolve the term to actual profiles.

## Trust & verifiability
`trust: trusted` — first-party Yandex data, authoritative for the Yandex ecosystem; just remember it reflects search behaviour, not verified facts about a person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wordstat-yandex-ru |
| category | search-engines |
| selectorsIn → selectorsOut | name → geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
