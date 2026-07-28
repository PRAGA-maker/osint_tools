---
id: extremist-profiles
name: Extremist Profiles
description: Use when you have a `name` and want to check whether they are a profiled extremist — returns `physical-description`, `associate` groups, and ideology background.
url: https://www.splcenter.org/resources/extremist-files/
category: public-records
path:
- public-records
bestFor: Looking up an individual in the SPLC's vetted database of profiled U.S. extremists.
selectorsIn:
- name
selectorsOut:
- physical-description
- associate
- employer-org
status: live
pricing: free
costNote: Free, no login. Maintained by the Southern Poverty Law Center (SPLC), a U.S. non-profit.
opsec: passive
opsecNote: Fully passive — you're reading a public non-profit website; the subject gets no signal. Standard web-request logging by SPLC only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: SPLC is an established civil-rights organisation; profiles are researched and sourced, though the SPLC's inclusion criteria are its own editorial judgment and have drawn criticism — treat as a lead, not legal fact.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- extremist-groups
- hate-map
aliases:
- SPLC Extremist Files
- SPLC individual extremists
tags:
- extremism
- splc
- named-individuals
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Extremist Profiles

> The SPLC's "Extremist Files": searchable, sourced profiles of named U.S. extremists — a way to check whether a person of interest is a documented ideologue and who they run with.

## When to use
You have a `name` (from a case, a social account, a piece of hate content) and want to know whether that person is a profiled extremist: their ideology, affiliated `associate` groups, notable statements, and often a photo/`physical-description`. Useful for threat-context and network mapping. For a missing-person case it's a niche check — relevant when a subject or associate is tied to extremist movements, which can bear on risk assessment and known associates.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.splcenter.org/resources/extremist-files/ (the individuals list is under Extremist Files → Individuals).
2. Use the keyword search or browse the alphabetical/ideology-filtered list for your `name`.
3. Open the profile: it gives a photo, background, ideology, affiliated groups, and sourced quotes/history.
4. Read the "In their own words" and affiliation sections for pivot leads.
5. Pivot: named `associate` groups feed `[[extremist-groups]]` and `[[hate-map]]`; a photo feeds face/reverse-image search.

## Inputs → Outputs
- **In:** `name`
- **Out:** `physical-description` (profile photo), `associate` (affiliated groups/people), `employer-org` (organisations they founded/led), ideology and history
- **Empty/negative result looks like:** no matching profile — the database is a curated set of ~150 individuals, so most names won't appear; absence is not evidence of anything.

## Gotchas & OpSec
- Passive and safe — reading a public site.
- Coverage is narrow (a few hundred profiled individuals/groups, U.S.-focused) and reflects SPLC's editorial criteria, which are contested; corroborate before relying on the label.
- Profiles are periodically updated or removed; note the "last updated" date on the page.

## Overlaps ("do both")
- Pairs with `[[extremist-groups]]` (organisation-level profiles) and `[[hate-map]]` (geographic distribution) — individual → group → location.

## Trust & verifiability
`trust: trusted` — SPLC is a long-established organisation and profiles are sourced, but inclusion is an editorial judgment that has been criticised; use it as a well-documented lead, not as an adjudicated fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | extremist-profiles |
| category | public-records |
| selectorsIn → selectorsOut | name → physical-description, associate, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
