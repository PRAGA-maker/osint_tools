---
id: r4ven
name: r4ven
description: Tracks GPS location and captures device/IP information via a hosted link.
url: https://github.com/spyboy-productions/r4ven
category: geolocation
path:
- geolocation
bestFor: Capturing precise geolocation and device fingerprint when a target opens a link.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
- device-id
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Active social-engineering geolocation tool; authorization required.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- spyboy-productions/r4ven
tags:
- geolocation
- phishing
- device-info
- gps
source: gh-topic-reconnaissance
lastVerified: ''
enrichment: full
---

# r4ven

> Tracks GPS location and captures device/IP information via a hosted link.

- **URL:** https://github.com/spyboy-productions/r4ven
- **Best for:** Capturing precise geolocation and device fingerprint when a target opens a link.
- **Source:** harvested from `gh-topic-reconnaissance`

Similar to Seeker/ISeeYou: serves a page that requests location and logs device/IP/battery details to a dashboard. Intrusive and active.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
