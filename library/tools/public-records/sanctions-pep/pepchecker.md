---
id: pepchecker
name: PepChecker
description: Use when you have a person's `name` and want to know if they are a politically exposed person or on a sanctions list — returns PEP/sanctions matches and exposure details.
url: https://pepchecker.com
category: public-records
path:
- public-records
- sanctions-pep
bestFor: Fast name screening against PEP and international sanctions lists (OFAC, DFAT and others) across 240+ countries.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: freemium
costNote: 10 free PEP/sanctions searches on signup; beyond that, and for bulk screening, monitoring and API, is paid.
opsec: passive
opsecNote: You query PepChecker's databases, not the subject's own infrastructure, so the person is not notified. The search runs inside your account, so the query is logged to your identity — use an appropriate account for sensitive work.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial compliance vendor aggregating public PEP/sanctions lists; matches are name-based and need manual disambiguation and confirmation against the primary list.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- PepChecker
- pepchecker.com
tags:
- sanctions
- pep
- compliance-screening
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# PepChecker

> A name-screening tool that checks a person against politically-exposed-person and international sanctions lists — a fast "is this person flagged?" check with a free allowance.

## When to use
You have a subject's `name` and want to know whether they appear as a politically exposed person (a senior official, their family, or close associates) or on a sanctions list. Useful when a case touches fraud, corruption, cross-border finance, or vetting an entity a missing person was involved with. It confirms exposure/sanctions status and surfaces the political role or associated organisation behind a match.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create a free account at https://pepchecker.com (grants ~10 free searches).
2. Enter the subject's full `name` (bulk upload is available on paid tiers).
3. Read the report:
   - **PEP match** — the person's political role, jurisdiction, and why they're exposed (self, family, or associate).
   - **Sanctions match** — which list (e.g. OFAC, DFAT) and the listing detail.
   - **Risk indicators** — supporting context; exportable as a PDF.
4. Disambiguate: common names produce look-alike hits — check DOB, country, and role before treating a match as your subject.
5. Pivot: a confirmed role/organisation feeds corporate-registry and news research; treat any positive as a lead to verify on the primary list.

## Inputs → Outputs
- **In:** `name`
- **Out:** PEP/sanctions match, political role, `employer-org` / office, and family/`associate` links
- **Empty/negative result looks like:** "no matches found" — the person isn't on the aggregated PEP/sanctions lists; it is not proof of a clean record generally, only of absence from those lists.

## Gotchas & OpSec
- Human-in-the-loop: an account login is required; the free tier is capped (~10 searches).
- Matches are **name-based** — expect false positives on common names and confirm identity (DOB/country/role) before relying on a hit.
- Always verify a positive against the authoritative source list (e.g. the actual OFAC SDN entry), not just the aggregator's summary.
- OpSec: passive toward the subject, but the query is tied to your account.

## Overlaps ("do both")
- Do both with a direct OFAC/EU/UN sanctions-list search: PepChecker is fast and aggregated, but the official list is authoritative — cross-check every positive there before acting on it.

## Trust & verifiability
`trust: unverified` — a commercial compliance vendor reselling public PEP/sanctions data. Coverage is broad and updated regularly, but confirm any match against the primary regulator's list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pepchecker |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
