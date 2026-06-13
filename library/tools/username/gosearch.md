---
id: gosearch
name: GoSearch
description: Search anyone's digital footprint across 300+ websites by username.
url: https://github.com/ibnaleem/gosearch
category: username
path:
- username
bestFor: Fast username enumeration with breach/HudsonRock integration
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Fast Go-based username searcher (3.4k stars); active community project.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- gosearch
tags:
- username
- go
- fast
- breach-check
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# GoSearch

> Search anyone's digital footprint across 300+ websites by username.

- **URL:** https://github.com/ibnaleem/gosearch
- **Best for:** Fast username enumeration with breach/HudsonRock integration
- **Source:** harvested from `gh-topic-osint-framework`

go install or download a release binary. Faster than Sherlock; integrates HudsonRock infostealer data and breach directory lookups. Good complement to Maigret.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
