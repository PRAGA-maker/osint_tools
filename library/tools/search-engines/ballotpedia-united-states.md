---
id: ballotpedia-united-states
name: Ballotpedia
description: Use when you have a `name` of a US politician, candidate, or public official and want their verified biography, offices held, and campaign/employment history — returns bio, employer-org, and associates.
url: https://ballotpedia.org
category: search-engines
path:
- search-engines
bestFor: Confirming a US elected official's or candidate's identity, career timeline, and public affiliations from a neutral encyclopedia.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- physical-description
status: live
pricing: free
costNote: Free to read; a paid "Ballotpedia Pro" tier adds bulk/analytics features but all article content is free.
opsec: passive
opsecNote: Reading public encyclopedia pages leaks nothing to the subject; no login needed. Safe to browse directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Nonpartisan digital encyclopedia of US politics run by the Lucy Burns Institute; professionally edited and sourced, not open crowd-editing like Wikipedia.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Ballotpedia
- ballotpedia.org
tags:
- toddington
- curated-directory
- specialty-search
- political-figures
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Ballotpedia

> The nonpartisan encyclopedia of American politics: verified profiles of officials, candidates, and offices from the federal level down to school boards.

## When to use
Your subject is (or ran to be) a US elected official, candidate, judge, or notable government appointee, and you have their `name`. Ballotpedia gives a sourced biography — offices held and sought, election dates and results, prior careers, and organizational affiliations — that helps confirm you have the right person and builds a timeline of where they were and who they worked with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://ballotpedia.org and search the subject's `name` in the site search box.
2. Open the matching profile; disambiguate using state, office, and party if several people share the name.
3. Read the biography: education, career/`employer-org` history, offices held, campaign history, and any endorsements or affiliated organizations.
4. Follow the article's cited sources (official filings, news) to primary documents.
5. Pivot: an `employer-org` or campaign committee feeds business/finance records; named `associate`s (running mates, appointees) feed further people-search.

## Inputs → Outputs
- **In:** `name` (of a US political / public figure)
- **Out:** biography, `employer-org` and career history, offices held, `associate`s (colleagues, endorsers), sometimes a `physical-description`/photo
- **Empty/negative result looks like:** no article, or only a stub election-results row — Ballotpedia covers people connected to US elections and government, so an absent subject is likely simply not a covered political figure, not proof of anything.

## Gotchas & OpSec
- Coverage is US-only and politics-focused; a private individual with no electoral/government role won't be here.
- Content is a secondary source — verify key facts against the primary filings it cites before relying on them.
- OpSec: fully passive; browse without an account.

## Overlaps ("do both")
- Pairs with FEC/campaign-finance and Wikipedia lookups — Ballotpedia's editorial sourcing and down-ballot coverage (local races, school boards) often exceeds Wikipedia's for minor officials.

## Trust & verifiability
`trust: trusted` — a professionally staffed, nonpartisan encyclopedia with editorial review, so more reliable than open-wiki sources, though still a secondary source to be corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ballotpedia-united-states |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, associate, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
