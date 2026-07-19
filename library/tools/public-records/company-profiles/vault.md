---
id: vault
name: Vault
description: Use when you have an `employer-org` and want company culture, rankings and employee-sentiment context — returns company profiles, industry rankings and internship/employer info (deep salary data is paid).
url: https://vault.com/
category: public-records
path:
- public-records
- company-profiles
bestFor: Company-culture, rankings and employer research to contextualize a subject's workplace.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Free sign-up gives company profiles, rankings and career content; "Vault Gold" is a paid tier for deeper salary/insider data.
opsec: passive
opsecNote: Reading company profiles is passive and involves no individual subject. Creating a free account ties activity to an email — use a research address. Nothing here reaches or reveals a person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Established careers/employer-research brand; profiles and rankings are editorial + crowd-sourced sentiment, so treat as context, not authoritative fact about any individual.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- vault.com
- Vault Gold
tags:
- company-profiles
- employer-research
- public-records
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Vault

> An employer-research site — company profiles, industry rankings, and employee-sentiment context to flesh out the `employer-org` side of a subject's profile.

## When to use
You know where a subject works or worked (`employer-org`) and want context on that organization: what it does, how it ranks in its industry, its culture and internship pipeline, and general employee sentiment. Useful for validating a claimed employer, understanding a workplace's structure, or generating leads (roles, programs) — it's background on the *company*, not records on the person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://vault.com/ and search the company name (`employer-org`).
2. Read the company profile: overview, industry ranking, culture notes, internship/entry programs, and sentiment summaries.
3. Note structural details (divisions, locations, program names) that can guide further searches for the subject's role.
4. Deeper salary/insider data sits behind "Vault Gold" (paid) — the free tier covers profiles and rankings.
5. Pivot: a confirmed employer + division feeds staff-directory/LinkedIn-style searches and email-pattern guessing.

## Inputs → Outputs
- **In:** `employer-org` (company name)
- **Out:** company profile, ranking, culture/sentiment context (organizational `employer-org` detail)
- **Empty/negative result looks like:** no profile for the company — Vault skews to larger/notable employers and certain sectors (e.g. law, finance, consulting); small/local employers won't appear.

## Gotchas & OpSec
- Coverage skews to prominent employers and specific industries; niche/small firms are often absent.
- Sentiment and rankings are editorial/crowd-sourced — treat as impressionistic context, not fact about the subject.
- Salary/insider depth is paywalled (Vault Gold); stay in the free tier for OSINT context.
- OpSec: passive; only a free-account email is exposed if you register.

## Overlaps ("do both")
- Pairs with Glassdoor-style review sites and official corporate registries — Vault adds culture/ranking framing, review sites add employee reports, and registries give the authoritative legal/officer facts. Use together to build the employer picture.

## Trust & verifiability
`trust: community` — a reputable employer-research brand, but its content is editorial and crowd-sourced; corroborate any load-bearing fact via primary corporate sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vault |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
