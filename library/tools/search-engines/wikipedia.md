---
id: wikipedia
name: Wikipedia
description: Use when you have a `name`, `employer-org`, or place and want a sourced biographical/background reference — returns structured facts, associates, dates, and outbound citations to primary sources.
url: https://en.wikipedia.org
category: search-engines
path:
- search-engines
bestFor: Getting a sourced background sketch and citation trail for a notable person, organization, or place.
selectorsIn:
- name
- employer-org
selectorsOut:
- associate
- employer-org
- dob
status: live
pricing: free
costNote: Free, non-profit, no account needed to read. Article history and cited references are all public.
opsec: passive
opsecNote: Reading is completely passive and unattributed. Note that anything you EDIT is public and tied to your IP or account, so never edit while investigating. Version history is itself an OSINT source — see who added what and when.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Crowdsourced, so individual facts can be wrong or vandalized — but every claim should carry a citation you can follow to a primary source, and edit history is fully transparent.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- en.wikipedia.org
- Wikipedia encyclopedia
tags:
- toddington
- curated-directory
- search-engines
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Wikipedia

> The crowdsourced encyclopedia — most useful in OSINT not for its prose but as a citation index and a transparent edit history pointing to primary sources.

## When to use
You have a `name` of a notable person, an `employer-org`, an institution, or a place and want a fast, sourced background sketch: dates, roles, family/associate links, and — critically — the list of references at the bottom that point to primary documents. For a private individual (typical missing-persons work) there is usually no article, so relevance is low; it earns its keep on public figures, companies, and locations that provide context around a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the `name`/`employer-org` at https://en.wikipedia.org (or the relevant language edition — foreign-language articles often carry local sources the English one lacks).
2. Read the infobox for structured facts (dates, affiliations, `associate` links via family/colleagues) and the body for narrative.
3. Scroll to **References** and **External links** — these citations are the real payload: follow them to primary sources (registries, news, official filings).
4. Open **View history** to see who edited what and when; a suspicious edit, an IP that removed unflattering material, or the timing of changes can itself be a lead.
5. Pivot: cited sources feed the appropriate selector tools; associate names feed people-search.

## Inputs → Outputs
- **In:** `name` or `employer-org` (of a notable subject)
- **Out:** `associate` links, `employer-org` / affiliation facts, `dob`, and a trail of outbound citations
- **Empty/negative result looks like:** no article, or a redirect/disambiguation page — the subject isn't notable enough for coverage. This is the norm for private individuals; do not force a match to a same-named public figure.

## Gotchas & OpSec
- Crowdsourced: any single fact may be outdated, biased, or vandalized. Trust the cited source, not the sentence — an uncited claim is unverified.
- Beware conflating your subject with a same-named notable person; verify identifying details before treating an article as being about your target.
- OpSec: reading is **passive**. Editing is public and attributable — never edit during an investigation.

## Overlaps ("do both")
- Use as a jumping-off point rather than a source of record: its references feed public-records, news-archive, and registry tools that give you primary documentation.

## Trust & verifiability
`trust: trusted` — as an institution Wikipedia is reliable and transparent (full edit history, citation requirements), but individual statements are only as good as their footnote. Always chase the citation to a primary source before relying on a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikipedia |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → associate, employer-org, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
