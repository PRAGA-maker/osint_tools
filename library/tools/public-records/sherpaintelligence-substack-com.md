---
id: sherpaintelligence-substack-com
name: sherpaintelligence.substack.com
description: Use when you need a methodology for investigating an organisation (charity/company) tied to a subject — returns a walkthrough of registries and records that yield `employer-org`, `address`, and `associate` links.
url: https://sherpaintelligence.substack.com/p/osint-basecamp-investigating-charities
category: public-records
path:
- public-records
bestFor: Learning how to investigate a charity/organisation and the people behind it via public registries.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free Substack article (Sherpa Intelligence "OSINT Basecamp" series); some posts in the publication may be subscriber-only.
opsec: passive
opsecNote: Reading the guide and querying public registries is passive — subjects and organisations are not notified. Work from a clean browser regardless.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Sherpa Intelligence is a practitioner-run OSINT training publication; sound methodology, but verify that named registries/links are current for your jurisdiction.
missingPersonsRelevance: high
coverage:
- uk
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Sherpa Intelligence OSINT Basecamp
- investigating charities OSINT
tags:
- companysites
- Company Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# sherpaintelligence.substack.com

> A "OSINT Basecamp" methodology article on investigating charities and the organisations behind a subject — how to pull trustees, filings, addresses, and connected people out of public registries.

## When to use
This is a **methodology reference, not a lookup**. When a subject is tied to a charity, company, or nonprofit — as a trustee, director, employer, or donor — investigating the *organisation* often unlocks the person: registries publish officers, registered addresses, and connected entities. This walkthrough shows which registries to hit (Charity Commission, Companies House and equivalents) and how to chase the people-links, so a name/`employer-org` becomes a network.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://sherpaintelligence.substack.com/p/osint-basecamp-investigating-charities for the registry workflow.
2. Take your subject's charity/company (`employer-org`) and pull its record: trustees/directors, registered `address`, filing history, linked organisations.
3. Chase the people — cross-reference officers/associates against other registries and people-search.
4. Pivot: registered addresses and co-officers (`associate`) become new leads for locating or corroborating the subject.

## Inputs → Outputs
- **In:** `name` and/or `employer-org` (charity/company)
- **Out:** techniques → officers/trustees (`associate`), registered `address`, and linked `employer-org`s
- **Empty/negative result looks like:** N/A — it's a guide; the failure mode is stopping at the org record without pivoting to its people.

## Gotchas & OpSec
- UK-leaning examples (Charity Commission/Companies House), but the *method* generalises — swap in your jurisdiction's registry.
- Registry URLs and search interfaces change; confirm the current portal before relying on a linked step.
- OpSec: **passive** — public-registry queries don't notify anyone.

## Overlaps ("do both")
- Pairs with company/charity registry tools and people-search — this teaches the org→people pivot; those execute each lookup.

## Trust & verifiability
`trust: community` — a credible practitioner publication; the methodology is solid, but verify named registries and links are current for your target's jurisdiction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sherpaintelligence-substack-com |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
