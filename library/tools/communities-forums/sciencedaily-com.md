---
id: sciencedaily-com
name: Sciencedaily.com
description: Use when you have a researcher `name` or `employer-org` and want their reported studies for background — returns science/health research news summaries linking to journals and institutions.
url: http://www.sciencedaily.com
category: communities-forums
path:
- communities-forums
bestFor: Background on a researcher or institution via summarized science/health research news.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to read and search; funded by ads. RSS and email newsletters available; no account needed.
opsec: passive
opsecNote: Reading a public science-news aggregator is passive; no subject is contacted. Standard clean-browser hygiene suffices — nothing here reveals anything about a target you look up.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running aggregator of press releases from universities/journals; summaries are reliable pointers, but each is a press release — follow the linked primary source for facts.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ScienceDaily
- sciencedaily.com
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-19'
enrichment: full
---

# Sciencedaily.com

> An aggregator of science/health research news drawn from university and journal press releases — a quick way to surface a researcher's or institution's reported work.

## When to use
You're building background on someone in academia/research, or on a research institution (`employer-org`), and want a fast index of their reported studies. ScienceDaily summarizes press releases across 500+ topics and links each to the originating university/journal, so a `name` search can reveal affiliations, co-authors (`associate`), and the subject's field of work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.sciencedaily.com and use its search, or Google-dork `site:sciencedaily.com "<researcher name>"`.
2. Open matching articles: each summarizes a study and names the researchers, their institution, and the source journal.
3. Note affiliations and named collaborators — these map `employer-org` and `associate` links.
4. Click through to the original university release / journal citation for the authoritative detail.
5. Pivot: a confirmed institution feeds a staff-directory / ORCID search; co-authors feed further `name` lookups.

## Inputs → Outputs
- **In:** researcher `name` or `employer-org`
- **Out:** research-news summaries with affiliations, collaborators (`employer-org`, `associate`), and journal links
- **Empty/negative result looks like:** no articles match — the person's work wasn't picked up as a press release here; try a scholarly index (Google Scholar, ORCID) instead of assuming they don't publish.

## Gotchas & OpSec
- Each item is a *press release* summary, inherently promotional — verify claims against the linked primary paper.
- Coverage is selective (only releases that get submitted/picked up), so absence is not evidence.
- OpSec: fully passive; nothing reaches the subject.

## Overlaps ("do both")
- Pairs with scholarly tools (Google Scholar, ORCID, PubMed) — ScienceDaily surfaces the *newsworthy* work and plain-language context, while scholarly indexes give the complete, authoritative publication record. Use ScienceDaily to spot, scholarly indexes to confirm.

## Trust & verifiability
`trust: trusted` — an established aggregator with links to primary sources; reliable as a pointer, but treat each summary as a press release and confirm facts in the cited journal/institution source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sciencedaily-com |
| category | communities-forums |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
