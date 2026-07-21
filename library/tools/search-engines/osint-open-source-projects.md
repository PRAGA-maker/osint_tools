---
id: osint-open-source-projects
name: OSINT Open Source Projects (Awesome Open Source)
description: Use when you want to discover open-source OSINT tools/repos by topic — a browsable directory of GitHub projects tagged "osint" — returns pointers to tooling, not subject data.
url: https://awesomeopensource.com/projects/osint
category: search-engines
path:
- search-engines
bestFor: Finding and comparing open-source OSINT projects/repositories by popularity within the "osint" topic.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free to browse; no account required.
opsec: passive
opsecNote: Tooling discovery only — no target is queried. Reading the directory reveals nothing about your investigation. OpSec considerations belong to whatever tool you go on to install and run.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator that ranks GitHub projects by stars/topic; useful for discovery, but inclusion is automated and implies no vetting of any listed tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- awesome-open-source
aliases:
- Awesome Open Source OSINT
- awesomeopensource.com osint
tags:
- tool-directory
- open-source
- discovery
source: osint4all
lastVerified: '2026-07-21'
enrichment: full
---

# OSINT Open Source Projects (Awesome Open Source)

> A topic page on Awesome Open Source that ranks GitHub repositories tagged "osint" by popularity — a discovery shelf for finding open-source investigative tooling.

## When to use
You are not researching a person here — you are looking for a *tool*. Use this when you want to discover, compare, or find alternatives to open-source OSINT software (scrapers, username enumerators, recon frameworks, geolocation utilities) ranked by GitHub stars within the "osint" topic. It is a meta-resource that feeds your toolkit, not your case file.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://awesomeopensource.com/projects/osint. It lists GitHub projects tagged with the "osint" topic, sorted by popularity.
2. Scan project names, star counts, and one-line descriptions to shortlist candidates for the capability you need.
3. Click through to the GitHub repo to check the README, last-commit date, license, and open issues before trusting or installing anything.
4. Pivot: install the chosen tool and run it against your actual selectors; return here to find alternatives when a tool is stale or unmaintained.

## Inputs → Outputs
- **In:** none (a topic/keyword browse, not a subject lookup)
- **Out:** none structured — a ranked list of GitHub repositories to evaluate
- **Empty/negative result looks like:** thin or dated listings; because ranking is by stars and the crawl is automated, popular-but-abandoned repos can rank above better-maintained newer ones. Always check the repo's recent activity.

## Gotchas & OpSec
- Inclusion is automated (topic + stars); it is not a vetted list. Verify each project on GitHub before use — check maintenance, license, and whether it still works against today's target sites.
- Star count reflects popularity, not current reliability. Many highly-starred OSINT scrapers break as target platforms change.
- OpSec: passive; discovery only.

## Overlaps ("do both")
- Pairs with `[[awesome-open-source]]` and hand-curated OSINT awesome-lists on GitHub — those are human-vetted and often better-annotated, while this ranks purely by popularity. Cross-check both when hunting for a tool.

## Trust & verifiability
`trust: community` — a third-party aggregator surfacing real GitHub repos. The listing is genuine but unvetted; trust flows to the individual repositories, which you must evaluate yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-open-source-projects |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
