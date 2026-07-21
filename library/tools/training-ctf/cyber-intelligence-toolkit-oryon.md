---
id: cyber-intelligence-toolkit-oryon
name: Cyber Intelligence Toolkit (oryon)
description: Use when you need investigation methodology rather than a lookup — a curated GitHub library of OSINT/OPSEC manuals, playbooks, and checklists to structure and document a case.
url: https://github.com/oryon-osint/cyber-intelligence-toolkit
category: training-ctf
path:
- training-ctf
bestFor: Methodology, playbooks, and investigator checklists for running and documenting OSINT investigations rigorously.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, publicly readable GitHub repository; clone or browse online, no account.
opsec: passive
opsecNote: Reading reference material is fully passive and reveals nothing about a case. Its OPSEC value is instructional — it teaches you how not to leak while investigating.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated methodology collection (~130 stars) maintained by oryon with OSINT360; reference material, so judge each guide on its merits.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- oryon cyber-intelligence-toolkit
tags:
- playbooks
- methodology
- opsec
- checklists
source: gh-topic-osint-framework
lastVerified: '2026-07-21'
enrichment: full
relatedTools:
- oryon-querytool
---

# Cyber Intelligence Toolkit (oryon)

> A reference library, not a data source: curated manuals, playbooks, and checklists for running an OSINT/OPSEC investigation methodically and documenting it defensibly.

## When to use
Reach for this **between** lookups, when you need process rather than data: structuring an investigation, choosing a verification method, avoiding OPSEC leaks, detecting AI-generated/altered media, or producing a checklist-driven, court-defensible workflow. Especially useful for a missing-persons case where consistency and documentation matter as much as the individual findings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/oryon-osint/cyber-intelligence-toolkit and read the README's index.
2. Navigate the four sections: **manuals** (in-depth guides), **playbooks** (step-by-step workflows), **checklists** (verification steps), and **appendices** (tools/references).
3. Pick the playbook/checklist matching your task (e.g. media verification, source vetting, OPSEC setup) and follow it against your live case.
4. Clone the repo to keep an offline copy and adapt the checklists into your own case template.
5. Pivot: the toolkit's tool/reference appendix points you to concrete lookup tools; use it as a map, then execute in those tools.

## Inputs → Outputs
- **In:** an investigator's need for methodology (no target selector)
- **Out:** structured guidance — manuals, workflows, checklists — to run and document the investigation
- **Empty/negative result looks like:** the topic you need isn't covered — it's a curated set, not exhaustive; supplement with other methodology sources.

## Gotchas & OpSec
- **Not a tool that finds people** — it produces no intelligence about a subject; its relevance is purely to the *quality* of your process.
- Community-maintained: verify any specific legal/forensic claim against an authoritative source before relying on it in a report.
- Guidance ages; check the repo's last update and cross-check fast-moving areas (platform-specific techniques, AI-detection).

## Overlaps ("do both")
- Pairs with the companion `[[oryon-querytool]]` and with hands-on OSINT frameworks — this gives the *how*, those give the *where*.

## Trust & verifiability
`trust: community` — a respected but community-curated collection; treat it as expert guidance to apply with judgement, not as authority to cite.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyber-intelligence-toolkit-oryon |
| category | training-ctf |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
