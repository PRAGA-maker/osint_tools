---
id: sources
name: Sources
description: Use when you have a name or a subject-matter area and want to confirm a person's role, employer, and public contact details as a media spokesperson/expert — returns employer-org, phone, email, social-profile.
url: http://www.sources.com
category: people-search
path:
- people-search
bestFor: Finding and verifying experts, spokespersons and organisational contacts by name or topic.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- phone
- email
- social-profile
status: live
pricing: free
costNote: Free to search the public directory; listing yourself as a source is a paid membership, but querying it is not.
opsec: passive
opsecNote: A public third-party directory — searching it does not touch the target. Entries are self-submitted by experts/organisations for publicity, so treat contact details as officially published rather than private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running Canadian journalists' source directory (Sources.com / Sources Select Resources); listings are self-submitted, so accuracy depends on the member.
missingPersonsRelevance: medium
coverage:
- ca
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Sources.com
- Sources Select Resources
tags:
- expert-search
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Sources

> A journalists' directory of experts and spokespersons — search it to attach a role, organisation and public contact details to a name.

## When to use
You have a `name` (or a subject area / `employer-org`) and want to check whether that person is a publicly listed expert, spokesperson or organisational media contact, and to pull their published contact details. Most valuable when a subject presents as a professional, academic, activist or industry figure who might self-list for press.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.sources.com/.
2. Use the search box for a name, or browse the **Complete Topic Index** / **A–Z Index** to find sources by subject or organisation.
3. Open a matching listing to read the biography, affiliation, and the contact block (phone, email, website, social links).
4. Cross-check the affiliation and contact details against other records; pivot the `email`/`phone`/`social-profile` into further lookups.

## Inputs → Outputs
- **In:** `name` or `employer-org` / topic.
- **Out:** `employer-org` (affiliation), `phone`, `email`, `social-profile`, plus a descriptive bio.
- **Empty/negative result looks like:** no listing returned — the person is simply not a registered source here, which says nothing about whether they exist elsewhere.

## Gotchas & OpSec
- Listings are **self-submitted for publicity**, so coverage skews toward people who *want* press contact; absence is not evidence.
- Details can be stale (an expert who changed jobs may not update) — always corroborate the organisation and contact.
- Canadian-centric but includes international experts; don't assume a miss means "not findable."

## Overlaps ("do both")
- Complements general people-search and professional-directory tools: this one uniquely surfaces *media/press* contact details and topical expertise that generic people finders miss.

## Trust & verifiability
`trust: community` — an established but self-submitted directory; the data is publicly published by the subjects themselves, making it good for confirming a public professional persona but weak as a sole source of fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sources |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → employer-org, phone, email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
