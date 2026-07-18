---
id: scinapse-io
name: Scinapse.io
description: Use when you have an academic's `name` and want their publications, affiliations and co-authors — returns papers, `employer-org` and `associate` links across ~48,000 journals.
url: https://scinapse.io
category: public-records
path:
- public-records
bestFor: Mapping an academic subject's publications, institution and co-author network.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- document-id
status: live
pricing: freemium
costNote: Free tier (basic paper/author search + collections) available after a free sign-up; paid Basic/Pro/Max plans ($23–$52/mo) add citation analysis and AI review generation.
opsec: passive
opsecNote: Searching for an author does not notify them. You must create an account to search, so use a sock-puppet login and email rather than an attributable identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Run by Pluto Network; aggregates third-party bibliographic metadata (Crossref/PubMed-style sources) rather than being an authoritative registry.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- research-rabbit
aliases:
- Scinapse
- scinapse academic search
tags:
- Science
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Scinapse.io

> Academic search engine over ~48,000 journals — turn a researcher's name into their papers, affiliation and collaborator graph.

## When to use
Your subject is (or claims to be) an academic, scientist or clinician and you have a `name`. Scinapse resolves that name to authored papers, the institutions they published from (`employer-org`), and the co-authors they publish with (`associate`) — useful for confirming a claimed affiliation, dating someone's activity, or expanding a network from a single name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://scinapse.io and sign up / log in with a sock-puppet account (search now requires registration).
2. Search the subject's `name`; switch to the **Authors** facet to disambiguate people with the same name by field and affiliation.
3. Open the matching author page to see their publication list, current/past institutions, and frequent co-authors.
4. Pivot: an affiliation feeds `employer-org` OSINT; a co-author list feeds `associate` mapping; a specific paper's DOI (`document-id`) feeds full-text or citation lookups elsewhere.

## Inputs → Outputs
- **In:** `name`
- **Out:** `document-id` (papers/DOIs), `employer-org` (affiliations), `associate` (co-authors)
- **Empty/negative result looks like:** no author match or only unrelated same-name authors — treat as "not indexed here," not proof the person never published; try a second academic index.

## Gotchas & OpSec
- Human-in-the-loop: registration/login is required before you can search — use a throwaway account.
- Name collisions are common; verify the field and institution before attributing papers to your subject.
- Coverage skews STEM; humanities/regional work may be thin.

## Overlaps ("do both")
- Pairs with `[[research-rabbit]]` — both map an author's works and collaborators, but Research Rabbit's visual citation graph surfaces connections a flat result list misses; cross-check to catch papers one index lacks.

## Trust & verifiability
`trust: community` — Scinapse (Pluto Network) aggregates third-party bibliographic metadata, so it is a convenient index rather than an authoritative source; confirm key facts against the publisher or an official registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scinapse-io |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
