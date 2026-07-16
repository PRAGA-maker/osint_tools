---
id: genealogy-bank
name: GenealogyBank
description: Use when you have a US `name` and want historical newspapers and obituaries — returns obituaries, articles, and SSDI records yielding `dob`/death dates and relatives (`associate`).
url: http://www.genealogybank.com
category: people-search
path:
- people-search
bestFor: Deep US historical newspaper archive plus obituaries and the Social Security Death Index for genealogy and death research.
selectorsIn:
- name
selectorsOut:
- dob
- associate
- name
status: live
pricing: freemium
costNote: Subscription service (monthly/annual) with a free trial; searching often shows hits/snippets free, but full articles/obituaries require a paid membership.
opsec: passive
opsecNote: Searching historical archives is passive and does not notify anyone. A trial/subscription requires your details — register with a sock-puppet identity; subjects are typically historical/deceased.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A large, reputable commercial newspaper/obituary archive (NewsBank); source documents are authentic, though OCR/indexing errors occur and full access is paywalled.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- legacy-com
- obituaries-from-newspapers-north-america
- family-search
- genealogybank-ssdi
aliases:
- Genealogy Bank
- genealogybank.com
tags:
- people-investigations
- newspapers
- obituaries
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# GenealogyBank

> A large US historical-newspaper and obituary archive (plus the Social Security Death Index) — mine decades of print for a subject's obituary, life events, and named relatives.

## When to use
You have a US `name` and want the depth that only historical newspapers provide: an obituary (naming relatives, hometown, dates → `associate`, `dob`/death), news mentions, marriage/birth announcements, and SSDI death records. It's especially strong for older or deceased subjects, filling gaps that modern people-search sites and even other genealogy databases miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.genealogybank.com and search the `name` (add date range/place to narrow).
2. Scan the hit list — obituaries, articles, and SSDI matches often show a free snippet/citation.
3. Open full items with a subscription (or the free trial) to read the obituary/article in full.
4. Extract named relatives, dates, and places from the text.
5. Pivot: relatives feed people-search; death dates cross-check `[[legacy-com]]` and `[[obituaries-from-newspapers-north-america]]`; anchor the family tree in `[[family-search]]`.

## Inputs → Outputs
- **In:** `name` (+ date range/place)
- **Out:** obituaries/articles yielding `dob`/death dates, relatives (`associate`), confirmed `name`
- **Empty/negative result looks like:** no hits or only paywalled snippets — the person may not appear in the digitised papers, or OCR missed the name (try variants); absence isn't proof.

## Gotchas & OpSec
- Human-in-the-loop: full articles are **paywalled** (subscription/trial); snippets/citations are the free layer.
- OCR and indexing miss names — search variants and nearby dates before concluding absence.
- US-focused; coverage varies by region and era of digitised papers.
- OpSec: passive; register a trial with a sock puppet.

## Overlaps ("do both")
- Overlaps with `[[legacy-com]]` and `[[obituaries-from-newspapers-north-america]]` (obituaries) and complements `[[family-search]]` (vital records) — cross-check death/relatives across all.

## Trust & verifiability
`trust: community` — a reputable commercial archive of authentic source documents; the caveats are OCR/index errors and the paywall, not authenticity. Confirm names/dates against the imaged original.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | genealogy-bank |
| category | people-search |
| selectorsIn → selectorsOut | name → dob, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
