---
id: security-first-umbrella
name: Security First - Umbrella
description: Use when you need a free, offline digital- and physical-security guide (checklists and how-tos) to plan investigator OpSec before or during fieldwork — returns operational-security guidance.
url: https://secfirst.org/umbrella/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A free open-source mobile/desktop app of practical digital and physical security guidance and checklists for activists, journalists, and investigators.
selectorsIn: []
selectorsOut: []
status: degraded
pricing: free
costNote: Free and open source (Security First). Distributed via Google Play, F-Droid, and GitHub; the project website was intermittently unreachable at last check, but the app itself remains available through app stores/GitHub.
opsec: passive
opsecNote: This is an OpSec reference for YOUR own tradecraft, not a lookup that touches a target. It works offline once installed, so reading it leaks nothing. Use it to plan sock-puppet hygiene, secure comms, and physical safety before an operation — it improves your OpSec rather than consuming any.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: mobile-app
trust: community
trustNote: Reputable open-source project by Security First, built with input from security trainers; guidance is well-regarded, though verify it against current best practice since threat landscapes evolve.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Umbrella
- Umbrella app
- Security First Umbrella
tags:
- opsec
- digital-security
- fieldwork
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Security First - Umbrella

> A free, open-source pocket security handbook — practical, checklist-driven guidance on digital and physical safety for anyone doing risky field or online work, usable entirely offline.

## When to use
You're about to run an investigation (especially anything sensitive or in-person) and want to get your own operational security right: how to set up sock-puppet identities safely, use secure messaging and browsing, protect devices, handle surveillance and physical risk, and respond if things go wrong. Umbrella packages this as searchable lessons and checklists you can follow step by step. It's a tradecraft reference for the investigator, not a data source about a subject.

## How to use it (`bestInteractionPattern`: mobile-app)
1. Install Umbrella from Google Play, F-Droid, or build from the GitHub source (works offline after install).
2. Browse the topic tree — digital security (secure comms, passwords, anonymity), physical security, and incident response.
3. Follow the relevant checklist before your task (e.g. "set up a research identity", "safe travel").
4. Use its risk-assessment prompts to plan for your specific threat model.
5. Apply it to your workflow: harden your research browser/identity per its guidance before touching any active tool in this library.

## Inputs → Outputs
- **In:** none — it's reference material you consult
- **Out:** actionable security checklists and guidance for your own OpSec
- **Empty/negative result looks like:** not applicable — it's a guide, not a query tool; if a topic isn't covered, supplement with current security-training resources.

## Gotchas & OpSec
- It advises on OpSec rather than performing lookups — no target interaction, fully offline.
- Security guidance ages — cross-check specific tool recommendations against current best practice.
- The main website was intermittently down at last check; get the app from F-Droid/Play/GitHub instead.

## Overlaps ("do both")
- Complements the tradecraft guidance implicit across this library's OpSec notes and dedicated privacy tools — Umbrella is the structured, checklist-based reference to operationalize good hygiene.

## Trust & verifiability
`trust: community` — well-regarded open-source security project; sound guidance, but verify tool-specific advice against current recommendations since the app may not be actively updated.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | security-first-umbrella |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | mobile-app |
| opsec | passive |
| human-in-loop | no |
