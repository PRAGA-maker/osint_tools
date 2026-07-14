---
id: alm-experts-united-states
name: ALM Experts (United States)
description: Use when you have a `name` or a specialty and want to identify or verify an expert witness / litigation consultant — a searchable directory returning the expert's firm, location and area of expertise.
url: https://www.law.com/expert-witness/
category: people-search
path:
- people-search
bestFor: Finding or vetting expert witnesses and litigation consultants by name or subject-matter, and pulling their firm/location/expertise.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: Free to search the directory. Now hosted under Law.com's Expert Witness Search (ALM's legal-media platform); listings are self-submitted professional profiles.
opsec: passive
opsecNote: Passive — you browse a public professional directory; nothing is submitted about the subject and no alert is generated. Ordinary browser hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by ALM (a major legal-media publisher) — a legitimate directory, but listings are self-submitted marketing profiles, so verify credentials independently.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ALM Experts
- almexperts.com
- Law.com Expert Witness Search
tags:
- toddington
- curated-directory
- people-search
- expert-witness
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# ALM Experts (United States)

> A searchable directory of expert witnesses and litigation consultants (formerly almexperts.com, now Law.com's Expert Witness Search) — for identifying or vetting a professional by name or specialty.

## When to use
A niche people-search: your subject is (or claims to be) an expert witness, consultant, or litigation-support professional, and you have a `name` or a specialty/subject-matter. This directory lets you confirm the person exists as a listed expert, find their firm, location and stated expertise, and cross-check credentials — useful for verifying professional claims or building context on someone tied to litigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.law.com/expert-witness/ (almexperts.com redirects here).
2. Search by expert `name`, or browse/search by category, subject-matter, and keywords to find experts in a field.
3. Open a matching profile.
4. Read the output: the expert's `name`, firm/`employer-org`, location (`address`), contact (`phone`), and detailed areas of expertise / representative cases.
5. Pivot: the firm and location feed corporate and geographic OSINT; the stated expertise/CV corroborates or contradicts claims; the name feeds broader people-search.

## Inputs → Outputs
- **In:** `name` (or specialty/keyword)
- **Out:** `employer-org` (firm), `address` (location), `phone`, plus expertise/CV detail
- **Empty/negative result looks like:** no matching expert — meaning the person isn't listed here (many experts aren't), not proof they lack the claimed expertise. Try other expert-directory and licensing sources.

## Gotchas & OpSec
- Listings are self-submitted marketing profiles — treat stated credentials as claims to verify, not vetted facts.
- US-focused legal-expert niche; irrelevant for most general subjects.
- OpSec: fully passive; public directory.

## Overlaps ("do both")
- Pairs with professional-licensing and court-record tools — this gives the expert's self-described profile; licensing boards and cause lists corroborate whether the credentials and case involvement are real.

## Trust & verifiability
`trust: community` — a legitimate directory from a major legal publisher (ALM/Law.com), but the profiles are self-submitted. Independently verify credentials before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | alm-experts-united-states |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, address, phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
