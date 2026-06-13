---
id: maltego
name: Maltego
description: OSINT and graphical link-analysis tool for gathering and connecting information.
url: https://maltego.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Visual link analysis connecting people, emails, domains, social profiles via transforms
selectorsIn:
- name
- email
- username
- phone
- domain
- ip-address
- social-profile
selectorsOut:
- name
- email
- social-profile
- associate
- domain
- ip-address
status: unknown
pricing: freemium
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Industry-standard link-analysis platform; free Community Edition with limits, paid for full transforms.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: true
aliases: []
tags:
- link-analysis
- graph
- transforms
- entity-mapping
source: gh-topic-footprinting
lastVerified: ''
enrichment: full
---

# Maltego

> OSINT and graphical link-analysis tool for gathering and connecting information.

- **URL:** https://maltego.com
- **Best for:** Visual link analysis connecting people, emails, domains, social profiles via transforms
- **Source:** harvested from `gh-topic-footprinting`

Community Edition is free but limited (12 entities/transform, registration required). Excellent for building an entity/relationship graph around a missing person from many data sources.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
