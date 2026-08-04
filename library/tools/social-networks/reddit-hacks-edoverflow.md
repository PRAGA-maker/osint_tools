---
id: reddit-hacks-edoverflow
name: Reddit Hacks (EdOverflow)
description: Use when you have a Reddit `username` and want a scripted way to pull their activity, plus assorted recon helpers — returns pointers/scripts for enumerating a profile.
url: https://github.com/EdOverflow/hacks
category: social-networks
path:
- social-networks
bestFor: A small personal collection of recon shell scripts (including a Reddit user-history helper) to script simple enumeration.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free open-source scripts on GitHub; no account. You run them yourself.
opsec: passive
opsecNote: The scripts hit public endpoints (e.g. Reddit's public JSON) — passive if you use a sock-puppet IP and do not authenticate. Review any script before running it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A personal "random scripts" repo (EdOverflow) with limited/old maintenance; treat it as example code to read and adapt, not a supported tool.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- EdOverflow hacks
tags:
- reddit
- reference
- techniques
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Reddit Hacks (EdOverflow)

> A grab-bag of small recon shell scripts — including a Reddit user-history helper — to script simple public-endpoint enumeration.

## When to use
You have a Reddit `username` and want a scriptable way to pull their public activity, or you want lightweight recon helpers (cloud-bucket enumeration, git grepping, open-redirect checks). It is a code reference to read and adapt, not a polished product.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/EdOverflow/hacks`.
2. **Read the script first** (it is short) to confirm what endpoints it hits.
3. Run the relevant script (e.g. the `reddit` helper) with the target `username` from a sock-puppet environment.
4. Feed the returned profile/activity into deeper Reddit-OSINT tooling for comment history, timezone and interest analysis.

## Inputs → Outputs
- **In:** a Reddit `username` (for the reddit script)
- **Out:** the user's public activity / a `social-profile` view
- **Empty/negative result looks like:** an empty JSON response (user has no public activity, is shadowbanned, or the endpoint changed) — verify the script still matches Reddit's current API shape.

## Gotchas & OpSec
- Human-in-the-loop: none, but the repo is old — endpoints it targets may have changed and need patching.
- OpSec: passive against public data; do not authenticate, and route through a sock-puppet IP to avoid rate-limit attribution.
- Always audit third-party scripts before executing them.

## Overlaps ("do both")
- Complements dedicated Reddit-analysis tools: this gives you a raw scriptable pull, those add comment-history, activity-heatmap and interest analysis on top.

## Trust & verifiability
`trust: unverified` — a personal, lightly-maintained scripts repo; useful as adaptable example code, not as a supported tool — verify behaviour before relying on output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-hacks-edoverflow |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
