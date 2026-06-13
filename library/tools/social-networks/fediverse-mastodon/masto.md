---
id: masto
name: Masto
description: Mastodon user profile investigation and account analysis
url: https://github.com/C3n7ral051nt4g3ncy/Masto
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Mastodon user profile investigation and account analysis
input: Mastodon username and instance (e.g., user@mastodon.social)
output: Profile details, recent toots, follower/following lists, account creation date, and metadata
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Makes API requests directly to the target Mastodon instance; instance admins can see request logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Masto

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/C3n7ral051nt4g3ncy/Masto
- **Best for:** Mastodon user profile investigation and account analysis
- **Input → Output:** Mastodon username and instance (e.g., user@mastodon.social) → Profile details, recent toots, follower/following lists, account creation date, and metadata
- **OpSec:** active. Makes API requests directly to the target Mastodon instance; instance admins can see request logs.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
