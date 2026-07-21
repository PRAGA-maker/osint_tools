---
id: terrorism-reports
name: Country Reports on Terrorism (US State Dept)
description: Use when you have a `name` or `employer-org` and want to check it against the US State Department's congressionally-mandated annual terrorism assessments — returns designations, associate/network context and country findings.
url: https://www.state.gov/country-reports-on-terrorism
category: search-engines
path:
- search-engines
bestFor: Authoritative background on foreign terrorist organizations, state sponsors and country-level terrorism findings when vetting a name, group or region.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free US government publication; no account needed. Full reports posted as web pages / PDFs each year.
opsec: passive
opsecNote: You are reading published government reports on state.gov; no query about your target is transmitted. Fully passive. If you want to keep even the state.gov visit off your own IP, read via a VPN or the Internet Archive mirror.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US Department of State publication, mandated by 22 U.S.C. 2656f and delivered to Congress annually. Authoritative but reflects US-government framing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- narcotics-control-reports
- voter-registration-data
aliases:
- Country Reports on Terrorism
- State Department terrorism reports
- Patterns of Global Terrorism
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Country Reports on Terrorism (US State Dept)

> The US State Department's annual, congressionally-mandated survey of terrorism worldwide — the authoritative reference for who is a designated Foreign Terrorist Organization, which states sponsor terror, and what happened by country and year.

## When to use
You have a `name`, an `employer-org`, or a region and need to check it against an authoritative record: is a group a designated Foreign Terrorist Organization (FTO)? Is a country a state sponsor? What terrorist activity is documented in the place your subject travelled to or is associated with? Useful for due-diligence on organisations, for understanding the security context of a disappearance abroad, and for corroborating claims about a group's status.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.state.gov/country-reports-on-terrorism and pick the year (reports run from ~2004 to the latest, e.g. 2024).
2. Each annual report is organised by chapter: country-by-country narratives, the FTO list, state-sponsors-of-terrorism chapter, and terrorist-safe-havens.
3. Use your browser's in-page find (Ctrl-F) within a report, or a site search `site:state.gov country reports on terrorism <name>`, to locate a specific group, country, or event.
4. Cross-check the current FTO/state-sponsor designations against the report year, since designations change over time.
5. Pivot: a confirmed group name feeds sanctions/entity searches; a country finding contextualises travel or last-known-location intelligence.

## Inputs → Outputs
- **In:** `name` / `employer-org` (a group or organisation) or a country/region
- **Out:** `employer-org` (designation status), `associate` (affiliated/umbrella groups), country-level findings
- **Empty/negative result looks like:** the name does not appear in any annual report — meaning it is not a US-designated or reported entity, NOT proof the group does not exist.

## Gotchas & OpSec
- Reflects US-government framing and designations; other governments' lists (EU, UN) may differ — corroborate against those where it matters.
- Older reports live at archived state.gov subdomains (e.g. `2009-2017.state.gov`, `2017-2021.state.gov`); the main portal links them.
- Fully passive: reading a published PDF leaks nothing about your subject.

## Overlaps ("do both")
- Pairs with `[[narcotics-control-reports]]` — the sibling INCSR series covers drug-trafficking country findings, complementing the terrorism angle for the same regions.

## Trust & verifiability
`trust: trusted` — a first-party US State Department publication mandated by statute and submitted to Congress; authoritative for US designations, though inherently one government's perspective.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | terrorism-reports |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
