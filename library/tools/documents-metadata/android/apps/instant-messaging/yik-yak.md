---
id: yik-yak
name: Yik Yak
description: Location-based event monitoring, community sentiment analysis, anonymity assessment
url: https://www.yikyak.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- instant-messaging
bestFor: Location-based event monitoring, community sentiment analysis, anonymity assessment
input: Location coordinates, proximity radius
output: Anonymous posts, location data, user engagement, community trends
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Designed for anonymity; minimal PII exposure, but location data and timing can reveal patterns
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: false
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Yik Yak

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.yikyak.com/
- **Best for:** Location-based event monitoring, community sentiment analysis, anonymity assessment
- **Input → Output:** Location coordinates, proximity radius → Anonymous posts, location data, user engagement, community trends
- **OpSec:** passive. Designed for anonymity; minimal PII exposure, but location data and timing can reveal patterns

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
