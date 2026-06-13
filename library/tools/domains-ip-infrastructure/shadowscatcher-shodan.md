---
id: shadowscatcher-shodan
name: shadowscatcher/shodan
description: Go client library for the Shodan.io internet-device search engine.
url: https://github.com/shadowscatcher/shodan
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Programmatic Shodan queries for exposed devices/services by IP or domain
selectorsIn:
- ip-address
- domain
selectorsOut:
- ip-address
- domain
status: unknown
pricing: freemium
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: 119 stars; a Go SDK wrapping the Shodan API (requires Shodan API key; Shodan has free and paid tiers).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: true
aliases:
- go-shodan
tags:
- shodan
- go
- internet-scanning
- iot
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# shadowscatcher/shodan

> Go client library for the Shodan.io internet-device search engine.

- **URL:** https://github.com/shadowscatcher/shodan
- **Best for:** Programmatic Shodan queries for exposed devices/services by IP or domain
- **Source:** harvested from `gh-topic-intelligence-gathering`

Library to query Shodan from Go. Infrastructure-focused; minimal people-finding use. Requires a Shodan account/API key (free tier limited).

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
