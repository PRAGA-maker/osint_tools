---
id: tookie-osint
name: Tookie-OSINT
description: Advanced OSINT tool that finds social media accounts based on inputs.
url: https://github.com/Alfredredbird/tookie-osint
category: username
path:
- username
bestFor: Finding social media accounts from a username
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
trustNote: Community username/account-finder (2.3k stars).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- tookie
tags:
- username
- social-media
- account-discovery
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# Tookie-OSINT

> Advanced OSINT tool that finds social media accounts based on inputs.

- **URL:** https://github.com/Alfredredbird/tookie-osint
- **Best for:** Finding social media accounts from a username
- **Source:** harvested from `gh-topic-osint-framework`

Python tool similar to Sherlock/Maigret; configurable site list. Verify hits manually as account-finders produce false positives.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
