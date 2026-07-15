---
id: behindthenames
name: Behind the Name
description: Use when you have a `name` and want its variants, diminutives, foreign-language forms and etymology to widen a search — returns alternate `name` spellings/nicknames to feed other tools.
url: https://www.behindthename.com
category: people-search
path:
- people-search
bestFor: Expanding a person's name into nicknames, diminutives, and cross-language variants before searching.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: freemium
costNote: Free to browse names, meanings, related forms and popularity. Optional free registration; no payment needed for the name data an investigator uses.
opsec: passive
opsecNote: Fully passive — you are looking up a name in a reference dictionary, not touching the subject or any of their accounts. Nothing is disclosed to anyone. No sock-puppet needed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running, well-regarded onomastics reference (given names + a companion surnames site). Authoritative for name etymology/variants; it holds no personal data about individuals.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- behindthename.com
- Behind the Surname
tags:
- name-variants
- Universal Contact Search and Leaks Search
- onomastics
source: cyb-detective
lastVerified: '2026-07-15'
enrichment: full
---

# Behind the Name

> An etymology dictionary of given names (with a companion surnames site) — used in OSINT to expand a subject's name into every nickname, diminutive and foreign-language variant worth searching.

## When to use
You have a `name` and your searches are coming up thin because you're only trying the one spelling. Behind the Name gives you the formal↔diminutive links (William ↔ Bill/Will/Liam), cross-language equivalents (Ivan ↔ John ↔ Juan ↔ Jean), and historical/regional variants. Each alternate is a new query to run against people-search, social, and public-records tools. Note: this is a name-reference database — it does NOT return addresses, emails, or phone numbers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.behindthename.com and search the subject's given name (use the surnames companion site for family names).
2. Read the "Related Names" / "Diminutives" / "Other Languages" sections to collect variants and nicknames.
3. Note gendered and regional forms that a subject might actually use day-to-day (e.g. a legal "Margaret" going by "Peggy").
4. Take each variant back to your real lookup tools (people-search, social, voter/records) and re-run.
5. Pivot: a nickname that hits on social media confirms which form the subject uses publicly.

## Inputs → Outputs
- **In:** `name` (given name or surname)
- **Out:** alternate `name` forms — diminutives, nicknames, cross-language equivalents, historical variants
- **Empty/negative result looks like:** a rare/invented name may not be in the database, or returns only etymology with no variants — that just means fewer alternate spellings to try, not a dead end.

## Gotchas & OpSec
- It is a reference, not a person-finder — do not expect it to identify or locate anyone.
- Variants are possibilities, not facts about your subject; only some will be forms they actually use. Confirm each downstream.
- A programmatic API exists for bulk variant lookups if you're scripting a name-expansion step.

## Overlaps ("do both")
- Feeds every people-search and social tool — generate variants here first, then fan them out. Especially valuable before username-enumeration and voter/records searches where exact spelling matters.

## Trust & verifiability
`trust: trusted` — an established, well-sourced onomastics reference; the etymology/variant data is reliable, and because it contains no personal data there's no data-quality risk about individuals.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | behindthenames |
| category | people-search |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
