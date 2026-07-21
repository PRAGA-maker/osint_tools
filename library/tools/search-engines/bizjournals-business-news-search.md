---
id: bizjournals-business-news-search
name: Bizjournals (American City Business Journals)
description: Use when you have a `name` or `employer-org` in US local business and want metro-level coverage — returns `employer-org`, `associate` and career/company context from articles.
url: https://www.bizjournals.com
category: search-engines
path:
- search-engines
bestFor: US metro-level business news — executives, local companies, deals, promotions, and awards across 40+ American cities.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: freemium
costNote: Headlines, search, and article previews are free; full articles metered behind a subscription. Many people-relevant details appear in the free preview.
opsec: passive
opsecNote: Searching and reading a public news network transmits nothing about your subject. Fully passive; a private window avoids personalisation cookies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: American City Business Journals — an established US local-business news network across 40+ metros. Reliable secondary source with the usual journalistic caveats.
missingPersonsRelevance: low
coverage:
- us
aliases:
- Bizjournals
- American City Business Journals
- bizjournals.com
tags:
- toddington
- curated-directory
- specialty-search
- business
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Bizjournals (American City Business Journals)

> The largest US network of metro business journals — the place to find local coverage of executives, mid-market companies, deals, and "People on the Move" that national outlets skip.

## When to use
Your subject is a US business person below national-celebrity level — a local executive, entrepreneur, professional, or board member. Bizjournals' city-by-city journals carry exactly the granular items that identify and place people: promotions, new hires, "People on the Move" columns, "40 Under 40" lists, funding/deal announcements, and local company profiles. Excellent for confirming an `employer-org`, a role/title, a city, and professional `associate`s.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bizjournals.com and use site search, or run: `site:bizjournals.com "Full Name"` / `"Company"`.
2. Note which metro journal covers the item (Atlanta, Dallas, Boston, etc.) — this itself locates the subject.
3. Read the free headline/preview for title, company, and city; "People on the Move" and award lists are especially name-rich.
4. Where the full article is metered, read the archived copy (`web.archive.org`) or the free preview, which often contains the key facts.
5. Pivot: confirmed employer/title feeds LinkedIn and state business-registry lookups; the covering metro narrows location; named colleagues feed people-search.

## Inputs → Outputs
- **In:** `name` / `employer-org` (US local business)
- **Out:** `employer-org`, role/title, covering metro (location signal), `associate` (colleagues)
- **Empty/negative result looks like:** no article matches — the person may be outside the business world or below coverage threshold; try LinkedIn, state registries, and local general news.

## Gotchas & OpSec
- Metered paywall on full articles — the free preview and archive.org usually recover the key facts.
- US metro business focus; non-US or non-business subjects won't appear.
- Fully passive — searching leaks nothing.

## Overlaps ("do both")
- Pairs with LinkedIn and state business registries — Bizjournals supplies the local news signal (promotion, city, deal), those confirm the current role and the company's official record.

## Trust & verifiability
`trust: trusted` — an established business-news network; reliable secondary sourcing, with specifics (titles, dates, deal terms) worth confirming against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bizjournals-business-news-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
