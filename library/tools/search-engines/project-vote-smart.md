---
id: project-vote-smart
name: Vote Smart
description: Use when you have a `name` of a U.S. elected official or candidate and want their public political record — returns biography, voting record, issue positions, interest-group ratings, and campaign/contact details.
url: http://votesmart.org/
category: search-engines
path:
- search-engines
bestFor: Comprehensive nonpartisan profiles of U.S. elected officials and candidates — bios, votes, positions, ratings.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- employer-org
- associate
status: live
pricing: free
costNote: Free nonpartisan nonprofit resource; no account required to search profiles.
opsec: passive
opsecNote: You browse published political records about public figures; nothing reaches the subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the nonpartisan Vote Smart nonprofit since 1992; data is compiled from official voting records, candidate self-reports (Political Courage Test), and public interest-group ratings — authoritative for public officials.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Project Vote Smart
- votesmart.org
tags:
- politics
- public-records
- elected-officials
source: awesome-osint
lastVerified: '2026-07-19'
enrichment: full
---

# Vote Smart

> A nonpartisan encyclopedia of U.S. elected officials and candidates — biographies, full voting records, stated issue positions, interest-group ratings, and campaign/contact details. The reference source when your subject holds or seeks public office.

## When to use
You have a `name` that is (or was) a U.S. elected official, appointee, or candidate at federal or state level and want their public political record: career biography, how they voted, positions on issues, ratings by advocacy groups, and official/campaign contact info. Useful for profiling a public figure connected to your investigation, establishing their affiliations and background, or corroborating a claimed political role.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://votesmart.org/.
2. Search the official/candidate by `name` and open their profile.
3. Browse the tabs: **Bio** (career, education, family/associations where public), **Votes** (legislative record), **Positions** (Political Courage Test), **Ratings** (interest-group scores), and contact/campaign info.
4. Note the sourcing on each section — votes are from official records; positions may be candidate self-reported.
5. Pivot: named affiliations, employers, and prior roles (`associate`/`employer-org`) feed people-search, campaign-finance (FEC/OpenSecrets), and news-archive lookups.

## Inputs → Outputs
- **In:** `name` (official/candidate) or `employer-org` (office/body)
- **Out:** `document-id` (bio, voting record, ratings), `employer-org` (offices held), and `associate` links (affiliations)
- **Empty/negative result looks like:** no profile — the person may not be a covered U.S. official/candidate, or a name variant differs; absence here just means they're not in the political-figures scope.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: fully **passive** — public records about public figures.
- Scope: U.S. elected officials and candidates only; not a general people-search. Position data can be candidate self-reported (Political Courage Test) — distinguish self-reported stances from the objective voting record.

## Overlaps ("do both")
- Pairs with FEC/OpenSecrets (campaign finance), Ballotpedia, and congressional records — Vote Smart gives the bio/votes/positions overview; those add money trails, election detail, and primary legislative documents for a fuller profile of a public official.

## Trust & verifiability
`trust: trusted` — a long-established nonpartisan nonprofit; voting records and ratings trace to official and public sources you can re-check, with the noted caveat that self-reported positions are the candidate's own statements.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | project-vote-smart |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → document-id, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
