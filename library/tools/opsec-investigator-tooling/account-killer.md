---
id: account-killer
name: AccountKiller
description: Use when you need to know how an account exists or can be removed on a given platform — provides per-site directions and direct links for deleting accounts, useful both for OpSec cleanup and understanding a platform's account model.
url: https://www.accountkiller.com/en/home
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A directory of step-by-step account-deletion guides and direct removal links for hundreds of social and people-search sites.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free community reference directory; no account required.
opsec: passive
opsecNote: Passive reference — you read deletion instructions; nothing is queried about a target. Its main investigator value is OpSec hygiene (removing your own personas/footprint) and understanding how a given people-search or social site handles accounts and removals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing crowd-maintained directory of deletion instructions; links can drift as sites change their settings pages, so verify against the live platform.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- accountkiller-com
aliases:
- AccountKiller
- accountkiller.com
tags:
- toddington
- account-deletion
- opsec
- privacy
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# AccountKiller

> A crowd-maintained directory of step-by-step guides and direct links for deleting accounts on hundreds of social, forum and people-search platforms.

## When to use
Two investigator uses. First, **OpSec hygiene**: when you need to tear down a sock-puppet or remove your own footprint from a service, AccountKiller tells you exactly where the (often hidden) deletion page is. Second, **reference**: it documents how specific people-search and social sites handle accounts and opt-outs, which helps you understand a platform's model — and where a subject could have removed themselves.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.accountkiller.com/en/home.
2. Search or browse for the target platform.
3. Read its entry — colour-coded difficulty (white/grey/black) plus step-by-step deletion instructions and a direct removal link where one exists.
4. Follow the steps on the actual platform to delete/opt-out.
5. Cross-check against the live site, since deletion flows change over time.

## Inputs → Outputs
- **In:** a platform name (no personal selector)
- **Out:** deletion/opt-out instructions and a direct link for that platform
- **Empty/negative result looks like:** the platform isn't listed, or its guide is outdated — go to the platform's own privacy/settings page directly.

## Gotchas & OpSec
- Links drift — sites relocate their deletion pages; verify on the live platform.
- Deleting a persona is irreversible; make sure you've exported anything you need first.
- It's a guide, not an automated deletion service — you still perform the steps yourself.

## Overlaps ("do both")
- Complements data-broker opt-out guides and persona-management practices — AccountKiller covers the account layer; broker opt-outs cover aggregated records about you.

## Trust & verifiability
`trust: community` — a helpful crowd-maintained reference whose instructions can lag site changes; always confirm the current deletion flow on the platform itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | account-killer |
