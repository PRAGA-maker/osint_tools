---
id: owlculus
name: Owlculus
description: OSINT case-management and investigation toolkit with a web UI for organizing entities and evidence.
url: https://github.com/be0vlk/owlculus
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: 'Managing a missing-persons case: tracking entities, evidence and running OSINT plugins.'
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- email
- associate
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: trusted
trustNote: Installed (Docker-based) in the Trace Labs VM (install_owlculus).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- case-management
- docker
- investigation-platform
- web-ui
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# Owlculus

> OSINT case-management and investigation toolkit with a web UI for organizing entities and evidence.

- **URL:** https://github.com/be0vlk/owlculus
- **Best for:** Managing a missing-persons case: tracking entities, evidence and running OSINT plugins.
- **Source:** harvested from `tracelabs-repos`

TL VM clones it to /opt/owlculus and starts a Docker stack; open the web UI manually. Combines case management with built-in OSINT plugins.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
