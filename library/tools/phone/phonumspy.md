---
id: phonumspy
name: PhoNumSpy
description: Phone number OSINT tool returning location, country code, city, carrier plus web and social-network footprint search.
url: https://github.com/CyberNDR/PhoNumSpy
category: phone
path:
- phone
bestFor: Enriching a phone number with carrier/location data and finding linked web/social footprint
selectorsIn:
- phone
selectorsOut:
- geolocation
- social-profile
- name
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: ~46 stars; small community tool, verify results.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- phone-osint
- carrier-lookup
- social-footprint
source: gh-topic-footprinting
lastVerified: ''
enrichment: full
---

# PhoNumSpy

> Phone number OSINT tool returning location, country code, city, carrier plus web and social-network footprint search.

- **URL:** https://github.com/CyberNDR/PhoNumSpy
- **Best for:** Enriching a phone number with carrier/location data and finding linked web/social footprint
- **Source:** harvested from `gh-topic-footprinting`

Also searches temporary/disposable phone number providers, which can flag burner numbers. Performs web and social searches, so it touches third-party sites (active).

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
