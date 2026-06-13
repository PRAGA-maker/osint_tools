---
id: osint-san
name: OSINT-SAN
description: Framework for rapid information discovery and user deanonymization.
url: https://github.com/Bafomet666/OSINT-SAN
category: people-search
path:
- people-search
bestFor: Multi-module deanonymization (IP, phone, social, geolocation)
selectorsIn:
- ip-address
- phone
- username
- name
selectorsOut:
- geolocation
- social-profile
- ip-address
- phone
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community deanonymization framework (604 stars); some modules use grabber/IP-logger techniques (active).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- osintsan
- OSINT SAN
tags:
- deanonymization
- geolocation
- ip
- phone
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# OSINT-SAN

> Framework for rapid information discovery and user deanonymization.

- **URL:** https://github.com/Bafomet666/OSINT-SAN
- **Best for:** Multi-module deanonymization (IP, phone, social, geolocation)
- **Source:** harvested from `gh-topic-osint-framework`

Includes IP-logger/grabber modules that interact with targets (active opsec). Use the passive modules only for casework. PRO variant exists (Bafomet666/OSINT-SAN-PRO).

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
