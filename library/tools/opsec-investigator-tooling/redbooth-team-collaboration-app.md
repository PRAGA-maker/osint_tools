---
id: redbooth-team-collaboration-app
name: Redbooth Team Collaboration App
description: Use when an investigation team needs a shared workspace to track case tasks, evidence, and communication — an operational collaboration tool, not a lookup source (no subject selectors in or out).
url: http://redbooth.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Coordinating a multi-person investigation — task assignment, deadlines, file sharing, and threaded discussion in one shared workspace.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free plan supports a small team (historically ~2 users / limited projects) with no credit card; larger teams, more projects, and reporting need paid Pro/Business tiers.
opsec: passive
opsecNote: This holds your team's case data, not the subject's — so the risk is inward. Anything you upload lives on Redbooth's cloud servers; keep sensitive PII and evidence out of it unless your org's data policy permits, and lock down membership so no outsider joins the workspace.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial SaaS collaboration product; dependable as a team tool but it is a third-party host for whatever case material you put in it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Redbooth
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- case-management
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Redbooth Team Collaboration App

> A project-management workspace repurposed as case-coordination tooling — task boards, deadlines, files, and chat for a team working an investigation together.

## When to use
Not for finding anything about a subject — Redbooth surfaces no selectors. Reach for it when **more than one investigator** is working a case and you need a shared operational picture: who is chasing which lead, what evidence has been collected, what's due, and a threaded record of decisions. It's the "how we run the case" layer, not the "what we found" layer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign up at https://redbooth.com (free tier, no card) and create a **private workspace** for the case.
2. Invite only vetted team members; confirm the workspace is not publicly discoverable and enforce strong auth.
3. Create task lists per workstream (e.g. "social accounts", "financial", "physical locations"), assign owners and due dates, and attach working files.
4. Use board / list / timeline views to see progress; keep discussion in task comments so the reasoning trail stays with the artifact.
5. Export or migrate findings into your system of record — treat Redbooth as coordination, not as the permanent evidence store.

## Inputs → Outputs
- **In:** none (operational tooling — you put your *own* team's data in)
- **Out:** none as subject selectors — produces a coordinated task/evidence workspace
- **Empty/negative result looks like:** N/A; this is infrastructure, not a query.

## Gotchas & OpSec
- **Inward-facing risk:** the sensitive data here is your investigation's, hosted on a third-party cloud. Apply your org's data-handling policy; keep raw PII/evidence out unless explicitly allowed.
- Requires an account and login (human-in-the-loop) — provision it under a work identity, not a personal one.
- Free-tier limits are tight; validate current caps before committing a large team.
- Off-boarding matters: remove departed members promptly so old collaborators can't retain case access.

## Overlaps ("do both")
- Interchangeable with any team task tracker (Trello/Asana/Notion) your organization already trusts — pick the one that matches your data-handling rules rather than running several.

## Trust & verifiability
`trust: community` — a mature commercial SaaS that reliably does what it claims; the caveat is custody, not capability — you are entrusting case material to an external host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redbooth-team-collaboration-app |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
