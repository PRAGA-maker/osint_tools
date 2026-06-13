---
id: h8mail-trace-labs-fork
name: h8mail (Trace Labs fork)
description: Email OSINT and breach-hunting tool that searches leaked credentials and breach databases for an email address.
url: https://github.com/tracelabs/h8mail
category: email
path:
- email
bestFor: Finding breached passwords, accounts and exposures tied to an email address.
selectorsIn:
- email
selectorsOut:
- email
- username
- associate
status: unknown
pricing: freemium
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Trace Labs fork of khast3x/h8mail.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- h8mail
tags:
- python
- email
- breach
- credentials
- tracelabs
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# h8mail (Trace Labs fork)

> Email OSINT and breach-hunting tool that searches leaked credentials and breach databases for an email address.

- **URL:** https://github.com/tracelabs/h8mail
- **Best for:** Finding breached passwords, accounts and exposures tied to an email address.
- **Source:** harvested from `tracelabs-repos`

Pip-installable (pip install h8mail). Free local breach files; some integrations (HIBP, Snusbase, etc.) require API keys.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
