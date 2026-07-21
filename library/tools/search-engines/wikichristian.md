---
id: wikichristian
name: WikiChristian
description: Use when you have a `name` of a religious figure, denomination, or Christian topic and want a community encyclopedia entry — returns background and associate/affiliation leads.
url: http://www.wikichristian.org
category: search-engines
path:
- search-engines
bestFor: Background on Christian topics, denominations, and figures from a crowd-sourced faith encyclopedia.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free community wiki; no account needed to read.
opsec: passive
opsecNote: Reading a public wiki is passive and anonymous; nothing reaches any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An open, crowd-edited faith wiki with a small contributor base; content is doctrinal and community-written, not authoritative biography.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WikiChristian
- wikichristian.org
tags:
- toddington
- curated-directory
- specialty-search
- religion
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# WikiChristian

> A small crowd-sourced encyclopedia of Christian faith, theology, and figures — a niche background source when a case has a religious dimension.

## When to use
A niche, low-priority reference. When a subject is a religious figure (clergy, denominational leader, ministry founder) or a case turns on a Christian organization, movement, or term, WikiChristian may hold a background entry — a person's affiliations, the structure of a denomination, or the meaning of a group's terminology. Coverage is doctrinal and uneven, so use it for orientation, not confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.wikichristian.org and search the `name`, denomination, or term.
2. Read the article for affiliations, organizational context, and related figures.
3. Follow internal links to connected people/`associate`s and `employer-org` ministries.
4. Treat everything as a lead — check the entry's claims against denominational records or mainstream sources.
5. Pivot: an organization or affiliated figure feeds nonprofit/registry and people-search.

## Inputs → Outputs
- **In:** a `name` (religious figure), denomination, or Christian topic
- **Out:** background text, `employer-org` (ministry/denomination) and `associate` leads
- **Empty/negative result looks like:** no article or a bare stub — the wiki is small, so most people/topics simply aren't covered; absence is not meaningful.

## Gotchas & OpSec
- Small, openly editable wiki: accuracy varies and articles can be doctrinally slanted — corroborate.
- Strongest for topics/terms, weakest for living individuals.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with Wikipedia and denominational directories — those are broader and better-sourced; WikiChristian occasionally covers a niche ministry or term they miss.

## Trust & verifiability
`trust: unverified` — a small crowd-edited faith wiki; useful for orientation only, with claims to be confirmed against authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikichristian |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
