---
id: the-economist-world-news-united-kingdom
name: The Economist
description: Use when you have a `name` or `employer-org` of some public prominence and want serious international coverage or analysis — returns `employer-org`, `associate` and event context from published articles.
url: https://www.economist.com
category: communities-forums
path:
- communities-forums
bestFor: Finding in-depth international news and analysis mentioning a notable person, company, or event.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: A hard metered paywall — a few free articles, then subscription required. Search results, headlines and standfirsts are free; full text usually is not.
opsec: passive
opsecNote: Searching and reading a public news site leaks nothing about your subject. The paywall sets cookies and may prompt sign-up; use a private window and decline. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A leading UK-based international newsweekly with rigorous editorial standards; a reliable secondary source, subject to its known analytical/house-view framing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- The Economist
- economist.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# The Economist

> A leading international newsweekly — searchable for serious coverage and analysis of notable people, companies, governments, and global events.

## When to use
Your subject has some public prominence — a business leader, official, academic, or a person tied to a company or event of international note — and you want authoritative context: what a reputable outlet reported about them, their organisation, or the situation they are connected to. Best for people/entities that reach international significance; ordinary private individuals will not appear.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.economist.com and use the site search, or run a scoped query: `site:economist.com "Full Name"` / `"Company"`.
2. Read headlines and standfirsts (free) to see whether and how the subject is covered and in what timeframe.
3. When the metered paywall blocks the article, read the archived copy (`web.archive.org`) or find the same event summarised elsewhere.
4. Note the subject's role/title, the organisation, dates, and any other named people.
5. Pivot: a confirmed role/employer feeds LinkedIn/registry lookups; a named associate feeds people-search; the article date bounds a timeline.

## Inputs → Outputs
- **In:** `name` / `employer-org` (of some prominence)
- **Out:** `employer-org`, `associate` (co-named figures), event/date and analytical context
- **Empty/negative result looks like:** no article matches — expected for most private individuals; treat absence as "not internationally notable here," not as evidence of anything. Try broader news search.

## Gotchas & OpSec
- Hard metered paywall — plan to use archive.org or headline/standfirst level for most articles.
- Coverage skews to internationally significant subjects; low hit rate for ordinary people.
- Analytical/house-view outlet: separate its interpretation from the underlying facts. Fully passive.

## Overlaps ("do both")
- Pairs with general news aggregators (Google News) and financial press — those give breadth and primary reporting, while The Economist adds vetted analysis and context on notable subjects.

## Trust & verifiability
`trust: trusted` — a rigorously edited international outlet; reliable as secondary sourcing, with the usual step of confirming specific facts (titles, dates) against a primary record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-economist-world-news-united-kingdom |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
