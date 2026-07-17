---
id: academictree
name: AcademicTree
description: Use when you have an academic's `name` and want their mentors, students and collaborators — returns `associate` links, `employer-org` affiliations and a scholarly network.
url: https://academictree.org/
category: public-records
path:
- public-records
bestFor: Mapping the mentor/student/collaborator network of a researcher or academic across 70+ disciplines.
selectorsIn:
- name
selectorsOut:
- associate
- employer-org
- name
status: live
pricing: free
costNote: Free, community-built database; no account needed to browse or search. Editing/adding nodes is also free.
opsec: passive
opsecNote: Read-only searching is passive and anonymous. If you create or edit a node you leave a public edit trail tied to whatever account you use — browse only unless you deliberately want to contribute.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced academic genealogy (originally Neurotree). Connections are user-submitted, so a well-cited node is reliable but sparse/unverified nodes may contain errors.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-scholar
- orcid
aliases:
- Academic Family Tree
- Neurotree
- academictree.org
tags:
- science
- academia
- genealogy
- network-analysis
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# AcademicTree

> Crowd-sourced "family tree" of academia (870k+ people): enter a researcher's name and see who mentored them, whom they trained, and who they collaborate with.

## When to use
Your subject is (or was) an academic/researcher and you want to enrich a `name` into their professional network — doctoral advisor, postdoc supervisors, graduate students, and collaborators. Those mentor/student edges are `associate` leads that rarely surface anywhere else, and the tree usually pins each person to the institutions (`employer-org`) where the relationship happened. Useful for locating people through their academic circle or corroborating an institutional affiliation and era.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://academictree.org/ (or the discipline-specific subsite, e.g. neurotree.org, that the person belongs to).
2. Search the subject's `name`. If the tree spans multiple disciplines you may need to pick the right field.
3. Open their node: it shows a graphical tree of "parents" (mentors) above and "children" (trainees) below, plus listed collaborators.
4. Read the affiliations attached to each relationship — these tie the person to specific labs/institutions and time periods.
5. Pivot: each connected person is a new `name`/`associate` to run through people-search; institutional affiliations feed `[[google-scholar]]` / `[[orcid]]` for publications and current contact points.

## Inputs → Outputs
- **In:** `name` (a researcher/academic)
- **Out:** `associate` (mentors, students, collaborators), `employer-org` (institutions), additional `name`s in the network
- **Empty/negative result looks like:** no node, or a bare node with no connections — common for non-academics or early-career researchers who nobody has entered. Absence is not evidence they aren't an academic.

## Gotchas & OpSec
- Coverage is deep in neuroscience/biology (its origins) and thinner in newer or non-STEM fields.
- Data is user-submitted: an unsourced connection is a lead, not a fact. Prefer nodes with citations or multiple contributors.
- OpSec: passive to browse. Do not edit nodes during an investigation — edits are public and attributable.

## Overlaps ("do both")
- Pairs with `[[google-scholar]]` and `[[orcid]]` — AcademicTree gives you the human relationship graph (who trained whom), while Scholar/ORCID give the publication record and current affiliation to confirm and update it.

## Trust & verifiability
`trust: community` — a volunteer-maintained academic genealogy project (formerly Neurotree, now the Academic Family Tree). Structure and well-cited nodes are trustworthy; treat sparse, single-editor connections as unverified until corroborated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | academictree |
| category | public-records |
| selectorsIn → selectorsOut | name → associate, employer-org, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
