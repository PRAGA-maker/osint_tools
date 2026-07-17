---
id: seart-github-search
name: SEART Github Search
description: Use when you want to find GitHub repositories by metadata (language, stars, commits, contributors, activity dates) rather than by name — returns a filtered list of repos and their attributes.
url: https://seart-ghs.si.usi.ch/
category: social-networks
path:
- social-networks
bestFor: Filtering GitHub repositories by rich metadata criteria that GitHub's own search exposes poorly.
selectorsIn:
- employer-org
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free public web app run by an academic research group (USI Lugano); open-source. No account needed.
opsec: passive
opsecNote: You query SEART's pre-crawled database, not GitHub or any target, so nothing is contacted directly. Fully passive; only SEART sees your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by the SoftwarE Analytics Research Team at USI (Università della Svizzera italiana) for empirical software-engineering studies; open-source and academically documented.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- map-of-github
aliases:
- SEART GHS
- GitHub Search Engine
- seart-ghs
tags:
- Social Media
- Github
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# SEART Github Search

> An academic GitHub search engine that filters a pre-crawled database of 700k+ repositories by metadata — stars, commits, contributors, language, dates — instead of by keyword.

## When to use
You want to enumerate GitHub repositories matching structural criteria rather than a name: repos in a given language above a star threshold, with a certain contributor count, created or updated in a date window. In an investigation this is a niche org/technical-footprint tool — useful for mapping a group's or company's (`employer-org`) open-source presence or narrowing a candidate set of projects — but it is not a person- or username-lookup, so direct missing-persons relevance is low.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://seart-ghs.si.usi.ch/.
2. Set filters: language, minimum/maximum stars, forks, commits, contributors, issues, and created/last-committed date ranges (all optional).
3. Run the search; browse the resulting repository table.
4. Click through to a repo on github.com to inspect owners, contributors, and linked accounts.
5. Pivot: repo owners/contributors → GitHub profile inspection and username tools; linked sites → domain tools.

## Inputs → Outputs
- **In:** repository metadata filters (language, stars, activity), optionally tied to an `employer-org`'s known projects
- **Out:** a filtered list of GitHub repositories (`social-profile` owners, project `domain`s) with their metadata
- **Empty/negative result looks like:** no rows — filters too strict, or the target repo is below the 10-star indexing threshold / in an unindexed language. Loosen filters or use GitHub's native search for small/new repos.

## Gotchas & OpSec
- **Indexing limits:** only repos with ≥10 stars in ~10 supported languages are indexed, so personal/toy projects and niche-language repos are absent by design.
- It is a research sampling tool, not a live mirror — data is periodically crawled and may lag GitHub by some interval.
- OpSec: **passive** — queries hit SEART's database, not GitHub or any target.

## Overlaps ("do both")
- Pairs with [[map-of-github]] — SEART filters by hard metadata; map-of-github explores by thematic similarity. Different angles on the same ecosystem.

## Trust & verifiability
`trust: trusted` — maintained by an academic software-engineering research group, open-source and peer-documented; the data is a faithful (if periodically refreshed) crawl of public GitHub metadata.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seart-github-search |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org → social-profile, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
