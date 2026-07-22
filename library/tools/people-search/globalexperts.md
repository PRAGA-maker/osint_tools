---
id: globalexperts
name: GlobalExperts
description: Use when you have a `name` of an academic, analyst or commentator and want to confirm they are a listed subject-matter expert and read their affiliation and public contact — returns `employer-org`, `social-profile`.
url: http://www.theglobalexperts.org
category: people-search
path:
- people-search
bestFor: Confirming a named academic/analyst is a vetted public commentator and reading their institutional affiliation.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
status: degraded
pricing: free
costNote: Free directory run by the UN Alliance of Civilizations; no account or payment to browse expert profiles.
opsec: passive
opsecNote: You read a public directory of opinion-leaders — no query reaches the subject. Only your own connection to the UNAOC site is exposed; use a sock-puppet browser if you want to hide research interest.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Directory developed by the UN Alliance of Civilizations for journalists; profiles are self/partner-submitted, so affiliations are strong leads to cross-check, not authoritative identity proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Global Experts
- UNAOC Global Experts
tags:
- expert-search
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# GlobalExperts

> The UN Alliance of Civilizations' directory of vetted commentators — used in OSINT to confirm a named academic/analyst is a real public expert and to read their affiliation.

## When to use
You have a `name` that appears in media as an "expert," "analyst," or "commentator" and you want to check whether they are a registered subject-matter expert and which institution they are tied to. Good for corroborating that a quoted person is who they claim and for pivoting a bare name to an `employer-org` and public contact channel.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.theglobalexperts.org in a clean/sock-puppet browser.
2. Browse or search by expert `name`, topic, or region.
3. Open the matching profile and read: institutional affiliation (`employer-org`), area of expertise, languages, and any listed public/press contact (`social-profile`).
4. Pivot: feed the affiliation into a staff-directory or LinkedIn lookup, and the name into broader people-search to widen the picture.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (affiliation), `social-profile` (listed public/press contact)
- **Empty/negative result looks like:** no profile for the name — this only means the person is not a registered Global Expert, not that they are not a real specialist.

## Gotchas & OpSec
- Automated access returned HTTP 503 at last check; a normal browser session may still load it, hence `status: degraded`. Treat outages as transient and retry, or read a cached copy.
- Profiles are self- or partner-submitted press listings, so affiliations are self-reported — verify before relying on them.
- OpSec: fully passive; nothing you do notifies the subject.

## Overlaps ("do both")
- Pairs with a general people-search plus a LinkedIn/institution staff lookup: this confirms *that* someone is a recognised commentator and their headline affiliation, while those enrich the identity into employment history and network.

## Trust & verifiability
`trust: community` — the platform is UNAOC-run and reputable, but individual entries are submitted press profiles, so the affiliation is a strong lead rather than authoritative identity confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | globalexperts |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
