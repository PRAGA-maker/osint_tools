---
id: open-hub
name: Open Hub
description: Use when you have a developer `username`/`name` or an open-source project and want their contribution history — returns linked `social-profile`s, projects, languages and commit activity.
url: https://www.openhub.net/
category: search-engines
path:
- search-engines
bestFor: Profiling a developer's open-source footprint — projects contributed to, languages, commit timeline, and linked accounts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to search and view profiles/projects; a free account is only needed to edit/claim listings.
opsec: passive
opsecNote: Open Hub reads from public repository metadata it has already indexed, so browsing a developer or project page doesn't touch the target. It's a directory of public FOSS activity; nothing you view alerts the person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established open-source directory (formerly Ohloh, run by Black Duck); data is aggregated from public repositories and can be stale or incompletely linked, since much depends on volunteer-maintained project entries.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Ohloh
- openhub.net
- Black Duck Open Hub
tags:
- toddington
- curated-directory
- specialty-search
- open-source
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Open Hub

> A directory of open-source software and the people who build it (formerly Ohloh) — turn a developer handle or project into a contribution history and a set of linked accounts.

## When to use
Your subject is a software developer, or you're investigating an open-source project. Open Hub aggregates public repository data into **contributor profiles** (projects they've committed to, languages used, a commit-activity timeline, and the accounts/emails they've linked) and **project pages** (contributor lists, codebase stats, licences). Use it to build a picture of a coder's interests and collaborators, to find other projects/handles tied to a known contributor, or to enumerate who works on a given project.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.openhub.net/.
2. Search a developer `username`/`name`, or a project name.
3. On a **developer profile**, read: projects contributed to, languages, commit timeline, and any **linked accounts** (other handles, sometimes an employer or homepage).
4. On a **project page**, read the contributor list to enumerate people, then click through to each contributor's profile.
5. Pivot: linked handles feed cross-platform username searches; contributed projects lead to repo hosts (GitHub/GitLab) where richer identity data lives.

## Inputs → Outputs
- **In:** developer `username`/`name`, or project name
- **Out:** `social-profile`(s) and linked accounts, projects/languages, commit history, and sometimes `employer-org`/homepage
- **Empty/negative result looks like:** no profile/project — the developer isn't indexed (Open Hub relies on projects being registered, so newer or GitHub-only work is often absent), or the handle differs. Go directly to GitHub/GitLab as the primary source.

## Gotchas & OpSec
- Human-in-the-loop: none for viewing.
- OpSec: **passive** — a read of an aggregated public directory; nobody is notified.
- Coverage skews to **older/registered** FOSS projects; much modern activity lives only on GitHub and never reaches Open Hub, so absence here means little. Use it as a supplement to GitHub/GitLab searches.
- Data can be stale and account-linking is incomplete (it depends on volunteer curation) — verify identity links at the source repository.

## Overlaps ("do both")
- Do both with GitHub/GitLab profile and code search and with `[[searchcode]]` — Open Hub gives an aggregated cross-project history and linked accounts, while the repo hosts give current, authoritative activity.

## Trust & verifiability
`trust: community` — a legitimate aggregator of public repository data; treat its links and stats as leads to confirm against the underlying repositories, since entries can be dated or partially linked.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | open-hub |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
