---
id: whoishere-py
name: whoishere.py
description: WiFi client detection tool that identifies people by naming devices seen issuing wireless probe requests.
url: https://github.com/hkm/whoishere.py
category: geolocation
path:
- geolocation
bestFor: Physical-presence detection of a person via their device's WiFi probe requests
selectorsIn:
- mac-address
- device-id
selectorsOut:
- mac-address
- device-id
- name
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: 248 stars; requires monitor-mode WiFi hardware and physical proximity.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- wifi
- probe-request
- device-tracking
- physical
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# whoishere.py

> WiFi client detection tool that identifies people by naming devices seen issuing wireless probe requests.

- **URL:** https://github.com/hkm/whoishere.py
- **Best for:** Physical-presence detection of a person via their device's WiFi probe requests
- **Source:** harvested from `gh-topic-intelligence-gathering`

Passively sniffs 802.11 probe requests to detect when a known device (and thus person) is physically nearby. Requires a WiFi adapter in monitor mode and on-site presence; legality varies by jurisdiction. Situational for confirming someone is at a location.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
