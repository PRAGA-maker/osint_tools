---
id: recon-ng-paralax-fork
name: Recon-ng (paralax fork)
description: Reconnaissance-focused OSINT framework (personal fork).
url: https://github.com/paralax/Recon-ng
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Modular recon with marketplace modules (contacts, profiles, hosts)
selectorsIn:
- domain
- email
- name
- username
selectorsOut:
- email
- social-profile
- domain
- associate
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Recon-ng is a well-known, mature framework; this is a personal fork (15 stars). Prefer the canonical lanmaster53/recon-ng.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- recon-ng
- reconng
tags:
- recon
- modules
- marketplace
- framework
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# Recon-ng (paralax fork)

> Reconnaissance-focused OSINT framework (personal fork).

- **URL:** https://github.com/paralax/Recon-ng
- **Best for:** Modular recon with marketplace modules (contacts, profiles, hosts)
- **Source:** harvested from `gh-topic-osint-framework`

Metasploit-style modular OSINT framework. Modules for contacts, profiles, hosts; many need API keys. Use the upstream lanmaster53/recon-ng rather than this fork. Contacts/profiles modules help on the people side.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
