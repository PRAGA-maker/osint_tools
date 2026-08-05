---
id: maltego-transforms-list
name: Maltego transforms list
description: Use when you already work in Maltego and want to discover which community transforms can turn a given selector (email, domain, name, etc.) into new graph entities — returns pointers to transform packages, not data itself.
url: https://github.com/cipher387/maltego-transforms-list
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Finding the right community/third-party Maltego transform to enrich a selector inside a Maltego graph.
selectorsIn:
- email
- domain
- name
- username
selectorsOut:
- social-profile
- domain
- email
status: live
pricing: free
costNote: Free, open GitHub reference list (curated by cipher387/cyb-detective); the listed transforms vary — some free, some need their own API keys.
opsec: passive
opsecNote: Reading the list is passive. Running any transform it points to is as active/passive as that specific transform — a transform that queries a target's infrastructure is active and may leave traces, so review each one before firing it in a live graph.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community-maintained catalog by a well-known OSINT curator (cipher387). It indexes third-party transforms whose individual quality/currency you must judge per entry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- advanced-search-operators-list
- apis-for-osint
- awesome-grep
- code-understanding-tools-list
- dorks-collections-list
- grep-for-osint
- python-osint-automation-examples
aliases:
- Maltego transforms catalog
- cipher387 maltego transforms
tags:
- My Projects
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Maltego transforms list

> A curated GitHub catalog of Maltego transforms — the "what can I plug into my graph to expand this entity" index for Maltego users.

## When to use
You are already running an investigation inside **Maltego** and have an entity (an `email`, `domain`, `name`, `username`) you want to expand into new nodes, but the built-in transforms fall short. This list points you to community and third-party transform packages that handle different data types, so you can find one that turns your current selector into fresh leads.

## How to use it (`bestInteractionPattern`: cli)
1. Open the repo: https://github.com/cipher387/maltego-transforms-list
2. Scan the catalog for a transform that accepts the entity type you hold and outputs what you need.
3. Follow the linked transform's own repo/hub page to install it into your Maltego (Transform Hub or local transform), providing any API key it requires.
4. Drop your entity onto a Maltego graph and run the transform to generate new nodes.
5. Pivot: the new entities (profiles, related domains, emails) feed further Maltego transforms or hand off to standalone tools.

## Inputs → Outputs
- **In:** an existing Maltego entity — `email`, `domain`, `name`, `username`, etc.
- **Out:** pointers to transforms that yield `social-profile`, `domain`, `email` and other entity types
- **Empty/negative result looks like:** no catalog entry matches your entity type — meaning you need a bespoke/local transform, not that no data exists.

## Gotchas & OpSec
- This is a **directory of tools**, not a data source — nothing is returned until you install and run a listed transform.
- Third-party transforms drift: links rot, APIs change, and some now require paid keys. Verify each before relying on it.
- OpSec depends entirely on the chosen transform: some passively query public data, others actively hit target infrastructure. Check before firing.

## Overlaps ("do both")
- Sits alongside the same curator's other reference lists — `[[apis-for-osint]]`, `[[dorks-collections-list]]`, `[[python-osint-automation-examples]]` — which cover the non-Maltego automation surface.

## Trust & verifiability
`trust: community` — it is a respected curator's index, but it only vouches for "these transforms exist," not for the quality or safety of each; validate the individual transform you adopt.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maltego-transforms-list |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain, name, username → social-profile, domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
