---
id: expertengine
name: ExpertEngine (Expert by Big Village)
description: Use when you have a subject `name` or a technical discipline and want to confirm whether they are a listed expert witness/consultant — returns names, credentials and employer/affiliation.
url: https://www.expertengine.com
category: people-search
path:
- people-search
bestFor: Checking whether a named person is a registered expert witness/consultant, or finding a credentialed specialist in a given field.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
- social-profile
status: live
pricing: freemium
costNote: The public directory of disciplines and expert bios is browsable for free; engaging or contacting an expert is a paid B2B litigation-support service, so full profile/contact details are gated behind an inquiry.
opsec: passive
opsecNote: Browsing the directory is passive and does not notify the person. Submitting an "engage an expert" inquiry, however, routes your request to Expert by Big Village recruiters and may reach the expert — stop at reading public bios if you only need to confirm existence.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial expert-witness directory (operating since 1984, now Expert by Big Village / Intellex); legitimate but curated as a sales directory, not an authoritative identity source.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Expert by Big Village
- Expert Engine
tags:
- people-search
- expert-witness
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# ExpertEngine (Expert by Big Village)

> A commercial directory of vetted expert witnesses and consultants across 30,000+ disciplines — useful for confirming a subject's professional standing, not for tracing ordinary people.

## When to use
This is a niche corroboration tool, not a general people finder. Reach for it when a subject presents themselves as a credentialed expert (engineering, medicine, forensics, construction, finance) and you want to check whether they appear in a professional expert-witness roster — a signal of a verifiable career and affiliations. Also useful in reverse: you need a named specialist in a technical field to interpret evidence. You have a `name` (or a `discipline`/`employer-org`) and want professional identity confirmation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.expertengine.com.
2. Browse by discipline, or search for the subject's `name` / field of expertise.
3. Read the public expert bios: name, area of expertise, high-level background and affiliations.
4. To go further you must submit an engagement inquiry — this is a paid, human-mediated litigation-support process, so treat it as a hard boundary for passive OSINT.
5. Pivot: a confirmed expert bio gives an `employer-org`/affiliation and specialty to corroborate elsewhere (LinkedIn, court records, professional-body registers).

## Inputs → Outputs
- **In:** `name` or discipline / `employer-org`
- **Out:** `name`, professional discipline, `employer-org`/affiliation, links to a public bio (`social-profile`)
- **Empty/negative result looks like:** no matching expert — which only means the person is not in *this* commercial roster, NOT that they lack the claimed expertise. Absence here is weak evidence.

## Gotchas & OpSec
- Scope trap: despite its "person search" categorisation, this is an expert-witness sales directory — do not treat it as a records database. Its missing-persons value is confirmation/de-confirmation of a professional claim only.
- Contact info and deeper details are paywalled behind a business inquiry; do not submit one just to snoop.
- OpSec: passive while browsing; an engagement inquiry is active outreach.

## Overlaps ("do both")
- Pairs with `[[linkedin]]`-style professional lookups — LinkedIn shows self-reported career, ExpertEngine shows a vetted third-party listing; agreement between them corroborates.
- Pairs with court-records tools when the expert has testified — case dockets confirm the testimony the directory claims.

## Trust & verifiability
`trust: community` — a legitimate, decades-old commercial directory, but curated for lead generation rather than as an authoritative identity register; use its listings as corroboration, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expertengine |
