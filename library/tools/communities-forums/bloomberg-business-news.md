---
id: bloomberg-business-news
name: Bloomberg Business News
description: Use when you have a `name`/`employer-org` and want business/financial news coverage — a major outlet; returns articles tying people to companies, deals, and events (metered paywall).
url: https://www.bloomberg.com
category: communities-forums
path:
- communities-forums
bestFor: Finding authoritative business/financial news mentions of a person or company (executives, deals, filings, controversies).
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Some articles are free; most sit behind a metered/subscription paywall. Headlines and snippets are usually visible free.
opsec: passive
opsecNote: Passive — reading news transmits nothing about a subject. To bypass a paywall use archives/cache rather than logging in; a login ties reading to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Bloomberg is a major, professionally edited financial-news organisation; reporting is authoritative and fact-checked (cite the article, verify claims against primary filings).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bloomberg
- bloomberg-com
- bloomberg-public-companies-search
- lei-bloomberg-com
aliases:
- Bloomberg
- Bloomberg.com
tags:
- toddington
- news-journalism
- business
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Bloomberg Business News

> A leading business-news outlet — search it to tie a person to companies, deals, filings, and events with authoritative reporting.

## When to use
Your subject has a business/financial dimension (an executive, investor, company officer, or someone caught up in a corporate story) and you want credible reporting: their role, affiliations, transactions, and any controversy. Bloomberg's coverage often names people alongside companies and dates, corroborating links.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search Bloomberg via its site search or a Google `site:bloomberg.com "<name>"` query.
2. Open matching articles; free snippets/headlines usually show even when the full text is metered.
3. For paywalled pieces, read via a web archive/cache rather than subscribing, when the snippet isn't enough.
4. Read the output: named associations (`name`↔`employer-org`), dates, roles. Pivot: confirm against primary filings (SEC/registries) and feed named companies/people onward.

## Inputs → Outputs
- **In:** a `name` / `employer-org`
- **Out:** news articles linking the person to companies, roles, deals, and events
- **Empty/negative result looks like:** no coverage means the subject isn't business-newsworthy — try general news aggregators and local press.

## Gotchas & OpSec
- **Metered paywall** — most full articles need a subscription; use archives for access rather than logging in.
- News is secondary reporting — verify any hard fact against primary sources (filings).
- Human-in-the-loop: paywall may block full text. OpSec: passive.

## Overlaps ("do both")
- Do both with `[[bloomberg-public-companies-search]]` and a news aggregator — the company search gives structured entity data; this gives the narrative reporting.

## Trust & verifiability
`trust: trusted` — professional edited journalism; authoritative reporting, but cite the specific article and confirm decisive facts against primary filings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bloomberg-business-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
