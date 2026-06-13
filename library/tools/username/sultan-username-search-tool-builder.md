---
id: sultan-username-search-tool-builder
name: SULTAN (Username Search Tool builder)
description: Sinwindie's own Python-based framework/script for building a username search tool across many sites, driven by a spreadsheet of site templates (SULTAN.py, SULTAN_DATA.xlsx). Distributed in the repo with a how-to PDF.
url: https://github.com/sinwindie/OSINT/tree/master/SULTAN
category: username
path:
- username
bestFor: Bulk-checking a username across many platforms to find a missing person's social footprint
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: unknown
pricing: free
opsec: unknown
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SULTAN
tags:
- username-enumeration
- self-hosted
- python
- sinwindie
source: sinwindie-osint
lastVerified: ''
enrichment: full
---

# SULTAN (Username Search Tool builder)

> Sinwindie's own Python-based framework/script for building a username search tool across many sites, driven by a spreadsheet of site templates (SULTAN.py, SULTAN_DATA.xlsx). Distributed in the repo with a how-to PDF.

- **URL:** https://github.com/sinwindie/OSINT/tree/master/SULTAN
- **Best for:** Bulk-checking a username across many platforms to find a missing person's social footprint
- **Source:** harvested from `sinwindie-osint`

Requires Python and the bundled SULTAN_DATA.xlsx. Conceptually similar to Sherlock/WhatsMyName. Includes RequestsValidator.py.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
