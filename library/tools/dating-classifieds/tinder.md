---
id: tinder
name: Tinder
description: High-volume casual matching and rapid local discovery
url: https://tinder.com/
category: dating-classifieds
path:
- dating-classifieds
bestFor: High-volume casual matching and rapid local discovery
input: Profile details, preferences, and geolocation
output: Swipe matches, profile suggestions, and messaging threads
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: active
opsecNote: Location and engagement behavior are continuously tracked for recommendations.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: false
localInstall: false
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

# Tinder

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://tinder.com/
- **Best for:** High-volume casual matching and rapid local discovery
- **Input → Output:** Profile details, preferences, and geolocation → Swipe matches, profile suggestions, and messaging threads
- **OpSec:** active. Location and engagement behavior are continuously tracked for recommendations.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
